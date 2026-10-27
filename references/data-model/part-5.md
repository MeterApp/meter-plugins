# Meter data-model reference

Generated from the `@meterapp/meter-sdk` catalog and DTO schemas; do not edit by hand. See the [reference index](../data-model.md) for all definitions.

## MyProfile

The caller's own editable profile. Role, fleet, payout and verification data are not editable through this server.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `id` | string |  | everyone | Your profile id. |
| `first_name` | string\|null |  | everyone | Your first name. |
| `last_name` | string\|null |  | everyone | Your last name. |
| `display_name` | string\|null |  | everyone | First and last name combined, as other people see it. |
| `email` | string\|null |  | self | Your email (read-only here). |
| `phone` | string\|null |  | self | Your phone (read-only here). |
| `company_name` | string\|null |  | everyone | Business name printed on your receipts. |
| `preferred_navigation_provider` | enum |  | everyone | Navigation app the meter opens for directions. Values: `in_app`, `apple_maps`, `google_maps`, `waze`, `naver_maps`. |
| `hide_contact_on_receipt` | boolean |  | everyone | Hide your phone and email on rider receipts (Meter Pro). |
| `pass_credit_card_fees_to_customer` | boolean |  | everyone | Add the Meter Pay card fee to the rider total instead of absorbing it (Meter Pro). |
| `fleets` | array |  | everyone | Your fleet memberships (read-only here; roles are changed by fleet owners in the console). |
| `fleets[].fleet_id` | string |  | everyone | Fleet id. |
| `fleets[].role` | enum |  | everyone | Role in the fleet. owner: created the fleet and controls billing; admin: manages members, vehicles, bookings and money; driver: drives and sees only their own trips, bookings and earnings. Values: `owner`, `admin`, `driver`. |
## MyProfileWrite

Result of update_my_profile: what changed and your profile after the call.

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
| `profile` | object |  | everyone | The caller's own editable profile. Role, fleet, payout and verification data are not editable through this server. |
| `profile.id` | string |  | everyone | Your profile id. |
| `profile.first_name` | string\|null |  | everyone | Your first name. |
| `profile.last_name` | string\|null |  | everyone | Your last name. |
| `profile.display_name` | string\|null |  | everyone | First and last name combined, as other people see it. |
| `profile.email` | string\|null |  | self | Your email (read-only here). |
| `profile.phone` | string\|null |  | self | Your phone (read-only here). |
| `profile.company_name` | string\|null |  | everyone | Business name printed on your receipts. |
| `profile.preferred_navigation_provider` | enum |  | everyone | Navigation app the meter opens for directions. Values: `in_app`, `apple_maps`, `google_maps`, `waze`, `naver_maps`. |
| `profile.hide_contact_on_receipt` | boolean |  | everyone | Hide your phone and email on rider receipts (Meter Pro). |
| `profile.pass_credit_card_fees_to_customer` | boolean |  | everyone | Add the Meter Pay card fee to the rider total instead of absorbing it (Meter Pro). |
| `profile.fleets` | array |  | everyone | Your fleet memberships (read-only here; roles are changed by fleet owners in the console). |
| `profile.fleets[].fleet_id` | string |  | everyone | Fleet id. |
| `profile.fleets[].role` | enum |  | everyone | Role in the fleet. owner: created the fleet and controls billing; admin: manages members, vehicles, bookings and money; driver: drives and sees only their own trips, bookings and earnings. Values: `owner`, `admin`, `driver`. |
## DriverAvailability

The caller's weekly availability that riders see when booking a specific driver.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `member_id` | string |  | everyone | The driver (the caller). |
| `timezone` | string |  | everyone | IANA timezone the shift times are expressed in. |
| `days` | array |  | everyone | Seven entries, Monday (1) to Sunday (7). |
| `days[].day_of_week` | number |  | everyone | ISO weekday: 1 = Monday ... 7 = Sunday. |
| `days[].shifts` | array |  | everyone | Availability windows on that day, earliest first. Empty means unavailable. |
| `days[].shifts[].start_time` | string |  | everyone | Shift start as HH:MM (24-hour) in the schedule timezone. |
| `days[].shifts[].end_time` | string |  | everyone | Shift end as HH:MM (24-hour); must be after start_time. |
| `updated_at` | string\|null | ISO 8601 | everyone | When the schedule last changed, or null when never saved. |
## DriverAvailabilityWrite

Result of update_my_availability: what changed and the weekly schedule after the call.

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
| `availability` | object |  | everyone | The caller's weekly availability that riders see when booking a specific driver. |
| `availability.member_id` | string |  | everyone | The driver (the caller). |
| `availability.timezone` | string |  | everyone | IANA timezone the shift times are expressed in. |
| `availability.days` | array |  | everyone | Seven entries, Monday (1) to Sunday (7). |
| `availability.days[].day_of_week` | number |  | everyone | ISO weekday: 1 = Monday ... 7 = Sunday. |
| `availability.days[].shifts` | array |  | everyone | Availability windows on that day, earliest first. Empty means unavailable. |
| `availability.days[].shifts[].start_time` | string |  | everyone | Shift start as HH:MM (24-hour) in the schedule timezone. |
| `availability.days[].shifts[].end_time` | string |  | everyone | Shift end as HH:MM (24-hour); must be after start_time. |
| `availability.updated_at` | string\|null | ISO 8601 | everyone | When the schedule last changed, or null when never saved. |
## OnboardingChecklist

Result of get_onboarding_checklist: setup progress for a fleet with the tool or page that completes each step. Payment-provider ids are never included.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string |  | everyone | The fleet. |
| `fleet_name` | string\|null |  | everyone | Fleet display name. |
| `booking_page_status` | enum |  | everyone | public_listed: bookable and listed in the rider app; unlisted_slug: bookable by link only (billing inactive); hidden_unavailable: riders cannot book yet. Values: `public_listed`, `unlisted_slug`, `hidden_unavailable`. |
| `booking_page_url` | string\|null |  | everyone | Public booking page to share with riders, or null until the fleet has a public link. |
| `done_count` | number |  | everyone | Items done. |
| `total_count` | number |  | everyone | Total items. |
| `required_remaining` | array |  | everyone | Keys of required items still open, in recommended order. |
| `items` | array |  | everyone | Checklist items in recommended order. |
| `items[].key` | enum |  | everyone | Stable identifier of the setup step. Values: `fleet_profile`, `brand_icon`, `service_area`, `ride_option_with_fare`, `booking_settings`, `vehicle`, `driver`, `payouts_connected`, `booking_link`, `first_booking`. |
| `items[].title` | string |  | everyone | Short human title of the step. |
| `items[].done` | boolean |  | everyone | True when the step is complete. |
| `items[].required` | boolean |  | everyone | True when riders cannot book until this step is done. |
| `items[].how_to` | string |  | everyone | What to do next: the MCP tool that completes the step when one exists, otherwise the web page. |
| `items[].tool` | string\|null |  | everyone | Name of the MCP tool that completes this step, or null when it needs the web console. |
| `items[].url` | string\|null |  | everyone | Absolute web URL where a human completes the step, or null. |
