---
name: meter-driver-personal
description: Help an individual Meter driver or rider with their own data through the Meter MCP tools: their trips (list_trips driver "me"), bookings (list_bookings scope "driver" or "rider"), Meter Pay earnings and pay stubs (get_earnings scope "me"), and their own profile and availability (whoami, update_my_profile, update_my_availability). Use when the signed-in person asks about "my trips", "my earnings", "my schedule", "my rides" or their account; do not use for fleet-wide questions (meter-fleet-insights) or fleet settings (meter-settings-changes), which need an owner or admin role.
---

# A driver's or rider's own Meter data

Most Meter users are individual drivers (solo or in a fleet) and riders. Their tools work regardless of fleet role and never require an operational fleet. This skill keeps the agent inside that person's own data.

## Start with `whoami`

- `fleets[]`: a driver may belong to one or more fleets; `role: "driver"` means fleet-wide tools will refuse. That is expected, not an error to work around.
- `is_rider: true`: the person has booked rides; `list_bookings` with `scope: "rider"` returns them.
- `profile`: the person's own name, email and phone (never anyone else's).

## Own trips and rides

| Ask | Call |
| --- | --- |
| "My trips this month" | `list_trips` with `driver: "me"`, `start_date`, `end_date`; page with `cursor` |
| "How far did I drive / how much did I collect" | Sum `distance_meters` and `total_minor` over all pages; state the range and currency |
| "My upcoming rides" | `list_bookings` with `scope: "driver"`, `after: now`, `sort: "asc"` |
| "The ride I booked" (as a rider) | `list_bookings` with `scope: "rider"`, then `get_booking` |
| "What happened to that booking" | `get_booking_audit_log` (redacted timeline) |

Solo drivers without a fleet still have trips: `list_trips` with `driver: "me"` and no `fleet_id`.

## Earnings and pay stubs

`get_earnings` with `scope: "me"` returns Meter Pay payouts (card payments transferred to the person's bank account) per currency, with a `day` or `week` series. It does **not** include cash fares. For a pay-stub style summary:

1. Call `get_earnings` for the pay period (`start_date` inclusive, `end_date` exclusive), `granularity: "week"`.
2. Call `list_trips` with `driver: "me"` for the same period and total trips, distance, fares and tips by payment method.
3. Present: period, trip count, gross fares, tips, card payouts (from earnings), cash collected (from trips with a cash payment method), currency, and the fleet's payout fraction if the person is in a fleet (`get_fleet` shows it to admins only; otherwise say it is set by the fleet).

Label every figure with its source tool. Do not present the result as an official tax document.

## Profile and availability

`update_my_profile` (name, business name on receipts, navigation app, receipt privacy options with Meter Pro) and `update_my_availability` (the weekly hours riders may book the driver for; the whole week is replaced, so include every working day) change only the signed-in person's own record. Follow the dry-run sequence from `meter-settings-changes`: call with `dry_run: true` first (it defaults to false), show the returned `changes` (`field`, `from`, `to`), get a yes, then repeat the call without `dry_run`. Email, phone, role and payout details are managed in the Meter app, not here.

## What this skill does not do

- It does not look at other drivers. `list_fleet_members`, `driver: "all"` and `scope: "fleet"` are owner/admin tools; a `forbidden` error confirms the person is a driver.
- It does not guess ids. Trip and booking ids come from the list tools.
- It does not change fares, fleet settings or bookings.

## References

- [Tool catalog](../../references/tools.md) (generated)
- [Data model](../../references/data-model.md) (generated; `Trip`, `Booking`, `EarningsSummary`)
