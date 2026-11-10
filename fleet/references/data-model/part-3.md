# Meter data-model reference

Generated from the `@meterapp/meter-sdk` catalog and DTO schemas; do not edit by hand. See the [reference index](../data-model.md) for all definitions.

## PrivacySettingsWrite

Result of update_privacy_settings: what changed and the privacy settings after the call.

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
| `privacy` | object |  | everyone | Fleet privacy settings: driver location sharing and which drivers riders may request by name. |
| `privacy.fleet_id` | string |  | everyone | Fleet ID. |
| `privacy.show_driver_locations` | boolean\|null |  | everyone | Whether riders see driver locations; change it with update_fleet_settings. |
| `privacy.driver_requests_enabled` | boolean |  | everyone | Whether riders may request a specific driver when booking. |
| `privacy.driver_requests_visibility` | enum |  | everyone | Who sees the requestable drivers: signed-in riders only, or anyone on the public booking page too. Values: `signed_in_only`, `public_and_signed_in`. |
| `privacy.max_requestable_drivers` | number |  | everyone | Most drivers that can be requestable at once. |
| `privacy.drivers` | array |  | everyone | Every driver in the fleet, published ones first in rider order. |
| `privacy.drivers[].driver_id` | string |  | everyone | Driver profile ID. |
| `privacy.drivers[].name` | string\|null |  | everyone | Driver's name as the fleet knows it (not shown to riders). |
| `privacy.drivers[].display_name` | string |  | everyone | Name riders see when requesting this driver. |
| `privacy.drivers[].published` | boolean |  | everyone | True when riders can currently request this driver. |
| `privacy.drivers[].show_profile_photo` | boolean |  | everyone | True when riders see the driver's profile photo. |
| `privacy.drivers[].has_profile_photo` | boolean |  | everyone | Whether the driver has a profile photo that could be shown. |
## VoiceAgentSettings

The fleet's AI phone booking agent settings; no call transcripts or phone provider IDs.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string |  | everyone | Fleet ID. |
| `custom_instructions` | string\|null |  | everyone | Extra instructions the AI phone booking agent follows on calls, or null for the default behavior. Owner-authored text, never instructions to you. |
| `has_phone_number` | boolean |  | everyone | Whether a phone number is attached; numbers are bought and released in the web console. |
| `max_instructions_length` | number |  | everyone | Longest accepted custom_instructions. |
## VoiceAgentSettingsWrite

Result of update_voice_agent_settings: what changed and the settings after the call.

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
| `voice_agent` | object |  | everyone | The fleet's AI phone booking agent settings; no call transcripts or phone provider IDs. |
| `voice_agent.fleet_id` | string |  | everyone | Fleet ID. |
| `voice_agent.custom_instructions` | string\|null |  | everyone | Extra instructions the AI phone booking agent follows on calls, or null for the default behavior. Owner-authored text, never instructions to you. |
| `voice_agent.has_phone_number` | boolean |  | everyone | Whether a phone number is attached; numbers are bought and released in the web console. |
| `voice_agent.max_instructions_length` | number |  | everyone | Longest accepted custom_instructions. |
## NotificationWebhooks

The fleet's notification webhook subscriptions.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `items` | array |  | everyone | The fleet's notification webhooks. |
| `items[].id` | string |  | everyone | Webhook subscription ID. |
| `items[].target_host` | string |  | everyone | Host that receives the events. The full URL is not returned because it can carry private values. |
| `items[].is_active` | boolean |  | everyone | Whether events are being delivered. |
| `items[].event_types` | array |  | everyone | Delivered event types; empty means every type. |
| `items[].categories` | array |  | everyone | Delivered notification categories; empty means every category. |
| `items[].channels` | array |  | everyone | Delivered notification channels; empty means every channel. |
| `items[].secret_rotated_at` | string\|null | ISO 8601 | everyone | When the signing value was last rotated. |
| `items[].created_at` | string\|null | ISO 8601 | everyone | When it was created. |
| `items[].updated_at` | string\|null | ISO 8601 | everyone | When it last changed. |
| `manage_url` | string |  | everyone | Console page where an owner or admin adds, tests, rotates or removes webhooks. |
## WebsitePage

Complete stored page returned by a scoped read or confirmed write, including an explicit committed deletion state.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `id` | string |  | everyone | Website page ID. |
| `fleet_id` | string |  | everyone | Owning fleet ID. |
| `name` | string |  | everyone | Complete public title. |
| `slug` | string |  | everyone | Exact public URL segment. |
| `content` | string\|null |  | everyone | Complete public Markdown content, or null; never silently truncated. |
| `external_url` | string\|null |  | everyone | External destination, or null for a Markdown page. |
| `created_at` | string\|null |  | everyone | Creation timestamp, or null for legacy data. |
| `deleted` | boolean |  | everyone | True only for the committed deletion result; the other fields describe the removed page. |
## WebsitePageSummary

Public website page metadata; no Markdown body or internal audit fields.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `id` | string |  | everyone | Website page ID. |
| `fleet_id` | string |  | everyone | Owning fleet ID. |
| `name` | string |  | everyone | Complete public page title. |
| `slug` | string |  | everyone | Exact public URL segment below the fleet page path. |
| `external_url` | string\|null |  | everyone | External destination URL, or null for a Markdown page. |
| `content_bytes` | number |  | everyone | UTF-8 size of stored Markdown. List results omit its body. |
| `created_at` | string\|null |  | everyone | Creation timestamp, or null for legacy data. |
## WebsitePages

Current administrator website-page listing; Markdown bodies are intentionally omitted.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `pages` | array |  | everyone | Page metadata ordered by immutable page ID. |
| `pages[].id` | string |  | everyone | Website page ID. |
| `pages[].fleet_id` | string |  | everyone | Owning fleet ID. |
| `pages[].name` | string |  | everyone | Complete public page title. |
| `pages[].slug` | string |  | everyone | Exact public URL segment below the fleet page path. |
| `pages[].external_url` | string\|null |  | everyone | External destination URL, or null for a Markdown page. |
| `pages[].content_bytes` | number |  | everyone | UTF-8 size of stored Markdown. List results omit its body. |
| `pages[].created_at` | string\|null |  | everyone | Creation timestamp, or null for legacy data. |
| `next_cursor` | string\|null |  | everyone | Opaque fleet-bound cursor, or null when no more pages remain. |
## WebsitePageWrite

WebsitePageWrite

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
| `page` | object\|null |  | everyone | Complete stored page returned by a scoped read or confirmed write, including an explicit committed deletion state. |
| `page.id` | string |  | everyone | Website page ID. |
| `page.fleet_id` | string |  | everyone | Owning fleet ID. |
| `page.name` | string |  | everyone | Complete public title. |
| `page.slug` | string |  | everyone | Exact public URL segment. |
| `page.content` | string\|null |  | everyone | Complete public Markdown content, or null; never silently truncated. |
| `page.external_url` | string\|null |  | everyone | External destination, or null for a Markdown page. |
| `page.created_at` | string\|null |  | everyone | Creation timestamp, or null for legacy data. |
| `page.deleted` | boolean |  | everyone | True only for the committed deletion result; the other fields describe the removed page. |
## QuoteActionResult

Committed quote action and truthful notification processing state without recipient or provider details.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `quote` | object |  | everyone | Frozen committed quote facts. |
| `quote.id` | string |  | everyone | Meter quote identifier. |
| `quote.fleet_id` | string\|null |  | everyone | Owning fleet, or null for an individually owned quote. |
| `quote.status` | enum |  | everyone | Stored quote status; converted means a booking was created. Values: `draft`, `open`, `converted`, `declined`, `expired`, `withdrawn`. |
| `quote.revision` | number |  | everyone | Current price revision, used when confirming a proposed change. |
| `quote.currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `quote.total_unit_amount` | number | minor currency units | everyone | Current quoted total in this currency’s minor units, including the stored custom-price decision. |
| `quote.custom_price_unit_amount` | number\|null | minor currency units | everyone | Custom total in currency minor units, or null when using the estimate. |
| `quote.pickup_at` | string |  | everyone | Scheduled pickup time. |
| `quote.expires_at` | string |  | everyone | Stored confirmation deadline; does not by itself reserve availability. |
| `quote.created_at` | string |  | everyone | Creation timestamp. |
| `quote.updated_at` | string |  | everyone | Last stored change timestamp. |
| `quote.sent_at` | string\|null |  | everyone | Most recent send timestamp, or null; not proof of notification delivery. |
| `quote.is_asap` | boolean |  | everyone | Whether the quote requests pickup as soon as possible. |
| `quote.is_time_booking` | boolean |  | everyone | Whether this quote is for a time-based booking. |
| `notification_state` | enum |  | everyone | Processing state only; does not prove provider acceptance or rider delivery. Started or uncertain attempts are not automatically resent. Values: `not_required`, `queued`, `completed`, `manual_handoff`, `superseded`. |
## QuoteActionWrite

Saved quote lifecycle confirmation and immutable committed outcome; no booking or money movement.

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
| `action` | object |  | everyone | Committed quote action and truthful notification processing state without recipient or provider details. |
| `action.quote` | object |  | everyone | Frozen committed quote facts. |
| `action.quote.id` | string |  | everyone | Meter quote identifier. |
| `action.quote.fleet_id` | string\|null |  | everyone | Owning fleet, or null for an individually owned quote. |
| `action.quote.status` | enum |  | everyone | Stored quote status; converted means a booking was created. Values: `draft`, `open`, `converted`, `declined`, `expired`, `withdrawn`. |
| `action.quote.revision` | number |  | everyone | Current price revision, used when confirming a proposed change. |
| `action.quote.currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `action.quote.total_unit_amount` | number | minor currency units | everyone | Current quoted total in this currency’s minor units, including the stored custom-price decision. |
| `action.quote.custom_price_unit_amount` | number\|null | minor currency units | everyone | Custom total in currency minor units, or null when using the estimate. |
| `action.quote.pickup_at` | string |  | everyone | Scheduled pickup time. |
| `action.quote.expires_at` | string |  | everyone | Stored confirmation deadline; does not by itself reserve availability. |
| `action.quote.created_at` | string |  | everyone | Creation timestamp. |
| `action.quote.updated_at` | string |  | everyone | Last stored change timestamp. |
| `action.quote.sent_at` | string\|null |  | everyone | Most recent send timestamp, or null; not proof of notification delivery. |
| `action.quote.is_asap` | boolean |  | everyone | Whether the quote requests pickup as soon as possible. |
| `action.quote.is_time_booking` | boolean |  | everyone | Whether this quote is for a time-based booking. |
| `action.notification_state` | enum |  | everyone | Processing state only; does not prove provider acceptance or rider delivery. Started or uncertain attempts are not automatically resent. Values: `not_required`, `queued`, `completed`, `manual_handoff`, `superseded`. |
## QuoteSummary

An authorized stored quote summary, excluding contact details, notes, preview/receipt internals, private delivery links and conversion leases.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `id` | string |  | everyone | Meter quote identifier. |
| `fleet_id` | string\|null |  | everyone | Owning fleet, or null for an individually owned quote. |
| `status` | enum |  | everyone | Stored quote status; converted means a booking was created. Values: `draft`, `open`, `converted`, `declined`, `expired`, `withdrawn`. |
| `revision` | number |  | everyone | Current price revision, used when confirming a proposed change. |
| `currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `total_unit_amount` | number | minor currency units | everyone | Current quoted total in this currency’s minor units, including the stored custom-price decision. |
| `custom_price_unit_amount` | number\|null | minor currency units | everyone | Custom total in currency minor units, or null when using the estimate. |
| `pickup_at` | string |  | everyone | Scheduled pickup time. |
| `expires_at` | string |  | everyone | Stored confirmation deadline; does not by itself reserve availability. |
| `created_at` | string |  | everyone | Creation timestamp. |
| `updated_at` | string |  | everyone | Last stored change timestamp. |
| `sent_at` | string\|null |  | everyone | Most recent send timestamp, or null; not proof of notification delivery. |
| `is_asap` | boolean |  | everyone | Whether the quote requests pickup as soon as possible. |
| `is_time_booking` | boolean |  | everyone | Whether this quote is for a time-based booking. |
## QuoteDetail

Authorized quote detail with minimal current notification processing; excludes job IDs, provider IDs, recipient data and private packets.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `id` | string |  | everyone | Meter quote identifier. |
| `fleet_id` | string\|null |  | everyone | Owning fleet, or null for an individually owned quote. |
| `status` | enum |  | everyone | Stored quote status; converted means a booking was created. Values: `draft`, `open`, `converted`, `declined`, `expired`, `withdrawn`. |
| `revision` | number |  | everyone | Current price revision, used when confirming a proposed change. |
| `currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `total_unit_amount` | number | minor currency units | everyone | Current quoted total in this currency’s minor units, including the stored custom-price decision. |
| `custom_price_unit_amount` | number\|null | minor currency units | everyone | Custom total in currency minor units, or null when using the estimate. |
| `pickup_at` | string |  | everyone | Scheduled pickup time. |
| `expires_at` | string |  | everyone | Stored confirmation deadline; does not by itself reserve availability. |
| `created_at` | string |  | everyone | Creation timestamp. |
| `updated_at` | string |  | everyone | Last stored change timestamp. |
| `sent_at` | string\|null |  | everyone | Most recent send timestamp, or null; not proof of notification delivery. |
| `is_asap` | boolean |  | everyone | Whether the quote requests pickup as soon as possible. |
| `is_time_booking` | boolean |  | everyone | Whether this quote is for a time-based booking. |
| `notification` | object\|null |  | everyone | Latest retained delivery marker for this exact revision, or null when none exists. |
| `notification.revision` | number |  | everyone | Exact current quote revision. |
| `notification.state` | enum |  | everyone | Current processing state; completed does not prove recipient delivery. Unknown or started attempts are never automatically resent. Values: `queued`, `processing`, `completed`, `manual_handoff`, `superseded`. |
| `notification.console_url` | string\|null |  | everyone | Existing operator quote detail page for manual handoff, or null for rider scope and other states. No automatic provider replay or money action. |
| `rider_followup_notification` | object\|null |  | everyone | Distinct rider-to-operator request processing for this exact revision. Null for rider scope or when absent; queued/completed is not delivery proof. |
| `rider_followup_notification.revision` | number |  | everyone | Exact current quote revision. |
| `rider_followup_notification.state` | enum |  | everyone | Current processing state; completed does not prove recipient delivery. Unknown or started attempts are never automatically resent. Values: `queued`, `processing`, `completed`, `manual_handoff`, `superseded`. |
| `rider_followup_notification.console_url` | string\|null |  | everyone | Existing operator quote detail page for manual handoff, or null for rider scope and other states. No automatic provider replay or money action. |
## QuotePage

A bounded page of currently authorized stored quotes.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `items` | array |  | everyone | The page of results, newest first unless the tool says otherwise. |
| `items[].id` | string |  | everyone | Meter quote identifier. |
| `items[].fleet_id` | string\|null |  | everyone | Owning fleet, or null for an individually owned quote. |
| `items[].status` | enum |  | everyone | Stored quote status; converted means a booking was created. Values: `draft`, `open`, `converted`, `declined`, `expired`, `withdrawn`. |
| `items[].revision` | number |  | everyone | Current price revision, used when confirming a proposed change. |
| `items[].currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `items[].total_unit_amount` | number | minor currency units | everyone | Current quoted total in this currency’s minor units, including the stored custom-price decision. |
| `items[].custom_price_unit_amount` | number\|null | minor currency units | everyone | Custom total in currency minor units, or null when using the estimate. |
| `items[].pickup_at` | string |  | everyone | Scheduled pickup time. |
| `items[].expires_at` | string |  | everyone | Stored confirmation deadline; does not by itself reserve availability. |
| `items[].created_at` | string |  | everyone | Creation timestamp. |
| `items[].updated_at` | string |  | everyone | Last stored change timestamp. |
| `items[].sent_at` | string\|null |  | everyone | Most recent send timestamp, or null; not proof of notification delivery. |
| `items[].is_asap` | boolean |  | everyone | Whether the quote requests pickup as soon as possible. |
| `items[].is_time_booking` | boolean |  | everyone | Whether this quote is for a time-based booking. |
| `next_cursor` | string\|null |  | everyone | Send this back as `cursor` to fetch the next page. Null when there are no more results. |
| `has_more` | boolean |  | everyone | True when another page exists. |
## QuoteWrite

Saved quote creation or pricing preview and immutable committed outcome; does not send or convert the quote.

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
| `quote` | object |  | everyone | An authorized stored quote summary, excluding contact details, notes, preview/receipt internals, private delivery links and conversion leases. |
| `quote.id` | string |  | everyone | Meter quote identifier. |
| `quote.fleet_id` | string\|null |  | everyone | Owning fleet, or null for an individually owned quote. |
| `quote.status` | enum |  | everyone | Stored quote status; converted means a booking was created. Values: `draft`, `open`, `converted`, `declined`, `expired`, `withdrawn`. |
| `quote.revision` | number |  | everyone | Current price revision, used when confirming a proposed change. |
| `quote.currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `quote.total_unit_amount` | number | minor currency units | everyone | Current quoted total in this currency’s minor units, including the stored custom-price decision. |
| `quote.custom_price_unit_amount` | number\|null | minor currency units | everyone | Custom total in currency minor units, or null when using the estimate. |
| `quote.pickup_at` | string |  | everyone | Scheduled pickup time. |
| `quote.expires_at` | string |  | everyone | Stored confirmation deadline; does not by itself reserve availability. |
| `quote.created_at` | string |  | everyone | Creation timestamp. |
| `quote.updated_at` | string |  | everyone | Last stored change timestamp. |
| `quote.sent_at` | string\|null |  | everyone | Most recent send timestamp, or null; not proof of notification delivery. |
| `quote.is_asap` | boolean |  | everyone | Whether the quote requests pickup as soon as possible. |
| `quote.is_time_booking` | boolean |  | everyone | Whether this quote is for a time-based booking. |
## MeterPayStatus

Read-only Meter Pay readiness with safe setup guidance and no provider IDs, URLs or KYC values.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `scope` | enum |  | everyone | Own account or explicitly selected fleet payment recipient. Values: `me`, `fleet`. |
| `fleet_id` | string\|null |  | everyone | Selected Meter fleet ID, or null for your own account. |
| `account_connected` | boolean |  | everyone | Whether an existing payment account is connected. |
| `country` | string\|null |  | everyone | Payment account or detected country code, when known. |
| `status` | enum |  | everyone | Current Meter Pay readiness stage. Values: `not_started`, `unsupported`, `requirements_due`, `pending_verification`, `restricted`, `ready`. |
| `payments_ready` | boolean |  | everyone | Whether this account can accept payments. |
| `payouts_ready` | boolean |  | everyone | Whether this account can receive payouts. |
| `tap_to_pay_ready` | boolean |  | everyone | Account and selected fleet support Tap to Pay. Device, OS and location eligibility must still be checked in the app. |
| `blockers` | array |  | everyone | Plain-language setup or readiness blockers, without provider identifiers. |
| `missing` | array |  | everyone | Required information categories and safe explanations; no raw provider field paths or personal values. |
| `missing[].category` | enum |  | everyone | Safe category of required account information. Values: `address`, `bank_account`, `business_profile`, `company`, `contact`, `director`, `document`, `executive`, `identity`, `individual`, `owner`, `representative`, `tax`, `terms_of_service`, `other`, `risk`. |
| `missing[].description` | string |  | everyone | Safe explanation of the missing information. |
| `missing[].status` | enum |  | everyone | When the information is required or whether verification is pending. Values: `currently_due`, `past_due`, `eventually_due`, `pending_verification`. |
| `management_action` | enum |  | everyone | Send this action to get_action_link; include fleet_id for fleet scope. Values: `meter_pay_setup`, `meter_pay_manage`. |
| `checked_at` | string | ISO 8601 | everyone | ISO 8601 timestamp with offset (UTC unless noted). |
## SubscriptionOverview

Read-only plan and subscription state with the hand-off actions to upgrade, change, cancel or update payment. No provider IDs, invoices or card details.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `plan` | enum |  | everyone | Plan the account is entitled to right now. meter_fleet includes Pro features. Values: `free`, `meter_pro`, `meter_fleet`, `meter_pro_and_fleet`. |
| `plan_check` | enum |  | everyone | live: read from the entitlement service. stored: that service was unavailable, so plan is derived from stored subscriptions and may miss granted access. Values: `live`, `stored`. |
| `pro_features_unlocked` | boolean |  | everyone | Whether Pro driver features (unlimited trips and premium tools) are unlocked, by Pro or by Fleet. |
| `subscriptions` | array |  | everyone | The current (or most recent) subscription per product family, newest first. Empty when the account never subscribed. |
| `subscriptions[].family` | enum |  | everyone | Product family of the subscription. other: a legacy add-on such as ad-free. Values: `pro`, `fleet`, `other`. |
| `subscriptions[].product_name` | string\|null |  | everyone | Product name as billed, when known. |
| `subscriptions[].status` | enum |  | everyone | Billing status. past_due: a renewal payment failed and is being retried; access continues while retrying. Values: `active`, `trialing`, `past_due`, `unpaid`, `incomplete`, `incomplete_expired`, `paused`, `canceled`. |
| `subscriptions[].gives_access` | boolean |  | everyone | Whether this subscription unlocks its plan right now (active, trialing or past_due within its period). |
| `subscriptions[].purchase_source` | enum |  | everyone | Who billed it: stripe_web (Meter web checkout), app_store, play_store, promotional (granted by Meter) or other. Values: `stripe_web`, `app_store`, `play_store`, `promotional`, `other`. |
| `subscriptions[].billing_model` | enum |  | everyone | flat: one fixed price per interval. per_active_driver: billed for each active driver in the period. store: priced and billed by the App Store or Google Play. Values: `flat`, `per_active_driver`, `store`. |
| `subscriptions[].price` | object\|null |  | everyone | List price per period for web (Stripe) subscriptions; null for store purchases, whose price is set by the store. |
| `subscriptions[].price.amount_minor` | number | minor currency units | everyone | Amount in the currency's minor unit (cents for USD/EUR, yen for JPY). Divide by 100 for most currencies. |
| `subscriptions[].price.currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `subscriptions[].price.interval` | enum |  | everyone | Billing interval. Values: `day`, `week`, `month`, `year`. |
| `subscriptions[].price.interval_count` | number |  | everyone | Number of intervals per billing period. |
| `subscriptions[].seats` | number\|null |  | everyone | Billed quantity reported by the provider (for per-driver fleet billing, drivers in the current period), or null. |
| `subscriptions[].trial_ends_at` | string\|null | ISO 8601 | everyone | ISO 8601 timestamp with offset, or null when not (yet) known. |
| `subscriptions[].current_period_end` | string\|null | ISO 8601 | everyone | End of the current paid period: the renewal date, or the access end date when cancel_at_period_end is true. |
| `subscriptions[].cancel_at_period_end` | boolean |  | everyone | True when cancellation is scheduled: access continues until current_period_end and the subscription does not renew. |
| `subscriptions[].manage` | object |  | everyone | How the human manages this purchase. |
| `subscriptions[].manage.where` | enum |  | everyone | Where the human changes, cancels or updates payment for this purchase. Store purchases can only be changed in that store; none means nothing to manage (granted access). Values: `meter_console`, `app_store`, `play_store`, `none`. |
| `subscriptions[].manage.actions` | array |  | everyone | get_action_link actions that open the right place, in order of usefulness. Include fleet_id for a fleet subscription when the caller owns it. |
| `granted_access` | array |  | everyone | Plans unlocked without a paid subscription on this account, such as a Meter promotion or membership of a paid fleet. Nothing to cancel or pay. |
| `granted_access[].family` | enum |  | everyone | pro: Meter Pro (driver features). fleet: Meter Fleet (a fleet's team, booking and dispatch features; also unlocks Pro features for the subscriber). Values: `pro`, `fleet`. |
| `granted_access[].expires_at` | string\|null | ISO 8601 | everyone | ISO 8601 timestamp with offset, or null when not (yet) known. |
| `store_notice` | object\|null |  | everyone | Latest store cancellation or refund that still applies, the same notice the Meter app shows, or null. |
| `store_notice.type` | enum |  | everyone | What the App Store or Google Play reported. Values: `cancellation_scheduled`, `refund_processed`. |
| `store_notice.platform` | enum\|null |  | everyone | Store platform of the purchase, when known. Values: `android`, `ios`. |
| `store_notice.occurred_at` | string | ISO 8601 | everyone | ISO 8601 timestamp with offset (UTC unless noted). |
| `store_notice.effective_at` | string\|null | ISO 8601 | everyone | ISO 8601 timestamp with offset, or null when not (yet) known. |
| `fleets` | array |  | everyone | Fleets the caller owns or administers, with their subscription state. Drivers' fleets are not listed. |
| `fleets[].fleet_id` | string |  | everyone | Meter fleet ID. |
| `fleets[].fleet_name` | string\|null |  | everyone | Fleet name. |
| `fleets[].role` | enum |  | everyone | Role in the fleet. owner: created the fleet and controls billing; admin: manages members, vehicles, bookings and money; driver: drives and sees only their own trips, bookings and earnings. Values: `owner`, `admin`, `driver`. |
| `fleets[].billing_status` | enum |  | everyone | Status of the fleet owner's Meter Fleet subscription; none when the fleet has never subscribed. Values: `active`, `trialing`, `past_due`, `unpaid`, `incomplete`, `incomplete_expired`, `paused`, `canceled`, `none`. |
| `fleets[].billing_active` | boolean |  | everyone | Whether fleet billing counts as active (active, trialing or past_due). Fleet features lock when false. |
| `fleets[].operational` | boolean |  | everyone | Whether the fleet is onboarded and paid, so fleet tools and driver features work. |
| `fleets[].manage_actions` | array |  | everyone | get_action_link actions for this fleet's billing (include fleet_id). Empty for admins: only the owner manages fleet billing. |
| `upgrade_actions` | array |  | everyone | get_action_link actions that start a plan this account does not have yet. Call list_plans to compare plans first. |
| `checked_at` | string | ISO 8601 | everyone | ISO 8601 timestamp with offset (UTC unless noted). |
## PlanCatalog

Meter plans with current prices, purchase channels and the capabilities each unlocks. Read-only; subscribing happens in Meter through get_action_link.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `currency` | string\|null |  | everyone | Requested display currency (ISO 4217, upper-case), or null for the catalog's base currency. |
| `plans` | array |  | everyone | Every Meter plan, from free to Fleet. |
| `plans[].plan` | enum |  | everyone | Plan code, as reported by get_subscription. Values: `free`, `meter_pro`, `meter_fleet`. |
| `plans[].name` | string |  | everyone | Plan name. |
| `plans[].includes` | array |  | everyone | Lower plans whose capabilities this plan also unlocks. |
| `plans[].purchase_channels` | array |  | everyone | Where the plan can be bought. Empty for the free plan. |
| `plans[].subscribe_action` | enum\|null |  | everyone | get_action_link action that starts this plan, or null for the free plan. Values: `subscribe_pro`, `subscribe_fleet`, `manage_subscription`, `manage_store_subscription`, `change_plan`, `cancel_subscription`, `update_payment_method`, `meter_pay_setup`, `meter_pay_manage`, `respond_to_dispute`, `request_refund`, `upload_documents`, `edit_fleet_member`, `change_email`, `change_phone`, `delete_account`, `delete_fleet`, `upload_fleet_icon`, `draw_service_area`, `download_pay_stub`, `download_export`, `add_payment_method`, `finish_ride_payment`, `track_ride`, `review_quote`, `tip_ride`. |
| `plans[].price_source` | enum |  | everyone | meter_catalog: prices below are Meter's web prices. store: the App Store or Google Play sets the price for the buyer's region; it is shown in the Meter app before purchase. Values: `free`, `meter_catalog`, `store`. |
| `plans[].prices` | array |  | everyone | Current prices. Empty for free and store-priced plans. |
| `plans[].prices[].interval` | enum |  | everyone | Billing interval. Values: `day`, `week`, `month`, `year`. |
| `plans[].prices[].interval_count` | number |  | everyone | Number of intervals per billing period. |
| `plans[].prices[].amount_minor` | number | minor currency units | everyone | Amount in the currency's minor unit (cents for USD/EUR, yen for JPY). Divide by 100 for most currencies. |
| `plans[].prices[].currency` | string |  | everyone | ISO 4217 currency code, lower- or upper-case as stored (e.g. "usd", "EUR"). |
| `plans[].prices[].formatted` | string |  | everyone | The amount formatted for display in the caller's language. |
| `plans[].prices[].requested_currency_available` | boolean |  | everyone | False when the requested currency is not offered and the base currency is shown instead. |
| `plans[].prices[].trial_days` | number\|null |  | everyone | Free trial length offered with this price, or null. |
| `plans[].prices[].billing_model` | enum |  | everyone | flat: one fixed price per interval. per_active_driver: billed for each active driver in the period. store: priced and billed by the App Store or Google Play. Values: `flat`, `per_active_driver`, `store`. |
| `plans[].capabilities` | array |  | everyone | Capabilities this plan unlocks beyond the lower plans it includes, derived from Meter's entitlement policy. |
| `plans[].capabilities[].id` | string |  | everyone | Stable Meter capability ID, as used in entitlement decisions. |
| `plans[].capabilities[].scope` | enum |  | everyone | account: unlocked for the subscriber's own driving. fleet: unlocked for an active fleet's members, subject to each member's role. Values: `account`, `fleet`. |
| `plans[].capabilities[].description` | string |  | everyone | What the capability allows, from Meter's entitlement policy. |
| `plans[].unlimited_trips` | boolean |  | everyone | Whether the free trip allowance limit is lifted. |
| `checked_at` | string | ISO 8601 | everyone | ISO 8601 timestamp with offset (UTC unless noted). |
## ActionLink

Human continuation in Meter. Issuing a link never purchases, pays, refunds, or deletes anything.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `action` | enum |  | everyone | The human action requested. Values: `subscribe_pro`, `subscribe_fleet`, `manage_subscription`, `manage_store_subscription`, `change_plan`, `cancel_subscription`, `update_payment_method`, `meter_pay_setup`, `meter_pay_manage`, `respond_to_dispute`, `request_refund`, `upload_documents`, `edit_fleet_member`, `change_email`, `change_phone`, `delete_account`, `delete_fleet`, `upload_fleet_icon`, `draw_service_area`, `download_pay_stub`, `download_export`, `add_payment_method`, `finish_ride_payment`, `track_ride`, `review_quote`, `tip_ride`. |
| `label` | string |  | everyone | Localized action label; payment setup is called Meter Pay. |
| `url` | string |  | everyone | Meter page URL to present unchanged. Never a provider session or signed download URL. |
| `where_in_console` | string |  | everyone | Where the human can find the action in Meter. |
| `where_in_app` | string |  | everyone | Native app guidance, or instructions to open the web console. |
| `why_handoff` | string |  | everyone | Why the human must finish this action and whether it needs the store or Meter support. |
## ChangeRequest

An actor-owned change history entry. Never includes stored input, basis, result, or internal completion identifiers.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `id` | string |  | everyone | Proposal id. Confirmation still requires the original actor and channel. |
| `tool` | string |  | everyone | Tool that proposed this change. |
| `title` | string |  | everyone | Human-readable tool title. |
| `target_label` | string\|null |  | everyone | Display label of the affected object, or null after retention redaction. |
| `risk` | enum |  | everyone | Risk tier of the change. Values: `low`, `standard`, `sensitive`. |
| `status` | enum |  | everyone | Current proposal or application outcome. Values: `proposed`, `applying`, `applied`, `declined`, `expired`, `stale`, `failed`. |
| `changes` | array |  | everyone | Field changes; empty after retention redaction. |
| `changes[].field` | string |  | everyone | Name of the changed argument, exactly as passed to the tool (e.g. "contact_phone", "fare.base"). |
| `changes[].from` | string\|number\|boolean\|null\|array\|array |  | everyone | Value before the change. |
| `changes[].to` | string\|number\|boolean\|null\|array\|array |  | everyone | Value after the change. |
| `created_at` | string | ISO 8601 | everyone | ISO 8601 timestamp with offset (UTC unless noted). |
| `expires_at` | string | ISO 8601 | everyone | ISO 8601 timestamp with offset (UTC unless noted). |
| `decided_at` | string\|null | ISO 8601 | everyone | ISO 8601 timestamp with offset, or null when not (yet) known. |
| `applied_at` | string\|null | ISO 8601 | everyone | ISO 8601 timestamp with offset, or null when not (yet) known. |
| `redacted_at` | string\|null | ISO 8601 | everyone | ISO 8601 timestamp with offset, or null when not (yet) known. |
| `error_code` | string\|null |  | everyone | Stable failure code, without internal error text. |
## ChangeRequestPage

A page of the signed-in actor’s assistant changes, with an opaque continuation cursor.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `items` | array |  | everyone | The page of results, newest first unless the tool says otherwise. |
| `items[].id` | string |  | everyone | Proposal id. Confirmation still requires the original actor and channel. |
| `items[].tool` | string |  | everyone | Tool that proposed this change. |
| `items[].title` | string |  | everyone | Human-readable tool title. |
| `items[].target_label` | string\|null |  | everyone | Display label of the affected object, or null after retention redaction. |
| `items[].risk` | enum |  | everyone | Risk tier of the change. Values: `low`, `standard`, `sensitive`. |
| `items[].status` | enum |  | everyone | Current proposal or application outcome. Values: `proposed`, `applying`, `applied`, `declined`, `expired`, `stale`, `failed`. |
| `items[].changes` | array |  | everyone | Field changes; empty after retention redaction. |
| `items[].changes[].field` | string |  | everyone | Name of the changed argument, exactly as passed to the tool (e.g. "contact_phone", "fare.base"). |
| `items[].changes[].from` | string\|number\|boolean\|null\|array\|array |  | everyone | Value before the change. |
| `items[].changes[].to` | string\|number\|boolean\|null\|array\|array |  | everyone | Value after the change. |
| `items[].created_at` | string | ISO 8601 | everyone | ISO 8601 timestamp with offset (UTC unless noted). |
| `items[].expires_at` | string | ISO 8601 | everyone | ISO 8601 timestamp with offset (UTC unless noted). |
| `items[].decided_at` | string\|null | ISO 8601 | everyone | ISO 8601 timestamp with offset, or null when not (yet) known. |
| `items[].applied_at` | string\|null | ISO 8601 | everyone | ISO 8601 timestamp with offset, or null when not (yet) known. |
| `items[].redacted_at` | string\|null | ISO 8601 | everyone | ISO 8601 timestamp with offset, or null when not (yet) known. |
| `items[].error_code` | string\|null |  | everyone | Stable failure code, without internal error text. |
| `next_cursor` | string\|null |  | everyone | Send this back as `cursor` to fetch the next page. Null when there are no more results. |
| `has_more` | boolean |  | everyone | True when another page exists. |
## Whoami

Result of `whoami`: who is calling and what they may read.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `profile` | object |  | everyone | The authenticated caller. |
| `profile.id` | string |  | everyone | Your profile id. Other tools refer to you by this id. |
| `profile.display_name` | string\|null |  | everyone | Your display name, or null if not set. |
| `profile.email` | string\|null |  | self | Your own email address (never shown for other users). |
| `profile.phone` | string\|null |  | self | Your own phone number in E.164 (never shown for other users). |
| `profile.created_at` | string\|null | ISO 8601 | everyone | When your Meter profile was created. |
| `fleets` | array |  | everyone | Every fleet you belong to. Empty for riders and solo drivers. |
| `fleets[].fleet_id` | string |  | everyone | Opaque fleet id. Send as `fleet_id` to fleet-scoped tools. |
| `fleets[].name` | string\|null |  | everyone | Fleet display name. |
| `fleets[].role` | enum |  | everyone | Role in the fleet. owner: created the fleet and controls billing; admin: manages members, vehicles, bookings and money; driver: drives and sees only their own trips, bookings and earnings. Values: `owner`, `admin`, `driver`. |
| `fleets[].is_operational` | boolean |  | everyone | True when the fleet has finished onboarding and billing is active. Admin-only tools (members, accounting, fleet-wide trips) require an operational fleet. |
| `is_rider` | boolean |  | everyone | True when you have a rider account (you have booked rides). Rider-scoped tools return your own bookings. |
| `is_fleet_admin` | boolean |  | everyone | True when you are owner or admin of at least one fleet. |
| `default_fleet_id` | string\|null |  | everyone | When you belong to exactly one fleet, its id; fleet-scoped tools use it when `fleet_id` is omitted. Null otherwise. |
| `capabilities` | array |  | everyone | Human-readable summary of what you can read through this server, derived from your roles. |
| `connection` | object\|null (optional) |  | everyone | Verified OAuth app grant, or null for a first-party session. Manage or revoke the grant in Connected apps. |
| `connection.app_name` | string\|null |  | everyone | Stored OAuth app name, never a client-supplied identity. |
| `connection.access` | enum |  | everyone | Current server-stored connection permission. Values: `read`, `read_write`. |
| `connection.manage_url` | enum |  | everyone | Meter page for managing this connection. Values: `/app/account/connected-apps`. |
| `suggested_next_tools` | array |  | everyone | Tool names that make sense to call next given your roles. |
## FleetSummary

A fleet as seen in list_fleets.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string |  | everyone | Opaque fleet id. |
| `name` | string\|null |  | everyone | Fleet display name. |
| `city` | string\|null |  | everyone | Primary city the fleet operates in. |
| `country_iso_code` | string\|null |  | everyone | ISO 3166-1 alpha-2 country code. |
| `currency_iso_code` | string\|null |  | everyone | ISO 4217 currency the fleet prices in. |
| `timezone` | string\|null |  | everyone | IANA timezone of the fleet, e.g. "America/New_York". |
| `role` | enum |  | everyone | Role in the fleet. owner: created the fleet and controls billing; admin: manages members, vehicles, bookings and money; driver: drives and sees only their own trips, bookings and earnings. Values: `owner`, `admin`, `driver`. |
| `is_operational` | boolean |  | everyone | True when onboarding is complete and billing is active; admin-only tools require this. |
| `created_at` | string\|null | ISO 8601 | everyone | When the fleet was created. |
## FleetDetail

Result of get_fleet. Drivers get public info; owners/admins also get settings and the driver invite.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string |  | everyone | Opaque fleet id. |
| `name` | string\|null |  | everyone | Fleet display name. |
| `city` | string\|null |  | everyone | Primary city the fleet operates in. |
| `country_iso_code` | string\|null |  | everyone | ISO 3166-1 alpha-2 country code. |
| `currency_iso_code` | string\|null |  | everyone | ISO 4217 currency the fleet prices in. |
| `timezone` | string\|null |  | everyone | IANA timezone of the fleet, e.g. "America/New_York". |
| `role` | enum |  | everyone | Role in the fleet. owner: created the fleet and controls billing; admin: manages members, vehicles, bookings and money; driver: drives and sees only their own trips, bookings and earnings. Values: `owner`, `admin`, `driver`. |
| `is_operational` | boolean |  | everyone | True when onboarding is complete and billing is active; admin-only tools require this. |
| `created_at` | string\|null | ISO 8601 | everyone | When the fleet was created. |
| `description` | string\|null |  | everyone | Public fleet description (bio). |
| `contact_phone` | string\|null |  | everyone | Public contact phone of the fleet. |
| `dispatch_phone` | string\|null |  | everyone | Public dispatch phone of the fleet. |
| `website` | string\|null |  | everyone | Public website URL. |
| `member_count` | number |  | everyone | Number of members (all roles). |
| `vehicle_count` | number |  | everyone | Number of active fleet vehicles. |
| `service_zones` | array |  | everyone | Service/pricing zones by name. |
| `service_zones[].zone_id` | number |  | everyone | Zone id, unique within Meter. |
| `service_zones[].name` | string |  | everyone | Zone name (e.g. "Downtown", "Airport"). |
| `service_zones[].description` | string\|null |  | everyone | Optional description of the zone. |
| `ride_options` | array |  | everyone | Bookable ride options with headline fares. |
| `ride_options[].id` | string |  | everyone | Ride option id. |
| `ride_options[].name` | string |  | everyone | Ride option name (e.g. "Sedan", "Van"). |
| `ride_options[].type` | string |  | everyone | Ride option type as stored (e.g. "standard", "xl"). |
| `ride_options[].capacity` | number |  | everyone | Passenger capacity. |
| `ride_options[].default_fare` | object\|null |  | everyone | Default fare for this option, or null. |
| `ride_options[].default_fare.display_name` | string\|null |  | everyone | Fare name shown to drivers and riders. |
| `ride_options[].default_fare.currency_code` | string |  | everyone | ISO 4217 currency of the rates below. |
| `ride_options[].default_fare.base` | number | major currency units | everyone | Flag-drop / base fare in major currency units (e.g. 3.50 = $3.50). |
| `ride_options[].default_fare.minimum_fare` | number | major currency units | everyone | Minimum total fare in major currency units. |
| `ride_options[].default_fare.distance_rate` | number | major currency units per mile or km | everyone | Rate per distance unit (mile, or kilometer when `metric` is true) in major units. |
| `ride_options[].default_fare.minute_rate` | number | major currency units per minute | everyone | Rate per minute in major currency units. |
| `ride_options[].default_fare.wait_time_minute_rate` | number | major currency units per minute | everyone | Rate per minute of waiting in major currency units. |
| `ride_options[].default_fare.metric` | boolean |  | everyone | True when distance_rate is per kilometer; false when per mile. |
| `booking_settings` | object\|null |  | owner, admin | Booking policy; null for drivers. |
| `booking_settings.dispatch_mode` | string |  | everyone | How bookings are dispatched to drivers (stored enum). |
| `booking_settings.payment_mode` | string\|null |  | everyone | Booking payment mode (stored enum), or null for the default. |
| `booking_settings.pre_payment_enabled` | boolean |  | everyone | Whether riders must authorize payment before the ride. |
| `booking_settings.min_lead_time_seconds` | number | seconds | everyone | Minimum notice for a scheduled booking. |
| `booking_settings.time_slot_minutes` | number\|null | minutes | everyone | Booking time-slot granularity, or null. |
| `booking_settings.minimum_duration_minutes` | number\|null | minutes | everyone | Minimum length of an hourly booking, or null when none is set. |
| `booking_settings.cancellation_fee_fraction` | number |  | everyone | Cancellation fee as a fraction of the fare (0-1). |
| `booking_settings.cancellation_grace_period_seconds` | number | seconds | everyone | Free-cancellation window after booking. |
| `booking_settings.individual_passenger_capacity` | number |  | everyone | Default passenger capacity for individual bookings. |
| `admin_settings` | object\|null |  | owner, admin | Operational settings; null for drivers. |
| `admin_settings.default_driver_payout_fraction` | number\|null |  | everyone | Default share of each fare paid to the driver (0-1), or null when payouts are not configured. |
| `admin_settings.allow_fleet_custom_fares` | boolean |  | everyone | Whether drivers may use custom fares. |
| `admin_settings.show_driver_locations` | boolean |  | everyone | Whether riders see live driver locations on the public booking page. |
| `admin_settings.trip_collection_mode` | string\|null |  | everyone | Deprecated: no longer affects how trip payments are collected. Kept for compatibility; may be null. |
| `admin_settings.tip_split_behavior` | string\|null |  | everyone | How tips are split between fleet and driver (stored enum), or null. |
| `admin_settings.pass_credit_card_fees_to_customer` | boolean\|null |  | everyone | Whether card fees are added to the rider total. |
| `driver_invite` | object\|null |  | owner, admin | How new drivers join this fleet; null for drivers. |
| `driver_invite.code` | string |  | everyone | Six-character invite code a driver can enter in the Meter app to join. |
| `driver_invite.url` | string |  | everyone | Invite link to share with drivers; opening it joins this fleet after sign-in. |
## FleetMember

A fleet member as listed by list_fleet_members (owners/admins only).

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `member_id` | string |  | everyone | Opaque member id (profile id). Use as `driver` in list_trips. |
| `display_name` | string\|null |  | everyone | Display name, or null if not set. |
| `role` | enum |  | everyone | Role in the fleet. owner: created the fleet and controls billing; admin: manages members, vehicles, bookings and money; driver: drives and sees only their own trips, bookings and earnings. Values: `owner`, `admin`, `driver`. |
| `joined_at` | string\|null | ISO 8601 | everyone | When the member joined the fleet. |
| `email` | string\|null |  | owner, admin | Member email. Visible to fleet owners/admins only. |
| `phone` | string\|null |  | owner, admin | Member phone (E.164). Visible to fleet owners/admins only. |
## Vehicle

A fleet vehicle as listed by list_vehicles.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `vehicle_id` | string |  | everyone | Opaque fleet vehicle id. |
| `fleet_id` | string |  | everyone | Fleet the vehicle belongs to. |
| `make` | string\|null |  | everyone | Manufacturer, e.g. "Toyota". |
| `model` | string\|null |  | everyone | Model, e.g. "Camry". |
| `year` | string\|null |  | everyone | Model year as a string, e.g. "2021". |
| `license_plate` | string\|null |  | everyone | License plate as entered. |
| `nickname` | string\|null |  | everyone | Optional nickname the fleet gave the vehicle. |
| `color` | string\|null |  | everyone | Exterior color as entered. |
| `created_at` | string | ISO 8601 | everyone | When the vehicle was added. |
| `assigned_driver` | object\|null |  | owner, admin | Driver currently assigned to this vehicle, or null. Only resolved for fleet owners/admins; always null for drivers. |
| `assigned_driver.id` | string |  | everyone | Opaque member id (a profile id). Use it as `driver` in list_trips or to match list_fleet_members. |
| `assigned_driver.display_name` | string\|null |  | everyone | Display name (first and last name). Null when the person has not set a name. |
## Trip

A metered trip. No GPS traces, device info or payment-provider ids.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `trip_id` | string |  | everyone | Opaque trip id. |
| `driver` | object\|null |  | everyone | The driver who ran the meter, or null if the account was deleted. |
| `driver.id` | string |  | everyone | Opaque member id (a profile id). Use it as `driver` in list_trips or to match list_fleet_members. |
| `driver.display_name` | string\|null |  | everyone | Display name (first and last name). Null when the person has not set a name. |
| `fleet_id` | string\|null |  | everyone | Fleet the trip was driven for, or null for a solo (non-fleet) trip. |
| `booking_id` | string\|null |  | everyone | Linked booking id when the trip fulfilled a booking; otherwise null. |
| `started_at` | string\|null | ISO 8601 | everyone | When the meter started. |
| `ended_at` | string\|null | ISO 8601 | everyone | When the meter stopped. |
| `duration_seconds` | number\|null | seconds | everyone | Metered duration. |
| `distance_meters` | number\|null | meters | everyone | Metered distance. |
| `pickup` | object\|null |  | everyone | Where the meter started. |
| `pickup.name` | string\|null |  | everyone | Short place name (e.g. business or airport name), or null. |
| `pickup.address` | string\|null |  | everyone | Formatted street address, or null. |
| `dropoff` | object\|null |  | everyone | Where the meter stopped. |
| `dropoff.name` | string\|null |  | everyone | Short place name (e.g. business or airport name), or null. |
| `dropoff.address` | string\|null |  | everyone | Formatted street address, or null. |
| `timezone` | string\|null |  | everyone | IANA timezone the trip happened in. |
| `fare_name` | string\|null |  | everyone | Name of the fare (rate card) used. |
| `currency` | string\|null |  | everyone | Currency of the amounts below. |
| `total_minor` | number\|null | minor currency units | everyone | Receipt total including fees, tip and tax, or null if no receipt. |
| `cash_total_minor` | number\|null (optional) | minor currency units | everyone | get_trip includes the stored cash receipt total in exact currency minor units. Null means missing, malformed or unsupported currency; never infer cash from the active or card total. List pages omit this field. |
| `tip_minor` | number\|null | minor currency units | everyone | Tip included in the total, or null. |
| `fee_count` | number |  | everyone | Number of fees applied (tolls, airport fees, ...). |
| `discount_count` | number |  | everyone | Number of discounts applied. |
| `adjustment_details` | object (optional) |  | everyone | get_trip includes up to 128 fees and 128 discounts with exact removal ids. complete is false when the count or encoded byte budget omits entries. A null id cannot be removed by an agent; null money means the stored value or currency is unsupported. List pages omit these details. |
| `adjustment_details.fees` | array |  | everyone | Bounded saved adjustment entries with exact selection IDs. |
| `adjustment_details.fees[].fee_id` | string\|null |  | everyone | Saved removal id, or null when unsupported. |
| `adjustment_details.fees[].memo` | string\|null |  | everyone | Bounded saved fee label. |
| `adjustment_details.fees[].amount_minor` | number\|null | minor currency units | everyone | Stored amount in exact receipt minor units; null when unsupported. |
| `adjustment_details.fees[].taxable` | boolean\|null |  | everyone | Whether the fee is taxable, or null when unknown. |
| `adjustment_details.fees[].is_tip` | boolean\|null |  | everyone | Whether the fee is a tip, or null when unknown. |
| `adjustment_details.discounts` | array |  | everyone | Bounded saved adjustment entries with exact selection IDs. |
| `adjustment_details.discounts[].discount_id` | string\|null |  | everyone | Saved removal id, or null when unsupported. |
| `adjustment_details.discounts[].type` | enum\|null |  | everyone | Stored discount kind, or null when unsupported. Values: `fixed`, `percentage`. |
| `adjustment_details.discounts[].amount_minor` | number\|null | minor currency units | everyone | Stored amount in exact receipt minor units; null when unsupported. |
| `adjustment_details.discounts[].percentage` | number\|null |  | everyone | Percentage discount from 0 to 100; null for fixed or unsupported discounts. |
| `adjustment_details.discounts[].reason` | string\|null |  | everyone | Bounded saved discount reason. |
| `adjustment_details.complete` | boolean |  | everyone | Whether all saved entries fit the bounded response. |
| `is_paid` | boolean |  | everyone | Whether the trip is marked paid. |
| `payment_method` | string\|null |  | everyone | How the trip was paid: cash, card (Meter Pay), other, or null when not recorded. |
| `void_status` | enum\|null |  | everyone | Set when the driver asked to void the trip (void_requested) or an admin voided it (voided). Values: `void_requested`, `voided`. |
| `created_at` | string | ISO 8601 | everyone | When the trip was uploaded to Meter. |
## TripPage

Result of list_trips: a page of trips, newest first.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `items` | array |  | everyone | The page of results, newest first unless the tool says otherwise. |
| `items[].trip_id` | string |  | everyone | Opaque trip id. |
| `items[].driver` | object\|null |  | everyone | The driver who ran the meter, or null if the account was deleted. |
| `items[].driver.id` | string |  | everyone | Opaque member id (a profile id). Use it as `driver` in list_trips or to match list_fleet_members. |
| `items[].driver.display_name` | string\|null |  | everyone | Display name (first and last name). Null when the person has not set a name. |
| `items[].fleet_id` | string\|null |  | everyone | Fleet the trip was driven for, or null for a solo (non-fleet) trip. |
| `items[].booking_id` | string\|null |  | everyone | Linked booking id when the trip fulfilled a booking; otherwise null. |
| `items[].started_at` | string\|null | ISO 8601 | everyone | When the meter started. |
| `items[].ended_at` | string\|null | ISO 8601 | everyone | When the meter stopped. |
| `items[].duration_seconds` | number\|null | seconds | everyone | Metered duration. |
| `items[].distance_meters` | number\|null | meters | everyone | Metered distance. |
| `items[].pickup` | object\|null |  | everyone | Where the meter started. |
| `items[].pickup.name` | string\|null |  | everyone | Short place name (e.g. business or airport name), or null. |
| `items[].pickup.address` | string\|null |  | everyone | Formatted street address, or null. |
| `items[].dropoff` | object\|null |  | everyone | Where the meter stopped. |
| `items[].dropoff.name` | string\|null |  | everyone | Short place name (e.g. business or airport name), or null. |
| `items[].dropoff.address` | string\|null |  | everyone | Formatted street address, or null. |
| `items[].timezone` | string\|null |  | everyone | IANA timezone the trip happened in. |
| `items[].fare_name` | string\|null |  | everyone | Name of the fare (rate card) used. |
| `items[].currency` | string\|null |  | everyone | Currency of the amounts below. |
| `items[].total_minor` | number\|null | minor currency units | everyone | Receipt total including fees, tip and tax, or null if no receipt. |
| `items[].cash_total_minor` | number\|null (optional) | minor currency units | everyone | get_trip includes the stored cash receipt total in exact currency minor units. Null means missing, malformed or unsupported currency; never infer cash from the active or card total. List pages omit this field. |
| `items[].tip_minor` | number\|null | minor currency units | everyone | Tip included in the total, or null. |
| `items[].fee_count` | number |  | everyone | Number of fees applied (tolls, airport fees, ...). |
| `items[].discount_count` | number |  | everyone | Number of discounts applied. |
| `items[].adjustment_details` | object (optional) |  | everyone | get_trip includes up to 128 fees and 128 discounts with exact removal ids. complete is false when the count or encoded byte budget omits entries. A null id cannot be removed by an agent; null money means the stored value or currency is unsupported. List pages omit these details. |
| `items[].adjustment_details.fees` | array |  | everyone | Bounded saved adjustment entries with exact selection IDs. |
| `items[].adjustment_details.fees[].fee_id` | string\|null |  | everyone | Saved removal id, or null when unsupported. |
| `items[].adjustment_details.fees[].memo` | string\|null |  | everyone | Bounded saved fee label. |
| `items[].adjustment_details.fees[].amount_minor` | number\|null | minor currency units | everyone | Stored amount in exact receipt minor units; null when unsupported. |
| `items[].adjustment_details.fees[].taxable` | boolean\|null |  | everyone | Whether the fee is taxable, or null when unknown. |
| `items[].adjustment_details.fees[].is_tip` | boolean\|null |  | everyone | Whether the fee is a tip, or null when unknown. |
| `items[].adjustment_details.discounts` | array |  | everyone | Bounded saved adjustment entries with exact selection IDs. |
| `items[].adjustment_details.discounts[].discount_id` | string\|null |  | everyone | Saved removal id, or null when unsupported. |
| `items[].adjustment_details.discounts[].type` | enum\|null |  | everyone | Stored discount kind, or null when unsupported. Values: `fixed`, `percentage`. |
| `items[].adjustment_details.discounts[].amount_minor` | number\|null | minor currency units | everyone | Stored amount in exact receipt minor units; null when unsupported. |
| `items[].adjustment_details.discounts[].percentage` | number\|null |  | everyone | Percentage discount from 0 to 100; null for fixed or unsupported discounts. |
| `items[].adjustment_details.discounts[].reason` | string\|null |  | everyone | Bounded saved discount reason. |
| `items[].adjustment_details.complete` | boolean |  | everyone | Whether all saved entries fit the bounded response. |
| `items[].is_paid` | boolean |  | everyone | Whether the trip is marked paid. |
| `items[].payment_method` | string\|null |  | everyone | How the trip was paid: cash, card (Meter Pay), other, or null when not recorded. |
| `items[].void_status` | enum\|null |  | everyone | Set when the driver asked to void the trip (void_requested) or an admin voided it (voided). Values: `void_requested`, `voided`. |
| `items[].created_at` | string | ISO 8601 | everyone | When the trip was uploaded to Meter. |
| `next_cursor` | string\|null |  | everyone | Send this back as `cursor` to fetch the next page. Null when there are no more results. |
| `has_more` | boolean |  | everyone | True when another page exists. |
## RideRequest

A ride request preview or the created booking.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `booking_id` | string\|null |  | everyone | Created booking id for get_ride_status; null in a preview. |
| `booking_status` | string\|null |  | everyone | Booking status after creation (pending, confirmed …); null in a preview. |
| `fleet_id` | string |  | everyone | Fleet being booked. |
| `fleet_name` | string\|null |  | everyone | Fleet display name. |
| `pickup` | object |  | everyone | Pickup. |
| `pickup.name` | string\|null |  | everyone | Place name, or null. |
| `pickup.address` | string\|null |  | everyone | Formatted address, or null. |
| `dropoff` | object\|null |  | everyone | Drop-off, or null for a metered ride without one. |
| `dropoff.name` | string\|null |  | everyone | Place name, or null. |
| `dropoff.address` | string\|null |  | everyone | Formatted address, or null. |
| `stops` | array |  | everyone | Intermediate stops in order. |
| `stops[].name` | string\|null |  | everyone | Place name, or null. |
| `stops[].address` | string\|null |  | everyone | Formatted address, or null. |
| `pickup_time` | string\|null | ISO 8601 | everyone | Requested pickup time (ISO 8601 with offset), or null for as soon as possible. |
| `timezone` | string\|null |  | everyone | IANA timezone of the pickup. |
| `distance_meters` | number\|null | meters | everyone | Estimated route distance. |
| `duration_seconds` | number\|null | seconds | everyone | Estimated route duration. |
| `passengers` | number |  | everyone | Passenger count. |
| `ride_option` | object |  | everyone | Selected ride option. |
| `ride_option.ride_option_id` | string |  | everyone | Ride option id. |
| `ride_option.name` | string |  | everyone | Ride option name. |
| `ride_option.capacity` | number\|null |  | everyone | Maximum passengers, or null. |
| `price` | object |  | everyone | Quoted price. |
| `price.amount_minor` | number | minor currency units | everyone | Price the rider is quoted, in minor units. |
| `price.currency` | string |  | everyone | ISO 4217 currency code, upper-case. |
| `price.display` | string |  | everyone | Price formatted for the human in the request locale. |
| `price.mode` | enum |  | everyone | fixed: the quoted price is the fare; estimate: the final fare can change (for example overtime); metered: charged by the meter, the amount is an estimate. Values: `fixed`, `estimate`, `metered`. |
| `price.disclosure` | string\|null |  | everyone | Pricing disclosure to show the human before confirming, or null. |
| `payment` | object |  | everyone | How the rider pays. |
| `payment.method` | enum |  | everyone | saved_card: the default card in the rider's Meter account is held and charged by the fleet; meter_checkout: the human confirms and pays on Meter's own page (nothing is booked in chat); pay_driver_after_trip: no card is needed now. Values: `saved_card`, `meter_checkout`, `pay_driver_after_trip`. |
| `payment.card_brand` | string\|null |  | everyone | Brand of the saved card (e.g. visa), or null. |
| `payment.card_last4` | string\|null |  | everyone | Last four digits of the saved card, or null. |
| `cancellation_policy` | object |  | everyone | Cancellation policy. |
| `cancellation_policy.grace_period_seconds` | number | seconds | everyone | Free cancellation window after booking. |
| `cancellation_policy.fee_minor` | number\|null | minor currency units | everyone | Fee for cancelling after the free window, in minor units; null when unknown or none. |
| `cancellation_policy.currency` | string\|null |  | everyone | Currency of the fee, or null. |
| `cancellation_policy.summary` | string |  | everyone | One-sentence policy summary for the human. |
| `payment_authorization_failed` | boolean |  | everyone | True when the booking was created but the card hold failed; send the human the finish_ride_payment link. |
| `action_link` | object\|null |  | everyone | Where the human tracks the ride, finishes payment or checks out on Meter; null in a preview. |
| `action_link.action` | enum |  | everyone | The human action requested. Values: `subscribe_pro`, `subscribe_fleet`, `manage_subscription`, `manage_store_subscription`, `change_plan`, `cancel_subscription`, `update_payment_method`, `meter_pay_setup`, `meter_pay_manage`, `respond_to_dispute`, `request_refund`, `upload_documents`, `edit_fleet_member`, `change_email`, `change_phone`, `delete_account`, `delete_fleet`, `upload_fleet_icon`, `draw_service_area`, `download_pay_stub`, `download_export`, `add_payment_method`, `finish_ride_payment`, `track_ride`, `review_quote`, `tip_ride`. |
| `action_link.label` | string |  | everyone | Localized action label; payment setup is called Meter Pay. |
| `action_link.url` | string |  | everyone | Meter page URL to present unchanged. Never a provider session or signed download URL. |
| `action_link.where_in_console` | string |  | everyone | Where the human can find the action in Meter. |
| `action_link.where_in_app` | string |  | everyone | Native app guidance, or instructions to open the web console. |
| `action_link.why_handoff` | string |  | everyone | Why the human must finish this action and whether it needs the store or Meter support. |
| `next_step` | enum |  | everyone | confirm: a preview, ask the human. send_checkout_link: nothing is booked yet; send action_link, the human confirms and pays on Meter, then check list_bookings or get_ride_status. track: booked; share action_link. finish_payment: booked but the card hold failed; send action_link. Values: `confirm`, `send_checkout_link`, `track`, `finish_payment`. |
| `checkout_expires_at` | string\|null | ISO 8601 | everyone | When the Meter checkout link stops working (about 30 minutes); null unless next_step is send_checkout_link. |
## BookingCancellation

Minimal committed booking cancellation; never proof of provider money movement.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `booking_id` | string |  | everyone | Booking identifier for get_booking. |
| `outcome` | enum |  | everyone | The booking cancellation committed; provider settlement is separate. Values: `cancellation_committed`. |
| `settlement` | enum |  | everyone | Financial/provider settlement was queued, not confirmed. Read get_booking for current handoff state. Values: `pending`. |
| `fee_unit_amount` | number |  | everyone | Approved cancellation fee in the explicit currency's minor units; not proof of a charge. |
| `currency_code` | string |  | everyone | Supported currency of the approved fee. |
## BookingCancellationWrite

Preview or confirmed booking cancellation.

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
| `booking_action` | object |  | everyone | Minimal committed booking cancellation; never proof of provider money movement. |
| `booking_action.booking_id` | string |  | everyone | Booking identifier for get_booking. |
| `booking_action.outcome` | enum |  | everyone | The booking cancellation committed; provider settlement is separate. Values: `cancellation_committed`. |
| `booking_action.settlement` | enum |  | everyone | Financial/provider settlement was queued, not confirmed. Read get_booking for current handoff state. Values: `pending`. |
| `booking_action.fee_unit_amount` | number |  | everyone | Approved cancellation fee in the explicit currency's minor units; not proof of a charge. |
| `booking_action.currency_code` | string |  | everyone | Supported currency of the approved fee. |
## BookingPaymentReminder

Minimal queued reminder; never proof of remote delivery.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `booking_id` | string |  | everyone | Booking identifier for get_booking. |
| `outcome` | enum |  | everyone | One bounded rider reminder was queued. Values: `reminder_queued`. |
| `delivery` | enum |  | everyone | Delivery was queued, not confirmed; ambiguous delivery is never automatically resent. Values: `pending`. |
## BookingPaymentReminderWrite

Preview or queued booking payment reminder.

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
| `booking_action` | object |  | everyone | Minimal queued reminder; never proof of remote delivery. |
| `booking_action.booking_id` | string |  | everyone | Booking identifier for get_booking. |
| `booking_action.outcome` | enum |  | everyone | One bounded rider reminder was queued. Values: `reminder_queued`. |
| `booking_action.delivery` | enum |  | everyone | Delivery was queued, not confirmed; ambiguous delivery is never automatically resent. Values: `pending`. |
## BookingChange

Immutable minimal booking outcome; read current details with get_booking.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `booking_id` | string |  | everyone | Booking identifier for get_booking. |
| `status` | enum |  | everyone | Booking status frozen at command completion. Values: `pending`, `confirmed`, `in_progress`, `completed`, `canceled`, `pending_payment`. |
| `assigned_driver_id` | string\|null |  | everyone | Assigned driver at completion, or null when unassigned. |
| `rider_id` | string\|null |  | everyone | Rider attached at completion, or null when absent. |
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
| `dispatch_id` | string |  | everyone | Offer to answer with respond_to_dispatch_offer. |
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
| `items[].dispatch_id` | string |  | everyone | Offer to answer with respond_to_dispatch_offer. |
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
| `dispatch_offer.dispatch_id` | string |  | everyone | Offer to answer with respond_to_dispatch_offer. |
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
| `next_cursor` | string\|null |  | everyone | Send this back as `cursor` to fetch the next page. Null when there are no more results. |
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
