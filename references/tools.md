# Meter MCP tools

Generated from the `@meterapp/meter-sdk` catalog (server version 1.0.0); do not edit by hand. Endpoint: `https://www.meterapp.co/api/mcp`. The live server describes itself too: call `describe_api` for this list and `explain_data` for any result field.

| Tool | Roles | Writes? | Returns |
| --- | --- | --- | --- |
| [`whoami`](#whoami) | anyone | no | Whoami |
| [`list_fleets`](#list_fleets) | anyone | no | FleetSummary |
| [`get_fleet`](#get_fleet) | fleet_member | no | FleetDetail |
| [`list_fleet_members`](#list_fleet_members) | fleet_admin | no | FleetMember |
| [`list_vehicles`](#list_vehicles) | fleet_member | no | Vehicle |
| [`list_trips`](#list_trips) | fleet_member | no | TripPage |
| [`get_trip`](#get_trip) | participant | no | Trip |
| [`list_bookings`](#list_bookings) | anyone | no | BookingPage |
| [`get_booking`](#get_booking) | participant | no | Booking |
| [`get_booking_audit_log`](#get_booking_audit_log) | participant | no | BookingAuditLog |
| [`get_earnings`](#get_earnings) | anyone | no | EarningsSummary |
| [`get_accounting_summary`](#get_accounting_summary) | fleet_admin | no | AccountingSummary |
| [`describe_api`](#describe_api) | anyone | no | text |
| [`explain_data`](#explain_data) | anyone | no | text |
| [`update_fleet_settings`](#update_fleet_settings) | fleet_admin | yes (dry_run first) | FleetSettingsWrite |
| [`update_booking_settings`](#update_booking_settings) | fleet_admin | yes (dry_run first) | BookingSettingsWrite |
| [`update_ride_option`](#update_ride_option) | fleet_admin | yes (dry_run first) | RideOptionWrite |
| [`assign_vehicle`](#assign_vehicle) | fleet_admin | yes (dry_run first) | VehicleAssignmentWrite |
| [`update_my_profile`](#update_my_profile) | anyone | yes (dry_run first) | MyProfileWrite |
| [`update_my_availability`](#update_my_availability) | anyone | yes (dry_run first) | DriverAvailabilityWrite |
| [`get_onboarding_checklist`](#get_onboarding_checklist) | fleet_admin | no | OnboardingChecklist |

Roles: `anyone` = any signed-in Meter user; `fleet_member` = owner, admin or driver of the fleet; `fleet_admin` = owner or admin of an operational fleet; `participant` = fleet owner/admin, or the driver/rider on the record; `self` = the signed-in person, acting on their own record.

## whoami

**Who am I** · roles: `anyone` · read-only · returns `Whoami`

Call this first. Returns the signed-in person: profile (their own name, email and phone), every fleet they belong to with their role (owner, admin or driver), whether they are a rider, a plain-language list of what they can read here, and suggested_next_tools. Use it to decide which fleet_id to pass and which tools apply; do not call it repeatedly in one session. Any signed-in user may call it.

No arguments.

Example:

```json
{"name":"whoami","arguments":{}}
```

## list_fleets

**List my fleets** · roles: `anyone` · read-only · returns `FleetSummary`

List the fleets the caller belongs to with their role and whether each fleet is operational (onboarded and billing active). Use it to pick a fleet_id when whoami shows more than one fleet. Returns FleetSummary items with name, city, country, currency and timezone. Riders and solo drivers get an empty list. Any signed-in user may call it.

No arguments.

Example:

```json
{"name":"list_fleets","arguments":{}}
```

## get_fleet

**Get fleet details** · roles: `fleet_member` · read-only · returns `FleetDetail`

Describe one fleet: public info (name, city, currency, timezone, contact and dispatch phones, website, description), service zones by name, bookable ride options with headline fare rates, and member and vehicle counts. Owners and admins additionally get booking_settings (dispatch and payment policy, lead time, cancellation terms) and admin_settings (payout fraction, collection mode). Drivers get the public part only. Requires membership in the fleet. Do not use it to list members or vehicles; use list_fleet_members and list_vehicles.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string (uuid) | no |  | Fleet id from whoami or list_fleets. Optional when the caller belongs to exactly one fleet. |

Example:

```json
{"name":"get_fleet","arguments":{"fleet_id":"11111111-1111-4111-8111-111111111111"}}
```

## list_fleet_members

**List fleet members** · roles: `fleet_admin` · read-only · returns `FleetMember`

List every member of a fleet with member_id, display name, role (owner, admin, driver), join date, email and phone. Owners and admins of an operational fleet only; drivers receive a permission error. Use member_id as the `driver` argument of list_trips or to match drivers in bookings and accounting. Optional role filter. Do not use it to find riders; riders are not fleet members.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string (uuid) | no |  | Fleet id from whoami or list_fleets. Optional when the caller belongs to exactly one fleet. |
| `role` | "owner" \| "admin" \| "driver" | no |  | Only members with this role. |

Example:

```json
{"name":"list_fleet_members","arguments":{"fleet_id":"11111111-1111-4111-8111-111111111111","role":"driver"}}
```

## list_vehicles

**List fleet vehicles** · roles: `fleet_member` · read-only · returns `Vehicle`

List the active vehicles of a fleet: make, model, year, license plate, nickname and color. Owners and admins also see assigned_driver (who currently drives each vehicle); for drivers that field is always null. Requires membership in the fleet. Vehicles that were removed from the fleet are not returned. Use get_fleet for the vehicle count only.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string (uuid) | no |  | Fleet id from whoami or list_fleets. Optional when the caller belongs to exactly one fleet. |

Example:

```json
{"name":"list_vehicles","arguments":{"fleet_id":"11111111-1111-4111-8111-111111111111"}}
```

## list_trips

**List metered trips** · roles: `fleet_member` · read-only · returns `TripPage`

List completed metered trips, newest first, with times, distance, pickup and drop-off addresses, fare name, receipt total and tip, payment method and paid status. Drivers get only their own trips (driver="me"). Owners and admins may pass driver="all" for every driver in the fleet or a member_id from list_fleet_members. Filter by start_date/end_date; page with cursor and limit (max 100). Trips are metered rides, not bookings: use list_bookings for scheduled rides that have not happened yet. No GPS traces are returned.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string (uuid) | no |  | Fleet id from whoami or list_fleets. Optional when the caller belongs to exactly one fleet. |
| `driver` | string | no | `"me"` | "me" (default) for the caller's own trips, "all" for every driver in the fleet (owners/admins only), or a member id from list_fleet_members (owners/admins only). |
| `start_date` | string | no |  | Only trips that started at or after this time (ISO 8601). |
| `end_date` | string | no |  | Only trips that started at or before this time (ISO 8601). |
| `cursor` | string | no |  | Opaque cursor from the previous page's next_cursor. Omit for the first page. |
| `limit` | integer | no | `50` | Page size, 1-100 (default 50). |

Example:

```json
{"name":"list_trips","arguments":{"fleet_id":"11111111-1111-4111-8111-111111111111","driver":"all","start_date":"2026-09-01","limit":25}}
```

## get_trip

**Get one trip** · roles: `participant` · read-only · returns `Trip`

Fetch one metered trip by id with the same fields as list_trips (times, distance, places, receipt total, tip, fee and discount counts, payment method, void status). Allowed for the driver who drove it and for owners/admins of the fleet it was driven for; anyone else gets a not-found error, so a missing trip and a forbidden trip look the same. Use list_trips to discover trip ids; never construct one.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `trip_id` | string (uuid) | yes |  | Trip id from list_trips or a booking's trip_id. |

Example:

```json
{"name":"get_trip","arguments":{"trip_id":"22222222-2222-4222-8222-222222222222"}}
```

## list_bookings

**List bookings** · roles: `anyone` · read-only · returns `BookingPage`

List bookings (scheduled and on-demand rides) with status, scheduled time, pickup and drop-off, rider, assigned driver, ride option and upfront estimate. scope auto picks the widest view the caller has: fleet-wide for owners/admins, own assigned rides for drivers, own booked rides for riders. Filter by status, and by scheduled time with before/after; page with cursor (a scheduled-time cursor) and limit. Pending-payment bookings are hidden unless requested in status. For a full timeline of one booking call get_booking_audit_log.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string (uuid) | no |  | Fleet id from whoami or list_fleets. Optional when the caller belongs to exactly one fleet. |
| `scope` | "auto" \| "fleet" \| "driver" \| "rider" | no | `"auto"` | auto (default): fleet-wide for owners/admins, own assigned bookings for drivers, own rides for riders. fleet: all bookings of the fleet (owners/admins). driver: bookings assigned to the caller. rider: bookings the caller booked as a rider. |
| `status` | array of "pending" \| "confirmed" \| "in_progress" \| "completed" \| "canceled" \| "pending_payment" | no |  | Only bookings in these statuses. Default: every status except pending_payment. |
| `after` | string | no |  | Only bookings scheduled after this time. |
| `before` | string | no |  | Only bookings scheduled before this time. |
| `sort` | "asc" \| "desc" | no | `"desc"` | Order by scheduled time; desc = newest first. |
| `cursor` | string | no |  | Opaque cursor from the previous page's next_cursor. Omit for the first page. |
| `limit` | integer | no | `50` | Page size, 1-100 (default 50). |

Example:

```json
{"name":"list_bookings","arguments":{"fleet_id":"11111111-1111-4111-8111-111111111111","status":["pending","confirmed"],"after":"2026-09-11T00:00:00Z","sort":"asc"}}
```

## get_booking

**Get one booking** · roles: `participant` · read-only · returns `Booking`

Fetch one booking by id with the same fields as list_bookings plus notes, flight number, cancellation reason and the linked trip id once completed. Allowed for owners/admins and members of the fleet, the assigned driver, and the rider who booked it; anyone else gets not-found. Rider contact details appear only for fleet owners/admins, the assigned driver, and the rider themselves. Use list_bookings to discover ids.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `booking_id` | string (uuid) | yes |  | Booking id from list_bookings. |

Example:

```json
{"name":"get_booking","arguments":{"booking_id":"33333333-3333-4333-8333-333333333333"}}
```

## get_booking_audit_log

**Get booking timeline** · roles: `participant` · read-only · returns `BookingAuditLog`

Return the redacted activity timeline of one booking, newest first: status changes, driver assignments, edits to time or route, payment events and notifications sent, each with a timestamp, title, one-line summary, the ROLE of who acted (owner, admin, driver, fleet_member, rider or system; never a name or id) and redacted field-level before/after values. Allowed for the same viewers as get_booking. Use it to answer "what happened to this booking and when"; use get_booking for the current state.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `booking_id` | string (uuid) | yes |  | Booking id from list_bookings or get_booking. |
| `cursor` | string | no |  | Opaque cursor from the previous page's next_cursor. Omit for the first page. |
| `limit` | integer | no | `50` | Page size, 1-100 (default 50). |

Example:

```json
{"name":"get_booking_audit_log","arguments":{"booking_id":"33333333-3333-4333-8333-333333333333","limit":20}}
```

## get_earnings

**Get Meter Pay earnings** · roles: `anyone` · read-only · returns `EarningsSummary`

Summarize Meter Pay payouts (card payments transferred to a bank account) over a period as totals per currency and a day or week time series. scope "me" is the caller's own payouts and works for anyone with a payout account; scope "fleet" (owners/admins) covers every payout to the fleet and its members, optionally with a per-member breakdown. Cash fares and unpaid trips are NOT included; use get_accounting_summary for the full ledger including cash and balances. Defaults to the last 30 days.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `scope` | "me" \| "fleet" | no | `"me"` | "me": the caller's own Meter Pay payouts. "fleet": all payouts to the fleet and its members (owners/admins only). |
| `fleet_id` | string (uuid) | no |  | Fleet id from whoami or list_fleets. Optional when the caller belongs to exactly one fleet. |
| `start_date` | string | no |  | Inclusive period start. Default: 30 days ago. |
| `end_date` | string | no |  | Exclusive period end. Default: now. |
| `granularity` | "day" \| "week" | no | `"day"` | Bucket size for the time series. |
| `include_members` | boolean | no | `false` | With scope "fleet": also return a per-member breakdown (owners/admins only). |

Example:

```json
{"name":"get_earnings","arguments":{"scope":"fleet","fleet_id":"11111111-1111-4111-8111-111111111111","start_date":"2026-08-01","end_date":"2026-09-01","granularity":"week","include_members":true}}
```

## get_accounting_summary

**Get fleet accounting summary** · roles: `fleet_admin` · read-only · returns `AccountingSummary`

Fleet ledger rollup for owners and admins of an operational fleet: per currency, trip counts, gross, tips, card fees, driver earnings vs fleet cut, what was collected by card, cash or other means, what is not yet marked paid, and outstanding balances between fleet and drivers; plus the same per driver and reconciliation queue counts. Optional start_date/end_date (default all time) and distance_unit. Drivers get a permission error; use get_earnings scope "me" for a driver's own payouts.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string (uuid) | no |  | Fleet id from whoami or list_fleets. Optional when the caller belongs to exactly one fleet. |
| `start_date` | string | no |  | Inclusive period start. Default: all time. |
| `end_date` | string | no |  | Exclusive period end. Default: now. |
| `distance_unit` | "mile" \| "kilometer" | no | `"mile"` | Unit for per-distance figures. |

Example:

```json
{"name":"get_accounting_summary","arguments":{"fleet_id":"11111111-1111-4111-8111-111111111111","start_date":"2026-09-01","distance_unit":"mile"}}
```

## describe_api

**Describe the Meter MCP API** · roles: `anyone` · read-only

Self-documentation. Without arguments returns the full tool catalog: each tool's purpose, who may call it (roles), its arguments and an example call. With a tool name returns that tool in detail including the fields of its result. Use it when unsure which tool answers a question or what an argument means; use explain_data for the meaning and units of result fields. Free and available to any signed-in user.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `tool` | string | no |  | A tool name to describe in detail (arguments, roles, example call, result fields). Omit for the whole catalog. |

Example:

```json
{"name":"describe_api","arguments":{"tool":"list_trips"}}
```

## explain_data

**Explain result fields** · roles: `anyone` · read-only

Self-documentation for data. Given a tool name (and optionally a field name or dot path) returns the meaning, JSON type, unit (minor currency units, seconds, meters, ISO 8601), allowed enum values and role visibility of the fields in that tool's result, generated from the same schemas the server validates against. Use it before interpreting money, statuses or timestamps for a human. Free and available to any signed-in user.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `tool` | string | yes |  | The tool whose result you want explained, e.g. "list_trips". |
| `field` | string | no |  | A field name or dot path inside the result, e.g. "total_minor" or "items.pickup.address". Omit for every field. |

Example:

```json
{"name":"explain_data","arguments":{"tool":"list_trips","field":"total_minor"}}
```

## update_fleet_settings

**Update fleet settings** · roles: `fleet_admin` · writes (pass `dry_run: true` first; it defaults to false) · returns `FleetSettingsWrite`

Change a fleet's public and operational settings: name, description, contact/WhatsApp/dispatch phones, website, city, country, region, currency, timezone, brand colors, whether riders see driver locations, whether drivers may use custom fares, and out-of-zone pickup/drop-off rules. Owners and admins of an operational fleet only; drivers get a permission error. Pass only the fields to change; unknown fields are rejected. Call with dry_run: true first to preview the changes unless the human already gave exact values. Does NOT change fares, booking policy, service zones, the join code, payouts or billing; use update_ride_option, update_booking_settings or the web console for those.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string (uuid) | no |  | Fleet id from whoami or list_fleets. Optional when the caller belongs to exactly one fleet. |
| `dry_run` | boolean | no | `false` | When true, validate and authorize the request and return the would-be changes without writing anything. Use it first when the human has not confirmed exact values. |
| `name` | string | no |  | Fleet display name shown to riders. |
| `description` | string \| null | no |  | Public description shown on the booking page. Pass null to clear. |
| `contact_phone` | string \| null | no |  | Public contact phone riders can call. Pass null to clear. |
| `contact_whatsapp` | string \| null | no |  | Public WhatsApp number. Pass null to clear. |
| `dispatch_phone` | string \| null | no |  | Dispatch desk phone number. Pass null to clear. |
| `website` | string \| null | no |  | Public website URL including https://. Pass null to clear. |
| `city` | string | no |  | Primary city the fleet operates in. |
| `country_iso_code` | string | no |  | ISO 3166-1 alpha-2 country code, e.g. "US". |
| `region_iso_code` | string \| null | no |  | ISO 3166-2 region/state code, e.g. "TX". Pass null to clear. |
| `currency_iso_code` | string | no |  | ISO 4217 currency code, e.g. "USD". Changing it does not convert existing fares. |
| `timezone` | string | no |  | IANA timezone, e.g. "America/Chicago". |
| `primary_color` | string \| null | no |  | Brand primary color as #RRGGBB. Pass null to clear. |
| `secondary_color` | string \| null | no |  | Brand secondary color as #RRGGBB. Pass null to clear. |
| `show_driver_locations` | boolean | no |  | Whether riders see live driver locations on the public booking page. |
| `allow_fleet_custom_fares` | boolean | no |  | Whether drivers may run the meter with their own custom fares. |
| `allow_outside_origin_pickup` | boolean | no |  | Whether riders may request pickups outside the service zones. |
| `allow_outside_destination_dropoff` | boolean | no |  | Whether riders may request drop-offs outside the service zones. |

Example:

```json
{"name":"update_fleet_settings","arguments":{"fleet_id":"11111111-1111-4111-8111-111111111111","dry_run":true,"contact_phone":"+1 512 555 0100","website":"https://fleet-x.example"}}
```

## update_booking_settings

**Update booking settings** · roles: `fleet_admin` · writes (pass `dry_run: true` first; it defaults to false) · returns `BookingSettingsWrite`

Change a fleet's booking policy: dispatch mode (manual, all online drivers, auto-dispatch), payment mode (disabled, optional, pre-payment required), minimum lead time, hourly-booking slot size and minimum duration, rider cancellation fee fraction/minimum and free-cancellation grace period, driver cancellation reasons/fee mode/no-show wait/post-pickup rule, and owner booking emails. Owners and admins of an operational fleet only. Pass only the fields to change; values outside the allowed sets are rejected. Call with dry_run: true first to preview. Creates the booking settings record when the fleet has none yet. Not for fares or ride options (use update_ride_option).

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string (uuid) | no |  | Fleet id from whoami or list_fleets. Optional when the caller belongs to exactly one fleet. |
| `dry_run` | boolean | no | `false` | When true, validate and authorize the request and return the would-be changes without writing anything. Use it first when the human has not confirmed exact values. |
| `dispatch_mode` | "NONE" \| "ALL_ONLINE_DRIVERS" \| "AUTO_DISPATCH" | no |  | NONE: dispatcher assigns manually; ALL_ONLINE_DRIVERS: offer to every online driver; AUTO_DISPATCH: nearest available driver. |
| `payment_mode` | "disabled" \| "payments_optional" \| "pre_payment_required" | no |  | disabled: no card payments; payments_optional: riders may add a card; pre_payment_required: card authorized before dispatch. |
| `min_lead_time_seconds` | integer | no |  | Minimum notice between booking and pickup, in seconds (0 to 30 days). |
| `time_slot_minutes` | 15 \| 30 \| 45 \| 60 \| null | no |  | Hourly-booking slot size: 15, 30, 45 or 60. Null to unset. |
| `minimum_duration_minutes` | integer \| null | no |  | Minimum length of an hourly booking in minutes; must be a multiple of time_slot_minutes and at least one slot. Null to unset. |
| `cancellation_fee_fraction` | number | no |  | Rider cancellation fee as a fraction of the fare, 0 to 1. |
| `cancellation_fee_minimum_unit_amount` | integer | no |  | Minimum rider cancellation fee in minor currency units (e.g. 500 = $5.00). |
| `cancellation_grace_period_seconds` | 0 \| 300 \| 600 \| 1800 \| 3600 \| 21600 \| 43200 \| 86400 | no |  | Free-cancellation window after booking: 0, 300, 600, 1800, 3600, 21600, 43200 or 86400 seconds. |
| `driver_cancellation_allowed_reasons` | array of "vehicle_issue" \| "safety" \| "payment_dispute" \| "address_unreachable" \| "rider_request" \| "driver_other" | no |  | Reasons a driver may choose when cancelling an accepted booking. |
| `driver_cancellation_fee_mode` | "none" \| "standard_cancellation_fee" \| "support_review" | no |  | none: no fee when a driver cancels; standard_cancellation_fee: charge the standard fee; support_review: Meter support decides. |
| `driver_no_show_grace_period_seconds` | 0 \| 60 \| 180 \| 300 \| 600 \| 900 | no |  | How long a driver waits at pickup before reporting a no-show: 0, 60, 180, 300, 600 or 900 seconds. |
| `driver_post_pickup_cancellation_mode` | "disabled" \| "driver_cancel" \| "support_approval" | no |  | disabled: drivers cannot cancel after pickup; driver_cancel: they can; support_approval: Meter support must approve. |
| `owner_booking_email_enabled` | boolean | no |  | Email the fleet owner about each new booking. |

Example:

```json
{"name":"update_booking_settings","arguments":{"fleet_id":"11111111-1111-4111-8111-111111111111","dry_run":true,"min_lead_time_seconds":3600,"cancellation_grace_period_seconds":600,"payment_mode":"pre_payment_required"}}
```

## update_ride_option

**Update a ride option and its fare** · roles: `fleet_admin` · writes (pass `dry_run: true` first; it defaults to false) · returns `RideOptionWrite`

Edit an existing bookable ride option (vehicle class) of a fleet: its name and passenger capacity, and the rates of its default fare (base, minimum, per-mile/km distance rate, per-minute rate, waiting rate, tax rate, metric vs imperial, display name). Rates are in major currency units as shown in the console (2.75 = $2.75) and must be 0 to 10000. Owners and admins of an operational fleet only. Fare edits are written to the fleet's fare audit log with the caller as the actor, exactly like the console, and apply to every ride option sharing that fare; official government tariffs cannot be edited. Cannot create or delete ride options or change the fare's currency; use the web console. Preview with dry_run: true first.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `ride_option_id` | string (uuid) | yes |  | Ride option id from get_fleet ride_options[].id. |
| `fleet_id` | string (uuid) | no |  | Fleet id from whoami or list_fleets. Optional when the caller belongs to exactly one fleet. |
| `dry_run` | boolean | no | `false` | When true, validate and authorize the request and return the would-be changes without writing anything. Use it first when the human has not confirmed exact values. |
| `name` | string | no |  | Ride option name shown to riders, e.g. "Sedan". |
| `capacity` | integer | no |  | Passenger capacity, 1 to 60. |
| `fare` | object | no |  | Fare (rate card) fields to change on the ride option's default fare. Only pass the fields you intend to change. |

Example:

```json
{"name":"update_ride_option","arguments":{"ride_option_id":"44444444-4444-4444-8444-444444444444","fleet_id":"11111111-1111-4111-8111-111111111111","dry_run":true,"fare":{"base":3.5,"distance_rate":2.75,"minute_rate":0.5}}}
```

## assign_vehicle

**Assign or unassign a fleet vehicle** · roles: `fleet_admin` · writes (pass `dry_run: true` first; it defaults to false) · returns `VehicleAssignmentWrite`

Assign a fleet vehicle (vehicle_id from list_vehicles) to a fleet member (member_id from list_fleet_members), replacing whoever drives it today and releasing any other vehicle that member was assigned; or pass member_id: null to unassign the current driver. Owners and admins of an operational fleet only. The member must belong to the same fleet. Returns the vehicle with its assigned_driver after the change. Does not add, edit or remove vehicles or members; use the web console for that. Preview with dry_run: true first when unsure who currently drives the vehicle.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `vehicle_id` | string (uuid) | yes |  | Vehicle id from list_vehicles. |
| `fleet_id` | string (uuid) | no |  | Fleet id from whoami or list_fleets. Optional when the caller belongs to exactly one fleet. |
| `dry_run` | boolean | no | `false` | When true, validate and authorize the request and return the would-be changes without writing anything. Use it first when the human has not confirmed exact values. |
| `member_id` | string (uuid) \| null | yes |  | The driver to assign (member_id from list_fleet_members), or null to unassign whoever currently drives the vehicle. |

Example:

```json
{"name":"assign_vehicle","arguments":{"vehicle_id":"55555555-5555-4555-8555-555555555555","fleet_id":"11111111-1111-4111-8111-111111111111","member_id":"bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb","dry_run":true}}
```

## update_my_profile

**Update my profile** · roles: `anyone` · writes (pass `dry_run: true` first; it defaults to false) · returns `MyProfileWrite`

Change the signed-in person's OWN profile: first and last name, business name printed on receipts, preferred navigation app, and (with Meter Pro or a Fleet plan) hiding contact details on receipts and passing card fees to riders. Any signed-in user may call it; it can never change another person's profile. Never changes email, phone, role, fleet membership, payout, subscription or verification data; those are managed in the Meter app. Pass only the fields to change and preview with dry_run: true when the human has not confirmed the exact spelling.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dry_run` | boolean | no | `false` | When true, validate and authorize the request and return the would-be changes without writing anything. Use it first when the human has not confirmed exact values. |
| `first_name` | string | no |  | Your first name. An empty string clears it. |
| `last_name` | string | no |  | Your last name. An empty string clears it. |
| `company_name` | string \| null | no |  | Business name printed on your receipts. Null to clear. |
| `preferred_navigation_provider` | "in_app" \| "apple_maps" \| "google_maps" \| "waze" \| "naver_maps" | no |  | Navigation app the meter opens for directions. |
| `hide_contact_on_receipt` | boolean | no |  | Hide your phone and email on rider receipts. Requires Meter Pro or a Fleet plan. |
| `pass_credit_card_fees_to_customer` | boolean | no |  | Add the Meter Pay card fee to the rider total instead of absorbing it. Requires Meter Pro or a Fleet plan. |

Example:

```json
{"name":"update_my_profile","arguments":{"dry_run":true,"first_name":"Ada","preferred_navigation_provider":"google_maps"}}
```

## update_my_availability

**Update my weekly availability** · roles: `anyone` · writes (pass `dry_run: true` first; it defaults to false) · returns `DriverAvailabilityWrite`

Replace the signed-in driver's OWN weekly availability (the hours riders may book them for, per ISO weekday 1 = Monday to 7 = Sunday, as HH:MM shifts in an IANA timezone). The whole week is replaced: days omitted or given an empty shifts list become unavailable, so include every day the driver works. Shifts must end after they start and may not overlap. Any signed-in user may call it; it never changes another driver's schedule and does not affect fleet booking hours (use update_booking_settings for fleet policy). Preview with dry_run: true to see which days change.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dry_run` | boolean | no | `false` | When true, validate and authorize the request and return the would-be changes without writing anything. Use it first when the human has not confirmed exact values. |
| `timezone` | string | no |  | IANA timezone the shift times are in, e.g. "America/Chicago". Defaults to your current schedule timezone. |
| `days` | array of object | yes |  | The full weekly schedule. Every listed day is replaced; days not listed become unavailable. Each day_of_week at most once. |

Example:

```json
{"name":"update_my_availability","arguments":{"dry_run":true,"timezone":"America/Chicago","days":[{"day_of_week":1,"shifts":[{"start_time":"08:00","end_time":"18:00"}]},{"day_of_week":6,"shifts":[{"start_time":"10:00","end_time":"14:00"},{"start_time":"20:00","end_time":"23:30"}]}]}}
```

## get_onboarding_checklist

**Get fleet onboarding checklist** · roles: `fleet_admin` · read-only · returns `OnboardingChecklist`

Setup progress for a fleet the caller administers, as a checklist: fleet profile (name, contact, country, currency), brand icon, service area, at least one ride option with a fare, booking settings, at least one vehicle, at least one driver, payouts connected (a yes/no only), a shareable booking link, and the first booking received. Each item says whether it is done, whether riders can book without it, and how to complete it: the MCP tool to call (update_fleet_settings, update_ride_option, update_booking_settings, assign_vehicle) or the web page to send the human to. Also returns booking_page_status and the public booking URL. Owners and admins only; works on fleets that are not operational yet. Use it to drive a new fleet to its first booking.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string (uuid) | no |  | Fleet id from whoami or list_fleets. Optional when the caller belongs to exactly one fleet. |

Example:

```json
{"name":"get_onboarding_checklist","arguments":{"fleet_id":"11111111-1111-4111-8111-111111111111"}}
```
