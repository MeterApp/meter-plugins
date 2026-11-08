# Meter tools reference

Generated from the `@meterapp/meter-sdk` catalog and DTO schemas; do not edit by hand. See the [reference index](../tools.md) for all definitions.

## submit_feedback

**Submit feedback** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · writes (preview with `dry_run: true`, then confirm `proposal_id`) · returns `FeedbackSubmissionWrite`

Use dry_run to preview the complete public idea or private report, then apply its saved proposal after human confirmation. Actor, surface and Rio provenance come from verified server context. An id reused for different text is rejected.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dry_run` | boolean | no | `false` | When true, validate and authorize the request and return the would-be changes without writing anything. Always preview before confirming; calls without a saved preview write nothing. |
| `proposal_id` | string (uuid) | no |  | Saved proposal to confirm. Repeat the original intended arguments unchanged after showing the human all changes. |
| `type` | "idea" \| "issue" | yes |  | A public idea or private report. |
| `title` | string | no |  | Complete title; required for ideas. Reports derive a title when omitted. |
| `body` | string | yes |  | Complete text to submit, never silently truncated. |
| `category` | string | yes |  | Exact category id from list_feedback_categories. |
| `subject` | object | no |  | Optional authorized context for a private report. |
| `idempotency_key` | string (uuid) | yes |  | Client-generated id for this payload. Preserve it on retries; use a new id for a different payload. |

Example:

```json
{"name":"submit_feedback","arguments":{"type":"issue","body":"The meter display stopped updating","category":"meter_fares","idempotency_key":"11111111-1111-4111-8111-111111111111","dry_run":true}}
```
## vote_on_idea

**Vote on an idea** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · writes (preview with `dry_run: true`, then confirm `proposal_id`) · returns `FeedbackVoteWrite`

Use dry_run to preview and confirm the caller's vote on a currently visible idea. Voting may automatically follow it; a previous explicit unfollow is preserved. Private reports cannot be voted on.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dry_run` | boolean | no | `false` | When true, validate and authorize the request and return the would-be changes without writing anything. Always preview before confirming; calls without a saved preview write nothing. |
| `proposal_id` | string (uuid) | no |  | Saved proposal to confirm. Repeat the original intended arguments unchanged after showing the human all changes. |
| `item_id` | string (uuid) | yes |  | Identifier from an authorized feedback result. |
| `voted` | boolean | yes |  | Desired vote state; voting also follows unless previously unfollowed. |

Example:

```json
{"name":"vote_on_idea","arguments":{"item_id":"11111111-1111-4111-8111-111111111111","voted":true,"dry_run":true}}
```
## follow_feedback_item

**Follow feedback** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · writes (preview with `dry_run: true`, then confirm `proposal_id`) · returns `FeedbackFollowWrite`

Use dry_run to preview and confirm the caller's notification following state for an authorized idea or private report. Current visibility is required when confirming or recovering a saved result.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dry_run` | boolean | no | `false` | When true, validate and authorize the request and return the would-be changes without writing anything. Always preview before confirming; calls without a saved preview write nothing. |
| `proposal_id` | string (uuid) | no |  | Saved proposal to confirm. Repeat the original intended arguments unchanged after showing the human all changes. |
| `item_id` | string (uuid) | yes |  | Identifier from an authorized feedback result. |
| `following` | boolean | yes |  | Desired notification following state. |

Example:

```json
{"name":"follow_feedback_item","arguments":{"item_id":"11111111-1111-4111-8111-111111111111","following":true,"dry_run":true}}
```
## comment_on_feedback_item

**Comment on feedback** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · writes (preview with `dry_run: true`, then confirm `proposal_id`) · returns `FeedbackCommentWrite`

Use dry_run to preview the complete customer-visible comment, then apply its saved proposal after human confirmation. Locked or merged items reject new comments. Preserve the payload id when retrying an interrupted confirmation.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dry_run` | boolean | no | `false` | When true, validate and authorize the request and return the would-be changes without writing anything. Always preview before confirming; calls without a saved preview write nothing. |
| `proposal_id` | string (uuid) | no |  | Saved proposal to confirm. Repeat the original intended arguments unchanged after showing the human all changes. |
| `item_id` | string (uuid) | yes |  | Identifier from an authorized feedback result. |
| `body` | string | yes |  | Complete customer-visible comment text. |
| `idempotency_key` | string (uuid) | yes |  | Client-generated id for this payload. Preserve it on retries; use a new id for a different payload. |

Example:

```json
{"name":"comment_on_feedback_item","arguments":{"item_id":"11111111-1111-4111-8111-111111111111","body":"I also need an earlier reminder","idempotency_key":"22222222-2222-4222-8222-222222222222","dry_run":true}}
```
## list_feedback_categories

**List feedback categories** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · read-only · returns `FeedbackCategories`

Read localized category ids and labels accepted for reports and ideas. Use these exact ids when submitting feedback; reading categories does not create or modify any feedback.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | "idea" \| "issue" | no |  | Optional submission type; categories currently apply to both types. |

Example:

```json
{"name":"list_feedback_categories","arguments":{}}
```
## list_ideas

**List public ideas** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · read-only · returns `FeedbackItemPage`

Read published public ideas, including current votes and availability. Private reports and internal attribution are excluded.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `query` | string | no | `""` | Public idea search text; empty lists all public ideas. |
| `status` | string | no |  | Exact customer status id. |
| `category` | string | no |  | Category id from list_feedback_categories. |
| `sort` | "top" \| "new" \| "trending" | no | `"top"` | Vote, creation-time or recent-vote ordering. |
| `cursor` | string | no |  | Opaque continuation cursor from the preceding matching page. |
| `limit` | integer | no | `5` | Record count, 1–5. Use cursors for more records. |

Example:

```json
{"name":"list_ideas","arguments":{}}
```
## find_similar_ideas

**Find similar public ideas** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · read-only · returns `FeedbackSimilarIdeas`

Search for duplicate public ideas before suggesting a new idea. Returns up to five visible public items; private reports, hidden ideas and staff evidence are excluded.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `title` | string | yes |  | Proposed idea title to search for duplicates. |
| `details` | string | no |  | Optional additional search text; no private report content is returned. |

Example:

```json
{"name":"find_similar_ideas","arguments":{"title":"Improve booking reminders"}}
```
## list_my_feedback

**List my feedback** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · read-only · returns `FeedbackItemPage`

Read authored or followed feedback. Fleet scope requires current administrator or owner access; no operational fleet subscription is required.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `scope` | "authored" \| "following" \| "fleet" | no | `"authored"` | Authored or followed feedback; fleet requires current administrator or owner membership. |
| `type` | "idea" \| "issue" | no |  | Optional feedback kind. |
| `status` | string | no |  | Exact customer status id. |
| `cursor` | string | no |  | Opaque continuation cursor from the preceding matching page. |
| `limit` | integer | no | `5` | Record count, 1–5. Use cursors for more records. |

Example:

```json
{"name":"list_my_feedback","arguments":{}}
```
## get_feedback_item

**Get feedback detail** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · read-only · returns `FeedbackDetail`

Read a feedback item by identifier, or a published public idea by slug, including customer-visible comments and status history. Provide exactly one identifier. Current record authorization always applies.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `item_id` | string (uuid) | no |  | Feedback identifier; provide exactly one of item_id or slug. |
| `slug` | string | no |  | Public idea slug; provide exactly one of slug or item_id. |

Example:

```json
{"name":"get_feedback_item","arguments":{"item_id":"11111111-1111-4111-8111-111111111111"}}
```
## list_changelog

**List published changelog** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · read-only · returns `FeedbackChangelogPage`

Read actually published release notes, newest first. Draft and future-dated entries, staff identities and private feedback links are excluded.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `cursor` | string | no |  | Opaque continuation cursor from the preceding matching page. |
| `limit` | integer | no | `1` | Full release-note entries per page; one bounds complete 20,000-character bodies. |

Example:

```json
{"name":"list_changelog","arguments":{}}
```
## find_tools

**Find Meter tools** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · read-only

Find authorized Meter tools by keywords, optionally narrowed to a domain or operation kind. Includes on-demand tools and returns bounded names, titles, risks and descriptions. Discovery does not grant access or execute a tool; call the matching run tool with the target's arguments.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `query` | string | yes |  | English keywords for tool names, titles and descriptions. |
| `domain` | "meta" \| "account" \| "billing" \| "meter_pay" \| "fleet" \| "members" \| "vehicles" \| "fares" \| "bookings" \| "quotes" \| "trips" \| "customers" \| "accounting" \| "insights" \| "storefront" \| "help" \| "feedback" | no |  | Optional domain filter; omit to search every authorized domain. |
| `kind` | "read" \| "write" \| "handoff" | no |  | Optional operation kind; discovery does not execute it. |
| `limit` | integer | no | `10` | Maximum matches, 1-20; defaults to 10. |

Example:

```json
{"name":"find_tools","arguments":{"query":"booking settings","limit":10}}
```
## run_read_tool

**Run a Meter read tool** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · read-only

Execute a discovered read tool with its original arguments. The target's input validation, account and record permissions, kill switch, read quota and output limits still apply. Refuses writes, handoffs and nested dispatch tools; discovery never authorizes a hidden target.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `tool` | string | yes |  | Concrete tool name returned by find_tools; nested dispatch is refused. |
| `arguments` | object | yes |  | Original target arguments. Write preview and confirmation fields, including dry_run and proposal_id, belong inside this object. |

Example:

```json
{"name":"run_read_tool","arguments":{"tool":"get_fleet","arguments":{}}}
```
## run_write_tool

**Run a Meter write tool** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · writes (preview with `dry_run: true`, then confirm `proposal_id`)

Execute a discovered write tool with its original arguments through the normal guarded saved-proposal flow. Preview with arguments.dry_run=true and show all changes; confirmation requires the target's saved proposal. Target permissions, connection grants, quotas and kill switches still apply. Refuses reads, handoffs and nested dispatch tools.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `tool` | string | yes |  | Concrete tool name returned by find_tools; nested dispatch is refused. |
| `arguments` | object | yes |  | Original target arguments. Write preview and confirmation fields, including dry_run and proposal_id, belong inside this object. |

Example:

```json
{"name":"run_write_tool","arguments":{"tool":"update_my_profile","arguments":{"first_name":"Ada","dry_run":true}}}
```
## list_change_requests

**List my assistant changes** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · read-only · returns `ChangeRequestPage`

Read the signed-in person’s assistant change history. Filter by exact proposal id, status, tool, or creation time; use the returned cursor for older entries. Fleet owners cannot read another person’s assistant history. Returns previewed field changes and safe outcome metadata, never stored tool input, internal identifiers, raw results or internal errors. This read does not confirm or repeat a change.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | string (uuid) | no |  | Exact proposal id for meter changes show; still restricted to the signed-in actor. |
| `status` | "proposed" \| "applying" \| "applied" \| "declined" \| "expired" \| "stale" \| "failed" | no |  | Only include this proposal status. |
| `tool` | string | no |  | Only include changes proposed by this exact tool name. |
| `since` | string (date-time) | no |  | Only include proposals created at or after this ISO timestamp. |
| `limit` | integer | no | `25` | Maximum entries, 1–50; default 25. |
| `cursor` | string | no |  | Opaque next_cursor returned by the previous page. |

Example:

```json
{"name":"list_change_requests","arguments":{"limit":25}}
```
## whoami

**Who am I** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · read-only · returns `Whoami`

Call this first. Returns the signed-in person: profile (their own name, email and phone), every fleet they belong to with their role (owner, admin or driver), whether they are a rider, a plain-language list of what they can read here, and suggested_next_tools. Use it to decide which fleet_id to pass and which tools apply; do not call it repeatedly in one session. Any signed-in user may call it.

No arguments.

Example:

```json
{"name":"whoami","arguments":{}}
```
## describe_api

**Describe the Meter MCP API** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · read-only

Read API documentation only; never executes another tool or changes account data. Every authorized operation is advertised separately by tools/list with its own input schema and annotations. Without arguments returns a compact domain index with tool counts and listed tool names. With domain, describes that domain's tools, access, risk and sensitive-field escalations. With tool, returns full detail including arguments, an example call and result fields. Choose domain or tool. Responses are capped at 64 KB; use explain_data with a tool and field for more focused result-field documentation. Free and available to any signed-in user.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `domain` | "meta" \| "account" \| "billing" \| "meter_pay" \| "fleet" \| "members" \| "vehicles" \| "fares" \| "bookings" \| "quotes" \| "trips" \| "customers" \| "accounting" \| "insights" \| "storefront" \| "help" \| "feedback" | no |  | A domain whose tools should be described. Choose domain or tool; omit both for the compact domain index. |
| `tool` | string | no |  | A tool name to describe in detail (arguments, personas, risk, example call, result fields). Choose tool or domain; omit both for the domain index. |

Example:

```json
{"name":"describe_api","arguments":{"tool":"list_trips"}}
```
## explain_data

**Explain result fields** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · read-only

Self-documentation for data. Given a tool name (and optionally a field name or dot path) returns the meaning, JSON type, unit (minor currency units, seconds, meters, ISO 8601), allowed enum values and role visibility of the fields in that tool's result, generated from the same schemas the server validates against. Use it before interpreting money, statuses or timestamps for a human. Free and available to any signed-in user.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `tool` | string | yes |  | The tool whose result you want explained, e.g. "list_trips". |
| `field` | string | no |  | A field name or dot path inside the result, e.g. "total_minor" or "items.pickup.address". Omit for every field. |

Example:

```json
{"name":"explain_data","arguments":{"tool":"list_trips","field":"total_minor"}}
```
## quote_booking

**Estimate a booking** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · read-only · returns `BookingQuoteEstimate`

Estimate fleet estimate-v2 pricing or your personal fare; creates no booking, quote, preview, snapshot or acknowledgement. Nonmembers can price public listed and unlisted-slug fleets; owning operators can price unpublished storefronts. Deleted fleets are unavailable. Estimates do not establish booking eligibility. Supports point-to-point, metered, time and zone pricing with routing fallbacks. Amounts use currency minor units; no availability reservation, discounts or tips. Use get_action_link to continue booking in Meter.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string (uuid) | no |  | Fleet ID. Set exactly one of fleet_id or fare_id. |
| `fare_id` | string (uuid) | no |  | Your own personal fare ID; private fares of other drivers are unavailable. |
| `ride_option_id` | string (uuid) | no |  | Optional ride option belonging to the selected fleet. |
| `service_type` | "POINT_TO_POINT" \| "METERED" \| "TIME" | no | `"POINT_TO_POINT"` | Ride product. Personal fares support point-to-point only. |
| `origin` | object | yes |  | Pickup coordinates. |
| `destination` | object | no |  | Drop-off coordinates; required for point-to-point, optional for TIME. |
| `waypoints` | array of object | no |  | Up to ten intermediate stops, in travel order. |
| `start_timestamp` | string (date-time) | no |  | Scheduled pickup with timezone, at least one minute in the future; omit for ASAP. |
| `duration_minutes` | integer | no |  | TIME booking duration in minutes, matching fleet slot and minimum rules. |
| `passenger_count` | integer | no | `1` | Requested passengers; fleet estimate-v2 falls back to one above its maximum capacity. |
| `enable_payment_method_scoped_card_fees` | boolean | no | `false` | Match estimate-v2 opt-in: keep cash as active total and expose a separate card variant. Personal fares use their existing payment policy. |

Example:

```json
{"name":"quote_booking","arguments":{"fleet_id":"11111111-1111-4111-8111-111111111111","origin":{"latitude":40.7,"longitude":-74},"destination":{"latitude":40.8,"longitude":-73.9}}}
```
## list_bookings

**List bookings** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · read-only · returns `BookingPage`

List bookings (scheduled and on-demand rides) with status, scheduled time, pickup and drop-off, rider, assigned driver, ride option and upfront estimate. scope auto picks the widest view the caller has: fleet-wide for owners/admins, own assigned rides for drivers (including solo drivers with no fleet), own booked rides for riders. Filter by status, and by scheduled time with before/after; page with cursor (a scheduled-time cursor) and limit. Pending-payment bookings are hidden unless requested in status. For a full timeline of one booking call get_booking_audit_log.

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

**Get one booking** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · read-only · returns `Booking`

Fetch one booking by id with the same fields as list_bookings plus notes, flight number, cancellation reason and the linked trip id once completed. Allowed for owners/admins and members of the fleet, the assigned driver, and the rider who booked it; anyone else gets not-found. Rider contact details appear only for fleet owners/admins, the assigned driver, and the rider themselves. Use list_bookings to discover ids.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `booking_id` | string (uuid) | yes |  | Booking id from list_bookings. |

Example:

```json
{"name":"get_booking","arguments":{"booking_id":"33333333-3333-4333-8333-333333333333"}}
```
## get_booking_audit_log

**Get booking timeline** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · read-only · returns `BookingAuditLog`

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
## cancel_booking

**Cancel a booking** · personas: `fleet_owner, fleet_admin, fleet_driver, solo_driver, rider` · writes (preview with `dry_run: true`, then confirm `proposal_id`) · returns `BookingCancellationWrite`

Cancel an existing booking as its current administrator, assigned driver, solo owner or rider. Preview with dry_run: true and show the scheduled time, cancellation fee and currency. Apply only the saved proposal with identical arguments; changed terms refuse the write. The booking cancellation commits atomically; financial settlement is pending and may need manual handoff after an ambiguous attempt. Never claim a charge, refund or provider cancellation succeeded from this result. In-progress/support-review cancellations use the native support flow.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `booking_id` | string (uuid) | yes |  | Booking to cancel. |
| `cancellation_reason` | "rider_no_show" \| "vehicle_issue" \| "safety" \| "payment_dispute" \| "address_unreachable" \| "rider_request" \| "driver_other" \| "admin_other" \| null | no | `null` | Native cancellation reason; driver/admin other requires notes. |
| `cancellation_notes` | string \| null | no | `null` | Optional bounded cancellation notes. |
| `dry_run` | boolean | no | `false` | When true, validate and authorize the request and return the would-be changes without writing anything. Always preview before confirming; calls without a saved preview write nothing. |
| `proposal_id` | string (uuid) | no |  | Saved proposal to confirm. Repeat the original intended arguments unchanged after showing the human all changes. |

Example:

```json
{"name":"cancel_booking","arguments":{"booking_id":"33333333-3333-4333-8333-333333333333","dry_run":true}}
```
## find_fleets

**Find fleets to book** · personas: `rider` · read-only · returns `RiderFleetPage`

Find taxi fleets the rider can book: saved fleets first (is_saved), then publicly listed fleets serving the point given by near or address, or matching query anywhere. Returns public profile fields only: name, city, rating, payment at booking, ride products and the public booking page. Use a fleet_id with estimate_ride.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `near` | object | no |  | Point to search around, e.g. the pickup. |
| `address` | string | no |  | Address to search around when coordinates are unknown. |
| `query` | string | no |  | Fleet name or city text; searches beyond the nearby area. |
| `limit` | integer | no | `20` | Page size, 1-50 (default 20). |
| `cursor` | string | no |  | Opaque cursor from the previous page's next_cursor. Omit for the first page. |

Example:

```json
{"name":"find_fleets","arguments":{"near":{"latitude":40.7128,"longitude":-74.006}}}
```
## search_places

**Look up a place** · personas: `rider` · read-only · returns `PlaceSearch`

Turn text such as an address, airport or business into up to five candidate places with coordinates. Confirm the right candidate with the human when several are plausible, then pass it as pickup, dropoff or a stop. Rate limited per caller.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `query` | string | yes |  | Address, landmark or business to look up. |
| `near` | object | no |  | Bias results toward this point. |
| `limit` | integer | no | `5` | Maximum candidates, 1-5 (default 5). |

Example:

```json
{"name":"search_places","arguments":{"query":"JFK Terminal 4"}}
```
## estimate_ride

**Price a ride** · personas: `rider` · read-only · returns `RideEstimate`

Price a ride with one fleet: each ride option's price (minor units, currency, formatted, fixed/estimate/metered), capacity and cancellation policy, plus route distance and duration. Locations may be text (resolved server-side; ambiguous text is refused, use search_places) or places from search_places. Omit pickup_time for as soon as possible. Books nothing and holds no money. Rate limited per caller.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string (uuid) | yes |  | Fleet id from find_fleets. |
| `pickup` | string \| object | yes |  | Pickup location. |
| `dropoff` | string \| object | no |  | Drop-off location; required for fixed-price rides. |
| `stops` | array of string \| object | no |  | Up to 10 intermediate stops, in order. |
| `pickup_time` | string (date-time) | no |  | Pickup time, ISO 8601 with offset. Omit for as soon as possible. |
| `passengers` | integer | no | `1` | Passenger count (default 1). |
| `ride_option_id` | string (uuid) | no |  | Ride option from estimate_ride; omit for the recommended one. |
| `service_type` | "POINT_TO_POINT" \| "METERED" | no |  | POINT_TO_POINT (fixed price, the default) or METERED. When omitted, metered options are priced if the fleet has no fixed-price options. |

Example:

```json
{"name":"estimate_ride","arguments":{"fleet_id":"11111111-1111-4111-8111-111111111111","pickup":{"latitude":40.7128,"longitude":-74.006,"name":"Home"},"dropoff":"JFK Terminal 4"}}
```
## request_ride

**Request a ride** · personas: `rider` · writes (preview with `dry_run: true`, then confirm `proposal_id`) · returns `RideRequestWrite`

Book a ride for yourself with a fleet. Call with dry_run: true first and show the human the route, pickup time, ride option, price, how they pay and the cancellation policy; then repeat the same arguments with proposal_id after they confirm. When the fleet takes no payment at booking the ride is booked at once. When it does, most assistants get next_step send_checkout_link: nothing is booked yet; send the human the Meter link (valid 30 minutes) to confirm and pay there, then check list_bookings or get_ride_status. Meter's own apps hold the card already saved in the rider's account instead. Cards are never entered here. A changed price refuses the booking with a fresh preview. At most a few bookings per hour.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string (uuid) | yes |  | Fleet id from find_fleets. |
| `pickup` | string \| object | yes |  | Pickup location. |
| `dropoff` | string \| object | no |  | Drop-off location; required for fixed-price rides. |
| `stops` | array of string \| object | no |  | Up to 10 intermediate stops, in order. |
| `pickup_time` | string (date-time) | no |  | Pickup time, ISO 8601 with offset. Omit for as soon as possible. |
| `passengers` | integer | no | `1` | Passenger count (default 1). |
| `ride_option_id` | string (uuid) | no |  | Ride option from estimate_ride; omit for the recommended one. |
| `service_type` | "POINT_TO_POINT" \| "METERED" | no |  | POINT_TO_POINT (fixed price, the default) or METERED. When omitted, metered options are priced if the fleet has no fixed-price options. |
| `preferred_driver_id` | string (uuid) | no |  | Driver the rider asks for, if the fleet allows requests. |
| `notes` | string | no |  | Notes for the driver (gate code, luggage …). |
| `flight_number` | string | no |  | Flight number for an airport pickup. |
| `promo_code` | string | no |  | Fleet promo code. |
| `dry_run` | boolean | no | `false` | When true, validate and authorize the request and return the would-be changes without writing anything. Always preview before confirming; calls without a saved preview write nothing. |
| `proposal_id` | string (uuid) | no |  | Saved proposal to confirm. Repeat the original intended arguments unchanged after showing the human all changes. |

Example:

```json
{"name":"request_ride","arguments":{"fleet_id":"11111111-1111-4111-8111-111111111111","pickup":{"latitude":40.7128,"longitude":-74.006,"name":"Home"},"dropoff":"JFK Terminal 4","pickup_time":"2026-10-20T08:30:00-04:00","dry_run":true}}
```
## get_ride_status

**Check a ride** · personas: `rider` · read-only · returns `RideStatus`

Status of one of your own rides: stage, pickup and drop-off, scheduled time, the driver's first name, photo, phone and vehicle once assigned, ETA and driver position while the trip is live, what cancelling now would cost, and the receipt page once completed. Other people's bookings return not-found.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `booking_id` | string (uuid) | yes |  | Your booking id from request_ride or list_bookings. |

Example:

```json
{"name":"get_ride_status","arguments":{"booking_id":"33333333-3333-4333-8333-333333333333"}}
```
## change_ride

**Change a ride** · personas: `rider` · writes (preview with `dry_run: true`, then confirm `proposal_id`) · returns `RideChangeWrite`

Change the pickup time, pickup, drop-off or stops of one of your own bookings. Call with dry_run: true and show the human the new route, time and price (price_before, price_after, price_change_minor); confirm with proposal_id. When next_step is open_link the change needs a higher card hold, which Meter never takes in chat for this assistant: send the human action_link to change and pay on the booking page, and do not confirm. Pickup and time changes close shortly before pickup (the fleet's policy).

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `booking_id` | string (uuid) | yes |  | Your booking id from list_bookings or request_ride. |
| `pickup_time` | string (date-time) | no |  | New pickup time, ISO 8601 with offset. Scheduled rides only. |
| `pickup` | string \| object | no |  | New pickup location. |
| `dropoff` | string \| object | no |  | New drop-off location. |
| `stops` | array of string \| object | no |  | Replacement stops in order; [] removes every stop. |
| `dry_run` | boolean | no | `false` | When true, validate and authorize the request and return the would-be changes without writing anything. Always preview before confirming; calls without a saved preview write nothing. |
| `proposal_id` | string (uuid) | no |  | Saved proposal to confirm. Repeat the original intended arguments unchanged after showing the human all changes. |

Example:

```json
{"name":"change_ride","arguments":{"booking_id":"33333333-3333-4333-8333-333333333333","pickup_time":"2026-10-20T09:00:00-04:00","dry_run":true}}
```
## update_ride_details

**Edit ride notes or flight** · personas: `rider` · writes (preview with `dry_run: true`, then confirm `proposal_id`) · returns `RideDetailsWrite`

Set or clear the driver notes or the flight number of one of your own upcoming bookings. Preview with dry_run: true, then confirm with proposal_id. A flight number that matches no flight on the pickup date is refused. The price never changes.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `booking_id` | string (uuid) | yes |  | Your booking id from list_bookings or request_ride. |
| `notes` | string \| null | no |  | Notes the driver sees (gate code, luggage …); null clears. |
| `flight_number` | string \| null | no |  | Flight number for an airport pickup, e.g. DL5463; null clears. It must match a real flight on the pickup date. |
| `dry_run` | boolean | no | `false` | When true, validate and authorize the request and return the would-be changes without writing anything. Always preview before confirming; calls without a saved preview write nothing. |
| `proposal_id` | string (uuid) | no |  | Saved proposal to confirm. Repeat the original intended arguments unchanged after showing the human all changes. |

Example:

```json
{"name":"update_ride_details","arguments":{"booking_id":"33333333-3333-4333-8333-333333333333","notes":"Gate code 4512","dry_run":true}}
```
## respond_to_quote

**Accept or decline a quote** · personas: `rider` · writes (preview with `dry_run: true`, then confirm `proposal_id`) · returns `QuoteResponseWrite`

Answer a quote a fleet sent you. Preview with dry_run: true and show the route, time, price, expiry and how payment works; confirm with proposal_id. Accepting books the ride. When payment is meter_page (next_step open_link) the human accepts and pays on Meter's quote page: send action_link and do not confirm. Declining is final and tells the fleet.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `quote_id` | string (uuid) | yes |  | Quote id from list_quotes or get_quote. |
| `decision` | "accept" \| "decline" | yes |  | accept books the quoted ride; decline turns it down. |
| `reason` | string | no |  | Why you decline, shared with the fleet. Decline only. |
| `dry_run` | boolean | no | `false` | When true, validate and authorize the request and return the would-be changes without writing anything. Always preview before confirming; calls without a saved preview write nothing. |
| `proposal_id` | string (uuid) | no |  | Saved proposal to confirm. Repeat the original intended arguments unchanged after showing the human all changes. |

Example:

```json
{"name":"respond_to_quote","arguments":{"quote_id":"11111111-1111-4111-8111-111111111111","decision":"accept","dry_run":true}}
```
## get_rating_prompt

**Ride waiting for a rating** · personas: `rider` · read-only · returns `RatingPrompt`

Your newest completed ride that still waits for a rating (within a week of the ride), or null, plus the reason codes rate_ride accepts. Use it after a ride ends to offer rating and tipping.

No arguments.

Example:

```json
{"name":"get_rating_prompt","arguments":{}}
```
## rate_ride

**Rate a ride** · personas: `rider` · writes (preview with `dry_run: true`, then confirm `proposal_id`) · returns `RideRatingWrite`

Rate one of your own completed rides 1-5 stars with optional reasons and comment, within 30 days of the ride. Rating again replaces your earlier rating. Preview with dry_run: true, then confirm with proposal_id. The result includes tip_link, a Meter page where the human may tip; tipping never happens in chat.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `booking_id` | string (uuid) | yes |  | Your booking id from list_bookings or request_ride. |
| `rating` | integer | yes |  | Stars, 1-5. |
| `tags` | array of "friendly_professional" \| "excellent_driving" \| "clean_vehicle" \| "on_time" \| "helpful_luggage" \| "great_communication" \| "smooth_pickup_dropoff" \| "driver_behavior" \| "driving_safety" \| "vehicle_cleanliness" \| "driver_late" \| "pickup_dropoff_issue" \| "incorrect_route" \| "communication_problem" \| "vehicle_condition" \| "booking_dispatch_problem" \| "pricing_issue" \| "app_problem" \| "payment_problem" \| "notification_problem" \| "wrong_fare_shown" \| "trip_status_wrong" \| "other" | no |  | Reasons from get_rating_prompt: compliments with 4-5 stars, issues with 1-3 stars. |
| `comment` | string | no |  | Optional comment for the fleet. |
| `dry_run` | boolean | no | `false` | When true, validate and authorize the request and return the would-be changes without writing anything. Always preview before confirming; calls without a saved preview write nothing. |
| `proposal_id` | string (uuid) | no |  | Saved proposal to confirm. Repeat the original intended arguments unchanged after showing the human all changes. |

Example:

```json
{"name":"rate_ride","arguments":{"booking_id":"33333333-3333-4333-8333-333333333333","rating":5,"tags":["on_time"],"dry_run":true}}
```
## report_ride_issue

**Report a ride problem** · personas: `rider` · writes (preview with `dry_run: true`, then confirm `proposal_id`) · returns `RideIssueReportWrite`

Report an app, booking, dispatch or payment problem with one of your own bookings to Meter support, including cancelled ones. It never changes a rating and is not shown to the driver. Preview with dry_run: true, then confirm with proposal_id; the result carries a support reference number. Refunds go through get_action_link request_refund.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `booking_id` | string (uuid) | yes |  | Your booking id from list_bookings or request_ride. |
| `category` | "app_problem" \| "notification_problem" \| "booking_problem" \| "dispatch_problem" \| "wrong_fare_shown" \| "payment_problem" \| "trip_status_wrong" \| "other" | yes |  | What kind of problem. |
| `description` | string | yes |  | What happened, in the rider's words. |
| `dry_run` | boolean | no | `false` | When true, validate and authorize the request and return the would-be changes without writing anything. Always preview before confirming; calls without a saved preview write nothing. |
| `proposal_id` | string (uuid) | no |  | Saved proposal to confirm. Repeat the original intended arguments unchanged after showing the human all changes. |

Example:

```json
{"name":"report_ride_issue","arguments":{"booking_id":"33333333-3333-4333-8333-333333333333","category":"payment_problem","description":"I was charged twice for this ride.","dry_run":true}}
```
## list_quotes

**List quotes** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · read-only · returns `QuotePage`

Read bounded currently authorized stored quote facts. Does not create estimates, contact riders, reserve bookings, or query payment providers.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `scope` | "me" \| "fleet" \| "rider" | no | `"me"` | Individually owned quotes, selected fleet quotes, or quotes attached to the caller as rider. Fleet drivers see only their authored or preferred-driver quotes. |
| `fleet_id` | string (uuid) | no |  | Fleet id from whoami or list_fleets. Optional when the caller belongs to exactly one fleet. |
| `status` | array of "draft" \| "open" \| "converted" \| "declined" \| "expired" \| "withdrawn" | no |  | Stored lifecycle statuses to include; omitted includes all statuses. |
| `cursor` | string | no |  | Opaque cursor from the previous page's next_cursor. Omit for the first page. |
| `limit` | integer | no | `50` | Page size, 1-100 (default 50). |

Example:

```json
{"name":"list_quotes","arguments":{"scope":"me","limit":50}}
```
## get_quote

**Get quote** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · read-only · returns `QuoteDetail`

Read one currently authorized stored quote summary. Stored prices and lifecycle timestamps are facts; they do not prove delivery or payment acceptance.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `scope` | "me" \| "fleet" \| "rider" | no | `"me"` | Individually owned quotes, selected fleet quotes, or quotes attached to the caller as rider. Fleet drivers see only their authored or preferred-driver quotes. |
| `fleet_id` | string (uuid) | no |  | Fleet id from whoami or list_fleets. Optional when the caller belongs to exactly one fleet. |
| `quote_id` | string (uuid) | yes |  | Quote identifier from list_quotes. |

Example:

```json
{"name":"get_quote","arguments":{"scope":"me","quote_id":"11111111-1111-4111-8111-111111111111"}}
```
## get_action_link

**Open a human action in Meter** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · read-only · returns `ActionLink`

Return a Meter link for the human to finish purchases, subscription management, Meter Pay setup, dispute evidence, refund requests, document uploads (a member's: edit_fleet_member), contact changes, deletion, map drawing or downloads. Present the link unchanged with its instructions. This tool never purchases, pays, refunds, deletes, uploads or creates a provider session. Fleet billing and deletion require the owner; other fleet management actions require an owner or admin.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `action` | "subscribe_pro" \| "subscribe_fleet" \| "manage_subscription" \| "manage_store_subscription" \| "change_plan" \| "cancel_subscription" \| "update_payment_method" \| "meter_pay_setup" \| "meter_pay_manage" \| "respond_to_dispute" \| "request_refund" \| "upload_documents" \| "edit_fleet_member" \| "change_email" \| "change_phone" \| "delete_account" \| "delete_fleet" \| "upload_fleet_icon" \| "draw_service_area" \| "download_pay_stub" \| "download_export" \| "add_payment_method" \| "finish_ride_payment" \| "track_ride" \| "review_quote" \| "tip_ride" | yes |  |  |
| `fleet_id` | string (uuid) | no |  | Fleet for fleet actions or a rider's add_payment_method. Meter Pay and subscriptions default to your own account. |
| `target_id` | string (uuid) | no |  | Dispute case or trip ID (respond_to_dispute, request_refund), your booking ID (track_ride, finish_ride_payment, tip_ride), a quote ID sent to you (review_quote), or a member_id (edit_fleet_member). Never a payment-provider ID. |

Example:

```json
{"name":"get_action_link","arguments":{"action":"meter_pay_setup"}}
```
## get_meter_pay_status

**Get Meter Pay status** · personas: `solo_driver, fleet_driver, fleet_admin, fleet_owner, rider` · read-only · returns `MeterPayStatus`

Read Meter Pay payment and payout readiness, missing information and account/fleet Tap to Pay eligibility. Defaults to your own account; explicit fleet scope requires owner/admin access. Never creates or changes a payment account. Status may be cached for 60 seconds; uncached provider reads are limited to 10/minute. Use get_action_link with management_action (and the returned fleet_id for fleet scope) to continue setup or management in Meter.

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `scope` | "me" \| "fleet" | no | `"me"` | Own account by default, even for a fleet admin. Fleet scope requires owner/admin access. |
| `fleet_id` | string (uuid) | no |  | Fleet to inspect with fleet scope. May be omitted only for a sole fleet membership. |

Example:

```json
{"name":"get_meter_pay_status","arguments":{"scope":"me"}}
```
