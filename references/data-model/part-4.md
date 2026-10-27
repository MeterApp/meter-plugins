# Meter data-model reference

Generated from the `@meterapp/meter-sdk` catalog and DTO schemas; do not edit by hand. See the [reference index](../data-model.md) for all definitions.

## BookingChangeWrite

Preview or confirmed saved booking change with immutable outcome.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `status` | string (optional) |  | everyone | Saved-proposal outcome; absent on older servers. |
| `proposal` | object\|null (optional) |  | everyone | Saved proposal and expiry. Confirm its exact changes before applying; absent on older servers. |
| `proposal.id` | string |  | everyone | Opaque saved proposal id. |
| `proposal.notes` | array (optional) |  | everyone | Warnings and consequences to show alongside the exact changes before confirmation; absent on older servers or when there are no notes. |
| `proposal.notes[].code` | string |  | everyone | Stable warning or explanatory-note code. |
| `proposal.notes[].text` | string |  | everyone | Human-readable consequence or context to show with the proposed changes. |
| `proposal.status` | string |  | everyone | Current saved proposal state; unknown future states must be preserved. |
| `proposal.risk` | enum |  | everyone | Effective risk after field-level escalation. Values: `low`, `standard`, `sensitive`. |
| `proposal.expires_at` | string |  | everyone | Time after which this proposal can no longer be applied. |
| `proposal.applied_at` | string\|null (optional) |  | everyone | Time the proposal was applied, if it was applied. |
| `proposal.replayed` | boolean (optional) |  | everyone | True when returning a stored result without applying again. |
| `applied` | boolean |  | everyone | True when the change was written. False on a dry run or when nothing differed from the current values. |
| `dry_run` | boolean |  | everyone | True when the call was a preview: values were validated and authorized but nothing was written. |
| `changes` | array |  | everyone | Field-level changes (empty when every requested value already matched). Summarize these back to the human. |
| `changes[].field` | string |  | everyone | Name of the changed argument, exactly as passed to the tool (e.g. "contact_phone", "fare.base"). |
| `changes[].from` | string\|number\|boolean\|null\|array\|array |  | everyone | Value before the change. |
| `changes[].to` | string\|number\|boolean\|null\|array\|array |  | everyone | Value after the change. |
| `booking` | object |  | everyone | Immutable minimal booking outcome; read current details with get_booking. |
| `booking.booking_id` | string |  | everyone | Booking identifier for get_booking. |
| `booking.status` | enum |  | everyone | Booking status frozen at command completion. Values: `pending`, `confirmed`, `in_progress`, `completed`, `canceled`, `pending_payment`. |
| `booking.assigned_driver_id` | string\|null |  | everyone | Assigned driver at completion, or null when unassigned. |
| `booking.rider_id` | string\|null |  | everyone | Rider attached at completion, or null when absent. |
## BookingLifecycle

Immutable minimal outcome of a driver or dispatcher booking step; read current details with get_booking.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `booking_id` | string |  | everyone | Booking identifier for get_booking. |
| `event` | enum |  | everyone | What this command recorded on the booking. Values: `accepted`, `enroute_to_pickup`, `arrived_at_pickup`, `picked_up`, `completed`, `no_show_reported`, `pickup_time_changed`. |
| `status` | enum |  | everyone | Booking status frozen at command completion. Values: `pending`, `confirmed`, `in_progress`, `completed`, `canceled`, `pending_payment`. |
| `assigned_driver_id` | string\|null |  | everyone | Assigned driver at completion, or null when unassigned. |
| `scheduled_time` | string | ISO 8601 | everyone | ISO 8601 timestamp with offset (UTC unless noted). |
| `trip_id` | string\|null |  | everyone | Trip created by completion, for get_trip; null for every other event. |
| `rider_confirmation_pending` | boolean |  | everyone | True when a new pickup time changed the price and the rider must accept it before it takes effect; the booking keeps its old time until then. |
## BookingLifecycleWrite

Preview or confirmed saved booking step with immutable outcome.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `status` | string (optional) |  | everyone | Saved-proposal outcome; absent on older servers. |
| `proposal` | object\|null (optional) |  | everyone | Saved proposal and expiry. Confirm its exact changes before applying; absent on older servers. |
| `proposal.id` | string |  | everyone | Opaque saved proposal id. |
| `proposal.notes` | array (optional) |  | everyone | Warnings and consequences to show alongside the exact changes before confirmation; absent on older servers or when there are no notes. |
| `proposal.notes[].code` | string |  | everyone | Stable warning or explanatory-note code. |
| `proposal.notes[].text` | string |  | everyone | Human-readable consequence or context to show with the proposed changes. |
| `proposal.status` | string |  | everyone | Current saved proposal state; unknown future states must be preserved. |
| `proposal.risk` | enum |  | everyone | Effective risk after field-level escalation. Values: `low`, `standard`, `sensitive`. |
| `proposal.expires_at` | string |  | everyone | Time after which this proposal can no longer be applied. |
| `proposal.applied_at` | string\|null (optional) |  | everyone | Time the proposal was applied, if it was applied. |
| `proposal.replayed` | boolean (optional) |  | everyone | True when returning a stored result without applying again. |
| `applied` | boolean |  | everyone | True when the change was written. False on a dry run or when nothing differed from the current values. |
| `dry_run` | boolean |  | everyone | True when the call was a preview: values were validated and authorized but nothing was written. |
| `changes` | array |  | everyone | Field-level changes (empty when every requested value already matched). Summarize these back to the human. |
| `changes[].field` | string |  | everyone | Name of the changed argument, exactly as passed to the tool (e.g. "contact_phone", "fare.base"). |
| `changes[].from` | string\|number\|boolean\|null\|array\|array |  | everyone | Value before the change. |
| `changes[].to` | string\|number\|boolean\|null\|array\|array |  | everyone | Value after the change. |
| `booking` | object |  | everyone | Immutable minimal outcome of a driver or dispatcher booking step; read current details with get_booking. |
| `booking.booking_id` | string |  | everyone | Booking identifier for get_booking. |
| `booking.event` | enum |  | everyone | What this command recorded on the booking. Values: `accepted`, `enroute_to_pickup`, `arrived_at_pickup`, `picked_up`, `completed`, `no_show_reported`, `pickup_time_changed`. |
| `booking.status` | enum |  | everyone | Booking status frozen at command completion. Values: `pending`, `confirmed`, `in_progress`, `completed`, `canceled`, `pending_payment`. |
| `booking.assigned_driver_id` | string\|null |  | everyone | Assigned driver at completion, or null when unassigned. |
| `booking.scheduled_time` | string | ISO 8601 | everyone | ISO 8601 timestamp with offset (UTC unless noted). |
| `booking.trip_id` | string\|null |  | everyone | Trip created by completion, for get_trip; null for every other event. |
| `booking.rider_confirmation_pending` | boolean |  | everyone | True when a new pickup time changed the price and the rider must accept it before it takes effect; the booking keeps its old time until then. |
## DispatchOffer

A ride offered to the calling driver by realtime dispatch. Offers expire within seconds to minutes.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `dispatch_id` | string |  | everyone | Offer to pass to respond_to_dispatch_offer. |
| `booking_id` | string |  | everyone | Offered booking, for get_booking. |
| `status` | enum |  | everyone | pending: waiting for this driver; accepted/declined: answered; expired: the driver did not answer in time; cancelled: withdrawn because the booking went to someone else or stopped waiting for a driver. Values: `pending`, `accepted`, `declined`, `expired`, `cancelled`. |
| `expires_at` | string | ISO 8601 | everyone | ISO 8601 timestamp with offset (UTC unless noted). |
| `scheduled_time` | string\|null | ISO 8601 | everyone | ISO 8601 timestamp with offset, or null when not (yet) known. |
| `pickup` | object\|null |  | everyone | A pickup or drop-off place. Coordinates and raw GPS are never exposed here. |
| `pickup.name` | string\|null |  | everyone | Short place name (e.g. business or airport name), or null. |
| `pickup.address` | string\|null |  | everyone | Formatted street address, or null. |
| `dropoff` | object\|null |  | everyone | A pickup or drop-off place. Coordinates and raw GPS are never exposed here. |
| `dropoff.name` | string\|null |  | everyone | Short place name (e.g. business or airport name), or null. |
| `dropoff.address` | string\|null |  | everyone | Formatted street address, or null. |
| `pickup_distance_meters` | number\|null | meters | everyone | Driving distance from the driver to the pickup when offered. |
| `pickup_duration_seconds` | number\|null | seconds | everyone | Driving time from the driver to the pickup when offered. |
| `trip_distance_meters` | number\|null | meters | everyone | Pickup-to-drop-off route distance. |
| `trip_duration_seconds` | number\|null | seconds | everyone | Pickup-to-drop-off route duration. |
| `expected_payout` | number\|null | minor currency units | everyone | What the driver is expected to earn after fees and fleet share, in minor units; null when unknown. |
| `currency` | string\|null |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
## DispatchOffers

Pending dispatch offers.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `items` | array |  | everyone | The caller's offers that are still waiting for an answer; empty when none. |
| `items[].dispatch_id` | string |  | everyone | Offer to pass to respond_to_dispatch_offer. |
| `items[].booking_id` | string |  | everyone | Offered booking, for get_booking. |
| `items[].status` | enum |  | everyone | pending: waiting for this driver; accepted/declined: answered; expired: the driver did not answer in time; cancelled: withdrawn because the booking went to someone else or stopped waiting for a driver. Values: `pending`, `accepted`, `declined`, `expired`, `cancelled`. |
| `items[].expires_at` | string | ISO 8601 | everyone | ISO 8601 timestamp with offset (UTC unless noted). |
| `items[].scheduled_time` | string\|null | ISO 8601 | everyone | ISO 8601 timestamp with offset, or null when not (yet) known. |
| `items[].pickup` | object\|null |  | everyone | A pickup or drop-off place. Coordinates and raw GPS are never exposed here. |
| `items[].pickup.name` | string\|null |  | everyone | Short place name (e.g. business or airport name), or null. |
| `items[].pickup.address` | string\|null |  | everyone | Formatted street address, or null. |
| `items[].dropoff` | object\|null |  | everyone | A pickup or drop-off place. Coordinates and raw GPS are never exposed here. |
| `items[].dropoff.name` | string\|null |  | everyone | Short place name (e.g. business or airport name), or null. |
| `items[].dropoff.address` | string\|null |  | everyone | Formatted street address, or null. |
| `items[].pickup_distance_meters` | number\|null | meters | everyone | Driving distance from the driver to the pickup when offered. |
| `items[].pickup_duration_seconds` | number\|null | seconds | everyone | Driving time from the driver to the pickup when offered. |
| `items[].trip_distance_meters` | number\|null | meters | everyone | Pickup-to-drop-off route distance. |
| `items[].trip_duration_seconds` | number\|null | seconds | everyone | Pickup-to-drop-off route duration. |
| `items[].expected_payout` | number\|null | minor currency units | everyone | What the driver is expected to earn after fees and fleet share, in minor units; null when unknown. |
| `items[].currency` | string\|null |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
## DispatchOfferWrite

Preview or confirmed answer to a dispatch offer.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `status` | string (optional) |  | everyone | Saved-proposal outcome; absent on older servers. |
| `proposal` | object\|null (optional) |  | everyone | Saved proposal and expiry. Confirm its exact changes before applying; absent on older servers. |
| `proposal.id` | string |  | everyone | Opaque saved proposal id. |
| `proposal.notes` | array (optional) |  | everyone | Warnings and consequences to show alongside the exact changes before confirmation; absent on older servers or when there are no notes. |
| `proposal.notes[].code` | string |  | everyone | Stable warning or explanatory-note code. |
| `proposal.notes[].text` | string |  | everyone | Human-readable consequence or context to show with the proposed changes. |
| `proposal.status` | string |  | everyone | Current saved proposal state; unknown future states must be preserved. |
| `proposal.risk` | enum |  | everyone | Effective risk after field-level escalation. Values: `low`, `standard`, `sensitive`. |
| `proposal.expires_at` | string |  | everyone | Time after which this proposal can no longer be applied. |
| `proposal.applied_at` | string\|null (optional) |  | everyone | Time the proposal was applied, if it was applied. |
| `proposal.replayed` | boolean (optional) |  | everyone | True when returning a stored result without applying again. |
| `applied` | boolean |  | everyone | True when the change was written. False on a dry run or when nothing differed from the current values. |
| `dry_run` | boolean |  | everyone | True when the call was a preview: values were validated and authorized but nothing was written. |
| `changes` | array |  | everyone | Field-level changes (empty when every requested value already matched). Summarize these back to the human. |
| `changes[].field` | string |  | everyone | Name of the changed argument, exactly as passed to the tool (e.g. "contact_phone", "fare.base"). |
| `changes[].from` | string\|number\|boolean\|null\|array\|array |  | everyone | Value before the change. |
| `changes[].to` | string\|number\|boolean\|null\|array\|array |  | everyone | Value after the change. |
| `dispatch_offer` | object |  | everyone | A ride offered to the calling driver by realtime dispatch. Offers expire within seconds to minutes. |
| `dispatch_offer.dispatch_id` | string |  | everyone | Offer to pass to respond_to_dispatch_offer. |
| `dispatch_offer.booking_id` | string |  | everyone | Offered booking, for get_booking. |
| `dispatch_offer.status` | enum |  | everyone | pending: waiting for this driver; accepted/declined: answered; expired: the driver did not answer in time; cancelled: withdrawn because the booking went to someone else or stopped waiting for a driver. Values: `pending`, `accepted`, `declined`, `expired`, `cancelled`. |
| `dispatch_offer.expires_at` | string | ISO 8601 | everyone | ISO 8601 timestamp with offset (UTC unless noted). |
| `dispatch_offer.scheduled_time` | string\|null | ISO 8601 | everyone | ISO 8601 timestamp with offset, or null when not (yet) known. |
| `dispatch_offer.pickup` | object\|null |  | everyone | A pickup or drop-off place. Coordinates and raw GPS are never exposed here. |
| `dispatch_offer.pickup.name` | string\|null |  | everyone | Short place name (e.g. business or airport name), or null. |
| `dispatch_offer.pickup.address` | string\|null |  | everyone | Formatted street address, or null. |
| `dispatch_offer.dropoff` | object\|null |  | everyone | A pickup or drop-off place. Coordinates and raw GPS are never exposed here. |
| `dispatch_offer.dropoff.name` | string\|null |  | everyone | Short place name (e.g. business or airport name), or null. |
| `dispatch_offer.dropoff.address` | string\|null |  | everyone | Formatted street address, or null. |
| `dispatch_offer.pickup_distance_meters` | number\|null | meters | everyone | Driving distance from the driver to the pickup when offered. |
| `dispatch_offer.pickup_duration_seconds` | number\|null | seconds | everyone | Driving time from the driver to the pickup when offered. |
| `dispatch_offer.trip_distance_meters` | number\|null | meters | everyone | Pickup-to-drop-off route distance. |
| `dispatch_offer.trip_duration_seconds` | number\|null | seconds | everyone | Pickup-to-drop-off route duration. |
| `dispatch_offer.expected_payout` | number\|null | minor currency units | everyone | What the driver is expected to earn after fees and fleet share, in minor units; null when unknown. |
| `dispatch_offer.currency` | string\|null |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
## Customer

A rider who has booked with the fleet (or with a solo driver). Contact fields follow the web console's customer list.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `rider_id` | string |  | everyone | Rider id for get_customer, update_booking or quotes. |
| `first_name` | string\|null |  | everyone | Rider first name, or null. |
| `last_name` | string\|null |  | everyone | Rider last name, or null. |
| `phone` | string\|null |  | owner, admin, self | Rider phone (E.164), or null. Only fleet owners/admins and the solo driver who serves the rider see it. |
| `email` | string\|null |  | owner, admin, self | Rider email, or null. Only fleet owners/admins and the solo driver who serves the rider see it. |
| `first_seen_at` | string | ISO 8601 | everyone | When the rider first booked with this fleet or driver. |
| `last_booking_at` | string\|null | ISO 8601 | everyone | When the rider last booked, or null. |
## CustomerPage

Customers, most recent booking first.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `items` | array |  | everyone | The page of results, newest first unless the tool says otherwise. |
| `items[].rider_id` | string |  | everyone | Rider id for get_customer, update_booking or quotes. |
| `items[].first_name` | string\|null |  | everyone | Rider first name, or null. |
| `items[].last_name` | string\|null |  | everyone | Rider last name, or null. |
| `items[].phone` | string\|null |  | owner, admin, self | Rider phone (E.164), or null. Only fleet owners/admins and the solo driver who serves the rider see it. |
| `items[].email` | string\|null |  | owner, admin, self | Rider email, or null. Only fleet owners/admins and the solo driver who serves the rider see it. |
| `items[].first_seen_at` | string | ISO 8601 | everyone | When the rider first booked with this fleet or driver. |
| `items[].last_booking_at` | string\|null | ISO 8601 | everyone | When the rider last booked, or null. |
| `next_cursor` | string\|null |  | everyone | Pass this back as `cursor` to fetch the next page. Null when there are no more results. |
| `has_more` | boolean |  | everyone | True when another page exists. |
## CustomerDetail

One customer with their recent bookings.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `customer` | object |  | everyone | A rider who has booked with the fleet (or with a solo driver). Contact fields follow the web console's customer list. |
| `customer.rider_id` | string |  | everyone | Rider id for get_customer, update_booking or quotes. |
| `customer.first_name` | string\|null |  | everyone | Rider first name, or null. |
| `customer.last_name` | string\|null |  | everyone | Rider last name, or null. |
| `customer.phone` | string\|null |  | owner, admin, self | Rider phone (E.164), or null. Only fleet owners/admins and the solo driver who serves the rider see it. |
| `customer.email` | string\|null |  | owner, admin, self | Rider email, or null. Only fleet owners/admins and the solo driver who serves the rider see it. |
| `customer.first_seen_at` | string | ISO 8601 | everyone | When the rider first booked with this fleet or driver. |
| `customer.last_booking_at` | string\|null | ISO 8601 | everyone | When the rider last booked, or null. |
| `recent_bookings` | array |  | everyone | Up to 20 of the rider's bookings with this fleet or driver, newest first. |
| `recent_bookings[].booking_id` | string |  | everyone | Booking id for get_booking. |
| `recent_bookings[].status` | enum |  | everyone | Booking status. Values: `pending`, `confirmed`, `in_progress`, `completed`, `canceled`, `pending_payment`. |
| `recent_bookings[].scheduled_time` | string\|null | ISO 8601 | everyone | ISO 8601 timestamp with offset, or null when not (yet) known. |
## CustomerWrite

Preview or result of create_customer / update_customer: the customer as the Customers page lists them (null in a preview of a customer Meter does not know yet).

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `status` | string (optional) |  | everyone | Saved-proposal outcome; absent on older servers. |
| `proposal` | object\|null (optional) |  | everyone | Saved proposal and expiry. Confirm its exact changes before applying; absent on older servers. |
| `proposal.id` | string |  | everyone | Opaque saved proposal id. |
| `proposal.notes` | array (optional) |  | everyone | Warnings and consequences to show alongside the exact changes before confirmation; absent on older servers or when there are no notes. |
| `proposal.notes[].code` | string |  | everyone | Stable warning or explanatory-note code. |
| `proposal.notes[].text` | string |  | everyone | Human-readable consequence or context to show with the proposed changes. |
| `proposal.status` | string |  | everyone | Current saved proposal state; unknown future states must be preserved. |
| `proposal.risk` | enum |  | everyone | Effective risk after field-level escalation. Values: `low`, `standard`, `sensitive`. |
| `proposal.expires_at` | string |  | everyone | Time after which this proposal can no longer be applied. |
| `proposal.applied_at` | string\|null (optional) |  | everyone | Time the proposal was applied, if it was applied. |
| `proposal.replayed` | boolean (optional) |  | everyone | True when returning a stored result without applying again. |
| `applied` | boolean |  | everyone | True when the change was written. False on a dry run or when nothing differed from the current values. |
| `dry_run` | boolean |  | everyone | True when the call was a preview: values were validated and authorized but nothing was written. |
| `changes` | array |  | everyone | Field-level changes (empty when every requested value already matched). Summarize these back to the human. |
| `changes[].field` | string |  | everyone | Name of the changed argument, exactly as passed to the tool (e.g. "contact_phone", "fare.base"). |
| `changes[].from` | string\|number\|boolean\|null\|array\|array |  | everyone | Value before the change. |
| `changes[].to` | string\|number\|boolean\|null\|array\|array |  | everyone | Value after the change. |
| `customer` | object\|null |  | everyone | A rider who has booked with the fleet (or with a solo driver). Contact fields follow the web console's customer list. |
| `customer.rider_id` | string |  | everyone | Rider id for get_customer, update_booking or quotes. |
| `customer.first_name` | string\|null |  | everyone | Rider first name, or null. |
| `customer.last_name` | string\|null |  | everyone | Rider last name, or null. |
| `customer.phone` | string\|null |  | owner, admin, self | Rider phone (E.164), or null. Only fleet owners/admins and the solo driver who serves the rider see it. |
| `customer.email` | string\|null |  | owner, admin, self | Rider email, or null. Only fleet owners/admins and the solo driver who serves the rider see it. |
| `customer.first_seen_at` | string | ISO 8601 | everyone | When the rider first booked with this fleet or driver. |
| `customer.last_booking_at` | string\|null | ISO 8601 | everyone | When the rider last booked, or null. |
## CustomerImport

A customer import: what each row would do (preview) or did (applied).

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string\|null |  | everyone | Fleet the customers belong to, or null for a solo driver's own customers. |
| `totals` | object |  | everyone | Row counts by status. |
| `totals.rows` | number |  | everyone | Rows received. |
| `totals.create` | number |  | everyone | New riders. |
| `totals.add_existing` | number |  | everyone | Existing Meter riders added as customers. |
| `totals.update_name` | number |  | everyone | Existing customers whose missing name is filled. |
| `totals.unchanged` | number |  | everyone | Already customers with nothing to change. |
| `totals.duplicate` | number |  | everyone | Rows repeating an earlier phone or email. |
| `totals.invalid` | number |  | everyone | Rows skipped. |
| `totals.failed` | number |  | everyone | Rows that could not be written (0 in a preview). |
| `rows` | array |  | everyone | Every row with its status, in request order. |
| `rows[].row` | number |  | everyone | 1-based position of the row in the request (CSV rows count from the first line after the header). |
| `rows[].status` | enum |  | everyone | create: a new Meter rider is created and added; add_existing: a rider Meter already knows is added to your customers; update_name: an existing customer gets the missing first/last name; unchanged: already a customer, nothing to do; duplicate: same phone or email as an earlier row, skipped; invalid: skipped, see reason; failed: the row could not be written, see reason. Values: `create`, `add_existing`, `update_name`, `unchanged`, `duplicate`, `invalid`, `failed`. |
| `rows[].reason` | string\|null |  | everyone | Why the row is invalid, a duplicate or failed; null otherwise. |
| `rows[].rider_id` | string\|null |  | everyone | Customer id once known (existing riders in a preview, every written row after confirming); null otherwise. |
| `rows[].first_name` | string\|null |  | everyone | First name from the row, or null. |
| `rows[].last_name` | string\|null |  | everyone | Last name from the row, or null. |
| `rows[].phone` | string\|null |  | owner, admin, self | Phone normalized to E.164, or null. |
| `rows[].email` | string\|null |  | owner, admin, self | Email from the row (lower-case), or null. Used only to find a rider Meter already knows. |
## CustomerImportWrite

Preview or result of import_customers.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `status` | string (optional) |  | everyone | Saved-proposal outcome; absent on older servers. |
| `proposal` | object\|null (optional) |  | everyone | Saved proposal and expiry. Confirm its exact changes before applying; absent on older servers. |
| `proposal.id` | string |  | everyone | Opaque saved proposal id. |
| `proposal.notes` | array (optional) |  | everyone | Warnings and consequences to show alongside the exact changes before confirmation; absent on older servers or when there are no notes. |
| `proposal.notes[].code` | string |  | everyone | Stable warning or explanatory-note code. |
| `proposal.notes[].text` | string |  | everyone | Human-readable consequence or context to show with the proposed changes. |
| `proposal.status` | string |  | everyone | Current saved proposal state; unknown future states must be preserved. |
| `proposal.risk` | enum |  | everyone | Effective risk after field-level escalation. Values: `low`, `standard`, `sensitive`. |
| `proposal.expires_at` | string |  | everyone | Time after which this proposal can no longer be applied. |
| `proposal.applied_at` | string\|null (optional) |  | everyone | Time the proposal was applied, if it was applied. |
| `proposal.replayed` | boolean (optional) |  | everyone | True when returning a stored result without applying again. |
| `applied` | boolean |  | everyone | True when the change was written. False on a dry run or when nothing differed from the current values. |
| `dry_run` | boolean |  | everyone | True when the call was a preview: values were validated and authorized but nothing was written. |
| `changes` | array |  | everyone | Field-level changes (empty when every requested value already matched). Summarize these back to the human. |
| `changes[].field` | string |  | everyone | Name of the changed argument, exactly as passed to the tool (e.g. "contact_phone", "fare.base"). |
| `changes[].from` | string\|number\|boolean\|null\|array\|array |  | everyone | Value before the change. |
| `changes[].to` | string\|number\|boolean\|null\|array\|array |  | everyone | Value after the change. |
| `import` | object |  | everyone | A customer import: what each row would do (preview) or did (applied). |
| `import.fleet_id` | string\|null |  | everyone | Fleet the customers belong to, or null for a solo driver's own customers. |
| `import.totals` | object |  | everyone | Row counts by status. |
| `import.totals.rows` | number |  | everyone | Rows received. |
| `import.totals.create` | number |  | everyone | New riders. |
| `import.totals.add_existing` | number |  | everyone | Existing Meter riders added as customers. |
| `import.totals.update_name` | number |  | everyone | Existing customers whose missing name is filled. |
| `import.totals.unchanged` | number |  | everyone | Already customers with nothing to change. |
| `import.totals.duplicate` | number |  | everyone | Rows repeating an earlier phone or email. |
| `import.totals.invalid` | number |  | everyone | Rows skipped. |
| `import.totals.failed` | number |  | everyone | Rows that could not be written (0 in a preview). |
| `import.rows` | array |  | everyone | Every row with its status, in request order. |
| `import.rows[].row` | number |  | everyone | 1-based position of the row in the request (CSV rows count from the first line after the header). |
| `import.rows[].status` | enum |  | everyone | create: a new Meter rider is created and added; add_existing: a rider Meter already knows is added to your customers; update_name: an existing customer gets the missing first/last name; unchanged: already a customer, nothing to do; duplicate: same phone or email as an earlier row, skipped; invalid: skipped, see reason; failed: the row could not be written, see reason. Values: `create`, `add_existing`, `update_name`, `unchanged`, `duplicate`, `invalid`, `failed`. |
| `import.rows[].reason` | string\|null |  | everyone | Why the row is invalid, a duplicate or failed; null otherwise. |
| `import.rows[].rider_id` | string\|null |  | everyone | Customer id once known (existing riders in a preview, every written row after confirming); null otherwise. |
| `import.rows[].first_name` | string\|null |  | everyone | First name from the row, or null. |
| `import.rows[].last_name` | string\|null |  | everyone | Last name from the row, or null. |
| `import.rows[].phone` | string\|null |  | owner, admin, self | Phone normalized to E.164, or null. |
| `import.rows[].email` | string\|null |  | owner, admin, self | Email from the row (lower-case), or null. Used only to find a rider Meter already knows. |
## OperatorBooking

A booking an operator creates for a customer: preview, or the created booking.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `booking_id` | string\|null |  | everyone | Created booking id for get_booking; null in a preview. |
| `status` | enum\|null |  | everyone | Booking status after creation; null in a preview. Values: `pending`, `confirmed`, `in_progress`, `completed`, `canceled`, `pending_payment`. |
| `fleet_id` | string |  | everyone | Fleet taking the booking. |
| `fleet_name` | string\|null |  | everyone | Fleet display name. |
| `customer` | object |  | everyone | Who rides. |
| `customer.rider_id` | string\|null |  | everyone | Customer id; null in a preview of a customer Meter does not know yet. |
| `customer.first_name` | string\|null |  | everyone | First name, or null. |
| `customer.last_name` | string\|null |  | everyone | Last name, or null. |
| `customer.phone` | string\|null |  | owner, admin, self | Phone (E.164), or null. |
| `customer.email` | string\|null |  | owner, admin, self | Email, or null. |
| `customer.is_new` | boolean |  | everyone | True when confirming creates this customer (a new Meter rider or a rider new to your customers). |
| `pickup` | object |  | everyone | Pickup. |
| `pickup.name` | string\|null |  | everyone | Place name, or null. |
| `pickup.address` | string\|null |  | everyone | Formatted address, or null. |
| `dropoff` | object\|null |  | everyone | Drop-off, or null for a metered ride without one. |
| `dropoff.name` | string\|null |  | everyone | Place name, or null. |
| `dropoff.address` | string\|null |  | everyone | Formatted address, or null. |
| `stops` | array |  | everyone | Intermediate stops in order. |
| `stops[].name` | string\|null |  | everyone | Place name, or null. |
| `stops[].address` | string\|null |  | everyone | Formatted address, or null. |
| `pickup_time` | string\|null | ISO 8601 | everyone | Pickup time (ISO 8601 with offset), or null for as soon as possible. |
| `timezone` | string\|null |  | everyone | IANA timezone of the pickup. |
| `passengers` | number |  | everyone | Passenger count. |
| `ride_option` | object |  | everyone | Ride option booked. |
| `ride_option.ride_option_id` | string |  | everyone | Ride option id. |
| `ride_option.name` | string |  | everyone | Ride option name. |
| `ride_option.capacity` | number\|null |  | everyone | Maximum passengers, or null. |
| `price` | object |  | everyone | Quoted fare the customer pays. |
| `price.amount_minor` | number | minor currency units | everyone | Price the rider is quoted, in minor units. |
| `price.currency` | string |  | everyone | ISO 4217 currency code, upper-case. |
| `price.display` | string |  | everyone | Price formatted for the human in the request locale. |
| `price.mode` | enum |  | everyone | fixed: the quoted price is the fare; estimate: the final fare can change (for example overtime); metered: charged by the meter, the amount is an estimate. Values: `fixed`, `estimate`, `metered`. |
| `price.disclosure` | string\|null |  | everyone | Pricing disclosure to show the human before confirming, or null. |
| `payment` | enum |  | everyone | after_trip: nothing is charged at booking; the customer pays the driver after the ride (cash, card in person or an invoice). For upfront payment through a Meter link use create_quote then send_quote instead. Values: `after_trip`. |
| `cancellation_policy` | object |  | everyone | Cancellation policy that applies to the customer. |
| `cancellation_policy.grace_period_seconds` | number | seconds | everyone | Free cancellation window after booking. |
| `cancellation_policy.fee_minor` | number\|null | minor currency units | everyone | Fee for cancelling after the free window, in minor units; null when unknown or none. |
| `cancellation_policy.currency` | string\|null |  | everyone | Currency of the fee, or null. |
| `cancellation_policy.summary` | string |  | everyone | One-sentence policy summary for the human. |
| `notes` | string\|null |  | everyone | Notes for the driver, or null. |
| `flight_number` | string\|null |  | everyone | Flight number, or null. |
| `driver_id` | string\|null |  | everyone | Driver requested for the booking, or null for the fleet's dispatch to pick one. |
| `driver_assignment` | enum |  | everyone | none: no driver chosen. requested: a preview that assigns driver_id on confirm. assigned: the driver has the booking. failed: the booking exists but the assignment was refused; use assign_booking. Values: `none`, `requested`, `assigned`, `failed`. |
| `customer_notifications` | array |  | everyone | How the customer is told about the booking (confirmation with a tracking link). Empty when Meter has no phone or email for them. |
## OperatorBookingWrite

Preview or result of create_booking.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `status` | string (optional) |  | everyone | Saved-proposal outcome; absent on older servers. |
| `proposal` | object\|null (optional) |  | everyone | Saved proposal and expiry. Confirm its exact changes before applying; absent on older servers. |
| `proposal.id` | string |  | everyone | Opaque saved proposal id. |
| `proposal.notes` | array (optional) |  | everyone | Warnings and consequences to show alongside the exact changes before confirmation; absent on older servers or when there are no notes. |
| `proposal.notes[].code` | string |  | everyone | Stable warning or explanatory-note code. |
| `proposal.notes[].text` | string |  | everyone | Human-readable consequence or context to show with the proposed changes. |
| `proposal.status` | string |  | everyone | Current saved proposal state; unknown future states must be preserved. |
| `proposal.risk` | enum |  | everyone | Effective risk after field-level escalation. Values: `low`, `standard`, `sensitive`. |
| `proposal.expires_at` | string |  | everyone | Time after which this proposal can no longer be applied. |
| `proposal.applied_at` | string\|null (optional) |  | everyone | Time the proposal was applied, if it was applied. |
| `proposal.replayed` | boolean (optional) |  | everyone | True when returning a stored result without applying again. |
| `applied` | boolean |  | everyone | True when the change was written. False on a dry run or when nothing differed from the current values. |
| `dry_run` | boolean |  | everyone | True when the call was a preview: values were validated and authorized but nothing was written. |
| `changes` | array |  | everyone | Field-level changes (empty when every requested value already matched). Summarize these back to the human. |
| `changes[].field` | string |  | everyone | Name of the changed argument, exactly as passed to the tool (e.g. "contact_phone", "fare.base"). |
| `changes[].from` | string\|number\|boolean\|null\|array\|array |  | everyone | Value before the change. |
| `changes[].to` | string\|number\|boolean\|null\|array\|array |  | everyone | Value after the change. |
| `booking` | object |  | everyone | A booking an operator creates for a customer: preview, or the created booking. |
| `booking.booking_id` | string\|null |  | everyone | Created booking id for get_booking; null in a preview. |
| `booking.status` | enum\|null |  | everyone | Booking status after creation; null in a preview. Values: `pending`, `confirmed`, `in_progress`, `completed`, `canceled`, `pending_payment`. |
| `booking.fleet_id` | string |  | everyone | Fleet taking the booking. |
| `booking.fleet_name` | string\|null |  | everyone | Fleet display name. |
| `booking.customer` | object |  | everyone | Who rides. |
| `booking.customer.rider_id` | string\|null |  | everyone | Customer id; null in a preview of a customer Meter does not know yet. |
| `booking.customer.first_name` | string\|null |  | everyone | First name, or null. |
| `booking.customer.last_name` | string\|null |  | everyone | Last name, or null. |
| `booking.customer.phone` | string\|null |  | owner, admin, self | Phone (E.164), or null. |
| `booking.customer.email` | string\|null |  | owner, admin, self | Email, or null. |
| `booking.customer.is_new` | boolean |  | everyone | True when confirming creates this customer (a new Meter rider or a rider new to your customers). |
| `booking.pickup` | object |  | everyone | Pickup. |
| `booking.pickup.name` | string\|null |  | everyone | Place name, or null. |
| `booking.pickup.address` | string\|null |  | everyone | Formatted address, or null. |
| `booking.dropoff` | object\|null |  | everyone | Drop-off, or null for a metered ride without one. |
| `booking.dropoff.name` | string\|null |  | everyone | Place name, or null. |
| `booking.dropoff.address` | string\|null |  | everyone | Formatted address, or null. |
| `booking.stops` | array |  | everyone | Intermediate stops in order. |
| `booking.stops[].name` | string\|null |  | everyone | Place name, or null. |
| `booking.stops[].address` | string\|null |  | everyone | Formatted address, or null. |
| `booking.pickup_time` | string\|null | ISO 8601 | everyone | Pickup time (ISO 8601 with offset), or null for as soon as possible. |
| `booking.timezone` | string\|null |  | everyone | IANA timezone of the pickup. |
| `booking.passengers` | number |  | everyone | Passenger count. |
| `booking.ride_option` | object |  | everyone | Ride option booked. |
| `booking.ride_option.ride_option_id` | string |  | everyone | Ride option id. |
| `booking.ride_option.name` | string |  | everyone | Ride option name. |
| `booking.ride_option.capacity` | number\|null |  | everyone | Maximum passengers, or null. |
| `booking.price` | object |  | everyone | Quoted fare the customer pays. |
| `booking.price.amount_minor` | number | minor currency units | everyone | Price the rider is quoted, in minor units. |
| `booking.price.currency` | string |  | everyone | ISO 4217 currency code, upper-case. |
| `booking.price.display` | string |  | everyone | Price formatted for the human in the request locale. |
| `booking.price.mode` | enum |  | everyone | fixed: the quoted price is the fare; estimate: the final fare can change (for example overtime); metered: charged by the meter, the amount is an estimate. Values: `fixed`, `estimate`, `metered`. |
| `booking.price.disclosure` | string\|null |  | everyone | Pricing disclosure to show the human before confirming, or null. |
| `booking.payment` | enum |  | everyone | after_trip: nothing is charged at booking; the customer pays the driver after the ride (cash, card in person or an invoice). For upfront payment through a Meter link use create_quote then send_quote instead. Values: `after_trip`. |
| `booking.cancellation_policy` | object |  | everyone | Cancellation policy that applies to the customer. |
| `booking.cancellation_policy.grace_period_seconds` | number | seconds | everyone | Free cancellation window after booking. |
| `booking.cancellation_policy.fee_minor` | number\|null | minor currency units | everyone | Fee for cancelling after the free window, in minor units; null when unknown or none. |
| `booking.cancellation_policy.currency` | string\|null |  | everyone | Currency of the fee, or null. |
| `booking.cancellation_policy.summary` | string |  | everyone | One-sentence policy summary for the human. |
| `booking.notes` | string\|null |  | everyone | Notes for the driver, or null. |
| `booking.flight_number` | string\|null |  | everyone | Flight number, or null. |
| `booking.driver_id` | string\|null |  | everyone | Driver requested for the booking, or null for the fleet's dispatch to pick one. |
| `booking.driver_assignment` | enum |  | everyone | none: no driver chosen. requested: a preview that assigns driver_id on confirm. assigned: the driver has the booking. failed: the booking exists but the assignment was refused; use assign_booking. Values: `none`, `requested`, `assigned`, `failed`. |
| `booking.customer_notifications` | array |  | everyone | How the customer is told about the booking (confirmation with a tracking link). Empty when Meter has no phone or email for them. |
## QuoteBookingConversion

A quote turned into a booking by its operator.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `quote_id` | string |  | everyone | Quote converted. |
| `quote_status` | string |  | everyone | Quote status: open/draft in a preview, converted after confirming. |
| `booking_id` | string\|null |  | everyone | Booking created from the quote for get_booking; null in a preview. |
| `booking_status` | enum\|null |  | everyone | Booking status after creation; null in a preview. Values: `pending`, `confirmed`, `in_progress`, `completed`, `canceled`, `pending_payment`. |
| `pickup_at` | string\|null | ISO 8601 | everyone | Quoted pickup time (ISO 8601). |
| `currency` | string |  | everyone | ISO 4217 currency code. |
| `total_unit_amount` | number\|null | minor currency units | everyone | Fare the customer pays (custom price when set), in minor units. |
| `payment` | enum |  | everyone | after_trip: the customer pays the driver after the ride; nothing is charged now. Values: `after_trip`. |
| `driver_id` | string\|null |  | everyone | Driver to assign (fleet quotes), or null. |
| `driver_assignment` | enum |  | everyone | none, requested (preview), assigned, or failed (booking exists; use assign_booking). Values: `none`, `requested`, `assigned`, `failed`. |
## QuoteBookingConversionWrite

Preview or result of book_quote.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `status` | string (optional) |  | everyone | Saved-proposal outcome; absent on older servers. |
| `proposal` | object\|null (optional) |  | everyone | Saved proposal and expiry. Confirm its exact changes before applying; absent on older servers. |
| `proposal.id` | string |  | everyone | Opaque saved proposal id. |
| `proposal.notes` | array (optional) |  | everyone | Warnings and consequences to show alongside the exact changes before confirmation; absent on older servers or when there are no notes. |
| `proposal.notes[].code` | string |  | everyone | Stable warning or explanatory-note code. |
| `proposal.notes[].text` | string |  | everyone | Human-readable consequence or context to show with the proposed changes. |
| `proposal.status` | string |  | everyone | Current saved proposal state; unknown future states must be preserved. |
| `proposal.risk` | enum |  | everyone | Effective risk after field-level escalation. Values: `low`, `standard`, `sensitive`. |
| `proposal.expires_at` | string |  | everyone | Time after which this proposal can no longer be applied. |
| `proposal.applied_at` | string\|null (optional) |  | everyone | Time the proposal was applied, if it was applied. |
| `proposal.replayed` | boolean (optional) |  | everyone | True when returning a stored result without applying again. |
| `applied` | boolean |  | everyone | True when the change was written. False on a dry run or when nothing differed from the current values. |
| `dry_run` | boolean |  | everyone | True when the call was a preview: values were validated and authorized but nothing was written. |
| `changes` | array |  | everyone | Field-level changes (empty when every requested value already matched). Summarize these back to the human. |
| `changes[].field` | string |  | everyone | Name of the changed argument, exactly as passed to the tool (e.g. "contact_phone", "fare.base"). |
| `changes[].from` | string\|number\|boolean\|null\|array\|array |  | everyone | Value before the change. |
| `changes[].to` | string\|number\|boolean\|null\|array\|array |  | everyone | Value after the change. |
| `conversion` | object |  | everyone | A quote turned into a booking by its operator. |
| `conversion.quote_id` | string |  | everyone | Quote converted. |
| `conversion.quote_status` | string |  | everyone | Quote status: open/draft in a preview, converted after confirming. |
| `conversion.booking_id` | string\|null |  | everyone | Booking created from the quote for get_booking; null in a preview. |
| `conversion.booking_status` | enum\|null |  | everyone | Booking status after creation; null in a preview. Values: `pending`, `confirmed`, `in_progress`, `completed`, `canceled`, `pending_payment`. |
| `conversion.pickup_at` | string\|null | ISO 8601 | everyone | Quoted pickup time (ISO 8601). |
| `conversion.currency` | string |  | everyone | ISO 4217 currency code. |
| `conversion.total_unit_amount` | number\|null | minor currency units | everyone | Fare the customer pays (custom price when set), in minor units. |
| `conversion.payment` | enum |  | everyone | after_trip: the customer pays the driver after the ride; nothing is charged now. Values: `after_trip`. |
| `conversion.driver_id` | string\|null |  | everyone | Driver to assign (fleet quotes), or null. |
| `conversion.driver_assignment` | enum |  | everyone | none, requested (preview), assigned, or failed (booking exists; use assign_booking). Values: `none`, `requested`, `assigned`, `failed`. |
## TripVoidRequest

A request to void a fleet trip and its review. Approving refunds a paid card trip.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `void_request_id` | string |  | everyone | Void request id. |
| `trip_id` | string |  | everyone | Trip the request is for, for get_trip. |
| `status` | enum |  | everyone | pending: waiting for a fleet owner/admin; approved: the trip is voided (a paid card trip was refunded); rejected: the trip stands. Values: `pending`, `approved`, `rejected`. |
| `reason` | string |  | everyone | Why the void was requested. |
| `requested_by` | string |  | everyone | Member who asked for the void. |
| `requested_at` | string | ISO 8601 | everyone | ISO 8601 timestamp with offset (UTC unless noted). |
| `reviewed_by` | string\|null |  | everyone | Owner/admin who approved or rejected it, or null. |
| `reviewed_at` | string\|null | ISO 8601 | everyone | ISO 8601 timestamp with offset, or null when not (yet) known. |
| `review_note` | string\|null |  | everyone | Reviewer's note, or null. |
## TripVoidRequestWrite

Preview or confirmed trip void request or review.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `status` | string (optional) |  | everyone | Saved-proposal outcome; absent on older servers. |
| `proposal` | object\|null (optional) |  | everyone | Saved proposal and expiry. Confirm its exact changes before applying; absent on older servers. |
| `proposal.id` | string |  | everyone | Opaque saved proposal id. |
| `proposal.notes` | array (optional) |  | everyone | Warnings and consequences to show alongside the exact changes before confirmation; absent on older servers or when there are no notes. |
| `proposal.notes[].code` | string |  | everyone | Stable warning or explanatory-note code. |
| `proposal.notes[].text` | string |  | everyone | Human-readable consequence or context to show with the proposed changes. |
| `proposal.status` | string |  | everyone | Current saved proposal state; unknown future states must be preserved. |
| `proposal.risk` | enum |  | everyone | Effective risk after field-level escalation. Values: `low`, `standard`, `sensitive`. |
| `proposal.expires_at` | string |  | everyone | Time after which this proposal can no longer be applied. |
| `proposal.applied_at` | string\|null (optional) |  | everyone | Time the proposal was applied, if it was applied. |
| `proposal.replayed` | boolean (optional) |  | everyone | True when returning a stored result without applying again. |
| `applied` | boolean |  | everyone | True when the change was written. False on a dry run or when nothing differed from the current values. |
| `dry_run` | boolean |  | everyone | True when the call was a preview: values were validated and authorized but nothing was written. |
| `changes` | array |  | everyone | Field-level changes (empty when every requested value already matched). Summarize these back to the human. |
| `changes[].field` | string |  | everyone | Name of the changed argument, exactly as passed to the tool (e.g. "contact_phone", "fare.base"). |
| `changes[].from` | string\|number\|boolean\|null\|array\|array |  | everyone | Value before the change. |
| `changes[].to` | string\|number\|boolean\|null\|array\|array |  | everyone | Value after the change. |
| `void_request` | object |  | everyone | A request to void a fleet trip and its review. Approving refunds a paid card trip. |
| `void_request.void_request_id` | string |  | everyone | Void request id. |
| `void_request.trip_id` | string |  | everyone | Trip the request is for, for get_trip. |
| `void_request.status` | enum |  | everyone | pending: waiting for a fleet owner/admin; approved: the trip is voided (a paid card trip was refunded); rejected: the trip stands. Values: `pending`, `approved`, `rejected`. |
| `void_request.reason` | string |  | everyone | Why the void was requested. |
| `void_request.requested_by` | string |  | everyone | Member who asked for the void. |
| `void_request.requested_at` | string | ISO 8601 | everyone | ISO 8601 timestamp with offset (UTC unless noted). |
| `void_request.reviewed_by` | string\|null |  | everyone | Owner/admin who approved or rejected it, or null. |
| `void_request.reviewed_at` | string\|null | ISO 8601 | everyone | ISO 8601 timestamp with offset, or null when not (yet) known. |
| `void_request.review_note` | string\|null |  | everyone | Reviewer's note, or null. |
## TripNote

A trip's private internal note.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `trip_id` | string |  | everyone | Trip id, for get_trip. |
| `internal_note` | string\|null |  | owner, admin, self | Private note seen only by the trip's driver and fleet owners/admins; null when cleared. |
## TripNoteWrite

Preview or confirmed trip note change.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `status` | string (optional) |  | everyone | Saved-proposal outcome; absent on older servers. |
| `proposal` | object\|null (optional) |  | everyone | Saved proposal and expiry. Confirm its exact changes before applying; absent on older servers. |
| `proposal.id` | string |  | everyone | Opaque saved proposal id. |
| `proposal.notes` | array (optional) |  | everyone | Warnings and consequences to show alongside the exact changes before confirmation; absent on older servers or when there are no notes. |
| `proposal.notes[].code` | string |  | everyone | Stable warning or explanatory-note code. |
| `proposal.notes[].text` | string |  | everyone | Human-readable consequence or context to show with the proposed changes. |
| `proposal.status` | string |  | everyone | Current saved proposal state; unknown future states must be preserved. |
| `proposal.risk` | enum |  | everyone | Effective risk after field-level escalation. Values: `low`, `standard`, `sensitive`. |
| `proposal.expires_at` | string |  | everyone | Time after which this proposal can no longer be applied. |
| `proposal.applied_at` | string\|null (optional) |  | everyone | Time the proposal was applied, if it was applied. |
| `proposal.replayed` | boolean (optional) |  | everyone | True when returning a stored result without applying again. |
| `applied` | boolean |  | everyone | True when the change was written. False on a dry run or when nothing differed from the current values. |
| `dry_run` | boolean |  | everyone | True when the call was a preview: values were validated and authorized but nothing was written. |
| `changes` | array |  | everyone | Field-level changes (empty when every requested value already matched). Summarize these back to the human. |
| `changes[].field` | string |  | everyone | Name of the changed argument, exactly as passed to the tool (e.g. "contact_phone", "fare.base"). |
| `changes[].from` | string\|number\|boolean\|null\|array\|array |  | everyone | Value before the change. |
| `changes[].to` | string\|number\|boolean\|null\|array\|array |  | everyone | Value after the change. |
| `trip_note` | object |  | everyone | A trip's private internal note. |
| `trip_note.trip_id` | string |  | everyone | Trip id, for get_trip. |
| `trip_note.internal_note` | string\|null |  | owner, admin, self | Private note seen only by the trip's driver and fleet owners/admins; null when cleared. |
## Booking

A booking (scheduled ride). No payment-provider ids, internal snapshots or dispatch internals.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `booking_id` | string |  | everyone | Opaque booking id (a scheduled ride). |
| `fleet_id` | string\|null |  | everyone | Fleet the ride was booked with, or null for a solo driver booking. |
| `status` | enum |  | everyone | Booking lifecycle: pending (awaiting a driver), confirmed (driver assigned), in_progress, completed, canceled, pending_payment (rider must pay before it is dispatched). Values: `pending`, `confirmed`, `in_progress`, `completed`, `canceled`, `pending_payment`. |
| `agent_action_status` | object (optional) |  | everyone | Details-only agent cancellation and reminder progress; omitted from list_bookings. |
| `agent_action_status.cancellation_settlement` | enum\|null |  | everyone | Native cancellation processor progress. Completed is not proof of a charge, refund or notification delivery; manual_handoff requires human review. Values: `pending`, `processing`, `completed`, `manual_handoff`. |
| `agent_action_status.payment_reminder_delivery` | enum\|null |  | everyone | Latest agent reminder delivery state; sending or unknown must not be automatically resent. Values: `pending`, `preparing`, `sending`, `completed`, `superseded`, `unknown`. |
| `agent_action_status.has_ambiguous_reminder` | boolean |  | everyone | A reminder may have been delivered; inspect before another reminder. |
| `is_asap` | boolean |  | everyone | True for on-demand ("as soon as possible") rides. |
| `is_time_booking` | boolean |  | everyone | True for hourly / by-the-hour bookings. |
| `booking_source` | string\|null |  | everyone | Where the booking came from: web, rider_app, meter_app, admin_web, voice, messaging. |
| `scheduled_at` | string | ISO 8601 | everyone | Requested pickup time. |
| `timezone` | string |  | everyone | IANA timezone of the pickup. |
| `pickup` | object |  | everyone | Pickup place. |
| `pickup.name` | string\|null |  | everyone | Short place name (e.g. business or airport name), or null. |
| `pickup.address` | string\|null |  | everyone | Formatted street address, or null. |
| `dropoff` | object\|null |  | everyone | Drop-off place, or null for open-ended time bookings. |
| `dropoff.name` | string\|null |  | everyone | Short place name (e.g. business or airport name), or null. |
| `dropoff.address` | string\|null |  | everyone | Formatted street address, or null. |
| `stop_count` | number |  | everyone | Number of intermediate stops. |
| `passenger_count` | number |  | everyone | Passengers requested. |
| `estimated_distance_meters` | number\|null | meters | everyone | Estimated route distance. |
| `estimated_duration_seconds` | number\|null | seconds | everyone | Estimated route duration. |
| `estimate` | object\|null |  | everyone | Upfront quote, or null when not priced. |
| `estimate.currency` | string |  | everyone | Currency of total_minor. |
| `estimate.total_minor` | number | minor currency units | everyone | Quoted total shown to the rider, in minor units. |
| `ride_option` | object\|null |  | everyone | Vehicle class booked, or null. |
| `ride_option.id` | string |  | everyone | Ride option id. |
| `ride_option.name` | string |  | everyone | Ride option name. |
| `ride_option.type` | string |  | everyone | Ride option type. |
| `ride_option.capacity` | number |  | everyone | Passenger capacity. |
| `assigned_driver` | object\|null |  | everyone | Driver assigned to the ride, or null while pending. |
| `assigned_driver.id` | string |  | everyone | Opaque member id (a profile id). Use it as `driver` in list_trips or to match list_fleet_members. |
| `assigned_driver.display_name` | string\|null |  | everyone | Display name (first and last name). Null when the person has not set a name. |
| `preferred_driver` | object\|null |  | everyone | Driver the rider or dispatcher preferred, or null. |
| `preferred_driver.id` | string |  | everyone | Opaque member id (a profile id). Use it as `driver` in list_trips or to match list_fleet_members. |
| `preferred_driver.display_name` | string\|null |  | everyone | Display name (first and last name). Null when the person has not set a name. |
| `rider` | object\|null |  | everyone | The rider, or null for a driver-entered booking without a rider. |
| `rider.display_name` | string\|null |  | everyone | Rider display name, or null. |
| `rider.phone` | string\|null |  | owner, admin, driver, rider | Rider phone (E.164). Only for fleet owners/admins, the assigned driver, or the rider themselves; null otherwise. |
| `rider.email` | string\|null |  | owner, admin, rider | Rider email. Only for fleet owners/admins or the rider themselves; null otherwise. |
| `notes` | string\|null |  | everyone | Pickup instructions the rider or dispatcher wrote for the driver. |
| `flight_number` | string\|null |  | everyone | Flight number for airport pickups, or null. |
| `cancellation_reason` | string\|null |  | everyone | Stored cancellation reason enum, or null. |
| `pre_payment_status` | string |  | everyone | Payment authorization state (stored enum). |
| `trip_id` | string\|null |  | everyone | Linked metered trip once the ride is completed, or null. |
| `created_at` | string | ISO 8601 | everyone | When the booking was created. |
| `updated_at` | string | ISO 8601 | everyone | When the booking last changed. |
## BookingPage

Result of list_bookings. Cursor pagination is by scheduled time.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `items` | array |  | everyone | The page of results, newest first unless the tool says otherwise. |
| `items[].booking_id` | string |  | everyone | Opaque booking id (a scheduled ride). |
| `items[].fleet_id` | string\|null |  | everyone | Fleet the ride was booked with, or null for a solo driver booking. |
| `items[].status` | enum |  | everyone | Booking lifecycle: pending (awaiting a driver), confirmed (driver assigned), in_progress, completed, canceled, pending_payment (rider must pay before it is dispatched). Values: `pending`, `confirmed`, `in_progress`, `completed`, `canceled`, `pending_payment`. |
| `items[].agent_action_status` | object (optional) |  | everyone | Details-only agent cancellation and reminder progress; omitted from list_bookings. |
| `items[].agent_action_status.cancellation_settlement` | enum\|null |  | everyone | Native cancellation processor progress. Completed is not proof of a charge, refund or notification delivery; manual_handoff requires human review. Values: `pending`, `processing`, `completed`, `manual_handoff`. |
| `items[].agent_action_status.payment_reminder_delivery` | enum\|null |  | everyone | Latest agent reminder delivery state; sending or unknown must not be automatically resent. Values: `pending`, `preparing`, `sending`, `completed`, `superseded`, `unknown`. |
| `items[].agent_action_status.has_ambiguous_reminder` | boolean |  | everyone | A reminder may have been delivered; inspect before another reminder. |
| `items[].is_asap` | boolean |  | everyone | True for on-demand ("as soon as possible") rides. |
| `items[].is_time_booking` | boolean |  | everyone | True for hourly / by-the-hour bookings. |
| `items[].booking_source` | string\|null |  | everyone | Where the booking came from: web, rider_app, meter_app, admin_web, voice, messaging. |
| `items[].scheduled_at` | string | ISO 8601 | everyone | Requested pickup time. |
| `items[].timezone` | string |  | everyone | IANA timezone of the pickup. |
| `items[].pickup` | object |  | everyone | Pickup place. |
| `items[].pickup.name` | string\|null |  | everyone | Short place name (e.g. business or airport name), or null. |
| `items[].pickup.address` | string\|null |  | everyone | Formatted street address, or null. |
| `items[].dropoff` | object\|null |  | everyone | Drop-off place, or null for open-ended time bookings. |
| `items[].dropoff.name` | string\|null |  | everyone | Short place name (e.g. business or airport name), or null. |
| `items[].dropoff.address` | string\|null |  | everyone | Formatted street address, or null. |
| `items[].stop_count` | number |  | everyone | Number of intermediate stops. |
| `items[].passenger_count` | number |  | everyone | Passengers requested. |
| `items[].estimated_distance_meters` | number\|null | meters | everyone | Estimated route distance. |
| `items[].estimated_duration_seconds` | number\|null | seconds | everyone | Estimated route duration. |
| `items[].estimate` | object\|null |  | everyone | Upfront quote, or null when not priced. |
| `items[].estimate.currency` | string |  | everyone | Currency of total_minor. |
| `items[].estimate.total_minor` | number | minor currency units | everyone | Quoted total shown to the rider, in minor units. |
| `items[].ride_option` | object\|null |  | everyone | Vehicle class booked, or null. |
| `items[].ride_option.id` | string |  | everyone | Ride option id. |
| `items[].ride_option.name` | string |  | everyone | Ride option name. |
| `items[].ride_option.type` | string |  | everyone | Ride option type. |
| `items[].ride_option.capacity` | number |  | everyone | Passenger capacity. |
| `items[].assigned_driver` | object\|null |  | everyone | Driver assigned to the ride, or null while pending. |
| `items[].assigned_driver.id` | string |  | everyone | Opaque member id (a profile id). Use it as `driver` in list_trips or to match list_fleet_members. |
| `items[].assigned_driver.display_name` | string\|null |  | everyone | Display name (first and last name). Null when the person has not set a name. |
| `items[].preferred_driver` | object\|null |  | everyone | Driver the rider or dispatcher preferred, or null. |
| `items[].preferred_driver.id` | string |  | everyone | Opaque member id (a profile id). Use it as `driver` in list_trips or to match list_fleet_members. |
| `items[].preferred_driver.display_name` | string\|null |  | everyone | Display name (first and last name). Null when the person has not set a name. |
| `items[].rider` | object\|null |  | everyone | The rider, or null for a driver-entered booking without a rider. |
| `items[].rider.display_name` | string\|null |  | everyone | Rider display name, or null. |
| `items[].rider.phone` | string\|null |  | owner, admin, driver, rider | Rider phone (E.164). Only for fleet owners/admins, the assigned driver, or the rider themselves; null otherwise. |
| `items[].rider.email` | string\|null |  | owner, admin, rider | Rider email. Only for fleet owners/admins or the rider themselves; null otherwise. |
| `items[].notes` | string\|null |  | everyone | Pickup instructions the rider or dispatcher wrote for the driver. |
| `items[].flight_number` | string\|null |  | everyone | Flight number for airport pickups, or null. |
| `items[].cancellation_reason` | string\|null |  | everyone | Stored cancellation reason enum, or null. |
| `items[].pre_payment_status` | string |  | everyone | Payment authorization state (stored enum). |
| `items[].trip_id` | string\|null |  | everyone | Linked metered trip once the ride is completed, or null. |
| `items[].created_at` | string | ISO 8601 | everyone | When the booking was created. |
| `items[].updated_at` | string | ISO 8601 | everyone | When the booking last changed. |
| `next_cursor` | string\|null |  | everyone | Pass this back as `cursor` to fetch the next page. Null when there are no more results. |
| `has_more` | boolean |  | everyone | True when another page exists. |
## BookingAuditLog

Result of get_booking_audit_log.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `booking_id` | string |  | everyone | The booking these entries belong to. |
| `entries` | array |  | everyone | Timeline entries, newest first. |
| `entries[].at` | string | ISO 8601 | everyone | When the event happened. |
| `entries[].event` | string |  | everyone | Short event title, e.g. "Driver assigned". |
| `entries[].summary` | string\|null |  | everyone | One-line human summary, or null. |
| `entries[].actor_role` | enum |  | everyone | Role of whoever acted: owner, admin, driver, fleet_member (fleet user of unrecorded role), rider, system (automation), unknown. Never an id or name. Values: `owner`, `admin`, `driver`, `fleet_member`, `rider`, `system`, `unknown`. |
| `entries[].category` | string |  | everyone | Event category: booking_change, status, dispatch, notification, payment, route, rider, driver, system. |
| `entries[].outcome` | string |  | everyone | ok, invalid (rejected request), error, pending or unknown. |
| `entries[].field_changes` | array |  | everyone | Redacted field-level changes, possibly empty. |
| `entries[].field_changes[].field` | string |  | everyone | Machine key of the changed field (e.g. "scheduled_time"). |
| `entries[].field_changes[].label` | string |  | everyone | Human label of the changed field. |
| `entries[].field_changes[].old` | string\|null |  | everyone | Previous value as display text, or null. |
| `entries[].field_changes[].new` | string\|null |  | everyone | New value as display text, or null. |
| `next_cursor` | string\|null |  | everyone | Cursor for the next (older) page, or null. |
| `has_more` | boolean |  | everyone | True when older entries exist. |
## EarningsSummary

Result of get_earnings: Meter Pay payouts, not cash collected. Use get_accounting_summary for the full ledger.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `scope` | enum |  | everyone | "me": your own payouts; "fleet": every payout to the fleet and its members. Values: `me`, `fleet`. |
| `fleet_id` | string\|null |  | everyone | Fleet id when scope is "fleet"; otherwise null. |
| `start_date` | string |  | everyone | Inclusive period start (ISO 8601). |
| `end_date` | string |  | everyone | Exclusive period end (ISO 8601). |
| `granularity` | enum |  | everyone | Bucket size of time_series. Values: `day`, `week`. |
| `fallback_currency` | string |  | everyone | Currency assumed for payouts without an explicit currency. |
| `totals` | array |  | everyone | Totals per currency over the whole period. |
| `totals[].currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `totals[].net_amount_minor` | number | minor currency units | everyone | Net amount paid out (after platform fees) in this currency. |
| `totals[].transfer_count` | number |  | everyone | Number of payouts making up the amount. |
| `time_series` | array |  | everyone | Per-bucket amounts, oldest first. |
| `time_series[].currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `time_series[].net_amount_minor` | number | minor currency units | everyone | Net amount paid out (after platform fees) in this currency. |
| `time_series[].transfer_count` | number |  | everyone | Number of payouts making up the amount. |
| `time_series[].period` | string |  | everyone | Bucket start as an ISO date (day granularity) or ISO week start (week granularity). |
| `members` | array\|null |  | owner, admin | Per-member breakdown when scope is "fleet" and the caller is owner/admin; otherwise null. |
| `members[].member_id` | string |  | everyone | Opaque member id (profile id). |
| `members[].display_name` | string\|null |  | everyone | Member display name, or null. |
| `members[].currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `members[].net_amount_minor` | number | minor currency units | everyone | Net amount paid out to this member in the period. |
| `members[].transfer_count` | number |  | everyone | Number of payouts to this member in the period. |
## TaxSummary

Tax amounts from native scalar trip pricing. Advanced fare models are omitted and mark the report incomplete.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `start_date` | string |  | everyone | Inclusive ISO period start. |
| `end_date` | string |  | everyone | Exclusive ISO period end. |
| `complete` | boolean |  | everyone | False when the report excludes rows. Narrow the period before treating totals as complete. |
| `fleet_id` | string\|null |  | everyone | Fleet constraint, otherwise null. |
| `driver_id` | string\|null |  | everyone | Driver constraint, otherwise all authorized fleet drivers. |
| `included_trip_count` | number |  | everyone | Trips included in these totals. |
| `skipped_trip_count` | number |  | everyone | Fetched trips with missing fares, unsupported fare models/currencies or unusable prices. |
| `assumed_currency_count` | number |  | everyone | Included trips whose missing currency used the console USD fallback. |
| `totals` | array |  | everyone | Saved-trip price totals, separately by currency. These are not a tax filing or a settlement report. |
| `totals[].currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `totals[].currency_fraction_digits` | number |  | everyone | Number of decimal places in this currency; minor amounts use this exponent. |
| `totals[].taxable_fare_minor` | number | minor currency units | everyone | Discounted taxable fare in minor currency units. |
| `totals[].tax_collected_minor` | number | minor currency units | everyone | Collected trip tax in minor currency units. |
| `totals[].non_taxable_income_minor` | number | minor currency units | everyone | Income outside the taxable subtotal in minor currency units. |
| `totals[].trip_count` | number |  | everyone | Included trips in this currency. |
## MileageReport

Native Mileage tracker classifications. No location traces or assumed tax deduction rate.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `start_date` | string |  | everyone | Inclusive ISO period start. |
| `end_date` | string |  | everyone | Exclusive ISO period end. |
| `complete` | boolean |  | everyone | False when the report excludes rows. Narrow the period before treating totals as complete. |
| `fleet_id` | string\|null |  | everyone | Fleet constraint, otherwise null. |
| `driver_id` | string\|null |  | everyone | Driver constraint, otherwise all authorized fleet drivers. |
| `trip_count` | number |  | everyone | Included non-excluded mileage records. |
| `total_meters` | number |  | everyone | Included tracked distance in meters. |
| `business_meters` | number |  | everyone | Business classified distance in meters. |
| `commute_meters` | number |  | everyone | Commute classified distance in meters. |
| `fleet_online_meters` | number |  | everyone | Fleet online classified distance in meters. |
| `personal_meters` | number |  | everyone | Personal classified distance in meters. |
| `unclassified_meters` | number |  | everyone | Distance without a confirmed classification in meters. |
| `excluded_meters` | number |  | everyone | Excluded distance in meters. |
| `review_count` | number |  | everyone | Mileage records still needing review. |
## AccountingSummary

Result of get_accounting_summary (owners/admins). Full ledger view: cash, card, payouts and balances.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string |  | everyone | The fleet. |
| `start_date` | string\|null |  | everyone | Inclusive period start (ISO 8601), or null for all time. |
| `end_date` | string\|null |  | everyone | Exclusive period end (ISO 8601), or null for now. |
| `distance_unit` | enum |  | everyone | Unit used for per-distance rates (totals stay in meters). Values: `mile`, `kilometer`. |
| `trip_count` | number |  | everyone | Trips in the period across currencies. |
| `by_currency` | array |  | everyone | Fleet-wide rollups per currency. |
| `by_currency[].currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `by_currency[].trip_count` | number |  | everyone | Trips in this currency in the period. |
| `by_currency[].paid_trip_count` | number |  | everyone | Trips marked paid (any channel). |
| `by_currency[].voided_trip_count` | number |  | everyone | Trips voided by an admin. |
| `by_currency[].gross_amount_minor` | number | minor currency units | everyone | Sum of trip totals before fees, including tips. |
| `by_currency[].tip_amount_minor` | number | minor currency units | everyone | Tips included in gross. |
| `by_currency[].card_processing_fee_minor` | number | minor currency units | everyone | Card processing fees on Meter Pay payments. |
| `by_currency[].net_after_fees_minor` | number | minor currency units | everyone | Gross minus card processing fees. |
| `by_currency[].driver_earnings_minor` | number | minor currency units | everyone | Portion owed to drivers under the payout policy. |
| `by_currency[].fleet_cut_minor` | number | minor currency units | everyone | Portion retained by the fleet. |
| `by_currency[].collected_amount_minor` | number | minor currency units | everyone | Amount actually collected (any channel). |
| `by_currency[].digital_collected_minor` | number | minor currency units | everyone | Collected through Meter Pay (card). |
| `by_currency[].cash_collected_minor` | number | minor currency units | everyone | Collected in cash by drivers. |
| `by_currency[].other_collected_minor` | number | minor currency units | everyone | Collected through other means (invoice, external terminal). |
| `by_currency[].not_marked_paid_amount_minor` | number | minor currency units | everyone | Value of trips not yet marked paid. |
| `by_currency[].fleet_owes_driver_minor` | number | minor currency units | everyone | Outstanding balance the fleet owes its drivers. |
| `by_currency[].driver_owes_fleet_minor` | number | minor currency units | everyone | Outstanding cash drivers still owe the fleet. |
| `by_currency[].distance_meters` | number | meters | everyone | Total metered distance. |
| `by_currency[].duration_seconds` | number | seconds | everyone | Total metered duration. |
| `trend` | array |  | everyone | Most recent 50 daily ledger currency buckets. Inspect trend_truncated; narrow the range or use query_metrics for complete aggregates. |
| `trend[].currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `trend[].trip_count` | number |  | everyone | Trips in this currency in the period. |
| `trend[].gross_amount_minor` | number | minor currency units | everyone | Sum of trip totals before fees, including tips. |
| `trend[].driver_earnings_minor` | number | minor currency units | everyone | Portion owed to drivers under the payout policy. |
| `trend[].fleet_cut_minor` | number | minor currency units | everyone | Portion retained by the fleet. |
| `trend[].collected_amount_minor` | number | minor currency units | everyone | Amount actually collected (any channel). |
| `trend[].digital_collected_minor` | number | minor currency units | everyone | Collected through Meter Pay (card). |
| `trend[].cash_collected_minor` | number | minor currency units | everyone | Collected in cash by drivers. |
| `trend[].other_collected_minor` | number | minor currency units | everyone | Collected through other means (invoice, external terminal). |
| `trend[].not_marked_paid_amount_minor` | number | minor currency units | everyone | Value of trips not yet marked paid. |
| `trend[].card_processing_fee_minor` | number | minor currency units | everyone | Card processing fees on Meter Pay payments. |
| `trend[].distance_meters` | number | meters | everyone | Total metered distance. |
| `trend[].duration_seconds` | number | seconds | everyone | Total metered duration. |
| `trend[].bucket_start` | string |  | everyone | Start of the accounting time bucket (ISO 8601). |
| `trend_truncated` | boolean |  | everyone | Older trend buckets were omitted. Summary totals and balances still cover the full requested range. |
| `drivers` | array |  | everyone | Per-driver rollups. |
| `drivers[].member_id` | string |  | everyone | Opaque member id, or "unknown" for trips whose driver account was deleted. |
| `drivers[].display_name` | string\|null |  | everyone | Driver display name, or null. |
| `drivers[].pending_void_requests` | number |  | everyone | Void requests from this driver awaiting review. |
| `drivers[].by_currency` | array |  | everyone | Rollups per currency for this driver. |
| `drivers[].by_currency[].currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `drivers[].by_currency[].trip_count` | number |  | everyone | Trips in this currency in the period. |
| `drivers[].by_currency[].paid_trip_count` | number |  | everyone | Trips marked paid (any channel). |
| `drivers[].by_currency[].voided_trip_count` | number |  | everyone | Trips voided by an admin. |
| `drivers[].by_currency[].gross_amount_minor` | number | minor currency units | everyone | Sum of trip totals before fees, including tips. |
| `drivers[].by_currency[].tip_amount_minor` | number | minor currency units | everyone | Tips included in gross. |
| `drivers[].by_currency[].card_processing_fee_minor` | number | minor currency units | everyone | Card processing fees on Meter Pay payments. |
| `drivers[].by_currency[].net_after_fees_minor` | number | minor currency units | everyone | Gross minus card processing fees. |
| `drivers[].by_currency[].driver_earnings_minor` | number | minor currency units | everyone | Portion owed to drivers under the payout policy. |
| `drivers[].by_currency[].fleet_cut_minor` | number | minor currency units | everyone | Portion retained by the fleet. |
| `drivers[].by_currency[].collected_amount_minor` | number | minor currency units | everyone | Amount actually collected (any channel). |
| `drivers[].by_currency[].digital_collected_minor` | number | minor currency units | everyone | Collected through Meter Pay (card). |
| `drivers[].by_currency[].cash_collected_minor` | number | minor currency units | everyone | Collected in cash by drivers. |
| `drivers[].by_currency[].other_collected_minor` | number | minor currency units | everyone | Collected through other means (invoice, external terminal). |
| `drivers[].by_currency[].not_marked_paid_amount_minor` | number | minor currency units | everyone | Value of trips not yet marked paid. |
| `drivers[].by_currency[].fleet_owes_driver_minor` | number | minor currency units | everyone | Outstanding balance the fleet owes its drivers. |
| `drivers[].by_currency[].driver_owes_fleet_minor` | number | minor currency units | everyone | Outstanding cash drivers still owe the fleet. |
| `drivers[].by_currency[].distance_meters` | number | meters | everyone | Total metered distance. |
| `drivers[].by_currency[].duration_seconds` | number | seconds | everyone | Total metered duration. |
| `queue_counts` | object\|null |  | everyone | Reconciliation queue counts, or null. |
| `queue_counts.unrecorded` | number |  | everyone | Trips with no payment recorded. |
| `queue_counts.cash` | number |  | everyone | Cash trips awaiting settlement. |
| `queue_counts.pending_void` | number |  | everyone | Void requests awaiting review. |
| `queue_counts.delete_eligible` | number |  | everyone | Trips eligible for deletion. |
## LedgerEntryPage

Result of list_ledger_entries: ledger rows, newest first, in the requested window.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `items` | array |  | everyone | The page of results, newest first unless the tool says otherwise. |
| `items[].entry_id` | string |  | everyone | Stable ledger entry id, e.g. "charge:<trip id>" or "settlement:<settlement id>". |
| `items[].occurred_at` | string | ISO 8601 | everyone | When the entry was posted. |
| `items[].type` | enum |  | everyone | charge: trip fare; booking_charge: booking charge without a trip; cash_payment/meterpay_payment: money collected; driver_payout/fleet_payout: transfers; processing_fee: card fees; settlement: cash settled between driver and fleet; void_adjustment/payout_reversal: reversals after an approved void. Values: `charge`, `booking_charge`, `cash_payment`, `meterpay_payment`, `driver_payout`, `fleet_payout`, `processing_fee`, `settlement`, `void_adjustment`, `payout_reversal`. |
| `items[].amount_minor` | number | minor currency units | everyone | Signed amount. Negative values leave the fleet (payouts, fees, reversals, settlements paid to drivers). |
| `items[].currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `items[].status` | enum |  | everyone | pending while a void request on the trip awaits review. Values: `posted`, `pending`. |
| `items[].description` | string |  | everyone | Short English entry label. |
| `items[].member_id` | string\|null |  | everyone | Driver (member id) the entry belongs to, or null. |
| `items[].driver_name` | string\|null |  | everyone | Driver display name, or null. |
| `items[].trip_id` | string\|null |  | everyone | Trip behind the entry, or null. |
| `items[].booking_id` | string\|null |  | everyone | Booking behind the entry, or null. |
| `items[].settlement_id` | string\|null |  | everyone | Settlement behind the entry, or null. |
| `items[].void_request_id` | string\|null |  | everyone | Void request that produced or holds the entry, or null. |
| `items[].payment_method` | string\|null |  | everyone | Recorded payment method of the trip or booking, or null. |
| `next_cursor` | string\|null |  | everyone | Pass this back as `cursor` to fetch the next page. Null when there are no more results. |
| `has_more` | boolean |  | everyone | True when another page exists. |
## DriverBalancePage

Result of list_driver_balances: per-driver balances and collections per currency for the window.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `items` | array |  | everyone | The page of results, newest first unless the tool says otherwise. |
| `items[].member_id` | string |  | everyone | Opaque member id, or "unknown" for trips whose driver account was deleted. |
| `items[].display_name` | string\|null |  | everyone | Driver display name, or null. |
| `items[].pending_void_requests` | number |  | everyone | Void requests from this driver awaiting review. |
| `items[].by_currency` | array |  | everyone | Rollups per currency for this driver. |
| `items[].by_currency[].currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `items[].by_currency[].trip_count` | number |  | everyone | Trips in this currency in the period. |
| `items[].by_currency[].paid_trip_count` | number |  | everyone | Trips marked paid (any channel). |
| `items[].by_currency[].voided_trip_count` | number |  | everyone | Trips voided by an admin. |
| `items[].by_currency[].gross_amount_minor` | number | minor currency units | everyone | Sum of trip totals before fees, including tips. |
| `items[].by_currency[].tip_amount_minor` | number | minor currency units | everyone | Tips included in gross. |
| `items[].by_currency[].card_processing_fee_minor` | number | minor currency units | everyone | Card processing fees on Meter Pay payments. |
| `items[].by_currency[].net_after_fees_minor` | number | minor currency units | everyone | Gross minus card processing fees. |
| `items[].by_currency[].driver_earnings_minor` | number | minor currency units | everyone | Portion owed to drivers under the payout policy. |
| `items[].by_currency[].fleet_cut_minor` | number | minor currency units | everyone | Portion retained by the fleet. |
| `items[].by_currency[].collected_amount_minor` | number | minor currency units | everyone | Amount actually collected (any channel). |
| `items[].by_currency[].digital_collected_minor` | number | minor currency units | everyone | Collected through Meter Pay (card). |
| `items[].by_currency[].cash_collected_minor` | number | minor currency units | everyone | Collected in cash by drivers. |
| `items[].by_currency[].other_collected_minor` | number | minor currency units | everyone | Collected through other means (invoice, external terminal). |
| `items[].by_currency[].not_marked_paid_amount_minor` | number | minor currency units | everyone | Value of trips not yet marked paid. |
| `items[].by_currency[].fleet_owes_driver_minor` | number | minor currency units | everyone | Outstanding balance the fleet owes its drivers. |
| `items[].by_currency[].driver_owes_fleet_minor` | number | minor currency units | everyone | Outstanding cash drivers still owe the fleet. |
| `items[].by_currency[].distance_meters` | number | meters | everyone | Total metered distance. |
| `items[].by_currency[].duration_seconds` | number | seconds | everyone | Total metered duration. |
| `next_cursor` | string\|null |  | everyone | Pass this back as `cursor` to fetch the next page. Null when there are no more results. |
| `has_more` | boolean |  | everyone | True when another page exists. |
## SettlementPage

Result of list_settlements: newest first.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `items` | array |  | everyone | The page of results, newest first unless the tool says otherwise. |
| `items[].settlement_id` | string |  | everyone | Settlement id. |
| `items[].member_id` | string |  | everyone | Driver (member id) who settled. |
| `items[].driver_name` | string\|null |  | everyone | Driver display name, or null. |
| `items[].direction` | enum |  | everyone | driver_to_fleet: the driver handed cash to the fleet; fleet_to_driver: the fleet paid the driver. Values: `driver_to_fleet`, `fleet_to_driver`. |
| `items[].source` | string |  | everyone | How the settlement was recorded (manual, payout offset, ...). |
| `items[].amount_minor` | number | minor currency units | everyone | Settled amount (positive). |
| `items[].currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `items[].settled_at` | string | ISO 8601 | everyone | When the money changed hands. |
| `items[].recorded_at` | string | ISO 8601 | everyone | When it was recorded in Meter. |
| `items[].trip_count` | number |  | everyone | Trips this settlement covers. |
| `items[].trips` | array |  | everyone | Up to 100 covered trips; trip_count has the full count. |
| `items[].trips[].trip_id` | string |  | everyone | Covered trip. |
| `items[].trips[].applied_amount_minor` | number | minor currency units | everyone | Part of the settlement applied to this trip. |
| `next_cursor` | string\|null |  | everyone | Pass this back as `cursor` to fetch the next page. Null when there are no more results. |
| `has_more` | boolean |  | everyone | True when another page exists. |
## AccountingExceptionPage

Result of list_accounting_exceptions.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `items` | array |  | everyone | The page of results, newest first unless the tool says otherwise. |
| `items[].exception_id` | string |  | everyone | Stable exception id. |
| `items[].code` | enum |  | everyone | missing_payment_method: paid without a method; uncaptured_payment: card authorized but not captured; refunded_payment: refunded after collection; payout_not_delivered: a payout did not arrive; recovered_trip: rebuilt from settlement evidence; settled_void: a settled trip was later voided; unavailable_settled_trip: a settled trip is no longer readable. Values: `missing_payment_method`, `uncaptured_payment`, `refunded_payment`, `payout_not_delivered`, `recovered_trip`, `settled_void`, `unavailable_settled_trip`. |
| `items[].trip_id` | string |  | everyone | Trip with the evidence mismatch. |
| `items[].member_id` | string\|null |  | everyone | Driver (member id), or null. |
| `items[].driver_name` | string\|null |  | everyone | Driver display name, or null. |
| `items[].amount_minor` | number | minor currency units | everyone | Amount at stake. |
| `items[].currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `items[].occurred_at` | string | ISO 8601 | everyone | When the trip happened. |
| `items[].settlement_ids` | array |  | everyone | Settlements linked to the trip. |
| `next_cursor` | string\|null |  | everyone | Pass this back as `cursor` to fetch the next page. Null when there are no more results. |
| `has_more` | boolean |  | everyone | True when another page exists. |
## DriverAccounting

Result of get_driver_accounting: one driver's balance, trips and settlements.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string\|null |  | everyone | The fleet, or null for a driver's own all-fleet view. |
| `start_date` | string\|null | ISO 8601 | everyone | Inclusive period start, or null for all time. |
| `end_date` | string\|null | ISO 8601 | everyone | Exclusive period end. |
| `driver` | object |  | everyone | Balance rollup. |
| `driver.member_id` | string |  | everyone | Opaque member id, or "unknown" for trips whose driver account was deleted. |
| `driver.display_name` | string\|null |  | everyone | Driver display name, or null. |
| `driver.pending_void_requests` | number |  | everyone | Void requests from this driver awaiting review. |
| `driver.by_currency` | array |  | everyone | Rollups per currency for this driver. |
| `driver.by_currency[].currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `driver.by_currency[].trip_count` | number |  | everyone | Trips in this currency in the period. |
| `driver.by_currency[].paid_trip_count` | number |  | everyone | Trips marked paid (any channel). |
| `driver.by_currency[].voided_trip_count` | number |  | everyone | Trips voided by an admin. |
| `driver.by_currency[].gross_amount_minor` | number | minor currency units | everyone | Sum of trip totals before fees, including tips. |
| `driver.by_currency[].tip_amount_minor` | number | minor currency units | everyone | Tips included in gross. |
| `driver.by_currency[].card_processing_fee_minor` | number | minor currency units | everyone | Card processing fees on Meter Pay payments. |
| `driver.by_currency[].net_after_fees_minor` | number | minor currency units | everyone | Gross minus card processing fees. |
| `driver.by_currency[].driver_earnings_minor` | number | minor currency units | everyone | Portion owed to drivers under the payout policy. |
| `driver.by_currency[].fleet_cut_minor` | number | minor currency units | everyone | Portion retained by the fleet. |
| `driver.by_currency[].collected_amount_minor` | number | minor currency units | everyone | Amount actually collected (any channel). |
| `driver.by_currency[].digital_collected_minor` | number | minor currency units | everyone | Collected through Meter Pay (card). |
| `driver.by_currency[].cash_collected_minor` | number | minor currency units | everyone | Collected in cash by drivers. |
| `driver.by_currency[].other_collected_minor` | number | minor currency units | everyone | Collected through other means (invoice, external terminal). |
| `driver.by_currency[].not_marked_paid_amount_minor` | number | minor currency units | everyone | Value of trips not yet marked paid. |
| `driver.by_currency[].fleet_owes_driver_minor` | number | minor currency units | everyone | Outstanding balance the fleet owes its drivers. |
| `driver.by_currency[].driver_owes_fleet_minor` | number | minor currency units | everyone | Outstanding cash drivers still owe the fleet. |
| `driver.by_currency[].distance_meters` | number | meters | everyone | Total metered distance. |
| `driver.by_currency[].duration_seconds` | number | seconds | everyone | Total metered duration. |
| `by_currency` | array |  | everyone | Totals per currency for this driver and period. |
| `by_currency[].currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `by_currency[].trip_count` | number |  | everyone | Trips in this currency in the period. |
| `by_currency[].paid_trip_count` | number |  | everyone | Trips marked paid (any channel). |
| `by_currency[].voided_trip_count` | number |  | everyone | Trips voided by an admin. |
| `by_currency[].gross_amount_minor` | number | minor currency units | everyone | Sum of trip totals before fees, including tips. |
| `by_currency[].tip_amount_minor` | number | minor currency units | everyone | Tips included in gross. |
| `by_currency[].card_processing_fee_minor` | number | minor currency units | everyone | Card processing fees on Meter Pay payments. |
| `by_currency[].net_after_fees_minor` | number | minor currency units | everyone | Gross minus card processing fees. |
| `by_currency[].driver_earnings_minor` | number | minor currency units | everyone | Portion owed to drivers under the payout policy. |
| `by_currency[].fleet_cut_minor` | number | minor currency units | everyone | Portion retained by the fleet. |
| `by_currency[].collected_amount_minor` | number | minor currency units | everyone | Amount actually collected (any channel). |
| `by_currency[].digital_collected_minor` | number | minor currency units | everyone | Collected through Meter Pay (card). |
| `by_currency[].cash_collected_minor` | number | minor currency units | everyone | Collected in cash by drivers. |
| `by_currency[].other_collected_minor` | number | minor currency units | everyone | Collected through other means (invoice, external terminal). |
| `by_currency[].not_marked_paid_amount_minor` | number | minor currency units | everyone | Value of trips not yet marked paid. |
| `by_currency[].fleet_owes_driver_minor` | number | minor currency units | everyone | Outstanding balance the fleet owes its drivers. |
| `by_currency[].driver_owes_fleet_minor` | number | minor currency units | everyone | Outstanding cash drivers still owe the fleet. |
| `by_currency[].distance_meters` | number | meters | everyone | Total metered distance. |
| `by_currency[].duration_seconds` | number | seconds | everyone | Total metered duration. |
| `trips` | object |  | everyone | Page of this driver's trips, newest first. Pass trips.next_cursor as cursor. |
| `trips.items` | array |  | everyone | The page of results, newest first unless the tool says otherwise. |
| `trips.items[].trip_id` | string |  | everyone | Trip id (use get_trip for details). |
| `trips.items[].occurred_at` | string | ISO 8601 | everyone | When the trip happened. |
| `trips.items[].currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `trips.items[].payment_method` | string\|null |  | everyone | Recorded payment method. |
| `trips.items[].payment_status` | string |  | everyone | paid_digital, paid_cash, paid_other or not_marked_paid. |
| `trips.items[].void_review_status` | string |  | everyone | none, pending, approved or rejected. |
| `trips.items[].is_voided` | boolean |  | everyone | Voided by an admin. |
| `trips.items[].gross_amount_minor` | number | minor currency units | everyone | Trip total incl. tip. |
| `trips.items[].tip_amount_minor` | number | minor currency units | everyone | Tip. |
| `trips.items[].card_processing_fee_minor` | number | minor currency units | everyone | Card fees. |
| `trips.items[].driver_earnings_minor` | number | minor currency units | everyone | Driver share. |
| `trips.items[].fleet_cut_minor` | number | minor currency units | everyone | Fleet share. |
| `trips.items[].collected_amount_minor` | number | minor currency units | everyone | Collected, any channel. |
| `trips.items[].cash_collected_minor` | number | minor currency units | everyone | Collected in cash. |
| `trips.items[].not_marked_paid_amount_minor` | number | minor currency units | everyone | Value not yet marked paid. |
| `trips.items[].driver_balance_delta_minor` | number |  | everyone | Change to the driver's balance with the fleet from this trip (positive: fleet owes driver). |
| `trips.items[].distance_meters` | number | meters | everyone | Metered distance. |
| `trips.items[].duration_seconds` | number | seconds | everyone | Metered duration. |
| `trips.next_cursor` | string\|null |  | everyone | Pass this back as `cursor` to fetch the next page. Null when there are no more results. |
| `trips.has_more` | boolean |  | everyone | True when another page exists. |
| `settlements` | array\|null |  | everyone | Most recent 50 settlements in the period (fleet view only), or null. |
| `settlements[].settlement_id` | string |  | everyone | Settlement id. |
| `settlements[].member_id` | string |  | everyone | Driver (member id) who settled. |
| `settlements[].driver_name` | string\|null |  | everyone | Driver display name, or null. |
| `settlements[].direction` | enum |  | everyone | driver_to_fleet: the driver handed cash to the fleet; fleet_to_driver: the fleet paid the driver. Values: `driver_to_fleet`, `fleet_to_driver`. |
| `settlements[].source` | string |  | everyone | How the settlement was recorded (manual, payout offset, ...). |
| `settlements[].amount_minor` | number | minor currency units | everyone | Settled amount (positive). |
| `settlements[].currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `settlements[].settled_at` | string | ISO 8601 | everyone | When the money changed hands. |
| `settlements[].recorded_at` | string | ISO 8601 | everyone | When it was recorded in Meter. |
| `settlements[].trip_count` | number |  | everyone | Trips this settlement covers. |
| `settlements[].trips` | array |  | everyone | Up to 100 covered trips; trip_count has the full count. |
| `settlements[].trips[].trip_id` | string |  | everyone | Covered trip. |
| `settlements[].trips[].applied_amount_minor` | number | minor currency units | everyone | Part of the settlement applied to this trip. |
## DataExport

Result of export_data: one chunk of a dataset rendered from the authorized list tools. Money columns have *_minor integers plus a decimal string column; timestamps are ISO 8601 in the fleet timezone.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `dataset` | enum |  | everyone | Exported dataset. Values: `trips`, `bookings`, `customers`, `members`, `vehicles`, `ledger`, `settlements`, `trip_invoices`, `quotes`. |
| `filename` | string |  | everyone | Suggested file name. |
| `format` | enum |  | everyone | Format of data. Values: `csv`, `json`. |
| `timezone` | string |  | everyone | IANA timezone the timestamp columns are rendered in. |
| `row_count` | number |  | everyone | Rows in this chunk. |
| `columns` | array |  | everyone | Column names. |
| `data` | string\|array |  | everyone | CSV text (format csv, header row first) or row objects (format json). |
| `truncated` | boolean |  | everyone | More rows exist; call again with cursor=next_cursor and append. |
| `next_cursor` | string\|null |  | everyone | Cursor for the next chunk, or null when complete. |
## FleetSettings

Editable public and operational settings of a fleet (owners/admins). Never contains join codes, payout or payment-provider data.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string |  | everyone | Opaque fleet id. |
| `name` | string\|null |  | everyone | Fleet display name shown to riders. |
| `description` | string\|null |  | everyone | Public description (bio) shown on the booking page. |
| `contact_phone` | string\|null |  | everyone | Public contact phone riders can call. |
| `contact_whatsapp` | string\|null |  | everyone | Public WhatsApp number, or null. |
| `dispatch_phone` | string\|null |  | everyone | Phone number the dispatch desk answers, or null. |
| `website` | string\|null |  | everyone | Public website URL, or null. |
| `city` | string\|null |  | everyone | Primary city the fleet operates in. |
| `country_iso_code` | string\|null |  | everyone | ISO 3166-1 alpha-2 country code. |
| `region_iso_code` | string\|null |  | everyone | ISO 3166-2 region/state code, or null. |
| `currency_iso_code` | string\|null |  | everyone | ISO 4217 currency the fleet prices in. |
| `timezone` | string\|null |  | everyone | IANA timezone of the fleet. |
| `primary_color` | string\|null |  | everyone | Brand primary color as a hex string (e.g. "#1E90FF"), or null. |
| `secondary_color` | string\|null |  | everyone | Brand secondary color as a hex string, or null. |
| `show_driver_locations` | boolean |  | everyone | Whether riders see live driver locations on the public booking page. |
| `allow_fleet_custom_fares` | boolean |  | everyone | Whether drivers may run the meter with their own custom fares. |
| `allow_outside_origin_pickup` | boolean |  | everyone | Whether riders may request pickups outside the service zones. |
| `allow_outside_destination_dropoff` | boolean |  | everyone | Whether riders may request drop-offs outside the service zones. |
## FleetSettingsWrite

Result of update_fleet_settings: what changed and the fleet settings after the call.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `status` | string (optional) |  | everyone | Saved-proposal outcome; absent on older servers. |
| `proposal` | object\|null (optional) |  | everyone | Saved proposal and expiry. Confirm its exact changes before applying; absent on older servers. |
| `proposal.id` | string |  | everyone | Opaque saved proposal id. |
| `proposal.notes` | array (optional) |  | everyone | Warnings and consequences to show alongside the exact changes before confirmation; absent on older servers or when there are no notes. |
| `proposal.notes[].code` | string |  | everyone | Stable warning or explanatory-note code. |
| `proposal.notes[].text` | string |  | everyone | Human-readable consequence or context to show with the proposed changes. |
| `proposal.status` | string |  | everyone | Current saved proposal state; unknown future states must be preserved. |
| `proposal.risk` | enum |  | everyone | Effective risk after field-level escalation. Values: `low`, `standard`, `sensitive`. |
| `proposal.expires_at` | string |  | everyone | Time after which this proposal can no longer be applied. |
| `proposal.applied_at` | string\|null (optional) |  | everyone | Time the proposal was applied, if it was applied. |
| `proposal.replayed` | boolean (optional) |  | everyone | True when returning a stored result without applying again. |
| `applied` | boolean |  | everyone | True when the change was written. False on a dry run or when nothing differed from the current values. |
| `dry_run` | boolean |  | everyone | True when the call was a preview: values were validated and authorized but nothing was written. |
| `changes` | array |  | everyone | Field-level changes (empty when every requested value already matched). Summarize these back to the human. |
| `changes[].field` | string |  | everyone | Name of the changed argument, exactly as passed to the tool (e.g. "contact_phone", "fare.base"). |
| `changes[].from` | string\|number\|boolean\|null\|array\|array |  | everyone | Value before the change. |
| `changes[].to` | string\|number\|boolean\|null\|array\|array |  | everyone | Value after the change. |
| `fleet` | object |  | everyone | Editable public and operational settings of a fleet (owners/admins). Never contains join codes, payout or payment-provider data. |
| `fleet.fleet_id` | string |  | everyone | Opaque fleet id. |
| `fleet.name` | string\|null |  | everyone | Fleet display name shown to riders. |
| `fleet.description` | string\|null |  | everyone | Public description (bio) shown on the booking page. |
| `fleet.contact_phone` | string\|null |  | everyone | Public contact phone riders can call. |
| `fleet.contact_whatsapp` | string\|null |  | everyone | Public WhatsApp number, or null. |
| `fleet.dispatch_phone` | string\|null |  | everyone | Phone number the dispatch desk answers, or null. |
| `fleet.website` | string\|null |  | everyone | Public website URL, or null. |
| `fleet.city` | string\|null |  | everyone | Primary city the fleet operates in. |
| `fleet.country_iso_code` | string\|null |  | everyone | ISO 3166-1 alpha-2 country code. |
| `fleet.region_iso_code` | string\|null |  | everyone | ISO 3166-2 region/state code, or null. |
| `fleet.currency_iso_code` | string\|null |  | everyone | ISO 4217 currency the fleet prices in. |
| `fleet.timezone` | string\|null |  | everyone | IANA timezone of the fleet. |
| `fleet.primary_color` | string\|null |  | everyone | Brand primary color as a hex string (e.g. "#1E90FF"), or null. |
| `fleet.secondary_color` | string\|null |  | everyone | Brand secondary color as a hex string, or null. |
| `fleet.show_driver_locations` | boolean |  | everyone | Whether riders see live driver locations on the public booking page. |
| `fleet.allow_fleet_custom_fares` | boolean |  | everyone | Whether drivers may run the meter with their own custom fares. |
| `fleet.allow_outside_origin_pickup` | boolean |  | everyone | Whether riders may request pickups outside the service zones. |
| `fleet.allow_outside_destination_dropoff` | boolean |  | everyone | Whether riders may request drop-offs outside the service zones. |
## BookingSettings

Booking policy of a fleet (owners/admins): dispatch, payment, lead time, cancellation terms.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string |  | everyone | The fleet these settings belong to. |
| `availability` | array (optional) |  | everyone | Weekly booking hours in fleet timezone. Overnight windows are supported; omitted days normalize to open all day. Absent only in replayed results saved before availability was exposed. |
| `availability[].day` | enum |  | everyone | Day of the week in fleet timezone. Values: `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`, `sunday`. |
| `availability[].enabled` | boolean |  | everyone | Whether riders may book on this day. |
| `availability[].start_time` | string |  | everyone | Opening time, HH:mm in fleet timezone. |
| `availability[].end_time` | string |  | everyone | Closing time, HH:mm. Earlier than opening means overnight. |
| `dispatch_mode` | enum |  | everyone | How new bookings reach drivers: NONE (dispatcher assigns manually), ALL_ONLINE_DRIVERS (offered to every online driver), AUTO_DISPATCH (nearest available driver). Values: `NONE`, `ALL_ONLINE_DRIVERS`, `AUTO_DISPATCH`. |
| `payment_mode` | enum |  | everyone | pre_payment_required: riders add a card when they book; it is authorized before pickup and charged the final fare after the trip. payments_optional: no card at booking; riders pay the driver after the trip (cash, Tap to Pay, payment link) or online from their trip receipt. disabled: deprecated; merged into payments_optional and no longer stored. Values: `disabled`, `payments_optional`, `pre_payment_required`. |
| `min_lead_time_seconds` | number | seconds | everyone | Minimum notice between booking and pickup. |
| `time_slot_minutes` | number\|null | minutes | everyone | Granularity of hourly (time) bookings, or null when not set. |
| `minimum_duration_minutes` | number\|null | minutes | everyone | Minimum length of an hourly booking, or null. |
| `cancellation_fee_fraction` | number |  | everyone | Rider cancellation fee as a fraction of the fare (0-1) once the grace period has passed. |
| `cancellation_fee_minimum_unit_amount` | number | minor currency units | everyone | Minimum rider cancellation fee in the fleet currency's minor unit. |
| `cancellation_grace_period_seconds` | number | seconds | everyone | How long after booking a rider may cancel for free. |
| `driver_cancellation_allowed_reasons` | array |  | everyone | Reasons a driver may pick when cancelling an accepted booking. |
| `driver_cancellation_fee_mode` | enum |  | everyone | What happens to the cancellation fee when a driver cancels. Values: `none`, `standard_cancellation_fee`, `support_review`. |
| `driver_no_show_grace_period_seconds` | number | seconds | everyone | How long a driver waits at pickup before reporting a no-show. |
| `driver_post_pickup_cancellation_mode` | enum |  | everyone | Whether drivers may cancel after pickup and whether support must approve. Values: `disabled`, `driver_cancel`, `support_approval`. |
| `owner_booking_email_enabled` | boolean |  | everyone | Whether the fleet owner is emailed about each new booking. |
| `individual_passenger_capacity` | number |  | everyone | Default passenger capacity for bookings without a ride option. |
| `updated_at` | string\|null | ISO 8601 | everyone | When the settings last changed. |
## BookingSettingsWrite

Result of update_booking_settings: what changed and the booking settings after the call.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `status` | string (optional) |  | everyone | Saved-proposal outcome; absent on older servers. |
| `proposal` | object\|null (optional) |  | everyone | Saved proposal and expiry. Confirm its exact changes before applying; absent on older servers. |
| `proposal.id` | string |  | everyone | Opaque saved proposal id. |
| `proposal.notes` | array (optional) |  | everyone | Warnings and consequences to show alongside the exact changes before confirmation; absent on older servers or when there are no notes. |
| `proposal.notes[].code` | string |  | everyone | Stable warning or explanatory-note code. |
| `proposal.notes[].text` | string |  | everyone | Human-readable consequence or context to show with the proposed changes. |
| `proposal.status` | string |  | everyone | Current saved proposal state; unknown future states must be preserved. |
| `proposal.risk` | enum |  | everyone | Effective risk after field-level escalation. Values: `low`, `standard`, `sensitive`. |
| `proposal.expires_at` | string |  | everyone | Time after which this proposal can no longer be applied. |
| `proposal.applied_at` | string\|null (optional) |  | everyone | Time the proposal was applied, if it was applied. |
| `proposal.replayed` | boolean (optional) |  | everyone | True when returning a stored result without applying again. |
| `applied` | boolean |  | everyone | True when the change was written. False on a dry run or when nothing differed from the current values. |
| `dry_run` | boolean |  | everyone | True when the call was a preview: values were validated and authorized but nothing was written. |
| `changes` | array |  | everyone | Field-level changes (empty when every requested value already matched). Summarize these back to the human. |
| `changes[].field` | string |  | everyone | Name of the changed argument, exactly as passed to the tool (e.g. "contact_phone", "fare.base"). |
| `changes[].from` | string\|number\|boolean\|null\|array\|array |  | everyone | Value before the change. |
| `changes[].to` | string\|number\|boolean\|null\|array\|array |  | everyone | Value after the change. |
| `booking_settings` | object\|null |  | everyone | The booking settings after the call. Null only on a dry run for a fleet that has no booking settings yet; the real call creates them. |
| `booking_settings.fleet_id` | string |  | everyone | The fleet these settings belong to. |
| `booking_settings.availability` | array (optional) |  | everyone | Weekly booking hours in fleet timezone. Overnight windows are supported; omitted days normalize to open all day. Absent only in replayed results saved before availability was exposed. |
| `booking_settings.availability[].day` | enum |  | everyone | Day of the week in fleet timezone. Values: `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`, `sunday`. |
| `booking_settings.availability[].enabled` | boolean |  | everyone | Whether riders may book on this day. |
| `booking_settings.availability[].start_time` | string |  | everyone | Opening time, HH:mm in fleet timezone. |
| `booking_settings.availability[].end_time` | string |  | everyone | Closing time, HH:mm. Earlier than opening means overnight. |
| `booking_settings.dispatch_mode` | enum |  | everyone | How new bookings reach drivers: NONE (dispatcher assigns manually), ALL_ONLINE_DRIVERS (offered to every online driver), AUTO_DISPATCH (nearest available driver). Values: `NONE`, `ALL_ONLINE_DRIVERS`, `AUTO_DISPATCH`. |
| `booking_settings.payment_mode` | enum |  | everyone | pre_payment_required: riders add a card when they book; it is authorized before pickup and charged the final fare after the trip. payments_optional: no card at booking; riders pay the driver after the trip (cash, Tap to Pay, payment link) or online from their trip receipt. disabled: deprecated; merged into payments_optional and no longer stored. Values: `disabled`, `payments_optional`, `pre_payment_required`. |
| `booking_settings.min_lead_time_seconds` | number | seconds | everyone | Minimum notice between booking and pickup. |
| `booking_settings.time_slot_minutes` | number\|null | minutes | everyone | Granularity of hourly (time) bookings, or null when not set. |
| `booking_settings.minimum_duration_minutes` | number\|null | minutes | everyone | Minimum length of an hourly booking, or null. |
| `booking_settings.cancellation_fee_fraction` | number |  | everyone | Rider cancellation fee as a fraction of the fare (0-1) once the grace period has passed. |
| `booking_settings.cancellation_fee_minimum_unit_amount` | number | minor currency units | everyone | Minimum rider cancellation fee in the fleet currency's minor unit. |
| `booking_settings.cancellation_grace_period_seconds` | number | seconds | everyone | How long after booking a rider may cancel for free. |
| `booking_settings.driver_cancellation_allowed_reasons` | array |  | everyone | Reasons a driver may pick when cancelling an accepted booking. |
| `booking_settings.driver_cancellation_fee_mode` | enum |  | everyone | What happens to the cancellation fee when a driver cancels. Values: `none`, `standard_cancellation_fee`, `support_review`. |
| `booking_settings.driver_no_show_grace_period_seconds` | number | seconds | everyone | How long a driver waits at pickup before reporting a no-show. |
| `booking_settings.driver_post_pickup_cancellation_mode` | enum |  | everyone | Whether drivers may cancel after pickup and whether support must approve. Values: `disabled`, `driver_cancel`, `support_approval`. |
| `booking_settings.owner_booking_email_enabled` | boolean |  | everyone | Whether the fleet owner is emailed about each new booking. |
| `booking_settings.individual_passenger_capacity` | number |  | everyone | Default passenger capacity for bookings without a ride option. |
| `booking_settings.updated_at` | string\|null | ISO 8601 | everyone | When the settings last changed. |
## RideOptionDetail

A bookable ride option with its editable default fare (owners/admins).

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `id` | string |  | everyone | Ride option id. |
| `fleet_id` | string |  | everyone | The fleet offering this option. |
| `name` | string |  | everyone | Ride option name (e.g. "Sedan", "Van"). |
| `type` | enum |  | everyone | POINT_TO_POINT: upfront quote from A to B; TIME: hourly booking; METERED: priced by the meter. Values: `POINT_TO_POINT`, `TIME`, `METERED`. |
| `capacity` | number |  | everyone | Passenger capacity. |
| `fare` | object\|null |  | everyone | The default fare (rate card) riders are quoted with, or null when none is attached. |
| `fare.display_name` | string\|null |  | everyone | Fare name shown to drivers and riders. |
| `fare.currency_code` | string |  | everyone | ISO 4217 currency of the rates below. |
| `fare.base` | number | major currency units | everyone | Flag-drop / base fare in major currency units (e.g. 3.50 = $3.50). |
| `fare.minimum_fare` | number | major currency units | everyone | Minimum total fare in major currency units. |
| `fare.distance_rate` | number | major currency units per mile or km | everyone | Rate per distance unit (mile, or kilometer when `metric` is true) in major units. |
| `fare.minute_rate` | number | major currency units per minute | everyone | Rate per minute in major currency units. |
| `fare.wait_time_minute_rate` | number | major currency units per minute | everyone | Rate per minute of waiting in major currency units. |
| `fare.metric` | boolean |  | everyone | True when distance_rate is per kilometer; false when per mile. |
| `fare.fare_id` | string |  | everyone | Opaque fare id. |
| `fare.tax_rate` | number |  | everyone | Tax rate applied to the fare as a fraction (0.08 = 8%). |
| `fare.distance_rounding` | number\|null |  | everyone | Distance rounding granularity in miles or km, or null. |
| `fare.minute_rate_speed_threshold_kph` | number\|null |  | everyone | When set, minute_rate only accrues below this speed (km/h); null charges time continuously. |
| `fare.hidden_from_drivers` | boolean |  | everyone | True when drivers cannot pick this fare in the meter app. |
| `fare.description` | string\|null |  | everyone | Short description of when this fare applies, or null. |
## RideOptionWrite

Result of update_ride_option: what changed and the ride option after the call.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `status` | string (optional) |  | everyone | Saved-proposal outcome; absent on older servers. |
| `proposal` | object\|null (optional) |  | everyone | Saved proposal and expiry. Confirm its exact changes before applying; absent on older servers. |
| `proposal.id` | string |  | everyone | Opaque saved proposal id. |
| `proposal.notes` | array (optional) |  | everyone | Warnings and consequences to show alongside the exact changes before confirmation; absent on older servers or when there are no notes. |
| `proposal.notes[].code` | string |  | everyone | Stable warning or explanatory-note code. |
| `proposal.notes[].text` | string |  | everyone | Human-readable consequence or context to show with the proposed changes. |
| `proposal.status` | string |  | everyone | Current saved proposal state; unknown future states must be preserved. |
| `proposal.risk` | enum |  | everyone | Effective risk after field-level escalation. Values: `low`, `standard`, `sensitive`. |
| `proposal.expires_at` | string |  | everyone | Time after which this proposal can no longer be applied. |
| `proposal.applied_at` | string\|null (optional) |  | everyone | Time the proposal was applied, if it was applied. |
| `proposal.replayed` | boolean (optional) |  | everyone | True when returning a stored result without applying again. |
| `applied` | boolean |  | everyone | True when the change was written. False on a dry run or when nothing differed from the current values. |
| `dry_run` | boolean |  | everyone | True when the call was a preview: values were validated and authorized but nothing was written. |
| `changes` | array |  | everyone | Field-level changes (empty when every requested value already matched). Summarize these back to the human. |
| `changes[].field` | string |  | everyone | Name of the changed argument, exactly as passed to the tool (e.g. "contact_phone", "fare.base"). |
| `changes[].from` | string\|number\|boolean\|null\|array\|array |  | everyone | Value before the change. |
| `changes[].to` | string\|number\|boolean\|null\|array\|array |  | everyone | Value after the change. |
| `ride_option` | object |  | everyone | A bookable ride option with its editable default fare (owners/admins). |
| `ride_option.id` | string |  | everyone | Ride option id. |
| `ride_option.fleet_id` | string |  | everyone | The fleet offering this option. |
| `ride_option.name` | string |  | everyone | Ride option name (e.g. "Sedan", "Van"). |
| `ride_option.type` | enum |  | everyone | POINT_TO_POINT: upfront quote from A to B; TIME: hourly booking; METERED: priced by the meter. Values: `POINT_TO_POINT`, `TIME`, `METERED`. |
| `ride_option.capacity` | number |  | everyone | Passenger capacity. |
| `ride_option.fare` | object\|null |  | everyone | The default fare (rate card) riders are quoted with, or null when none is attached. |
| `ride_option.fare.display_name` | string\|null |  | everyone | Fare name shown to drivers and riders. |
| `ride_option.fare.currency_code` | string |  | everyone | ISO 4217 currency of the rates below. |
| `ride_option.fare.base` | number | major currency units | everyone | Flag-drop / base fare in major currency units (e.g. 3.50 = $3.50). |
| `ride_option.fare.minimum_fare` | number | major currency units | everyone | Minimum total fare in major currency units. |
| `ride_option.fare.distance_rate` | number | major currency units per mile or km | everyone | Rate per distance unit (mile, or kilometer when `metric` is true) in major units. |
| `ride_option.fare.minute_rate` | number | major currency units per minute | everyone | Rate per minute in major currency units. |
| `ride_option.fare.wait_time_minute_rate` | number | major currency units per minute | everyone | Rate per minute of waiting in major currency units. |
| `ride_option.fare.metric` | boolean |  | everyone | True when distance_rate is per kilometer; false when per mile. |
| `ride_option.fare.fare_id` | string |  | everyone | Opaque fare id. |
| `ride_option.fare.tax_rate` | number |  | everyone | Tax rate applied to the fare as a fraction (0.08 = 8%). |
| `ride_option.fare.distance_rounding` | number\|null |  | everyone | Distance rounding granularity in miles or km, or null. |
| `ride_option.fare.minute_rate_speed_threshold_kph` | number\|null |  | everyone | When set, minute_rate only accrues below this speed (km/h); null charges time continuously. |
| `ride_option.fare.hidden_from_drivers` | boolean |  | everyone | True when drivers cannot pick this fare in the meter app. |
| `ride_option.fare.description` | string\|null |  | everyone | Short description of when this fare applies, or null. |
## VehicleAssignmentWrite

Result of assign_vehicle: the vehicle with its (new) assigned_driver.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `status` | string (optional) |  | everyone | Saved-proposal outcome; absent on older servers. |
| `proposal` | object\|null (optional) |  | everyone | Saved proposal and expiry. Confirm its exact changes before applying; absent on older servers. |
| `proposal.id` | string |  | everyone | Opaque saved proposal id. |
| `proposal.notes` | array (optional) |  | everyone | Warnings and consequences to show alongside the exact changes before confirmation; absent on older servers or when there are no notes. |
| `proposal.notes[].code` | string |  | everyone | Stable warning or explanatory-note code. |
| `proposal.notes[].text` | string |  | everyone | Human-readable consequence or context to show with the proposed changes. |
| `proposal.status` | string |  | everyone | Current saved proposal state; unknown future states must be preserved. |
| `proposal.risk` | enum |  | everyone | Effective risk after field-level escalation. Values: `low`, `standard`, `sensitive`. |
| `proposal.expires_at` | string |  | everyone | Time after which this proposal can no longer be applied. |
| `proposal.applied_at` | string\|null (optional) |  | everyone | Time the proposal was applied, if it was applied. |
| `proposal.replayed` | boolean (optional) |  | everyone | True when returning a stored result without applying again. |
| `applied` | boolean |  | everyone | True when the change was written. False on a dry run or when nothing differed from the current values. |
| `dry_run` | boolean |  | everyone | True when the call was a preview: values were validated and authorized but nothing was written. |
| `changes` | array |  | everyone | Field-level changes (empty when every requested value already matched). Summarize these back to the human. |
| `changes[].field` | string |  | everyone | Name of the changed argument, exactly as passed to the tool (e.g. "contact_phone", "fare.base"). |
| `changes[].from` | string\|number\|boolean\|null\|array\|array |  | everyone | Value before the change. |
| `changes[].to` | string\|number\|boolean\|null\|array\|array |  | everyone | Value after the change. |
| `vehicle` | object |  | everyone | A fleet vehicle as listed by list_vehicles. |
| `vehicle.vehicle_id` | string |  | everyone | Opaque fleet vehicle id. |
| `vehicle.fleet_id` | string |  | everyone | Fleet the vehicle belongs to. |
| `vehicle.make` | string\|null |  | everyone | Manufacturer, e.g. "Toyota". |
| `vehicle.model` | string\|null |  | everyone | Model, e.g. "Camry". |
| `vehicle.year` | string\|null |  | everyone | Model year as a string, e.g. "2021". |
| `vehicle.license_plate` | string\|null |  | everyone | License plate as entered. |
| `vehicle.nickname` | string\|null |  | everyone | Optional nickname the fleet gave the vehicle. |
| `vehicle.color` | string\|null |  | everyone | Exterior color as entered. |
| `vehicle.created_at` | string | ISO 8601 | everyone | When the vehicle was added. |
| `vehicle.assigned_driver` | object\|null |  | owner, admin | Driver currently assigned to this vehicle, or null. Only resolved for fleet owners/admins; always null for drivers. |
| `vehicle.assigned_driver.id` | string |  | everyone | Opaque member id (a profile id). Use it as `driver` in list_trips or to match list_fleet_members. |
| `vehicle.assigned_driver.display_name` | string\|null |  | everyone | Display name (first and last name). Null when the person has not set a name. |
