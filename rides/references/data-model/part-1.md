# Meter data-model reference

Generated from the `@meterapp/meter-sdk` catalog and DTO schemas; do not edit by hand. See the [reference index](../data-model.md) for all definitions.

## BookingQuoteEstimate

Read-only booking price estimates with currency minor units and explicit limitations.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string\|null |  | everyone | Fleet being estimated, or null for your personal fare. |
| `timezone` | string |  | everyone | Pickup timezone resolved from coordinates. |
| `service_type` | enum |  | everyone | Requested ride product. Values: `POINT_TO_POINT`, `METERED`, `TIME`. |
| `estimates` | array |  | everyone | Estimates for eligible fleet options or one personal fare. |
| `estimates[].ride_option_id` | string\|null |  | everyone | Fleet ride option, or null for a personal fare. |
| `estimates[].name` | string |  | everyone | Ride option or personal fare display name. |
| `estimates[].capacity` | number\|null |  | everyone | Fleet option capacity; null for a personal fare. |
| `estimates[].recommended` | boolean |  | everyone | The first capacity-suitable option, matching estimate-v2. |
| `estimates[].passenger_count` | number |  | everyone | Effective passenger count after estimate-v2 normalization. |
| `estimates[].currency` | string |  | everyone | Currency code for all amounts. |
| `estimates[].total_unit_amount` | number\|null |  | everyone | Active estimate in currency minor units; null for rate-only metered service. |
| `estimates[].cash_unit_amount` | number\|null |  | everyone | Cash variant in currency minor units when calculated. |
| `estimates[].card_unit_amount` | number\|null |  | everyone | Card variant in currency minor units when calculated. |
| `estimates[].card_fee_unit_amount` | number\|null |  | everyone | Card processing fee in currency minor units when calculated. |
| `estimates[].distance_meters` | number\|null |  | everyone | Estimated distance; null when no route is priced. |
| `estimates[].duration_seconds` | number\|null |  | everyone | Estimated route or booked TIME duration in seconds. |
| `estimates[].settlement_mode` | enum |  | everyone | How the eventual booking fare settles; an estimate is not an accepted quote. Values: `fixed_quote`, `time_minimum_plus_overtime`, `metered_actuals`. |
| `estimates[].routing` | enum |  | everyone | Road estimate, approximation, or non-route pricing. Values: `road`, `route_with_gaps`, `straight_line`, `time`, `rate_only`. |
| `limitations` | array |  | everyone | Explicit limits: no booking, quote, reservation, discount, tip, or acknowledgement is created. |
## FeedbackSubmissionWrite

FeedbackSubmissionWrite

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
| `item` | object\|null |  | everyone | Customer-visible idea or private report, filtered by current access and moderation. |
| `item.id` | string |  | everyone | Opaque identifier of this record. |
| `item.reference` | string |  | everyone | Customer-facing feedback reference. |
| `item.type` | string |  | everyone | Record kind, preserving future values. |
| `item.slug` | string (optional) |  | everyone | Public idea URL segment when supplied. |
| `item.url` | string (optional) |  | everyone | Public idea address when supplied. |
| `item.title` | string |  | everyone | Complete customer-visible title. |
| `item.body` | string |  | everyone | Customer-visible text; null for a deleted comment. |
| `item.visibility` | object (optional) |  | everyone | Text visibility only; private screenshots and diagnostics retain separate authorization. |
| `item.visibility.scope` | string |  | everyone | Server-authorized text audience; public, fleet or reporter. Preserve future values. This never grants attachment or diagnostic access. |
| `item.visibility.label` | string |  | everyone | Localized explanation of who can read the text. |
| `item.language` | string (optional) |  | everyone | Submitted language when supplied. |
| `item.moderation_state` | string (optional) |  | everyone | Moderation state visible to this caller when supplied. |
| `item.category` | object |  | everyone | Localized category of the feedback. |
| `item.category.key` | string |  | everyone | Stable category or status id, preserving future values. |
| `item.category.label` | string |  | everyone | Localized customer-facing label. |
| `item.status` | object |  | everyone | Current customer-visible status and its change timestamp. |
| `item.status.key` | string |  | everyone | Stable category or status id, preserving future values. |
| `item.status.label` | string |  | everyone | Localized customer-facing label. |
| `item.status.changed_at` | string |  | everyone | Timestamp when the current status was reached. |
| `item.subject` | object (optional) |  | everyone | Private report subject, only when visible to the caller. |
| `item.subject.type` | string |  | everyone | Record kind, preserving future values. |
| `item.subject.id` | string (optional) |  | everyone | Opaque identifier of this record. |
| `item.subject.label` | string (optional) |  | everyone | Localized customer-facing label. |
| `item.subject.occurred_at` | string (optional) |  | everyone | Timestamp of the linked subject when supplied. |
| `item.subject.deep_link` | string (optional) |  | everyone | Authorized application link to the subject when supplied. |
| `item.author` | object |  | everyone | Privacy-filtered public author identity. |
| `item.author.display_name` | string (optional) |  | everyone | Privacy-filtered first name, or Meter team for staff; omitted when unavailable. |
| `item.author.role` | string |  | everyone | Public role label, preserving future values. |
| `item.author.is_viewer` | boolean |  | everyone | Whether this author is the verified caller. |
| `item.counts` | object |  | everyone | Current engagement counts. |
| `item.counts.votes` | number |  | everyone | Current vote count. |
| `item.counts.comments` | number |  | everyone | Current visible comment count. |
| `item.viewer` | object |  | everyone | Current caller interactions and permissions. |
| `item.viewer.has_voted` | boolean |  | everyone | Whether the caller currently votes on this idea. |
| `item.viewer.is_following` | boolean |  | everyone | Whether the caller currently follows updates. |
| `item.viewer.can_vote` | boolean |  | everyone | Whether the caller may vote under current access and moderation rules. |
| `item.viewer.can_comment` | boolean |  | everyone | Whether the caller may comment under current access and moderation rules. |
| `item.viewer.can_delete` | boolean |  | everyone | Whether the caller may withdraw this item. |
| `item.availability` | array |  | everyone | Verified per-platform availability. |
| `item.availability[].platform` | string |  | everyone | Target platform, preserving future values. |
| `item.availability[].state` | string |  | everyone | Availability or attachment state, preserving future values. |
| `item.availability[].fixed_in_version` | string (optional) |  | everyone | Verified release version when supplied. |
| `item.availability[].available_at` | string (optional) |  | everyone | Release availability timestamp when supplied. |
| `item.merged_into` | object (optional) |  | everyone | Visible canonical destination when this item was merged. |
| `item.merged_into.id` | string |  | everyone | Opaque identifier of this record. |
| `item.merged_into.slug` | string (optional) |  | everyone | Public idea URL segment when supplied. |
| `item.merged_into.title` | string (optional) |  | everyone | Complete customer-visible title. |
| `item.device_details` | object (optional) |  | everyone | Submitted device details, visible only to the report author. |
| `item.device_details.platform` | string (optional) |  | everyone | Target platform, preserving future values. |
| `item.device_details.app_version` | string (optional) |  | everyone | Submitted application version, visible only under feedback access rules. |
| `item.device_details.os_version` | string (optional) |  | everyone | Submitted operating-system version, visible only under feedback access rules. |
| `item.device_details.device_model` | string (optional) |  | everyone | Submitted device model, visible only under feedback access rules. |
| `item.attachments` | array |  | everyone | Attachments authorized for this caller. |
| `item.attachments[].id` | string |  | everyone | Opaque identifier of this record. |
| `item.attachments[].status` | string |  | everyone | Attachment processing status, preserving future values. |
| `item.attachments[].content_type` | string |  | everyone | Stored attachment media type. |
| `item.attachments[].width` | number (optional) |  | everyone | Image width in pixels when available. |
| `item.attachments[].height` | number (optional) |  | everyone | Image height in pixels when available. |
| `item.attachments[].download_url` | string (optional) |  | everyone | Short-lived attachment URL authorized for this caller. |
| `item.attachments[].download_url_expires_at` | string (optional) |  | everyone | Expiry timestamp of the authorized attachment URL. |
| `item.created_at` | string |  | everyone | Creation timestamp. |
| `item.updated_at` | string |  | everyone | Last update timestamp. |
## FeedbackVoteWrite

FeedbackVoteWrite

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
| `vote` | object\|null |  | everyone | Committed vote and following state for an authorized public idea. |
| `vote.item_id` | string |  | everyone | Public idea identifier. |
| `vote.voted` | boolean |  | everyone | The caller's committed vote state. |
| `vote.vote_count` | number |  | everyone | Total votes at commit. |
| `vote.is_following` | boolean |  | everyone | The caller's following state at commit. |
## FeedbackFollowWrite

FeedbackFollowWrite

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
| `follow` | object\|null |  | everyone | Committed following state for an authorized feedback item. |
| `follow.item_id` | string |  | everyone | Authorized feedback identifier. |
| `follow.following` | boolean |  | everyone | The caller's committed following state. |
## FeedbackCommentWrite

FeedbackCommentWrite

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
| `comment` | object\|null |  | everyone | Customer-visible comment with privacy-filtered author and authorized attachments. |
| `comment.id` | string |  | everyone | Opaque identifier of this record. |
| `comment.body` | string\|null |  | everyone | Customer-visible text; null for a deleted comment. |
| `comment.author` | object |  | everyone | Privacy-filtered public author identity. |
| `comment.author.display_name` | string (optional) |  | everyone | Privacy-filtered first name, or Meter team for staff; omitted when unavailable. |
| `comment.author.role` | string |  | everyone | Public role label, preserving future values. |
| `comment.author.is_viewer` | boolean |  | everyone | Whether this author is the verified caller. |
| `comment.created_at` | string |  | everyone | Creation timestamp. |
| `comment.updated_at` | string |  | everyone | Last update timestamp. |
| `comment.edited_at` | string (optional) |  | everyone | Comment edit timestamp when supplied. |
| `comment.deleted_at` | string (optional) |  | everyone | Comment deletion timestamp when supplied. |
| `comment.attachments` | array |  | everyone | Attachments authorized for this caller. |
| `comment.attachments[].id` | string |  | everyone | Opaque identifier of this record. |
| `comment.attachments[].status` | string |  | everyone | Attachment processing status, preserving future values. |
| `comment.attachments[].content_type` | string |  | everyone | Stored attachment media type. |
| `comment.attachments[].width` | number (optional) |  | everyone | Image width in pixels when available. |
| `comment.attachments[].height` | number (optional) |  | everyone | Image height in pixels when available. |
| `comment.attachments[].download_url` | string (optional) |  | everyone | Short-lived attachment URL authorized for this caller. |
| `comment.attachments[].download_url_expires_at` | string (optional) |  | everyone | Expiry timestamp of the authorized attachment URL. |
## FeedbackCategories

Categories accepted by the feedback service.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `items` | array |  | everyone | Available report and idea categories. |
| `items[].key` | string |  | everyone | Stable submission category id. |
| `items[].label` | string |  | everyone | Localized category label. |
## FeedbackItemPage

A bounded page of customer-visible feedback.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `items` | array |  | everyone | Feedback records visible to the caller. |
| `items[].id` | string |  | everyone | Opaque identifier of this record. |
| `items[].reference` | string |  | everyone | Customer-facing feedback reference. |
| `items[].type` | string |  | everyone | Record kind, preserving future values. |
| `items[].slug` | string (optional) |  | everyone | Public idea URL segment when supplied. |
| `items[].url` | string (optional) |  | everyone | Public idea address when supplied. |
| `items[].title` | string |  | everyone | Complete customer-visible title. |
| `items[].body` | string |  | everyone | Customer-visible text; null for a deleted comment. |
| `items[].visibility` | object (optional) |  | everyone | Text visibility only; private screenshots and diagnostics retain separate authorization. |
| `items[].visibility.scope` | string |  | everyone | Server-authorized text audience; public, fleet or reporter. Preserve future values. This never grants attachment or diagnostic access. |
| `items[].visibility.label` | string |  | everyone | Localized explanation of who can read the text. |
| `items[].language` | string (optional) |  | everyone | Submitted language when supplied. |
| `items[].moderation_state` | string (optional) |  | everyone | Moderation state visible to this caller when supplied. |
| `items[].category` | object |  | everyone | Localized category of the feedback. |
| `items[].category.key` | string |  | everyone | Stable category or status id, preserving future values. |
| `items[].category.label` | string |  | everyone | Localized customer-facing label. |
| `items[].status` | object |  | everyone | Current customer-visible status and its change timestamp. |
| `items[].status.key` | string |  | everyone | Stable category or status id, preserving future values. |
| `items[].status.label` | string |  | everyone | Localized customer-facing label. |
| `items[].status.changed_at` | string |  | everyone | Timestamp when the current status was reached. |
| `items[].subject` | object (optional) |  | everyone | Private report subject, only when visible to the caller. |
| `items[].subject.type` | string |  | everyone | Record kind, preserving future values. |
| `items[].subject.id` | string (optional) |  | everyone | Opaque identifier of this record. |
| `items[].subject.label` | string (optional) |  | everyone | Localized customer-facing label. |
| `items[].subject.occurred_at` | string (optional) |  | everyone | Timestamp of the linked subject when supplied. |
| `items[].subject.deep_link` | string (optional) |  | everyone | Authorized application link to the subject when supplied. |
| `items[].author` | object |  | everyone | Privacy-filtered public author identity. |
| `items[].author.display_name` | string (optional) |  | everyone | Privacy-filtered first name, or Meter team for staff; omitted when unavailable. |
| `items[].author.role` | string |  | everyone | Public role label, preserving future values. |
| `items[].author.is_viewer` | boolean |  | everyone | Whether this author is the verified caller. |
| `items[].counts` | object |  | everyone | Current engagement counts. |
| `items[].counts.votes` | number |  | everyone | Current vote count. |
| `items[].counts.comments` | number |  | everyone | Current visible comment count. |
| `items[].viewer` | object |  | everyone | Current caller interactions and permissions. |
| `items[].viewer.has_voted` | boolean |  | everyone | Whether the caller currently votes on this idea. |
| `items[].viewer.is_following` | boolean |  | everyone | Whether the caller currently follows updates. |
| `items[].viewer.can_vote` | boolean |  | everyone | Whether the caller may vote under current access and moderation rules. |
| `items[].viewer.can_comment` | boolean |  | everyone | Whether the caller may comment under current access and moderation rules. |
| `items[].viewer.can_delete` | boolean |  | everyone | Whether the caller may withdraw this item. |
| `items[].availability` | array |  | everyone | Verified per-platform availability. |
| `items[].availability[].platform` | string |  | everyone | Target platform, preserving future values. |
| `items[].availability[].state` | string |  | everyone | Availability or attachment state, preserving future values. |
| `items[].availability[].fixed_in_version` | string (optional) |  | everyone | Verified release version when supplied. |
| `items[].availability[].available_at` | string (optional) |  | everyone | Release availability timestamp when supplied. |
| `items[].merged_into` | object (optional) |  | everyone | Visible canonical destination when this item was merged. |
| `items[].merged_into.id` | string |  | everyone | Opaque identifier of this record. |
| `items[].merged_into.slug` | string (optional) |  | everyone | Public idea URL segment when supplied. |
| `items[].merged_into.title` | string (optional) |  | everyone | Complete customer-visible title. |
| `items[].device_details` | object (optional) |  | everyone | Submitted device details, visible only to the report author. |
| `items[].device_details.platform` | string (optional) |  | everyone | Target platform, preserving future values. |
| `items[].device_details.app_version` | string (optional) |  | everyone | Submitted application version, visible only under feedback access rules. |
| `items[].device_details.os_version` | string (optional) |  | everyone | Submitted operating-system version, visible only under feedback access rules. |
| `items[].device_details.device_model` | string (optional) |  | everyone | Submitted device model, visible only under feedback access rules. |
| `items[].attachments` | array |  | everyone | Attachments authorized for this caller. |
| `items[].attachments[].id` | string |  | everyone | Opaque identifier of this record. |
| `items[].attachments[].status` | string |  | everyone | Attachment processing status, preserving future values. |
| `items[].attachments[].content_type` | string |  | everyone | Stored attachment media type. |
| `items[].attachments[].width` | number (optional) |  | everyone | Image width in pixels when available. |
| `items[].attachments[].height` | number (optional) |  | everyone | Image height in pixels when available. |
| `items[].attachments[].download_url` | string (optional) |  | everyone | Short-lived attachment URL authorized for this caller. |
| `items[].attachments[].download_url_expires_at` | string (optional) |  | everyone | Expiry timestamp of the authorized attachment URL. |
| `items[].created_at` | string |  | everyone | Creation timestamp. |
| `items[].updated_at` | string |  | everyone | Last update timestamp. |
| `next_cursor` | string\|null |  | everyone | Opaque continuation cursor, or null at the end. |
## FeedbackSimilarIdeas

Public duplicate suggestions; private reports are excluded.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `items` | array |  | everyone | Up to five visible public ideas matching the supplied text. |
| `items[].id` | string |  | everyone | Opaque identifier of this record. |
| `items[].reference` | string |  | everyone | Customer-facing feedback reference. |
| `items[].type` | string |  | everyone | Record kind, preserving future values. |
| `items[].slug` | string (optional) |  | everyone | Public idea URL segment when supplied. |
| `items[].url` | string (optional) |  | everyone | Public idea address when supplied. |
| `items[].title` | string |  | everyone | Complete customer-visible title. |
| `items[].body` | string |  | everyone | Customer-visible text; null for a deleted comment. |
| `items[].visibility` | object (optional) |  | everyone | Text visibility only; private screenshots and diagnostics retain separate authorization. |
| `items[].visibility.scope` | string |  | everyone | Server-authorized text audience; public, fleet or reporter. Preserve future values. This never grants attachment or diagnostic access. |
| `items[].visibility.label` | string |  | everyone | Localized explanation of who can read the text. |
| `items[].language` | string (optional) |  | everyone | Submitted language when supplied. |
| `items[].moderation_state` | string (optional) |  | everyone | Moderation state visible to this caller when supplied. |
| `items[].category` | object |  | everyone | Localized category of the feedback. |
| `items[].category.key` | string |  | everyone | Stable category or status id, preserving future values. |
| `items[].category.label` | string |  | everyone | Localized customer-facing label. |
| `items[].status` | object |  | everyone | Current customer-visible status and its change timestamp. |
| `items[].status.key` | string |  | everyone | Stable category or status id, preserving future values. |
| `items[].status.label` | string |  | everyone | Localized customer-facing label. |
| `items[].status.changed_at` | string |  | everyone | Timestamp when the current status was reached. |
| `items[].subject` | object (optional) |  | everyone | Private report subject, only when visible to the caller. |
| `items[].subject.type` | string |  | everyone | Record kind, preserving future values. |
| `items[].subject.id` | string (optional) |  | everyone | Opaque identifier of this record. |
| `items[].subject.label` | string (optional) |  | everyone | Localized customer-facing label. |
| `items[].subject.occurred_at` | string (optional) |  | everyone | Timestamp of the linked subject when supplied. |
| `items[].subject.deep_link` | string (optional) |  | everyone | Authorized application link to the subject when supplied. |
| `items[].author` | object |  | everyone | Privacy-filtered public author identity. |
| `items[].author.display_name` | string (optional) |  | everyone | Privacy-filtered first name, or Meter team for staff; omitted when unavailable. |
| `items[].author.role` | string |  | everyone | Public role label, preserving future values. |
| `items[].author.is_viewer` | boolean |  | everyone | Whether this author is the verified caller. |
| `items[].counts` | object |  | everyone | Current engagement counts. |
| `items[].counts.votes` | number |  | everyone | Current vote count. |
| `items[].counts.comments` | number |  | everyone | Current visible comment count. |
| `items[].viewer` | object |  | everyone | Current caller interactions and permissions. |
| `items[].viewer.has_voted` | boolean |  | everyone | Whether the caller currently votes on this idea. |
| `items[].viewer.is_following` | boolean |  | everyone | Whether the caller currently follows updates. |
| `items[].viewer.can_vote` | boolean |  | everyone | Whether the caller may vote under current access and moderation rules. |
| `items[].viewer.can_comment` | boolean |  | everyone | Whether the caller may comment under current access and moderation rules. |
| `items[].viewer.can_delete` | boolean |  | everyone | Whether the caller may withdraw this item. |
| `items[].availability` | array |  | everyone | Verified per-platform availability. |
| `items[].availability[].platform` | string |  | everyone | Target platform, preserving future values. |
| `items[].availability[].state` | string |  | everyone | Availability or attachment state, preserving future values. |
| `items[].availability[].fixed_in_version` | string (optional) |  | everyone | Verified release version when supplied. |
| `items[].availability[].available_at` | string (optional) |  | everyone | Release availability timestamp when supplied. |
| `items[].merged_into` | object (optional) |  | everyone | Visible canonical destination when this item was merged. |
| `items[].merged_into.id` | string |  | everyone | Opaque identifier of this record. |
| `items[].merged_into.slug` | string (optional) |  | everyone | Public idea URL segment when supplied. |
| `items[].merged_into.title` | string (optional) |  | everyone | Complete customer-visible title. |
| `items[].device_details` | object (optional) |  | everyone | Submitted device details, visible only to the report author. |
| `items[].device_details.platform` | string (optional) |  | everyone | Target platform, preserving future values. |
| `items[].device_details.app_version` | string (optional) |  | everyone | Submitted application version, visible only under feedback access rules. |
| `items[].device_details.os_version` | string (optional) |  | everyone | Submitted operating-system version, visible only under feedback access rules. |
| `items[].device_details.device_model` | string (optional) |  | everyone | Submitted device model, visible only under feedback access rules. |
| `items[].attachments` | array |  | everyone | Attachments authorized for this caller. |
| `items[].attachments[].id` | string |  | everyone | Opaque identifier of this record. |
| `items[].attachments[].status` | string |  | everyone | Attachment processing status, preserving future values. |
| `items[].attachments[].content_type` | string |  | everyone | Stored attachment media type. |
| `items[].attachments[].width` | number (optional) |  | everyone | Image width in pixels when available. |
| `items[].attachments[].height` | number (optional) |  | everyone | Image height in pixels when available. |
| `items[].attachments[].download_url` | string (optional) |  | everyone | Short-lived attachment URL authorized for this caller. |
| `items[].attachments[].download_url_expires_at` | string (optional) |  | everyone | Expiry timestamp of the authorized attachment URL. |
| `items[].created_at` | string |  | everyone | Creation timestamp. |
| `items[].updated_at` | string |  | everyone | Last update timestamp. |
## FeedbackDetail

Authorized feedback detail with comments and status history.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `item` | object |  | everyone | Feedback record authorized for the caller. |
| `item.id` | string |  | everyone | Opaque identifier of this record. |
| `item.reference` | string |  | everyone | Customer-facing feedback reference. |
| `item.type` | string |  | everyone | Record kind, preserving future values. |
| `item.slug` | string (optional) |  | everyone | Public idea URL segment when supplied. |
| `item.url` | string (optional) |  | everyone | Public idea address when supplied. |
| `item.title` | string |  | everyone | Complete customer-visible title. |
| `item.body` | string |  | everyone | Customer-visible text; null for a deleted comment. |
| `item.visibility` | object (optional) |  | everyone | Text visibility only; private screenshots and diagnostics retain separate authorization. |
| `item.visibility.scope` | string |  | everyone | Server-authorized text audience; public, fleet or reporter. Preserve future values. This never grants attachment or diagnostic access. |
| `item.visibility.label` | string |  | everyone | Localized explanation of who can read the text. |
| `item.language` | string (optional) |  | everyone | Submitted language when supplied. |
| `item.moderation_state` | string (optional) |  | everyone | Moderation state visible to this caller when supplied. |
| `item.category` | object |  | everyone | Localized category of the feedback. |
| `item.category.key` | string |  | everyone | Stable category or status id, preserving future values. |
| `item.category.label` | string |  | everyone | Localized customer-facing label. |
| `item.status` | object |  | everyone | Current customer-visible status and its change timestamp. |
| `item.status.key` | string |  | everyone | Stable category or status id, preserving future values. |
| `item.status.label` | string |  | everyone | Localized customer-facing label. |
| `item.status.changed_at` | string |  | everyone | Timestamp when the current status was reached. |
| `item.subject` | object (optional) |  | everyone | Private report subject, only when visible to the caller. |
| `item.subject.type` | string |  | everyone | Record kind, preserving future values. |
| `item.subject.id` | string (optional) |  | everyone | Opaque identifier of this record. |
| `item.subject.label` | string (optional) |  | everyone | Localized customer-facing label. |
| `item.subject.occurred_at` | string (optional) |  | everyone | Timestamp of the linked subject when supplied. |
| `item.subject.deep_link` | string (optional) |  | everyone | Authorized application link to the subject when supplied. |
| `item.author` | object |  | everyone | Privacy-filtered public author identity. |
| `item.author.display_name` | string (optional) |  | everyone | Privacy-filtered first name, or Meter team for staff; omitted when unavailable. |
| `item.author.role` | string |  | everyone | Public role label, preserving future values. |
| `item.author.is_viewer` | boolean |  | everyone | Whether this author is the verified caller. |
| `item.counts` | object |  | everyone | Current engagement counts. |
| `item.counts.votes` | number |  | everyone | Current vote count. |
| `item.counts.comments` | number |  | everyone | Current visible comment count. |
| `item.viewer` | object |  | everyone | Current caller interactions and permissions. |
| `item.viewer.has_voted` | boolean |  | everyone | Whether the caller currently votes on this idea. |
| `item.viewer.is_following` | boolean |  | everyone | Whether the caller currently follows updates. |
| `item.viewer.can_vote` | boolean |  | everyone | Whether the caller may vote under current access and moderation rules. |
| `item.viewer.can_comment` | boolean |  | everyone | Whether the caller may comment under current access and moderation rules. |
| `item.viewer.can_delete` | boolean |  | everyone | Whether the caller may withdraw this item. |
| `item.availability` | array |  | everyone | Verified per-platform availability. |
| `item.availability[].platform` | string |  | everyone | Target platform, preserving future values. |
| `item.availability[].state` | string |  | everyone | Availability or attachment state, preserving future values. |
| `item.availability[].fixed_in_version` | string (optional) |  | everyone | Verified release version when supplied. |
| `item.availability[].available_at` | string (optional) |  | everyone | Release availability timestamp when supplied. |
| `item.merged_into` | object (optional) |  | everyone | Visible canonical destination when this item was merged. |
| `item.merged_into.id` | string |  | everyone | Opaque identifier of this record. |
| `item.merged_into.slug` | string (optional) |  | everyone | Public idea URL segment when supplied. |
| `item.merged_into.title` | string (optional) |  | everyone | Complete customer-visible title. |
| `item.device_details` | object (optional) |  | everyone | Submitted device details, visible only to the report author. |
| `item.device_details.platform` | string (optional) |  | everyone | Target platform, preserving future values. |
| `item.device_details.app_version` | string (optional) |  | everyone | Submitted application version, visible only under feedback access rules. |
| `item.device_details.os_version` | string (optional) |  | everyone | Submitted operating-system version, visible only under feedback access rules. |
| `item.device_details.device_model` | string (optional) |  | everyone | Submitted device model, visible only under feedback access rules. |
| `item.attachments` | array |  | everyone | Attachments authorized for this caller. |
| `item.attachments[].id` | string |  | everyone | Opaque identifier of this record. |
| `item.attachments[].status` | string |  | everyone | Attachment processing status, preserving future values. |
| `item.attachments[].content_type` | string |  | everyone | Stored attachment media type. |
| `item.attachments[].width` | number (optional) |  | everyone | Image width in pixels when available. |
| `item.attachments[].height` | number (optional) |  | everyone | Image height in pixels when available. |
| `item.attachments[].download_url` | string (optional) |  | everyone | Short-lived attachment URL authorized for this caller. |
| `item.attachments[].download_url_expires_at` | string (optional) |  | everyone | Expiry timestamp of the authorized attachment URL. |
| `item.created_at` | string |  | everyone | Creation timestamp. |
| `item.updated_at` | string |  | everyone | Last update timestamp. |
| `comments` | array |  | everyone | Visible comments under the customer API's bounded history rules. |
| `comments[].id` | string |  | everyone | Opaque identifier of this record. |
| `comments[].body` | string\|null |  | everyone | Customer-visible text; null for a deleted comment. |
| `comments[].author` | object |  | everyone | Privacy-filtered public author identity. |
| `comments[].author.display_name` | string (optional) |  | everyone | Privacy-filtered first name, or Meter team for staff; omitted when unavailable. |
| `comments[].author.role` | string |  | everyone | Public role label, preserving future values. |
| `comments[].author.is_viewer` | boolean |  | everyone | Whether this author is the verified caller. |
| `comments[].created_at` | string |  | everyone | Creation timestamp. |
| `comments[].updated_at` | string |  | everyone | Last update timestamp. |
| `comments[].edited_at` | string (optional) |  | everyone | Comment edit timestamp when supplied. |
| `comments[].deleted_at` | string (optional) |  | everyone | Comment deletion timestamp when supplied. |
| `comments[].attachments` | array |  | everyone | Attachments authorized for this caller. |
| `comments[].attachments[].id` | string |  | everyone | Opaque identifier of this record. |
| `comments[].attachments[].status` | string |  | everyone | Attachment processing status, preserving future values. |
| `comments[].attachments[].content_type` | string |  | everyone | Stored attachment media type. |
| `comments[].attachments[].width` | number (optional) |  | everyone | Image width in pixels when available. |
| `comments[].attachments[].height` | number (optional) |  | everyone | Image height in pixels when available. |
| `comments[].attachments[].download_url` | string (optional) |  | everyone | Short-lived attachment URL authorized for this caller. |
| `comments[].attachments[].download_url_expires_at` | string (optional) |  | everyone | Expiry timestamp of the authorized attachment URL. |
| `status_events` | array |  | everyone | Customer-visible status history without staff evidence. |
| `status_events[].id` | string |  | everyone | Opaque identifier of this record. |
| `status_events[].type` | string |  | everyone | Record kind, preserving future values. |
| `status_events[].from_status` | string (optional) |  | everyone | Previous status id when supplied. |
| `status_events[].to_status` | string (optional) |  | everyone | New status id when supplied. |
| `status_events[].public_note` | string (optional) |  | everyone | Customer-visible status note when supplied. |
| `status_events[].platform` | string (optional) |  | everyone | Target platform, preserving future values. |
| `status_events[].created_at` | string |  | everyone | Creation timestamp. |
## FeedbackChangelogPage

A bounded page of actually published release notes.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `entries` | array |  | everyone | Published release notes, newest first. |
| `entries[].id` | string |  | everyone | Published changelog entry identifier. |
| `entries[].slug` | string |  | everyone | Public changelog address segment. |
| `entries[].title` | string |  | everyone | Complete public release title. |
| `entries[].body` | string |  | everyone | Complete public release description. |
| `entries[].platforms` | array |  | everyone | Platforms covered by this release. |
| `entries[].published_at` | string |  | everyone | Actual publication timestamp. |
| `next_cursor` | string\|null |  | everyone | Opaque public continuation cursor, or null at the end. |
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
| `next_cursor` | string\|null |  | everyone | Pass this back as `cursor` to fetch the next page. Null when there are no more results. |
| `has_more` | boolean |  | everyone | True when another page exists. |
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
| `management_action` | enum |  | everyone | Pass this action to get_action_link; include fleet_id for fleet scope. Values: `meter_pay_setup`, `meter_pay_manage`. |
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
| `next_cursor` | string\|null |  | everyone | Pass this back as `cursor` to fetch the next page. Null when there are no more results. |
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
| `fleets[].fleet_id` | string |  | everyone | Opaque fleet id. Pass as `fleet_id` to fleet-scoped tools. |
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
## RiderFleetPage

Bookable fleets for a rider.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `items` | array |  | everyone | Fleets, saved fleets first, then by rating and distance. |
| `items[].fleet_id` | string |  | everyone | Fleet id for estimate_ride and request_ride. |
| `items[].slug` | string\|null |  | everyone | Public booking-page slug, or null. |
| `items[].name` | string\|null |  | everyone | Fleet display name. |
| `items[].city` | string\|null |  | everyone | City the fleet is based in, or null. |
| `items[].region` | string\|null |  | everyone | Region or state code, or null. |
| `items[].country` | string\|null |  | everyone | ISO 3166-1 alpha-2 country, or null. |
| `items[].currency` | string\|null |  | everyone | ISO 4217 currency the fleet prices in, or null. |
| `items[].rating` | object |  | everyone | Public rating summary. |
| `items[].rating.average` | number\|null |  | everyone | Average rider rating from 1 to 5, or null. |
| `items[].rating.review_count` | number |  | everyone | Number of reviews. |
| `items[].is_saved` | boolean |  | everyone | True when the rider already saved or booked this fleet; saved fleets come first. |
| `items[].payment_at_booking` | enum |  | everyone | saved_card: a card saved in the rider's Meter account is held when booking; pay_driver_after_trip: no card is needed to book. Values: `saved_card`, `pay_driver_after_trip`. |
| `items[].service_types` | array |  | everyone | Ride products offered: POINT_TO_POINT, METERED and/or TIME. |
| `items[].max_capacity` | number\|null |  | everyone | Largest passenger capacity among ride options, or null. |
| `items[].distance_meters` | number\|null | meters | everyone | Distance from the searched point when known, or null. |
| `items[].booking_url` | string\|null |  | everyone | Public booking page, or null when the fleet has no slug. |
| `next_cursor` | string\|null |  | everyone | Pass back as cursor for the next page; null when done. |
| `has_more` | boolean |  | everyone | True when another page exists. |
| `scope` | enum |  | everyone | nearby: fleets serving the searched point plus saved fleets; global: every publicly listed fleet matching the query. Values: `nearby`, `global`. |
## PlaceSearch

Places matching a text search.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `places` | array |  | everyone | Best matches first. Confirm the right one with the human when more than one is plausible. |
| `places[].name` | string |  | everyone | Place name. |
| `places[].address` | string |  | everyone | Formatted address. |
| `places[].place_id` | string\|null |  | everyone | Google place id, or null. |
| `places[].latitude` | number |  | everyone | Latitude in degrees. |
| `places[].longitude` | number |  | everyone | Longitude in degrees. |
## RideEstimate

Prices for a ride. Books nothing and holds no money.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
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
| `options` | array |  | everyone | Priced ride options, cheapest first. |
| `options[].ride_option_id` | string |  | everyone | Pass to request_ride as ride_option_id. |
| `options[].estimate_id` | string |  | everyone | Server estimate reference for this option. |
| `options[].name` | string |  | everyone | Ride option name, e.g. Sedan. |
| `options[].capacity` | number\|null |  | everyone | Maximum passengers, or null. |
| `options[].recommended` | boolean |  | everyone | True for the option best matching the passenger count. |
| `options[].price` | object |  | everyone | Quoted price. |
| `options[].price.amount_minor` | number | minor currency units | everyone | Price the rider is quoted, in minor units. |
| `options[].price.currency` | string |  | everyone | ISO 4217 currency code, upper-case. |
| `options[].price.display` | string |  | everyone | Price formatted for the human in the request locale. |
| `options[].price.mode` | enum |  | everyone | fixed: the quoted price is the fare; estimate: the final fare can change (for example overtime); metered: charged by the meter, the amount is an estimate. Values: `fixed`, `estimate`, `metered`. |
| `options[].price.disclosure` | string\|null |  | everyone | Pricing disclosure to show the human before confirming, or null. |
| `options[].cancellation_policy` | object |  | everyone | Cancellation policy for this option. |
| `options[].cancellation_policy.grace_period_seconds` | number | seconds | everyone | Free cancellation window after booking. |
| `options[].cancellation_policy.fee_minor` | number\|null | minor currency units | everyone | Fee for cancelling after the free window, in minor units; null when unknown or none. |
| `options[].cancellation_policy.currency` | string\|null |  | everyone | Currency of the fee, or null. |
| `options[].cancellation_policy.summary` | string |  | everyone | One-sentence policy summary for the human. |
| `options[].bookable_here` | boolean |  | everyone | False when this option can only be booked in the Meter app (it needs pricing features an agent cannot show). |
## RideRequestWrite

Preview or created rider booking.

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
| `ride_request` | object |  | everyone | A ride request preview or the created booking. |
| `ride_request.booking_id` | string\|null |  | everyone | Created booking id for get_ride_status; null in a preview. |
| `ride_request.booking_status` | string\|null |  | everyone | Booking status after creation (pending, confirmed …); null in a preview. |
| `ride_request.fleet_id` | string |  | everyone | Fleet being booked. |
| `ride_request.fleet_name` | string\|null |  | everyone | Fleet display name. |
| `ride_request.pickup` | object |  | everyone | Pickup. |
| `ride_request.pickup.name` | string\|null |  | everyone | Place name, or null. |
| `ride_request.pickup.address` | string\|null |  | everyone | Formatted address, or null. |
| `ride_request.dropoff` | object\|null |  | everyone | Drop-off, or null for a metered ride without one. |
| `ride_request.dropoff.name` | string\|null |  | everyone | Place name, or null. |
| `ride_request.dropoff.address` | string\|null |  | everyone | Formatted address, or null. |
| `ride_request.stops` | array |  | everyone | Intermediate stops in order. |
| `ride_request.stops[].name` | string\|null |  | everyone | Place name, or null. |
| `ride_request.stops[].address` | string\|null |  | everyone | Formatted address, or null. |
| `ride_request.pickup_time` | string\|null | ISO 8601 | everyone | Requested pickup time (ISO 8601 with offset), or null for as soon as possible. |
| `ride_request.timezone` | string\|null |  | everyone | IANA timezone of the pickup. |
| `ride_request.distance_meters` | number\|null | meters | everyone | Estimated route distance. |
| `ride_request.duration_seconds` | number\|null | seconds | everyone | Estimated route duration. |
| `ride_request.passengers` | number |  | everyone | Passenger count. |
| `ride_request.ride_option` | object |  | everyone | Selected ride option. |
| `ride_request.ride_option.ride_option_id` | string |  | everyone | Ride option id. |
| `ride_request.ride_option.name` | string |  | everyone | Ride option name. |
| `ride_request.ride_option.capacity` | number\|null |  | everyone | Maximum passengers, or null. |
| `ride_request.price` | object |  | everyone | Quoted price. |
| `ride_request.price.amount_minor` | number | minor currency units | everyone | Price the rider is quoted, in minor units. |
| `ride_request.price.currency` | string |  | everyone | ISO 4217 currency code, upper-case. |
| `ride_request.price.display` | string |  | everyone | Price formatted for the human in the request locale. |
| `ride_request.price.mode` | enum |  | everyone | fixed: the quoted price is the fare; estimate: the final fare can change (for example overtime); metered: charged by the meter, the amount is an estimate. Values: `fixed`, `estimate`, `metered`. |
| `ride_request.price.disclosure` | string\|null |  | everyone | Pricing disclosure to show the human before confirming, or null. |
| `ride_request.payment` | object |  | everyone | How the rider pays. |
| `ride_request.payment.method` | enum |  | everyone | saved_card: the default card in the rider's Meter account is held and charged by the fleet; meter_checkout: the human confirms and pays on Meter's own page (nothing is booked in chat); pay_driver_after_trip: no card is needed now. Values: `saved_card`, `meter_checkout`, `pay_driver_after_trip`. |
| `ride_request.payment.card_brand` | string\|null |  | everyone | Brand of the saved card (e.g. visa), or null. |
| `ride_request.payment.card_last4` | string\|null |  | everyone | Last four digits of the saved card, or null. |
| `ride_request.cancellation_policy` | object |  | everyone | Cancellation policy. |
| `ride_request.cancellation_policy.grace_period_seconds` | number | seconds | everyone | Free cancellation window after booking. |
| `ride_request.cancellation_policy.fee_minor` | number\|null | minor currency units | everyone | Fee for cancelling after the free window, in minor units; null when unknown or none. |
| `ride_request.cancellation_policy.currency` | string\|null |  | everyone | Currency of the fee, or null. |
| `ride_request.cancellation_policy.summary` | string |  | everyone | One-sentence policy summary for the human. |
| `ride_request.payment_authorization_failed` | boolean |  | everyone | True when the booking was created but the card hold failed; send the human the finish_ride_payment link. |
| `ride_request.action_link` | object\|null |  | everyone | Where the human tracks the ride, finishes payment or checks out on Meter; null in a preview. |
| `ride_request.action_link.action` | enum |  | everyone | The human action requested. Values: `subscribe_pro`, `subscribe_fleet`, `manage_subscription`, `manage_store_subscription`, `change_plan`, `cancel_subscription`, `update_payment_method`, `meter_pay_setup`, `meter_pay_manage`, `respond_to_dispute`, `request_refund`, `upload_documents`, `edit_fleet_member`, `change_email`, `change_phone`, `delete_account`, `delete_fleet`, `upload_fleet_icon`, `draw_service_area`, `download_pay_stub`, `download_export`, `add_payment_method`, `finish_ride_payment`, `track_ride`, `review_quote`, `tip_ride`. |
| `ride_request.action_link.label` | string |  | everyone | Localized action label; payment setup is called Meter Pay. |
| `ride_request.action_link.url` | string |  | everyone | Meter page URL to present unchanged. Never a provider session or signed download URL. |
| `ride_request.action_link.where_in_console` | string |  | everyone | Where the human can find the action in Meter. |
| `ride_request.action_link.where_in_app` | string |  | everyone | Native app guidance, or instructions to open the web console. |
| `ride_request.action_link.why_handoff` | string |  | everyone | Why the human must finish this action and whether it needs the store or Meter support. |
| `ride_request.next_step` | enum |  | everyone | confirm: a preview, ask the human. send_checkout_link: nothing is booked yet; send action_link, the human confirms and pays on Meter, then check list_bookings or get_ride_status. track: booked; share action_link. finish_payment: booked but the card hold failed; send action_link. Values: `confirm`, `send_checkout_link`, `track`, `finish_payment`. |
| `ride_request.checkout_expires_at` | string\|null | ISO 8601 | everyone | When the Meter checkout link stops working (about 30 minutes); null unless next_step is send_checkout_link. |
## RideStatus

Rider view of one of their own rides.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `booking_id` | string |  | everyone | Booking id. |
| `status` | string |  | everyone | Booking status: pending, pending_payment, confirmed, in_progress, completed, canceled … |
| `trip_state` | string |  | everyone | Rider-facing stage: payment_required, pending, dispatching, assigned, arriving, in_progress, completed, canceled or unknown. |
| `fleet_name` | string\|null |  | everyone | Fleet display name. |
| `pickup` | object |  | everyone | Pickup. |
| `pickup.name` | string\|null |  | everyone | Place name, or null. |
| `pickup.address` | string\|null |  | everyone | Formatted address, or null. |
| `dropoff` | object\|null |  | everyone | Drop-off, or null. |
| `dropoff.name` | string\|null |  | everyone | Place name, or null. |
| `dropoff.address` | string\|null |  | everyone | Formatted address, or null. |
| `stops` | array |  | everyone | Intermediate stops. |
| `stops[].name` | string\|null |  | everyone | Place name, or null. |
| `stops[].address` | string\|null |  | everyone | Formatted address, or null. |
| `scheduled_at` | string\|null | ISO 8601 | everyone | Scheduled pickup (ISO 8601). |
| `timezone` | string\|null |  | everyone | IANA timezone of the pickup. |
| `is_asap` | boolean |  | everyone | True for an as-soon-as-possible ride. |
| `price` | object\|null |  | everyone | Quoted total, or null when unknown. |
| `price.amount_minor` | number | minor currency units | everyone | Quoted total in minor units. |
| `price.currency` | string |  | everyone | ISO 4217 currency code, upper-case. |
| `driver` | object\|null |  | everyone | Assigned driver, or null before assignment. |
| `driver.first_name` | string\|null |  | everyone | Driver first name. |
| `driver.photo_url` | string\|null |  | everyone | Driver photo URL, or null. |
| `driver.phone` | string\|null |  | everyone | Driver phone the rider may call, or null. |
| `driver.vehicle` | object\|null |  | everyone | Assigned vehicle, or null. |
| `driver.vehicle.make` | string\|null |  | everyone | Vehicle make. |
| `driver.vehicle.model` | string\|null |  | everyone | Vehicle model. |
| `driver.vehicle.color` | string\|null |  | everyone | Vehicle color. |
| `driver.vehicle.license_plate` | string\|null |  | everyone | License plate. |
| `tracking` | object |  | everyone | Live tracking; present only while the trip view provides it. |
| `tracking.status` | string |  | everyone | live, stale, not_started or unavailable. |
| `tracking.pickup_eta` | string\|null | ISO 8601 | everyone | Estimated driver arrival at pickup (ISO 8601), or null. |
| `tracking.dropoff_eta` | string\|null | ISO 8601 | everyone | Estimated arrival at drop-off (ISO 8601), or null. |
| `tracking.driver_position` | object\|null |  | everyone | Driver position while the ride is live, or null. |
| `tracking.driver_position.latitude` | number |  | everyone | Latitude in degrees. |
| `tracking.driver_position.longitude` | number |  | everyone | Longitude in degrees. |
| `tracking.driver_position.updated_at` | string\|null |  | everyone | When the position was reported. |
| `cancellation` | object\|null |  | everyone | What cancelling now would cost, or null when the ride can no longer be cancelled by the rider. |
| `cancellation.can_cancel` | boolean |  | everyone | True when the rider can cancel with cancel_booking now. |
| `cancellation.fee_minor` | number\|null | minor currency units | everyone | Fee if cancelled now, in minor units; 0 when free. |
| `cancellation.currency` | string\|null |  | everyone | Currency of the fee. |
| `cancellation.free_until` | string\|null | ISO 8601 | everyone | End of the free cancellation window (ISO 8601), or null. |
| `requires_payment_action` | boolean |  | everyone | True when the human must finish payment (bank authentication or a new card); use the finish_ride_payment link. |
| `track_url` | string\|null |  | everyone | Meter page where the human follows this ride and sees the receipt. |
| `receipt_url` | string\|null |  | everyone | Receipt page once completed (requires sign-in), or null. |
| `tip_url` | string\|null |  | everyone | Meter page where the human can tip the driver once the ride is completed, or null. A link only: nothing is charged from chat. |
## RideChangeWrite

Preview or applied change to a rider's booking.

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
| `ride_change` | object |  | everyone | A change to one of the rider's own bookings. |
| `ride_change.booking_id` | string |  | everyone | Booking id. |
| `ride_change.pickup` | object |  | everyone | Pickup after the change. |
| `ride_change.pickup.name` | string\|null |  | everyone | Place name, or null. |
| `ride_change.pickup.address` | string\|null |  | everyone | Formatted address, or null. |
| `ride_change.dropoff` | object\|null |  | everyone | Drop-off after the change. |
| `ride_change.dropoff.name` | string\|null |  | everyone | Place name, or null. |
| `ride_change.dropoff.address` | string\|null |  | everyone | Formatted address, or null. |
| `ride_change.stops` | array |  | everyone | Stops after the change, in order. |
| `ride_change.stops[].name` | string\|null |  | everyone | Place name, or null. |
| `ride_change.stops[].address` | string\|null |  | everyone | Formatted address, or null. |
| `ride_change.pickup_time` | string\|null | ISO 8601 | everyone | Scheduled pickup after the change (ISO 8601), or null for as soon as possible. |
| `ride_change.timezone` | string\|null |  | everyone | IANA timezone of the pickup. |
| `ride_change.price_before` | object\|null |  | everyone | Fare before the change, or null when unknown. |
| `ride_change.price_before.amount_minor` | number | minor currency units | everyone | Amount in minor units. |
| `ride_change.price_before.currency` | string |  | everyone | ISO 4217 currency code, upper-case. |
| `ride_change.price_before.display` | string |  | everyone | Amount formatted for the human. |
| `ride_change.price_after` | object\|null |  | everyone | Fare after the change, or null when unknown. |
| `ride_change.price_after.amount_minor` | number | minor currency units | everyone | Amount in minor units. |
| `ride_change.price_after.currency` | string |  | everyone | ISO 4217 currency code, upper-case. |
| `ride_change.price_after.display` | string |  | everyone | Amount formatted for the human. |
| `ride_change.price_change_minor` | number\|null | minor currency units | everyone | New fare minus old fare in minor units; positive costs more. Null when unknown. |
| `ride_change.next_step` | enum |  | everyone | confirm: a preview, ask the human then confirm with proposal_id. done: applied. open_link: Meter does not apply this in chat; send the human action_link and do not confirm. finish_payment: applied, but the bank needs the human; send action_link. Values: `confirm`, `done`, `open_link`, `finish_payment`. |
| `ride_change.action_link` | object\|null |  | everyone | Booking page where the human makes or pays for the change; present for open_link and finish_payment. |
| `ride_change.action_link.action` | enum |  | everyone | The human action requested. Values: `subscribe_pro`, `subscribe_fleet`, `manage_subscription`, `manage_store_subscription`, `change_plan`, `cancel_subscription`, `update_payment_method`, `meter_pay_setup`, `meter_pay_manage`, `respond_to_dispute`, `request_refund`, `upload_documents`, `edit_fleet_member`, `change_email`, `change_phone`, `delete_account`, `delete_fleet`, `upload_fleet_icon`, `draw_service_area`, `download_pay_stub`, `download_export`, `add_payment_method`, `finish_ride_payment`, `track_ride`, `review_quote`, `tip_ride`. |
| `ride_change.action_link.label` | string |  | everyone | Localized action label; payment setup is called Meter Pay. |
| `ride_change.action_link.url` | string |  | everyone | Meter page URL to present unchanged. Never a provider session or signed download URL. |
| `ride_change.action_link.where_in_console` | string |  | everyone | Where the human can find the action in Meter. |
| `ride_change.action_link.where_in_app` | string |  | everyone | Native app guidance, or instructions to open the web console. |
| `ride_change.action_link.why_handoff` | string |  | everyone | Why the human must finish this action and whether it needs the store or Meter support. |
## RideDetailsWrite

Preview or applied notes and flight number.

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
| `ride_details` | object |  | everyone | Notes and flight number of a rider's booking. |
| `ride_details.booking_id` | string |  | everyone | Booking id. |
| `ride_details.notes` | string\|null |  | everyone | Notes the driver sees, or null. |
| `ride_details.flight_number` | string\|null |  | everyone | Flight number the pickup follows, or null. |
## QuoteResponseWrite

Preview or applied answer to a quote.

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
| `quote_response` | object |  | everyone | The rider's answer to a fleet's quote. |
| `quote_response.quote_id` | string |  | everyone | Quote id. |
| `quote_response.decision` | enum |  | everyone | The rider's answer. Values: `accept`, `decline`. |
| `quote_response.status` | string |  | everyone | Quote status: open before the answer, converted once accepted, declined once declined. |
| `quote_response.fleet_name` | string\|null |  | everyone | Who sent the quote. |
| `quote_response.pickup` | object |  | everyone | Pickup. |
| `quote_response.pickup.name` | string\|null |  | everyone | Place name, or null. |
| `quote_response.pickup.address` | string\|null |  | everyone | Formatted address, or null. |
| `quote_response.dropoff` | object\|null |  | everyone | Drop-off, or null. |
| `quote_response.dropoff.name` | string\|null |  | everyone | Place name, or null. |
| `quote_response.dropoff.address` | string\|null |  | everyone | Formatted address, or null. |
| `quote_response.pickup_time` | string\|null | ISO 8601 | everyone | Scheduled pickup (ISO 8601), or null for as soon as possible. |
| `quote_response.price` | object\|null |  | everyone | Quoted price, or null. |
| `quote_response.price.amount_minor` | number | minor currency units | everyone | Amount in minor units. |
| `quote_response.price.currency` | string |  | everyone | ISO 4217 currency code, upper-case. |
| `quote_response.price.display` | string |  | everyone | Amount formatted for the human. |
| `quote_response.expires_at` | string | ISO 8601 | everyone | When the quote stops accepting answers. |
| `quote_response.payment` | enum |  | everyone | none_at_booking: accepting books the ride with nothing charged now. saved_card: the card saved in the rider's Meter account is held. meter_page: the human accepts and pays on Meter's quote page. Values: `none_at_booking`, `saved_card`, `meter_page`. |
| `quote_response.booking_id` | string\|null |  | everyone | Booking the accepted quote became; null otherwise. |
| `quote_response.next_step` | enum |  | everyone | confirm: a preview, ask the human then confirm with proposal_id. done: applied. open_link: Meter does not apply this in chat; send the human action_link and do not confirm. finish_payment: applied, but the bank needs the human; send action_link. Values: `confirm`, `done`, `open_link`, `finish_payment`. |
| `quote_response.action_link` | object\|null |  | everyone | Quote page (open_link) or booking page (done, finish_payment). |
| `quote_response.action_link.action` | enum |  | everyone | The human action requested. Values: `subscribe_pro`, `subscribe_fleet`, `manage_subscription`, `manage_store_subscription`, `change_plan`, `cancel_subscription`, `update_payment_method`, `meter_pay_setup`, `meter_pay_manage`, `respond_to_dispute`, `request_refund`, `upload_documents`, `edit_fleet_member`, `change_email`, `change_phone`, `delete_account`, `delete_fleet`, `upload_fleet_icon`, `draw_service_area`, `download_pay_stub`, `download_export`, `add_payment_method`, `finish_ride_payment`, `track_ride`, `review_quote`, `tip_ride`. |
| `quote_response.action_link.label` | string |  | everyone | Localized action label; payment setup is called Meter Pay. |
| `quote_response.action_link.url` | string |  | everyone | Meter page URL to present unchanged. Never a provider session or signed download URL. |
| `quote_response.action_link.where_in_console` | string |  | everyone | Where the human can find the action in Meter. |
| `quote_response.action_link.where_in_app` | string |  | everyone | Native app guidance, or instructions to open the web console. |
| `quote_response.action_link.why_handoff` | string |  | everyone | Why the human must finish this action and whether it needs the store or Meter support. |
## RideRatingWrite

Preview or saved ride rating.

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
| `ride_rating` | object |  | everyone | The rider's rating of one completed ride. |
| `ride_rating.booking_id` | string |  | everyone | Booking id. |
| `ride_rating.rating` | number |  | everyone | Stars, 1-5. |
| `ride_rating.tags` | array |  | everyone | Selected reasons. |
| `ride_rating.comment` | string\|null |  | everyone | Comment, or null. |
| `ride_rating.replaced_rating` | number\|null |  | everyone | The rider's earlier rating this one replaces, or null. |
| `ride_rating.tip_link` | object\|null |  | everyone | Meter page where the human can tip the driver; null when unavailable. |
| `ride_rating.tip_link.action` | enum |  | everyone | The human action requested. Values: `subscribe_pro`, `subscribe_fleet`, `manage_subscription`, `manage_store_subscription`, `change_plan`, `cancel_subscription`, `update_payment_method`, `meter_pay_setup`, `meter_pay_manage`, `respond_to_dispute`, `request_refund`, `upload_documents`, `edit_fleet_member`, `change_email`, `change_phone`, `delete_account`, `delete_fleet`, `upload_fleet_icon`, `draw_service_area`, `download_pay_stub`, `download_export`, `add_payment_method`, `finish_ride_payment`, `track_ride`, `review_quote`, `tip_ride`. |
| `ride_rating.tip_link.label` | string |  | everyone | Localized action label; payment setup is called Meter Pay. |
| `ride_rating.tip_link.url` | string |  | everyone | Meter page URL to present unchanged. Never a provider session or signed download URL. |
| `ride_rating.tip_link.where_in_console` | string |  | everyone | Where the human can find the action in Meter. |
| `ride_rating.tip_link.where_in_app` | string |  | everyone | Native app guidance, or instructions to open the web console. |
| `ride_rating.tip_link.why_handoff` | string |  | everyone | Why the human must finish this action and whether it needs the store or Meter support. |
## RideIssueReportWrite

Preview or filed ride issue report.

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
| `ride_issue_report` | object |  | everyone | An app, booking or payment problem reported to Meter. Never changes a rating. |
| `ride_issue_report.booking_id` | string |  | everyone | Booking id. |
| `ride_issue_report.category` | enum |  | everyone | Issue category. Values: `app_problem`, `notification_problem`, `booking_problem`, `dispatch_problem`, `wrong_fare_shown`, `payment_problem`, `trip_status_wrong`, `other`. |
| `ride_issue_report.description` | string |  | everyone | What went wrong. |
| `ride_issue_report.reference_number` | number\|null |  | everyone | Meter support reference once filed; null in a preview. |
## RatingPrompt

Which ride to rate, and the reasons a rating may carry.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `prompt` | object\|null |  | everyone | The newest completed ride waiting for a rating, or null. |
| `prompt.booking_id` | string |  | everyone | Booking to rate. |
| `prompt.completed_at` | string | ISO 8601 | everyone | When the ride ended. |
| `prompt.prompt_expires_at` | string | ISO 8601 | everyone | When Meter stops asking for this rating. |
| `prompt.driver_first_name` | string\|null |  | everyone | Driver first name. |
| `prompt.fleet_name` | string\|null |  | everyone | Fleet display name. |
| `compliment_tags` | array |  | everyone | Reasons rate_ride accepts with 4-5 stars. |
| `issue_tags` | array |  | everyone | Reasons rate_ride accepts with 1-3 stars. |
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
| `booking_source` | string\|null |  | everyone | Where the booking came from: web, web_embedded, rider_app, meter_app, admin_web, voice, messaging. |
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
| `items[].booking_source` | string\|null |  | everyone | Where the booking came from: web, web_embedded, rider_app, meter_app, admin_web, voice, messaging. |
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
| `entries[].field_changes[].field` | string |  | everyone | Machine name of the changed field (e.g. "scheduled_time"). |
| `entries[].field_changes[].label` | string |  | everyone | Human label of the changed field. |
| `entries[].field_changes[].old` | string\|null |  | everyone | Previous value as display text, or null. |
| `entries[].field_changes[].new` | string\|null |  | everyone | New value as display text, or null. |
| `next_cursor` | string\|null |  | everyone | Cursor for the next (older) page, or null. |
| `has_more` | boolean |  | everyone | True when older entries exist. |
