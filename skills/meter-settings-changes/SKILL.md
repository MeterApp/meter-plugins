---
name: meter-settings-changes
description: "Safely change Meter fleet settings, booking settings, ride options and fares, vehicle assignments, or the signed-in person's own profile and availability through the Meter MCP write tools (update_fleet_settings, update_booking_settings, update_ride_option, assign_vehicle, update_my_profile, update_my_availability). Enforces the dry_run: true preview, echo changes, explicit confirmation, apply sequence. Use whenever a request would modify fleet settings or the person's own profile in Meter; do not use for read-only questions (meter-fleet-insights, meter-driver-personal), for first-time fleet setup as a whole (meter-fleet-onboarding), or for booking, changing or cancelling a ride as a rider (meter-ride)."
---

# Changing settings in Meter

Every Meter write tool requires a saved proposal. With `dry_run: true` the server validates and authorizes the request, computes the exact changes, saves the proposal and writes nothing. A first call without a live proposal also writes nothing and returns `confirmation_required`. This skill exists so that no change ever happens without the human seeing those changes first.

## The result envelope

A preview includes the following envelope (with the returned proposal ID saved for confirmation):

```json
{
  "status": "preview",
  "proposal": { "id": "the opaque ID returned by this preview" },
  "applied": false,
  "dry_run": true,
  "changes": [{ "field": "payment_mode", "from": "payments_optional", "to": "pre_payment_required" }],
  "booking_settings": { "...": "the resulting object (the current one on a dry run)" }
}
```

- `status` identifies preview, confirmation required, or applied results. `applied` is `false` on a preview and for an applied no-op, and `true` after a mutation. Preserve the complete returned proposal; never construct its ID.
- `changes` lists only the fields that would differ, each with `field`, `from` and `to`. An empty list means nothing would change.
- The last key is the DTO (`fleet`, `booking_settings`, `ride_option`, `vehicle`, `profile`, `availability`); `explain_data` documents its fields.

## The sequence, every time

1. **Read first.** `whoami` for the role, then the matching read tool (`get_fleet` for fleet, booking and ride-option settings; `list_vehicles` and `list_fleet_members` for assignments). Quote the current value.
2. **Dry run.** Call the write tool with `dry_run: true` and only the fields the human named. Never pass fields "to be safe"; omitted fields are left alone and unknown fields are rejected.
3. **Echo the changes.** Show `changes` exactly as returned: each `field` with its `from` and `to` value, plus any warnings. If the list is empty, say nothing would change and stop.
4. **Ask.** One clear question: "Apply these N changes to <fleet name>? (yes/no)". Wait for the answer. A vague reply ("sure, whatever works") is not a yes for money fields; ask again with the numbers.
5. **Apply.** Repeat the intended arguments with the saved `proposal_id` and `dry_run: false`. Confirm `status: applied`; an applied no-op has `applied: false` and no changes. For stale or expired proposals, show the fresh replacement and ask for confirmation again. Report the result and, for fleet settings, re-read with `get_fleet`.

Never skip the dry run because the change "is small", never apply in the same turn as the dry run without an answer in between, and never apply a change the human did not see in the echoed list.

## Money changes need the numbers

Fares (`update_ride_option`: `fare.base`, `fare.minimum_fare`, `fare.distance_rate`, `fare.minute_rate`, `fare.wait_time_minute_rate`, `fare.tax_rate`, in major currency units as shown in the console, 0 to 10000) and cancellation fees (`update_booking_settings`) are money. State `from` and `to` with the currency, e.g. "Base fare: 3.50 -> 4.00 USD". If the human gave a percentage or a vague direction ("raise it a bit"), compute the concrete value, show it, and get a yes on the concrete value. Official government tariffs cannot be edited; the tool says so.

## Who may change what

| Tool | Role |
| --- | --- |
| `update_fleet_settings`, `update_booking_settings`, `update_ride_option`, `assign_vehicle` | fleet owner or admin of an operational fleet |
| `update_my_profile`, `update_my_availability` | the signed-in person, for themselves only |

A `forbidden` error is final for that person. Do not retry with another fleet or another id; explain who can make the change. Every write is attributed to the signed-in person in Meter's audit trail exactly as if they had used the app.

## Scope discipline

- One request, one tool, one fleet. If the human asks for changes across several fleets or several ride options, run the sequence once per target.
- Do not change settings the human did not mention because a dry run surfaced something else; report it and ask.
- The write tools do not create or delete ride options, vehicles or members, do not change a fare's currency, and never touch billing, payouts or the join code. For those, point to the web console at `https://www.meterapp.co/app/fleet`.
- `update_my_availability` replaces the whole week: include every day the driver works, not just the one that changes.

## From a terminal

`npx @meterapp/meter call <tool> --<field> <value> --dry-run` runs the same preview. After explicit human confirmation, resend the intended arguments with the returned `proposal_id` and `dry_run: false`; if the client cannot pass the proposal ID, repeat the identical intended arguments only after confirmation. A missing or expired preview requires fresh confirmation.

## After a change

Summarize what changed (the `to` values), and mention how to undo it: the same tool with the `from` values, again through a dry run.

## References

- [Tool catalog](../../references/tools.md) (generated; argument names and roles)
- [Data model](../../references/data-model.md) (generated; the `*Write` envelopes and DTOs)
- [Safety](../../references/safety.md)
