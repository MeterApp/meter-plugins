---
name: meter-settings-changes
description: "Configure Meter driver and fleet settings, including service areas and boundaries, fares and pricing, booking and dispatch rules, website pages and custom domains, branding, privacy, fees, vehicles, members, profile and availability. Use the matching Meter tool with a saved preview and explicit confirmation. Use for a requested change. Do not use for read-only questions, full fleet onboarding, or rider bookings."
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
- The last field is the DTO (`fleet`, `booking_settings`, `ride_option`, `vehicle`, `profile`, `availability`); `explain_data` documents its fields.

## The sequence, every time

1. **Read first.** Check the role and connection access with `whoami`, then call the matching read tool below. Quote the current value.
2. **Dry run.** Call the write tool with `dry_run: true` and only the fields the human named. Never send fields "to be safe"; omitted fields are left alone and unknown fields are rejected.
3. **Echo the changes.** Show `changes` exactly as returned: each `field` with its `from` and `to` value, plus any warnings. If the list is empty, say nothing would change and stop.
4. **Ask.** One clear question: "Apply these N changes to <fleet name>? (yes/no)". Wait for the answer. A vague reply ("sure, whatever works") is not a yes for money fields; ask again with the numbers.
5. **Apply.** Repeat the intended arguments with the saved `proposal_id` and `dry_run: false`. Confirm `status: applied`; an applied no-op has `applied: false` and no changes. For stale or expired proposals, show the fresh replacement and ask for confirmation again. Report the result and, for fleet settings, re-read with `get_fleet`.

Never skip the dry run because the change "is small", never apply in the same turn as the dry run without an answer in between, and never apply a change the human did not see in the echoed list.

## Money changes need the numbers

Fares (check the units for the specific fare tool) and cancellation fees (`update_booking_settings`) are money. State `from` and `to` with the currency, for example, "Base fare goes from 3.50 to 4.00 USD". If the human gave a percentage or a vague direction ("raise it a bit"), compute the concrete value, show it, and get a yes on the concrete value. Official government tariffs cannot be edited; the tool says so.

## Find the right tool

Use the connected server's tool list and `describe_api` to find the exact operation and `explain_data` for argument details. This table gives common paths. The connected catalog determines what is available.

| Setting | Tools |
| --- | --- |
| Fleet profile, branding and contact information | `get_fleet`, `update_fleet_settings` |
| Service areas, pickup and drop-off boundaries | `list_service_zones`, `find_zone_boundary`, `save_service_zone` |
| Fares, flat rates and ride options | `list_fares`, `get_fare`, `create_fare`, `update_fare`, `delete_fare`, `list_zone_fares`, `set_zone_fare`, `set_zone_fares`, and the ride option tools |
| Booking rules, dispatch, cancellation and fees | `get_fleet`, `update_booking_settings`, `update_fee_settings`, `get_dynamic_pricing`, `update_dynamic_pricing` |
| Website address and pages | `get_storefront_settings`, `update_storefront_settings` for the Meter address, `update_fleet_settings` for branding and contact details, and the website page tools |
| Existing custom domain | `get_fleet_site_domain`, `connect_fleet_site_domain`, `check_fleet_site_domain`, `disconnect_fleet_site_domain` |
| Google listing and reviews | `search_google_places`, `link_google_maps_place`, `unlink_google_maps_place` |
| Privacy and voice agent | `get_privacy_settings`, `update_privacy_settings`, `get_voice_agent_settings`, `update_voice_agent_settings` |
| Vehicle and member settings | `list_vehicles`, `list_fleet_members`, the vehicle and member tools, and `assign_vehicle` |
| Personal details and schedule | `whoami`, `update_my_profile`, `update_my_availability`. Availability replaces the whole week, so include every intended working day. |

Use the signed-in person's role and scope. Fleet-wide settings normally require a fleet owner or admin. For a domain, show the exact hostname and which fleet it will serve. After connecting, relay the returned DNS records and ask the person to enter them at their provider. Report the site as live only when the tool returns `active`. For a domain purchase or renewal, open the returned Website settings link for the person to complete in Meter.

If `whoami.connection.access` is `read`, show the person [Connected apps](https://www.meterapp.co/app/account/connected-apps) and ask them to switch this connection to **Look and change**. Refresh the tool list or start a new session after they grant access. If the connection is writable and the tool is missing, say which operation is unavailable in this connection. Use a relevant Meter page for actions the person must finish themselves, such as account authorization, billing and bank setup. Never report a change without an applied result.

Run the preview and approval separately for each target. Use only IDs returned by Meter. When `find_zone_boundary` returns multiple possible boundaries, confirm the intended area before saving it.

## From a terminal

`npx @meterapp/meter call <tool> --<field> <value> --dry-run` runs the same preview. After explicit human confirmation, resend the intended arguments with the returned `proposal_id` and `dry_run: false`; if the client cannot send the proposal ID, repeat the identical intended arguments only after confirmation. A missing or expired preview requires fresh confirmation.

## After a change

Summarize the applied result. If the change can be reversed, explain the matching operation and preview it if the person requests it.

## References

- [Tool catalog](../../references/tools.md) (generated; argument names and roles)
- [Data model](../../references/data-model.md) (generated; the `*Write` envelopes and DTOs)
- [Safety](../../references/safety.md)
