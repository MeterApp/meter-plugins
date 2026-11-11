# Meter data-model reference

Generated from the `@meterapp/meter-sdk` catalog and DTO schemas; do not edit by hand. See the [reference index](../data-model.md) for all definitions.

## FleetMemberRemovalWrite

Result of remove_fleet_member: what changed and the removed member.

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
| `member` | object |  | everyone | A member removed by remove_fleet_member. Their past trips and the membership history are kept. |
| `member.member_id` | string |  | everyone | Opaque member id (profile id). |
| `member.display_name` | string\|null |  | everyone | Display name, or null if not set. |
| `member.previous_role` | enum |  | everyone | Role in the fleet. owner: created the fleet and controls billing; admin: manages members, vehicles, bookings and money; driver: drives and sees only their own trips, bookings and earnings. Values: `owner`, `admin`, `driver`. |
| `member.removed` | boolean |  | everyone | True once the member is out of the fleet. |
## FleetMemberNameWrite

Result of update_member_name: what changed and the member after the call.

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
| `member` | object |  | everyone | A fleet member as listed by list_fleet_members (owners/admins only). |
| `member.member_id` | string |  | everyone | Opaque member id (profile id). Use as `driver` in list_trips. |
| `member.display_name` | string\|null |  | everyone | Display name, or null if not set. |
| `member.role` | enum |  | everyone | Role in the fleet. owner: created the fleet and controls billing; admin: manages members, vehicles, bookings and money; driver: drives and sees only their own trips, bookings and earnings. Values: `owner`, `admin`, `driver`. |
| `member.joined_at` | string\|null | ISO 8601 | everyone | When the member joined the fleet. |
| `member.email` | string\|null |  | owner, admin | Member email. Visible to fleet owners/admins only. |
| `member.phone` | string\|null |  | owner, admin | Member phone (E.164). Visible to fleet owners/admins only. |
## MemberOnlineRequest

A request sent to a driver's Meter app to go online or offline. The app acts on it when it is reachable.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `member_id` | string |  | everyone | Opaque member id (profile id). |
| `display_name` | string\|null |  | everyone | Display name, or null if not set. |
| `requested_state` | enum |  | everyone | What the driver's Meter app was asked to do. Values: `online`, `offline`. |
| `devices_notified` | number\|null |  | everyone | For online: how many of the driver's devices were asked (0 means none can receive it). Null for offline. |
## MemberOnlineRequestWrite

Result of set_member_online_state: what was requested and from how many devices.

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
| `request` | object |  | everyone | A request sent to a driver's Meter app to go online or offline. The app acts on it when it is reachable. |
| `request.member_id` | string |  | everyone | Opaque member id (profile id). |
| `request.display_name` | string\|null |  | everyone | Display name, or null if not set. |
| `request.requested_state` | enum |  | everyone | What the driver's Meter app was asked to do. Values: `online`, `offline`. |
| `request.devices_notified` | number\|null |  | everyone | For online: how many of the driver's devices were asked (0 means none can receive it). Null for offline. |
## VehicleUpdateWrite

Result of update_vehicle: what changed and the vehicle after the call.

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
## VehicleRemovalWrite

Result of remove_vehicle: what changed and the vehicle as it was removed (its driver unassigned).

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
## FareRead

Strict full supported fare pricing; preserves saved currency precision.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `display_name` | string\|null |  | everyone | Fare name shown to drivers and riders. |
| `currency_code` | string\|null |  | everyone | Saved currency, or null when legacy data omitted it. Never inferred or backfilled by these reads. |
| `base` | number | major currency units | everyone | Flag-drop / base fare in major currency units (e.g. 3.50 = $3.50). |
| `minimum_fare` | number | major currency units | everyone | Minimum total fare in major currency units. |
| `distance_rate` | number | major currency units per mile or km | everyone | Rate per distance unit (mile, or kilometer when `metric` is true) in major units. |
| `minute_rate` | number | major currency units per minute | everyone | Rate per minute in major currency units. |
| `wait_time_minute_rate` | number | major currency units per minute | everyone | Rate per minute of waiting in major currency units. |
| `metric` | boolean |  | everyone | True when distance_rate is per kilometer; false when per mile. |
| `id` | string |  | everyone | Fare id. |
| `source` | enum |  | everyone | Custom fare or saved published tariff; published tariffs are read-only. Values: `custom`, `saved_official`. |
| `has_advanced_pricing` | boolean |  | everyone | True when headline rates do not describe all pricing; inspect get_fare before quoting or changing rates. |
| `hidden_from_drivers` | boolean |  | everyone | Whether this fleet fare is hidden from drivers. Hidden fares are admin-only. |
| `tax_rate` | number | percentage points | everyone | Tax percentage points as stored, e.g. 8 means eight percent. |
| `distance_rounding` | number\|null |  | everyone | Legacy distance-rounding increment in the fare distance unit. |
| `minute_rate_speed_threshold_kph` | number\|null | km/h | everyone | Legacy speed threshold for time charging, in kilometers per hour. |
| `distance_tiers` | array\|null |  | everyone | Complete supported legacy distance tiers, or null. |
| `distance_tiers[].threshold` | number |  | everyone | Distance threshold in miles or kilometers according to metric. |
| `distance_tiers[].rate` | number | major currency units per mile or km | everyone | Major currency units per distance unit. |
| `fees` | array\|null |  | everyone | Complete supported legacy fees without internal identifiers. |
| `fees[].name` | string |  | everyone | Human fee name. |
| `fees[].currency` | string |  | everyone | Fee currency as stored; do not combine different currencies. |
| `fees[].unitAmount` | number | minor currency units | everyone | Fee amount in minor currency units. |
| `fees[].optional` | boolean\|null |  | everyone | Whether driver choice is required; null preserves legacy unspecified state. |
| `fare_model` | object\|null |  | everyone | Complete supported canonical pricing. Amount fields ending minor are integer minor currency units. Semantic rule/tariff identifiers are retained for cross-references; source provenance is excluded. |
| `fare_model.schema_version` | enum |  | everyone | Canonical pricing schema version. Values: `1`. |
| `fare_model.fare_kind` | enum |  | everyone | Metered fare pricing model. Values: `metered`. |
| `fare_model.source_semantics` | enum |  | everyone | Regulatory meaning of the saved tariff, independent of source ownership or provenance. Values: `exact_published_tariff`, `official_maximum`, `regulated_range`, `fixed_route_override`, `negotiated_optional`, `source_only`, `unsupported`. |
| `fare_model.calculation_profile` | enum (optional) |  | everyone | Compatibility calculation rules for this saved model. Values: `legacy_scalar_parity_v1`. |
| `fare_model.currency_code` | string |  | everyone | ISO 4217 currency; canonical money amounts use its minor unit. |
| `fare_model.unit_system` | enum |  | everyone | Display distance unit system; explicit meter and second fields retain their stated units. Values: `metric`, `imperial`. |
| `fare_model.timezone` | string |  | everyone | IANA timezone for local tariff schedules. |
| `fare_model.tax_mode` | enum |  | everyone | Whether prices include tax, exclude tax, or have no tax. Values: `included`, `excluded`, `none`. |
| `fare_model.rounding` | object (optional) |  | everyone | Explicit monetary rounding policy. |
| `fare_model.rounding.stage` | enum |  | everyone | Pricing stage at which monetary rounding applies. Values: `none`, `meter`, `line_item`, `tax`, `total`. |
| `fare_model.rounding.increment_minor` | number (optional) |  | everyone | Rounding quantum in integer minor currency units. |
| `fare_model.rounding.mode` | enum |  | everyone | Direction of monetary rounding: nearest, up, or down. Values: `nearest`, `up`, `down`. |
| `fare_model.tariffs` | array |  | everyone | Complete bounded set of pricing tariffs. |
| `fare_model.tariffs[].tariff_id` | string |  | everyone | Semantic tariff identifier used within the model; not a provider or database identifier. |
| `fare_model.tariffs[].display_name` | string (optional) |  | everyone | Human-readable pricing label. |
| `fare_model.tariffs[].schedule` | object (optional) |  | everyone | Local-time conditions for this tariff or rule. |
| `fare_model.tariffs[].schedule.days` | array |  | everyone | Weekdays on which the local schedule starts. |
| `fare_model.tariffs[].schedule.start_local_time` | string |  | everyone | Schedule start in local HH:mm time. |
| `fare_model.tariffs[].schedule.end_local_time` | string |  | everyone | Schedule end in local HH:mm time; earlier end crosses midnight, equal start and end means a full day. |
| `fare_model.tariffs[].schedule.holiday_behavior` | enum |  | everyone | Whether holidays are included, excluded, or required. Values: `include`, `exclude`, `only`. |
| `fare_model.tariffs[].activation_conditions` | object (optional) |  | everyone | Service and pickup conditions that select this tariff. |
| `fare_model.tariffs[].activation_conditions.service_class` | enum |  | everyone | Service class required for tariff activation. Values: `standard`, `airport`, `wheelchair`, `premium`, `van`, `motorcycle`, `auto_rickshaw`, `jurisdiction_specific`. |
| `fare_model.tariffs[].activation_conditions.pickup_location_tags` | array |  | everyone | Pickup categories applicable to the tariff or rule. |
| `fare_model.tariffs[].meter_logic` | object\|object |  | everyone | Complete typed meter calculation: continuous components or whichever-first pulses. |
| `fare_model.tariffs[].minimum_fare_minor` | number (optional) |  | everyone | Minimum charge in integer minor currency units. |
| `fare_model.booking_rules` | array |  | everyone | Fixed booking-channel charges and their optional schedules. |
| `fare_model.booking_rules[].rule_id` | string |  | everyone | Semantic rule identifier within this pricing model. |
| `fare_model.booking_rules[].channel` | enum |  | everyone | Booking channel to which the charge applies. Values: `street_hail`, `dispatch`, `phone`, `app`, `web`, `stand`, `airport_queue`. |
| `fare_model.booking_rules[].amount_minor` | number |  | everyone | Charge in integer minor currency units. |
| `fare_model.booking_rules[].schedule` | object (optional) |  | everyone | Local-time conditions for this tariff or rule. |
| `fare_model.booking_rules[].schedule.days` | array |  | everyone | Weekdays on which the local schedule starts. |
| `fare_model.booking_rules[].schedule.start_local_time` | string |  | everyone | Schedule start in local HH:mm time. |
| `fare_model.booking_rules[].schedule.end_local_time` | string |  | everyone | Schedule end in local HH:mm time; earlier end crosses midnight, equal start and end means a full day. |
| `fare_model.booking_rules[].schedule.holiday_behavior` | enum |  | everyone | Whether holidays are included, excluded, or required. Values: `include`, `exclude`, `only`. |
| `fare_model.additive_rules` | array |  | everyone | Conditional fixed or percentage pricing additions. |
| `fare_model.additive_rules[].rule_id` | string |  | everyone | Semantic rule identifier within this pricing model. |
| `fare_model.additive_rules[].type` | enum |  | everyone | Category of conditional pricing addition. Values: `booking`, `dispatch`, `passenger`, `luggage`, `vehicle_class`, `airport_pickup`, `port_pickup`, `station_pickup`, `night`, `peak`, `holiday`, `jurisdiction_specific`. |
| `fare_model.additive_rules[].amount` | object\|object |  | everyone | Fixed minor-unit amount or percentage with an explicit calculation base. |
| `fare_model.additive_rules[].schedule` | object (optional) |  | everyone | Local-time conditions for this tariff or rule. |
| `fare_model.additive_rules[].schedule.days` | array |  | everyone | Weekdays on which the local schedule starts. |
| `fare_model.additive_rules[].schedule.start_local_time` | string |  | everyone | Schedule start in local HH:mm time. |
| `fare_model.additive_rules[].schedule.end_local_time` | string |  | everyone | Schedule end in local HH:mm time; earlier end crosses midnight, equal start and end means a full day. |
| `fare_model.additive_rules[].schedule.holiday_behavior` | enum |  | everyone | Whether holidays are included, excluded, or required. Values: `include`, `exclude`, `only`. |
| `fare_model.additive_rules[].service_classes` | array (optional) |  | everyone | Service classes to which this rule applies. |
| `fare_model.additive_rules[].pickup_location_tags` | array (optional) |  | everyone | Pickup categories applicable to the tariff or rule. |
| `fare_model.passthrough_rules` | array |  | everyone | Rules for passing actual, manual, or estimated costs to the rider. |
| `fare_model.passthrough_rules[].rule_id` | string |  | everyone | Semantic rule identifier within this pricing model. |
| `fare_model.passthrough_rules[].type` | enum |  | everyone | Category of passthrough cost. Values: `toll`, `parking`, `ferry`, `airport_fee`, `manual_extra`, `jurisdiction_specific`. |
| `fare_model.passthrough_rules[].mode` | enum |  | everyone | Whether the passthrough cost is actual, manually entered, or estimated. Values: `actual`, `manual`, `estimated`. |
| `fare_model.passthrough_rules[].taxable` | boolean |  | everyone | Whether this passthrough cost is taxable. |
| `fare_model.passthrough_rules[].display_name` | string (optional) |  | everyone | Human-readable pricing label. |
| `fare_model.passthrough_rules[].default_amount_minor` | number (optional) |  | everyone | Default cost in integer minor currency units. |
| `fare_model.passthrough_rules[].application` | enum (optional) |  | everyone | Whether the passthrough charge is required or optional. Values: `required`, `optional`. |
| `fare_model.capabilities` | object (optional) |  | everyone | Saved model support and client/entitlement requirements. |
| `fare_model.capabilities.support_level` | enum |  | everyone | Supported calculation level for the saved pricing model. Values: `legacy_scalar`, `source_only`, `estimate_capable`, `live_meter_capable`, `unsupported`. |
| `fare_model.capabilities.required_client_capabilities` | array |  | everyone | Capabilities a client must support before using this model. |
| `fare_model.capabilities.entitlement_requirements` | object (optional) |  | everyone | Paid access requirements for authoring or personal live use. |
| `fare_model.capabilities.entitlement_requirements.advanced_authoring` | array |  | everyone | Entitlements required to author advanced pricing. |
| `fare_model.capabilities.entitlement_requirements.personal_live_use` | array |  | everyone | Entitlements required for personal live metering. |
| `fare_model.capabilities.unsupported_reason` | string (optional) |  | everyone | Reason this saved model is not supported, when present. |
| `pricing_status` | enum |  | everyone | Unsupported legacy pricing is not silently treated as complete; see limitations. Values: `supported`, `unsupported_legacy`. |
| `limitations` | array |  | everyone | Concrete unsupported saved fields. Do not quote a complete price when nonempty. |
## TripAdjustmentWrite

Preview or confirmed trip adjustment. Amounts are in the currency's smallest unit; cash-paid is bookkeeping.

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
| `trip_adjustment` | object\|null |  | everyone | Current finite receipt in preview or frozen confirmed command proof. |
| `trip_adjustment.trip_id` | string |  | everyone | Trip identifier for the confirmed adjustment. |
| `trip_adjustment.currency` | string |  | everyone | Exact receipt currency; determines the minor-unit exponent. |
| `trip_adjustment.previous_total_minor` | number | minor currency units | everyone | Active receipt total before this command, in minor units. |
| `trip_adjustment.total_minor` | number | minor currency units | everyone | Confirmed active total, or confirmed cash amount, in minor units. |
| `trip_adjustment.fee_id` | string\|null |  | everyone | Added or removed saved fee identifier; null for other changes. |
| `trip_adjustment.discount_id` | string\|null |  | everyone | Added or removed saved discount identifier; null for other changes. |
| `trip_adjustment.is_paid` | boolean |  | everyone | Whether this command recorded the trip as paid. |
| `trip_adjustment.payment_method` | enum\|null |  | everyone | Cash when this command recorded cash received; otherwise null. Values: `cash`. |
## FareWrite

Preview or confirmed custom fare. Deleted fares return null; stored pricing is never inferred from an audit log.

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
| `fare` | object\|null |  | everyone | Strict full supported fare pricing; preserves saved currency precision. |
| `fare.display_name` | string\|null |  | everyone | Fare name shown to drivers and riders. |
| `fare.currency_code` | string\|null |  | everyone | Saved currency, or null when legacy data omitted it. Never inferred or backfilled by these reads. |
| `fare.base` | number | major currency units | everyone | Flag-drop / base fare in major currency units (e.g. 3.50 = $3.50). |
| `fare.minimum_fare` | number | major currency units | everyone | Minimum total fare in major currency units. |
| `fare.distance_rate` | number | major currency units per mile or km | everyone | Rate per distance unit (mile, or kilometer when `metric` is true) in major units. |
| `fare.minute_rate` | number | major currency units per minute | everyone | Rate per minute in major currency units. |
| `fare.wait_time_minute_rate` | number | major currency units per minute | everyone | Rate per minute of waiting in major currency units. |
| `fare.metric` | boolean |  | everyone | True when distance_rate is per kilometer; false when per mile. |
| `fare.id` | string |  | everyone | Fare id. |
| `fare.source` | enum |  | everyone | Custom fare or saved published tariff; published tariffs are read-only. Values: `custom`, `saved_official`. |
| `fare.has_advanced_pricing` | boolean |  | everyone | True when headline rates do not describe all pricing; inspect get_fare before quoting or changing rates. |
| `fare.hidden_from_drivers` | boolean |  | everyone | Whether this fleet fare is hidden from drivers. Hidden fares are admin-only. |
| `fare.tax_rate` | number | percentage points | everyone | Tax percentage points as stored, e.g. 8 means eight percent. |
| `fare.distance_rounding` | number\|null |  | everyone | Legacy distance-rounding increment in the fare distance unit. |
| `fare.minute_rate_speed_threshold_kph` | number\|null | km/h | everyone | Legacy speed threshold for time charging, in kilometers per hour. |
| `fare.distance_tiers` | array\|null |  | everyone | Complete supported legacy distance tiers, or null. |
| `fare.distance_tiers[].threshold` | number |  | everyone | Distance threshold in miles or kilometers according to metric. |
| `fare.distance_tiers[].rate` | number | major currency units per mile or km | everyone | Major currency units per distance unit. |
| `fare.fees` | array\|null |  | everyone | Complete supported legacy fees without internal identifiers. |
| `fare.fees[].name` | string |  | everyone | Human fee name. |
| `fare.fees[].currency` | string |  | everyone | Fee currency as stored; do not combine different currencies. |
| `fare.fees[].unitAmount` | number | minor currency units | everyone | Fee amount in minor currency units. |
| `fare.fees[].optional` | boolean\|null |  | everyone | Whether driver choice is required; null preserves legacy unspecified state. |
| `fare.fare_model` | object\|null |  | everyone | Complete supported canonical pricing. Amount fields ending minor are integer minor currency units. Semantic rule/tariff identifiers are retained for cross-references; source provenance is excluded. |
| `fare.fare_model.schema_version` | enum |  | everyone | Canonical pricing schema version. Values: `1`. |
| `fare.fare_model.fare_kind` | enum |  | everyone | Metered fare pricing model. Values: `metered`. |
| `fare.fare_model.source_semantics` | enum |  | everyone | Regulatory meaning of the saved tariff, independent of source ownership or provenance. Values: `exact_published_tariff`, `official_maximum`, `regulated_range`, `fixed_route_override`, `negotiated_optional`, `source_only`, `unsupported`. |
| `fare.fare_model.calculation_profile` | enum (optional) |  | everyone | Compatibility calculation rules for this saved model. Values: `legacy_scalar_parity_v1`. |
| `fare.fare_model.currency_code` | string |  | everyone | ISO 4217 currency; canonical money amounts use its minor unit. |
| `fare.fare_model.unit_system` | enum |  | everyone | Display distance unit system; explicit meter and second fields retain their stated units. Values: `metric`, `imperial`. |
| `fare.fare_model.timezone` | string |  | everyone | IANA timezone for local tariff schedules. |
| `fare.fare_model.tax_mode` | enum |  | everyone | Whether prices include tax, exclude tax, or have no tax. Values: `included`, `excluded`, `none`. |
| `fare.fare_model.rounding` | object (optional) |  | everyone | Explicit monetary rounding policy. |
| `fare.fare_model.rounding.stage` | enum |  | everyone | Pricing stage at which monetary rounding applies. Values: `none`, `meter`, `line_item`, `tax`, `total`. |
| `fare.fare_model.rounding.increment_minor` | number (optional) |  | everyone | Rounding quantum in integer minor currency units. |
| `fare.fare_model.rounding.mode` | enum |  | everyone | Direction of monetary rounding: nearest, up, or down. Values: `nearest`, `up`, `down`. |
| `fare.fare_model.tariffs` | array |  | everyone | Complete bounded set of pricing tariffs. |
| `fare.fare_model.tariffs[].tariff_id` | string |  | everyone | Semantic tariff identifier used within the model; not a provider or database identifier. |
| `fare.fare_model.tariffs[].display_name` | string (optional) |  | everyone | Human-readable pricing label. |
| `fare.fare_model.tariffs[].schedule` | object (optional) |  | everyone | Local-time conditions for this tariff or rule. |
| `fare.fare_model.tariffs[].schedule.days` | array |  | everyone | Weekdays on which the local schedule starts. |
| `fare.fare_model.tariffs[].schedule.start_local_time` | string |  | everyone | Schedule start in local HH:mm time. |
| `fare.fare_model.tariffs[].schedule.end_local_time` | string |  | everyone | Schedule end in local HH:mm time; earlier end crosses midnight, equal start and end means a full day. |
| `fare.fare_model.tariffs[].schedule.holiday_behavior` | enum |  | everyone | Whether holidays are included, excluded, or required. Values: `include`, `exclude`, `only`. |
| `fare.fare_model.tariffs[].activation_conditions` | object (optional) |  | everyone | Service and pickup conditions that select this tariff. |
| `fare.fare_model.tariffs[].activation_conditions.service_class` | enum |  | everyone | Service class required for tariff activation. Values: `standard`, `airport`, `wheelchair`, `premium`, `van`, `motorcycle`, `auto_rickshaw`, `jurisdiction_specific`. |
| `fare.fare_model.tariffs[].activation_conditions.pickup_location_tags` | array |  | everyone | Pickup categories applicable to the tariff or rule. |
| `fare.fare_model.tariffs[].meter_logic` | object\|object |  | everyone | Complete typed meter calculation: continuous components or whichever-first pulses. |
| `fare.fare_model.tariffs[].minimum_fare_minor` | number (optional) |  | everyone | Minimum charge in integer minor currency units. |
| `fare.fare_model.booking_rules` | array |  | everyone | Fixed booking-channel charges and their optional schedules. |
| `fare.fare_model.booking_rules[].rule_id` | string |  | everyone | Semantic rule identifier within this pricing model. |
| `fare.fare_model.booking_rules[].channel` | enum |  | everyone | Booking channel to which the charge applies. Values: `street_hail`, `dispatch`, `phone`, `app`, `web`, `stand`, `airport_queue`. |
| `fare.fare_model.booking_rules[].amount_minor` | number |  | everyone | Charge in integer minor currency units. |
| `fare.fare_model.booking_rules[].schedule` | object (optional) |  | everyone | Local-time conditions for this tariff or rule. |
| `fare.fare_model.booking_rules[].schedule.days` | array |  | everyone | Weekdays on which the local schedule starts. |
| `fare.fare_model.booking_rules[].schedule.start_local_time` | string |  | everyone | Schedule start in local HH:mm time. |
| `fare.fare_model.booking_rules[].schedule.end_local_time` | string |  | everyone | Schedule end in local HH:mm time; earlier end crosses midnight, equal start and end means a full day. |
| `fare.fare_model.booking_rules[].schedule.holiday_behavior` | enum |  | everyone | Whether holidays are included, excluded, or required. Values: `include`, `exclude`, `only`. |
| `fare.fare_model.additive_rules` | array |  | everyone | Conditional fixed or percentage pricing additions. |
| `fare.fare_model.additive_rules[].rule_id` | string |  | everyone | Semantic rule identifier within this pricing model. |
| `fare.fare_model.additive_rules[].type` | enum |  | everyone | Category of conditional pricing addition. Values: `booking`, `dispatch`, `passenger`, `luggage`, `vehicle_class`, `airport_pickup`, `port_pickup`, `station_pickup`, `night`, `peak`, `holiday`, `jurisdiction_specific`. |
| `fare.fare_model.additive_rules[].amount` | object\|object |  | everyone | Fixed minor-unit amount or percentage with an explicit calculation base. |
| `fare.fare_model.additive_rules[].schedule` | object (optional) |  | everyone | Local-time conditions for this tariff or rule. |
| `fare.fare_model.additive_rules[].schedule.days` | array |  | everyone | Weekdays on which the local schedule starts. |
| `fare.fare_model.additive_rules[].schedule.start_local_time` | string |  | everyone | Schedule start in local HH:mm time. |
| `fare.fare_model.additive_rules[].schedule.end_local_time` | string |  | everyone | Schedule end in local HH:mm time; earlier end crosses midnight, equal start and end means a full day. |
| `fare.fare_model.additive_rules[].schedule.holiday_behavior` | enum |  | everyone | Whether holidays are included, excluded, or required. Values: `include`, `exclude`, `only`. |
| `fare.fare_model.additive_rules[].service_classes` | array (optional) |  | everyone | Service classes to which this rule applies. |
| `fare.fare_model.additive_rules[].pickup_location_tags` | array (optional) |  | everyone | Pickup categories applicable to the tariff or rule. |
| `fare.fare_model.passthrough_rules` | array |  | everyone | Rules for passing actual, manual, or estimated costs to the rider. |
| `fare.fare_model.passthrough_rules[].rule_id` | string |  | everyone | Semantic rule identifier within this pricing model. |
| `fare.fare_model.passthrough_rules[].type` | enum |  | everyone | Category of passthrough cost. Values: `toll`, `parking`, `ferry`, `airport_fee`, `manual_extra`, `jurisdiction_specific`. |
| `fare.fare_model.passthrough_rules[].mode` | enum |  | everyone | Whether the passthrough cost is actual, manually entered, or estimated. Values: `actual`, `manual`, `estimated`. |
| `fare.fare_model.passthrough_rules[].taxable` | boolean |  | everyone | Whether this passthrough cost is taxable. |
| `fare.fare_model.passthrough_rules[].display_name` | string (optional) |  | everyone | Human-readable pricing label. |
| `fare.fare_model.passthrough_rules[].default_amount_minor` | number (optional) |  | everyone | Default cost in integer minor currency units. |
| `fare.fare_model.passthrough_rules[].application` | enum (optional) |  | everyone | Whether the passthrough charge is required or optional. Values: `required`, `optional`. |
| `fare.fare_model.capabilities` | object (optional) |  | everyone | Saved model support and client/entitlement requirements. |
| `fare.fare_model.capabilities.support_level` | enum |  | everyone | Supported calculation level for the saved pricing model. Values: `legacy_scalar`, `source_only`, `estimate_capable`, `live_meter_capable`, `unsupported`. |
| `fare.fare_model.capabilities.required_client_capabilities` | array |  | everyone | Capabilities a client must support before using this model. |
| `fare.fare_model.capabilities.entitlement_requirements` | object (optional) |  | everyone | Paid access requirements for authoring or personal live use. |
| `fare.fare_model.capabilities.entitlement_requirements.advanced_authoring` | array |  | everyone | Entitlements required to author advanced pricing. |
| `fare.fare_model.capabilities.entitlement_requirements.personal_live_use` | array |  | everyone | Entitlements required for personal live metering. |
| `fare.fare_model.capabilities.unsupported_reason` | string (optional) |  | everyone | Reason this saved model is not supported, when present. |
| `fare.pricing_status` | enum |  | everyone | Unsupported legacy pricing is not silently treated as complete; see limitations. Values: `supported`, `unsupported_legacy`. |
| `fare.limitations` | array |  | everyone | Concrete unsupported saved fields. Do not quote a complete price when nonempty. |
## FareReadPage

A bounded page of authorized fare headlines.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `items` | array |  | everyone | Authorized fare headlines. |
| `items[].display_name` | string\|null |  | everyone | Fare name shown to drivers and riders. |
| `items[].currency_code` | string\|null |  | everyone | Saved currency, or null when legacy data omitted it. Never inferred or backfilled by these reads. |
| `items[].base` | number | major currency units | everyone | Flag-drop / base fare in major currency units (e.g. 3.50 = $3.50). |
| `items[].minimum_fare` | number | major currency units | everyone | Minimum total fare in major currency units. |
| `items[].distance_rate` | number | major currency units per mile or km | everyone | Rate per distance unit (mile, or kilometer when `metric` is true) in major units. |
| `items[].minute_rate` | number | major currency units per minute | everyone | Rate per minute in major currency units. |
| `items[].wait_time_minute_rate` | number | major currency units per minute | everyone | Rate per minute of waiting in major currency units. |
| `items[].metric` | boolean |  | everyone | True when distance_rate is per kilometer; false when per mile. |
| `items[].id` | string |  | everyone | Fare id. |
| `items[].source` | enum |  | everyone | Custom fare or saved published tariff; published tariffs are read-only. Values: `custom`, `saved_official`. |
| `items[].has_advanced_pricing` | boolean |  | everyone | True when headline rates do not describe all pricing; inspect get_fare before quoting or changing rates. |
| `items[].hidden_from_drivers` | boolean |  | everyone | Whether this fleet fare is hidden from drivers. Hidden fares are admin-only. |
| `next_cursor` | string\|null |  | everyone | Next-page cursor, or null. |
| `has_more` | boolean |  | everyone | Whether another page exists. |
## FareAuditPage

A bounded page of pricing history within the current authorized ownership and visibility period.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `items` | array |  | everyone | Current-scope pricing history; historical ownership/visibility boundaries are not crossed. |
| `items[].id` | string |  | everyone | Audit entry id. |
| `items[].action` | enum |  | everyone | Recorded operation. Values: `INSERT`, `UPDATE`, `DELETE`. |
| `items[].changed_at` | string |  | everyone | ISO timestamp of the recorded change. |
| `items[].changes` | array |  | everyone | Only validated public pricing changes; no actor identity or internal provenance. |
| `items[].omitted_pricing_fields` | array |  | everyone | Public pricing fields whose legacy values could not be represented safely; internal fields are never listed. |
| `items[].agent_change_id` | string\|null |  | everyone | Saved change id only when visible to this actor and connection, otherwise null. |
| `next_cursor` | string\|null |  | everyone | Cursor for older entries, or null. |
| `has_more` | boolean |  | everyone | Whether older authorized entries exist. |
## FeedbackVote

Committed vote and following state for an authorized public idea.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `item_id` | string |  | everyone | Public idea identifier. |
| `voted` | boolean |  | everyone | The caller's committed vote state. |
| `vote_count` | number |  | everyone | Total votes at commit. |
| `is_following` | boolean |  | everyone | The caller's following state at commit. |
## FeedbackFollow

Committed following state for an authorized feedback item.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `item_id` | string |  | everyone | Authorized feedback identifier. |
| `following` | boolean |  | everyone | The caller's committed following state. |
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
## FeedbackChangelogEntry

Published release notes without author identities or private feedback links.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `id` | string |  | everyone | Published changelog entry identifier. |
| `slug` | string |  | everyone | Public changelog address segment. |
| `title` | string |  | everyone | Complete public release title. |
| `body` | string |  | everyone | Complete public release description. |
| `platforms` | array |  | everyone | Platforms covered by this release. |
| `published_at` | string |  | everyone | Actual publication timestamp. |
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
## FeedbackItem

Customer-visible idea or private report, filtered by current access and moderation.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `id` | string |  | everyone | Opaque identifier of this record. |
| `reference` | string |  | everyone | Customer-facing feedback reference. |
| `type` | string |  | everyone | Record kind, preserving future values. |
| `slug` | string (optional) |  | everyone | Public idea URL segment when supplied. |
| `url` | string (optional) |  | everyone | Public idea address when supplied. |
| `title` | string |  | everyone | Complete customer-visible title. |
| `body` | string |  | everyone | Customer-visible text; null for a deleted comment. |
| `visibility` | object (optional) |  | everyone | Text visibility only; private screenshots and diagnostics retain separate authorization. |
| `visibility.scope` | string |  | everyone | Server-authorized text audience; public, fleet or reporter. Preserve future values. This never grants attachment or diagnostic access. |
| `visibility.label` | string |  | everyone | Localized explanation of who can read the text. |
| `language` | string (optional) |  | everyone | Submitted language when supplied. |
| `moderation_state` | string (optional) |  | everyone | Moderation state visible to this caller when supplied. |
| `category` | object |  | everyone | Localized category of the feedback. |
| `category.key` | string |  | everyone | Stable category or status id, preserving future values. |
| `category.label` | string |  | everyone | Localized customer-facing label. |
| `status` | object |  | everyone | Current customer-visible status and its change timestamp. |
| `status.key` | string |  | everyone | Stable category or status id, preserving future values. |
| `status.label` | string |  | everyone | Localized customer-facing label. |
| `status.changed_at` | string |  | everyone | Timestamp when the current status was reached. |
| `subject` | object (optional) |  | everyone | Private report subject, only when visible to the caller. |
| `subject.type` | string |  | everyone | Record kind, preserving future values. |
| `subject.id` | string (optional) |  | everyone | Opaque identifier of this record. |
| `subject.label` | string (optional) |  | everyone | Localized customer-facing label. |
| `subject.occurred_at` | string (optional) |  | everyone | Timestamp of the linked subject when supplied. |
| `subject.deep_link` | string (optional) |  | everyone | Authorized application link to the subject when supplied. |
| `author` | object |  | everyone | Privacy-filtered public author identity. |
| `author.display_name` | string (optional) |  | everyone | Privacy-filtered first name, or Meter team for staff; omitted when unavailable. |
| `author.role` | string |  | everyone | Public role label, preserving future values. |
| `author.is_viewer` | boolean |  | everyone | Whether this author is the verified caller. |
| `counts` | object |  | everyone | Current engagement counts. |
| `counts.votes` | number |  | everyone | Current vote count. |
| `counts.comments` | number |  | everyone | Current visible comment count. |
| `viewer` | object |  | everyone | Current caller interactions and permissions. |
| `viewer.has_voted` | boolean |  | everyone | Whether the caller currently votes on this idea. |
| `viewer.is_following` | boolean |  | everyone | Whether the caller currently follows updates. |
| `viewer.can_vote` | boolean |  | everyone | Whether the caller may vote under current access and moderation rules. |
| `viewer.can_comment` | boolean |  | everyone | Whether the caller may comment under current access and moderation rules. |
| `viewer.can_delete` | boolean |  | everyone | Whether the caller may withdraw this item. |
| `availability` | array |  | everyone | Verified per-platform availability. |
| `availability[].platform` | string |  | everyone | Target platform, preserving future values. |
| `availability[].state` | string |  | everyone | Availability or attachment state, preserving future values. |
| `availability[].fixed_in_version` | string (optional) |  | everyone | Verified release version when supplied. |
| `availability[].available_at` | string (optional) |  | everyone | Release availability timestamp when supplied. |
| `merged_into` | object (optional) |  | everyone | Visible canonical destination when this item was merged. |
| `merged_into.id` | string |  | everyone | Opaque identifier of this record. |
| `merged_into.slug` | string (optional) |  | everyone | Public idea URL segment when supplied. |
| `merged_into.title` | string (optional) |  | everyone | Complete customer-visible title. |
| `device_details` | object (optional) |  | everyone | Submitted device details, visible only to the report author. |
| `device_details.platform` | string (optional) |  | everyone | Target platform, preserving future values. |
| `device_details.app_version` | string (optional) |  | everyone | Submitted application version, visible only under feedback access rules. |
| `device_details.os_version` | string (optional) |  | everyone | Submitted operating-system version, visible only under feedback access rules. |
| `device_details.device_model` | string (optional) |  | everyone | Submitted device model, visible only under feedback access rules. |
| `attachments` | array |  | everyone | Attachments authorized for this caller. |
| `attachments[].id` | string |  | everyone | Opaque identifier of this record. |
| `attachments[].status` | string |  | everyone | Attachment processing status, preserving future values. |
| `attachments[].content_type` | string |  | everyone | Stored attachment media type. |
| `attachments[].width` | number (optional) |  | everyone | Image width in pixels when available. |
| `attachments[].height` | number (optional) |  | everyone | Image height in pixels when available. |
| `attachments[].download_url` | string (optional) |  | everyone | Short-lived attachment URL authorized for this caller. |
| `attachments[].download_url_expires_at` | string (optional) |  | everyone | Expiry timestamp of the authorized attachment URL. |
| `created_at` | string |  | everyone | Creation timestamp. |
| `updated_at` | string |  | everyone | Last update timestamp. |
## FeedbackComment

Customer-visible comment with privacy-filtered author and authorized attachments.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `id` | string |  | everyone | Opaque identifier of this record. |
| `body` | string\|null |  | everyone | Customer-visible text; null for a deleted comment. |
| `author` | object |  | everyone | Privacy-filtered public author identity. |
| `author.display_name` | string (optional) |  | everyone | Privacy-filtered first name, or Meter team for staff; omitted when unavailable. |
| `author.role` | string |  | everyone | Public role label, preserving future values. |
| `author.is_viewer` | boolean |  | everyone | Whether this author is the verified caller. |
| `created_at` | string |  | everyone | Creation timestamp. |
| `updated_at` | string |  | everyone | Last update timestamp. |
| `edited_at` | string (optional) |  | everyone | Comment edit timestamp when supplied. |
| `deleted_at` | string (optional) |  | everyone | Comment deletion timestamp when supplied. |
| `attachments` | array |  | everyone | Attachments authorized for this caller. |
| `attachments[].id` | string |  | everyone | Opaque identifier of this record. |
| `attachments[].status` | string |  | everyone | Attachment processing status, preserving future values. |
| `attachments[].content_type` | string |  | everyone | Stored attachment media type. |
| `attachments[].width` | number (optional) |  | everyone | Image width in pixels when available. |
| `attachments[].height` | number (optional) |  | everyone | Image height in pixels when available. |
| `attachments[].download_url` | string (optional) |  | everyone | Short-lived attachment URL authorized for this caller. |
| `attachments[].download_url_expires_at` | string (optional) |  | everyone | Expiry timestamp of the authorized attachment URL. |
## FeedbackStatusEvent

Customer-visible feedback history event, without internal evidence or staff notes.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `id` | string |  | everyone | Opaque identifier of this record. |
| `type` | string |  | everyone | Record kind, preserving future values. |
| `from_status` | string (optional) |  | everyone | Previous status id when supplied. |
| `to_status` | string (optional) |  | everyone | New status id when supplied. |
| `public_note` | string (optional) |  | everyone | Customer-visible status note when supplied. |
| `platform` | string (optional) |  | everyone | Target platform, preserving future values. |
| `created_at` | string |  | everyone | Creation timestamp. |
## FeedbackAvailability

Verified availability for one target platform.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `platform` | string |  | everyone | Target platform, preserving future values. |
| `state` | string |  | everyone | Availability or attachment state, preserving future values. |
| `fixed_in_version` | string (optional) |  | everyone | Verified release version when supplied. |
| `available_at` | string (optional) |  | everyone | Release availability timestamp when supplied. |
## FeedbackAttachment

Authorized attachment metadata and any short-lived download address.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `id` | string |  | everyone | Opaque identifier of this record. |
| `status` | string |  | everyone | Attachment processing status, preserving future values. |
| `content_type` | string |  | everyone | Stored attachment media type. |
| `width` | number (optional) |  | everyone | Image width in pixels when available. |
| `height` | number (optional) |  | everyone | Image height in pixels when available. |
| `download_url` | string (optional) |  | everyone | Short-lived attachment URL authorized for this caller. |
| `download_url_expires_at` | string (optional) |  | everyone | Expiry timestamp of the authorized attachment URL. |
## BookingBlock

One dated block or indefinite pause on a booking calendar.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `id` | string |  | everyone | Block ID for editing or removing the block. |
| `starts_at` | string |  | everyone | Start instant with timezone offset. |
| `ends_at` | string\|null |  | everyone | Exclusive end instant, or null when bookings are paused indefinitely. |
| `all_day` | boolean |  | everyone | Whether the block spans full days in its timezone. |
| `timezone` | string |  | everyone | IANA timezone the block was entered in. |
| `note` | string\|null |  | everyone | Private calendar note. |
## BookingBlockList

Booking blocks on the selected calendar.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `blocks` | array |  | everyone | Blocks intersecting the requested date range. |
| `blocks[].id` | string |  | everyone | Block ID for editing or removing the block. |
| `blocks[].starts_at` | string |  | everyone | Start instant with timezone offset. |
| `blocks[].ends_at` | string\|null |  | everyone | Exclusive end instant, or null when bookings are paused indefinitely. |
| `blocks[].all_day` | boolean |  | everyone | Whether the block spans full days in its timezone. |
| `blocks[].timezone` | string |  | everyone | IANA timezone the block was entered in. |
| `blocks[].note` | string\|null |  | everyone | Private calendar note. |
| `has_more` | boolean |  | everyone | Whether a narrower date range is needed to see all results. |
## BookingBlockWrite

Result of saving or removing a booking block.

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
| `block` | object |  | everyone | One dated block or indefinite pause on a booking calendar. |
| `block.id` | string |  | everyone | Block ID for editing or removing the block. |
| `block.starts_at` | string |  | everyone | Start instant with timezone offset. |
| `block.ends_at` | string\|null |  | everyone | Exclusive end instant, or null when bookings are paused indefinitely. |
| `block.all_day` | boolean |  | everyone | Whether the block spans full days in its timezone. |
| `block.timezone` | string |  | everyone | IANA timezone the block was entered in. |
| `block.note` | string\|null |  | everyone | Private calendar note. |
## DriverSite

The signed-in driver's website.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `site` | object\|null |  | everyone | The driver's site, or null before it is created. |
| `site.slug` | string |  | everyone | The current address segment under meterapp.co/drivers. |
| `site.url` | string |  | everyone | The driver's public website URL. |
| `site.business_name` | string\|null |  | everyone | Public business name, or null to show the driver's name. |
| `site.bio` | string\|null |  | everyone | Public website biography. |
| `site.service_area` | string\|null |  | everyone | Public service area description. |
| `site.primary_color` | string\|null |  | everyone | Public accent color, or null to use the default. |
| `site.show_phone` | boolean |  | everyone | Whether the driver permits showing their phone on their website. |
## DriverSiteSettings

The signed-in driver's public website settings.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `slug` | string |  | everyone | The current address segment under meterapp.co/drivers. |
| `url` | string |  | everyone | The driver's public website URL. |
| `business_name` | string\|null |  | everyone | Public business name, or null to show the driver's name. |
| `bio` | string\|null |  | everyone | Public website biography. |
| `service_area` | string\|null |  | everyone | Public service area description. |
| `primary_color` | string\|null |  | everyone | Public accent color, or null to use the default. |
| `show_phone` | boolean |  | everyone | Whether the driver permits showing their phone on their website. |
## DriverSiteSettingsWrite

Result of changing the driver's website settings.

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
| `site` | object |  | everyone | The signed-in driver's public website settings. |
| `site.slug` | string |  | everyone | The current address segment under meterapp.co/drivers. |
| `site.url` | string |  | everyone | The driver's public website URL. |
| `site.business_name` | string\|null |  | everyone | Public business name, or null to show the driver's name. |
| `site.bio` | string\|null |  | everyone | Public website biography. |
| `site.service_area` | string\|null |  | everyone | Public service area description. |
| `site.primary_color` | string\|null |  | everyone | Public accent color, or null to use the default. |
| `site.show_phone` | boolean |  | everyone | Whether the driver permits showing their phone on their website. |
## PersonalBookingSettings

The signed-in driver's personal booking policy.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `booking_fare_id` | string\|null |  | everyone | Point-to-point fare, or null when disabled. |
| `time_booking_fare_id` | string\|null |  | everyone | Hourly fare, or null when disabled. |
| `payment_mode` | enum |  | everyone | When riders pay for new bookings. Values: `payments_optional`, `pre_payment_required`. |
| `min_lead_time_seconds` | number |  | everyone | Minimum notice for a pickup, in seconds. |
| `time_slot_minutes` | number\|null |  | everyone | Hourly booking slot size in minutes. |
| `minimum_duration_minutes` | number\|null |  | everyone | Minimum hourly booking duration in minutes. |
| `cancellation_grace_period_seconds` | number |  | everyone | Free cancellation window, in seconds. |
| `cancellation_fee_fraction` | number |  | everyone | Cancellation fee as a fraction of the fare. |
| `cancellation_fee_minimum_unit_amount` | number |  | everyone | Cancellation fee minimum in the selected fare's currency minor units. |
| `individual_passenger_capacity` | number |  | everyone | Maximum passengers for the personal booking page. |
| `availability` | array |  | everyone | Weekly personal booking hours. |
| `availability[].day` | enum |  | everyone | Day of the week in fleet timezone. Values: `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`, `sunday`. |
| `availability[].enabled` | boolean |  | everyone | Whether riders may book on this day. |
| `availability[].start_time` | string |  | everyone | Opening time, HH:mm in fleet timezone. |
| `availability[].end_time` | string |  | everyone | Closing time, HH:mm. Earlier than opening means overnight. |
| `availability_timezone` | string\|null |  | everyone | IANA timezone for personal booking hours. |
| `booking_buffer_minutes` | number |  | everyone | Extra minutes between bookings. |
| `travel_time_buffer_enabled` | boolean |  | everyone | Whether travel time is added to the booking buffer. |
## PersonalBookingSettingsWrite

Result of changing personal booking settings.

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
| `booking_settings` | object |  | everyone | The signed-in driver's personal booking policy. |
| `booking_settings.booking_fare_id` | string\|null |  | everyone | Point-to-point fare, or null when disabled. |
| `booking_settings.time_booking_fare_id` | string\|null |  | everyone | Hourly fare, or null when disabled. |
| `booking_settings.payment_mode` | enum |  | everyone | When riders pay for new bookings. Values: `payments_optional`, `pre_payment_required`. |
| `booking_settings.min_lead_time_seconds` | number |  | everyone | Minimum notice for a pickup, in seconds. |
| `booking_settings.time_slot_minutes` | number\|null |  | everyone | Hourly booking slot size in minutes. |
| `booking_settings.minimum_duration_minutes` | number\|null |  | everyone | Minimum hourly booking duration in minutes. |
| `booking_settings.cancellation_grace_period_seconds` | number |  | everyone | Free cancellation window, in seconds. |
| `booking_settings.cancellation_fee_fraction` | number |  | everyone | Cancellation fee as a fraction of the fare. |
| `booking_settings.cancellation_fee_minimum_unit_amount` | number |  | everyone | Cancellation fee minimum in the selected fare's currency minor units. |
| `booking_settings.individual_passenger_capacity` | number |  | everyone | Maximum passengers for the personal booking page. |
| `booking_settings.availability` | array |  | everyone | Weekly personal booking hours. |
| `booking_settings.availability[].day` | enum |  | everyone | Day of the week in fleet timezone. Values: `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`, `sunday`. |
| `booking_settings.availability[].enabled` | boolean |  | everyone | Whether riders may book on this day. |
| `booking_settings.availability[].start_time` | string |  | everyone | Opening time, HH:mm in fleet timezone. |
| `booking_settings.availability[].end_time` | string |  | everyone | Closing time, HH:mm. Earlier than opening means overnight. |
| `booking_settings.availability_timezone` | string\|null |  | everyone | IANA timezone for personal booking hours. |
| `booking_settings.booking_buffer_minutes` | number |  | everyone | Extra minutes between bookings. |
| `booking_settings.travel_time_buffer_enabled` | boolean |  | everyone | Whether travel time is added to the booking buffer. |
## NotificationPreference

A notification preference for the signed-in account.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `category_key` | string |  | everyone | Category identifier to use when changing this preference. |
| `display_name` | string |  | everyone | Name of the notification category. |
| `channel` | enum |  | everyone | Delivery channel. Values: `email`, `sms`, `whatsapp`, `push`. |
| `enabled` | boolean |  | everyone | Whether notifications are enabled for this category and channel. |
| `forced_on` | boolean |  | everyone | Whether the account role requires this channel to stay enabled. |
| `quiet_hours` | object\|null |  | everyone | Delivery quiet hours, or null when unset. |
| `quiet_hours.start` | string |  | everyone | Start in local 24-hour time. |
| `quiet_hours.end` | string |  | everyone | End in local 24-hour time. May be the next day. |
| `quiet_hours.timezone` | string |  | everyone | IANA timezone for the quiet hours. |
## NotificationPreferences

Notification preferences for the signed-in account.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `preferences` | array |  | everyone | Matching preferences for the signed-in account. |
| `preferences[].category_key` | string |  | everyone | Category identifier to use when changing this preference. |
| `preferences[].display_name` | string |  | everyone | Name of the notification category. |
| `preferences[].channel` | enum |  | everyone | Delivery channel. Values: `email`, `sms`, `whatsapp`, `push`. |
| `preferences[].enabled` | boolean |  | everyone | Whether notifications are enabled for this category and channel. |
| `preferences[].forced_on` | boolean |  | everyone | Whether the account role requires this channel to stay enabled. |
| `preferences[].quiet_hours` | object\|null |  | everyone | Delivery quiet hours, or null when unset. |
| `preferences[].quiet_hours.start` | string |  | everyone | Start in local 24-hour time. |
| `preferences[].quiet_hours.end` | string |  | everyone | End in local 24-hour time. May be the next day. |
| `preferences[].quiet_hours.timezone` | string |  | everyone | IANA timezone for the quiet hours. |
## NotificationPreferenceWrite

Result of changing one personal notification preference.

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
| `preference` | object |  | everyone | A notification preference for the signed-in account. |
| `preference.category_key` | string |  | everyone | Category identifier to use when changing this preference. |
| `preference.display_name` | string |  | everyone | Name of the notification category. |
| `preference.channel` | enum |  | everyone | Delivery channel. Values: `email`, `sms`, `whatsapp`, `push`. |
| `preference.enabled` | boolean |  | everyone | Whether notifications are enabled for this category and channel. |
| `preference.forced_on` | boolean |  | everyone | Whether the account role requires this channel to stay enabled. |
| `preference.quiet_hours` | object\|null |  | everyone | Delivery quiet hours, or null when unset. |
| `preference.quiet_hours.start` | string |  | everyone | Start in local 24-hour time. |
| `preference.quiet_hours.end` | string |  | everyone | End in local 24-hour time. May be the next day. |
| `preference.quiet_hours.timezone` | string |  | everyone | IANA timezone for the quiet hours. |
## FleetSiteDomain

Custom domain settings for a fleet booking website.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string |  | everyone | Fleet ID. |
| `configured` | boolean |  | everyone | Whether Meter can connect a custom domain. |
| `domain` | object\|null |  | everyone | Current hostname and verification state, including the exact DNS records to enter at the provider. |
| `domain.hostname` | string |  | everyone | The public custom hostname. |
| `domain.source` | enum |  | everyone | Connected from an external provider or purchased in Meter. Values: `connected`, `purchased`. |
| `domain.status` | enum |  | everyone | Whether payment, DNS verification, or renewal is pending, or the hostname is active. Values: `pending_purchase`, `pending_dns`, `active`, `expired`. |
| `domain.pending_reason` | string\|null |  | everyone | The remaining ownership, DNS, or certificate check. |
| `domain.dns_records` | array |  | everyone | Records Meter needs to verify and serve the hostname. |
| `domain.dns_records[].type` | enum |  | everyone | DNS record type. Values: `A`, `CNAME`, `TXT`. |
| `domain.dns_records[].name` | string |  | everyone | Name to enter at the DNS provider. |
| `domain.dns_records[].value` | string |  | everyone | Exact value to enter for the record. |
| `domain.dns_records[].purpose` | enum |  | everyone | Routes traffic or proves ownership. Values: `routing`, `ownership`. |
| `domain.last_checked_at` | string\|null |  | everyone | Time of the last DNS check, if any. |
| `domain.expires_at` | string\|null |  | everyone | Registration expiry for a domain purchased in Meter. |
| `website_settings_url` | string |  | everyone | Meter console for domain purchases and renewals. Select the intended fleet there. |
