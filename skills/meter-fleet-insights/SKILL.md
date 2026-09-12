---
name: meter-fleet-insights
description: Answer questions about a Meter fleet's trips, bookings, drivers, vehicles, earnings and accounting using the Meter MCP tools (whoami, list_trips, list_bookings, list_fleet_members, list_vehicles, get_earnings, get_accounting_summary). Covers picking the right tool, role limits, pagination and presenting money and times correctly. Use for any "how many / how much / who / which / when" question about a fleet; do not use for changing settings (meter-settings-changes), setting up a new fleet (meter-fleet-onboarding), an individual driver's own data (meter-driver-personal), or explaining the API itself (meter-api-explainer).
---

# Fleet insights with Meter

The Meter MCP server at `https://www.meterapp.co/api/mcp` returns the data the signed-in person already sees in the Meter apps. Owners and admins see the whole fleet; drivers see only themselves. Nothing in this skill changes data.

## Always start with `whoami`

Call `whoami` once per session. It returns:

- `fleets[]` with `fleet_id`, `role` (`owner`, `admin`, `driver`) and `is_operational`
- `default_fleet_id` when the person belongs to exactly one fleet (then `fleet_id` may be omitted everywhere)
- `suggested_next_tools`

If there are several fleets and the question does not name one, ask which fleet before calling anything else. Never construct a `fleet_id`.

## Pick the right tool

| Question | Tool | Notes |
| --- | --- | --- |
| Who is in the fleet, which drivers exist | `list_fleet_members` | owners/admins only; `member_id` feeds `list_trips` |
| Which cars, who drives which | `list_vehicles` | `assigned_driver` is admin-only |
| Completed metered rides, revenue per trip, tips | `list_trips` | `driver: "all"` (admins) or a `member_id`; filter with `start_date`/`end_date` |
| One trip in detail | `get_trip` | id from `list_trips` |
| Scheduled and on-demand rides, what is unassigned | `list_bookings` | `scope: "fleet"` for admins; filter by `status`, `after`, `before` |
| What happened to a booking and when | `get_booking_audit_log` | redacted timeline; roles, never names |
| Card payouts to bank accounts | `get_earnings` | `scope: "fleet"`, `include_members: true` for a per-driver split |
| Full ledger: cash, card, unpaid, balances between fleet and drivers | `get_accounting_summary` | owners/admins of an operational fleet |
| Fleet settings, ride options, service zones | `get_fleet` | admins also get booking and payout settings |
| How far a new fleet is from its first booking | `get_onboarding_checklist` | owners/admins; works before the fleet is operational (see `meter-fleet-onboarding`) |

`get_earnings` counts only Meter Pay card payouts. For "how much did the fleet make" including cash, use `get_accounting_summary`. Say which one you used.

## Pagination and time ranges

- Lists return `items` and `next_cursor`. Pass `cursor` back until it is null; keep `limit` at or below 100. For totals over a period, page through everything or use the summary tools instead of stopping early.
- `start_date`/`end_date` (trips, earnings, accounting) and `after`/`before` (bookings) take ISO 8601 dates. Interpret "last week" in the fleet's timezone (`get_fleet` or `list_fleets` return `timezone`), and state the range you used.
- Trips are metered rides that happened. Bookings are scheduled rides, some of which become trips (`trip_id` on the booking once completed). Do not add them together.

## Present numbers correctly

- Money fields end in `_minor` and are in the currency's minor unit: divide by 100 for USD, EUR, GBP and most currencies (JPY and a few others have no minor unit). Show the currency code from the result.
- Distances are meters, durations are seconds, timestamps are ISO 8601. Convert for the human and keep the fleet timezone.
- When a field's meaning is unclear, call `explain_data` with the tool and field name rather than guessing.

## Role limits are final

A `forbidden` error means the person's role does not allow that view. Do not retry with other ids or arguments. Drivers can still get their own data: `list_trips` with `driver: "me"`, `list_bookings` with `scope: "driver"`, `get_earnings` with `scope: "me"`. A `fleet_not_operational` error means fleet-wide data is unavailable until onboarding and billing are complete; own-data tools still work.

## Privacy

Results already exclude payment-provider ids, GPS traces, internal notes and other people's contact details beyond what the role allows. Do not infer them, and do not compile per-person profiles the human did not ask for. Rider contact details appear only where the role permits; treat them as confidential.

## References

- [Tool catalog](../../references/tools.md) (generated)
- [Data model](../../references/data-model.md) (generated)
- [Safety](../../references/safety.md)
