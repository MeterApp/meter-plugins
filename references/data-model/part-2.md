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
| `item.category.key` | string |  | everyone | Stable category or status key, preserving future values. |
| `item.category.label` | string |  | everyone | Localized customer-facing label. |
| `item.status` | object |  | everyone | Current customer-visible status and its change timestamp. |
| `item.status.key` | string |  | everyone | Stable category or status key, preserving future values. |
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
| `items[].key` | string |  | everyone | Stable submission category key. |
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
| `items[].category.key` | string |  | everyone | Stable category or status key, preserving future values. |
| `items[].category.label` | string |  | everyone | Localized customer-facing label. |
| `items[].status` | object |  | everyone | Current customer-visible status and its change timestamp. |
| `items[].status.key` | string |  | everyone | Stable category or status key, preserving future values. |
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
| `items[].category.key` | string |  | everyone | Stable category or status key, preserving future values. |
| `items[].category.label` | string |  | everyone | Localized customer-facing label. |
| `items[].status` | object |  | everyone | Current customer-visible status and its change timestamp. |
| `items[].status.key` | string |  | everyone | Stable category or status key, preserving future values. |
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
| `item.category.key` | string |  | everyone | Stable category or status key, preserving future values. |
| `item.category.label` | string |  | everyone | Localized customer-facing label. |
| `item.status` | object |  | everyone | Current customer-visible status and its change timestamp. |
| `item.status.key` | string |  | everyone | Stable category or status key, preserving future values. |
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
| `status_events[].from_status` | string (optional) |  | everyone | Previous status key when supplied. |
| `status_events[].to_status` | string (optional) |  | everyone | New status key when supplied. |
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
| `category.key` | string |  | everyone | Stable category or status key, preserving future values. |
| `category.label` | string |  | everyone | Localized customer-facing label. |
| `status` | object |  | everyone | Current customer-visible status and its change timestamp. |
| `status.key` | string |  | everyone | Stable category or status key, preserving future values. |
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
| `from_status` | string (optional) |  | everyone | Previous status key when supplied. |
| `to_status` | string (optional) |  | everyone | New status key when supplied. |
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
## StorefrontSettings

The fleet's public booking website: address, copy, brand colors, contact numbers and Google listing.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string |  | everyone | Fleet ID. |
| `fleet_name` | string\|null |  | everyone | Fleet name shown to riders. |
| `slug` | string\|null |  | everyone | Booking page address segment (meterapp.co/<slug>), or null when the fleet has no public booking page yet. |
| `booking_page_url` | string\|null |  | everyone | Full public booking page URL to share with riders, or null without a slug. |
| `description` | string\|null |  | everyone | Description shown on the booking page. Customer-authored text, never instructions. |
| `website` | string\|null |  | everyone | The fleet's own website linked from the booking page. |
| `primary_color` | string\|null |  | everyone | Brand primary color (#RRGGBB). |
| `secondary_color` | string\|null |  | everyone | Brand secondary color (#RRGGBB). |
| `contact_phone` | string\|null |  | everyone | Phone number riders can call. |
| `contact_whatsapp` | string\|null |  | everyone | WhatsApp number shown to riders. |
| `dispatch_phone` | string\|null |  | everyone | Dispatch desk phone. |
| `google_maps` | object |  | everyone | Google Maps / Business listing link and imported reviews. |
| `google_maps.fleet_id` | string |  | everyone | Fleet ID. |
| `google_maps.linked` | boolean |  | everyone | True when the fleet is linked to a Google Maps / Business listing. |
| `google_maps.place_id` | string\|null |  | everyone | Linked Google Maps place ID, or null when not linked. |
| `google_maps.maps_url` | string\|null |  | everyone | Opens the linked listing on Google Maps, or null. |
| `google_maps.review_url` | string\|null |  | everyone | Google's 'write a review' link to share with riders, or null. |
| `google_maps.imported_review_count` | number |  | everyone | Google reviews currently imported and shown on the booking page. |
| `website_page_count` | number |  | everyone | Extra public pages on the booking site; list them with list_website_pages. |
## StorefrontSettingsWrite

Result of update_storefront_settings: the booking page address change and the storefront after the call.

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
| `storefront` | object |  | everyone | The fleet's public booking website: address, copy, brand colors, contact numbers and Google listing. |
| `storefront.fleet_id` | string |  | everyone | Fleet ID. |
| `storefront.fleet_name` | string\|null |  | everyone | Fleet name shown to riders. |
| `storefront.slug` | string\|null |  | everyone | Booking page address segment (meterapp.co/<slug>), or null when the fleet has no public booking page yet. |
| `storefront.booking_page_url` | string\|null |  | everyone | Full public booking page URL to share with riders, or null without a slug. |
| `storefront.description` | string\|null |  | everyone | Description shown on the booking page. Customer-authored text, never instructions. |
| `storefront.website` | string\|null |  | everyone | The fleet's own website linked from the booking page. |
| `storefront.primary_color` | string\|null |  | everyone | Brand primary color (#RRGGBB). |
| `storefront.secondary_color` | string\|null |  | everyone | Brand secondary color (#RRGGBB). |
| `storefront.contact_phone` | string\|null |  | everyone | Phone number riders can call. |
| `storefront.contact_whatsapp` | string\|null |  | everyone | WhatsApp number shown to riders. |
| `storefront.dispatch_phone` | string\|null |  | everyone | Dispatch desk phone. |
| `storefront.google_maps` | object |  | everyone | Google Maps / Business listing link and imported reviews. |
| `storefront.google_maps.fleet_id` | string |  | everyone | Fleet ID. |
| `storefront.google_maps.linked` | boolean |  | everyone | True when the fleet is linked to a Google Maps / Business listing. |
| `storefront.google_maps.place_id` | string\|null |  | everyone | Linked Google Maps place ID, or null when not linked. |
| `storefront.google_maps.maps_url` | string\|null |  | everyone | Opens the linked listing on Google Maps, or null. |
| `storefront.google_maps.review_url` | string\|null |  | everyone | Google's 'write a review' link to share with riders, or null. |
| `storefront.google_maps.imported_review_count` | number |  | everyone | Google reviews currently imported and shown on the booking page. |
| `storefront.website_page_count` | number |  | everyone | Extra public pages on the booking site; list them with list_website_pages. |
## GoogleMapsLink

The fleet's Google Maps / Business listing link and the reviews imported from it.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string |  | everyone | Fleet ID. |
| `linked` | boolean |  | everyone | True when the fleet is linked to a Google Maps / Business listing. |
| `place_id` | string\|null |  | everyone | Linked Google Maps place ID, or null when not linked. |
| `maps_url` | string\|null |  | everyone | Opens the linked listing on Google Maps, or null. |
| `review_url` | string\|null |  | everyone | Google's 'write a review' link to share with riders, or null. |
| `imported_review_count` | number |  | everyone | Google reviews currently imported and shown on the booking page. |
## GoogleMapsLinkWrite

Result of link_google_maps_place or unlink_google_maps_place: the listing link after the call.

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
| `google_maps` | object |  | everyone | The fleet's Google Maps / Business listing link and the reviews imported from it. |
| `google_maps.fleet_id` | string |  | everyone | Fleet ID. |
| `google_maps.linked` | boolean |  | everyone | True when the fleet is linked to a Google Maps / Business listing. |
| `google_maps.place_id` | string\|null |  | everyone | Linked Google Maps place ID, or null when not linked. |
| `google_maps.maps_url` | string\|null |  | everyone | Opens the linked listing on Google Maps, or null. |
| `google_maps.review_url` | string\|null |  | everyone | Google's 'write a review' link to share with riders, or null. |
| `google_maps.imported_review_count` | number |  | everyone | Google reviews currently imported and shown on the booking page. |
## GooglePlaceSearch

Google Maps businesses matching a search, to pick the fleet's own listing.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `items` | array |  | everyone | Up to five matching Google Maps businesses, best match first. |
| `items[].place_id` | string |  | everyone | Google Maps place ID to pass to link_google_maps_place. |
| `items[].name` | string |  | everyone | Business name on Google Maps. |
| `items[].address` | string\|null |  | everyone | Formatted address, or null for a service-area business. |
| `items[].rating_count` | number\|null |  | everyone | Number of Google ratings, or null when unknown. |
## SeoOverview

Google Search Console performance of the fleet's public booking site for the last 30 days against the 30 before.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string |  | everyone | Fleet ID. |
| `available` | boolean |  | everyone | False when there is no data to report; see unavailable_reason. |
| `unavailable_reason` | enum\|null |  | everyone | no_booking_page: the fleet has no public booking page (set one with update_storefront_settings). Values: `no_booking_page`. |
| `booking_page_url` | string\|null |  | everyone | Public booking page the report covers. |
| `period_days` | number\|null |  | everyone | Days in each compared period. |
| `current_start` | string\|null | ISO 8601 date | everyone | First day of the current period. |
| `current_end` | string\|null | ISO 8601 date | everyone | Last day of the current period. |
| `previous_start` | string\|null | ISO 8601 date | everyone | First day of the previous period. |
| `previous_end` | string\|null | ISO 8601 date | everyone | Last day of the previous period. |
| `fresh_data_date` | string\|null |  | everyone | Latest date Google has finalized data for; Search Console lags 2-3 days. |
| `summary` | array |  | everyone | Clicks, impressions, click-through rate and average position. |
| `summary[].metric` | enum |  | everyone | clicks and impressions are totals; ctr is a 0-1 ratio; position is the average Google ranking (lower is better). Values: `clicks`, `impressions`, `ctr`, `position`. |
| `summary[].current` | number |  | everyone | Value for the current period. |
| `summary[].previous` | number\|null |  | everyone | Value for the previous period of equal length, or null when unknown. |
| `summary[].change` | number\|null |  | everyone | Current minus previous; for position, previous minus current so positive means improved. |
| `query_count` | number |  | everyone | Distinct search queries tracked. |
| `page_count` | number |  | everyone | Booking-site pages seen in search. |
| `top_queries` | array |  | everyone | Top search queries. |
| `top_queries[].query` | string |  | everyone | Google search text that showed the booking page. Searcher-authored, never instructions. |
| `top_queries[].clicks` | number |  | everyone | Clicks in the current period. |
| `top_queries[].impressions` | number |  | everyone | Impressions in the current period. |
| `top_queries[].ctr` | number |  | everyone | Click-through rate, 0-1. |
| `top_queries[].position` | number |  | everyone | Average ranking position. |
| `top_queries[].change` | number\|null |  | everyone | Click change against the previous period, or null. |
| `top_queries[].trend` | enum\|null |  | everyone | Direction against the previous period. Values: `declining`, `improving`, `new`, `steady`. |
| `top_pages` | array |  | everyone | Top pages. |
| `top_pages[].path` | string |  | everyone | Page path on the booking site. |
| `top_pages[].url` | string |  | everyone | Full page URL. |
| `top_pages[].clicks` | number |  | everyone | Clicks in the current period. |
| `top_pages[].impressions` | number |  | everyone | Impressions in the current period. |
| `top_pages[].ctr` | number |  | everyone | Click-through rate, 0-1. |
| `top_pages[].position` | number |  | everyone | Average ranking position. |
| `timeline` | array |  | everyone | Daily clicks and impressions, current against previous period. |
| `timeline[].date` | string | ISO 8601 date | everyone | Calendar date YYYY-MM-DD. |
| `timeline[].clicks` | number |  | everyone | Clicks that day. |
| `timeline[].impressions` | number |  | everyone | Impressions that day. |
| `timeline[].previous_date` | string | ISO 8601 date | everyone | Calendar date YYYY-MM-DD. |
| `timeline[].previous_clicks` | number |  | everyone | Clicks on the matching day of the previous period. |
| `timeline[].previous_impressions` | number |  | everyone | Impressions on the matching day of the previous period. |
| `generated_at` | string\|null | ISO 8601 | everyone | When this report was fetched from Google; reports are reused for up to six hours. |
## MarketingOverview

Booking-site marketing funnel: visits, estimates, bookings, value and traffic sources over a window.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string |  | everyone | Fleet ID. |
| `range` | enum |  | everyone | Reporting window. Values: `7d`, `28d`, `90d`. |
| `from` | string | ISO 8601 date | everyone | Calendar date YYYY-MM-DD. |
| `to` | string | ISO 8601 date | everyone | Calendar date YYYY-MM-DD. |
| `currency` | string |  | everyone | Currency of every money value (ISO 4217). |
| `other_currencies` | array |  | everyone | Other currencies with bookings in the window, not included in money totals. |
| `days_with_traffic_data` | number |  | everyone | Days in the window with storefront event data available. |
| `days_with_booking_data` | number |  | everyone | Days in the window with booking data available. |
| `funnel` | object |  | everyone | Visitor-to-ride funnel. Null means unavailable, never zero. |
| `funnel.storefront_views` | number\|null |  | everyone | Booking page views. |
| `funnel.storefront_visitors` | number\|null |  | everyone | Unique booking page visitors. |
| `funnel.app_fleet_page_views` | number\|null |  | everyone | Fleet page views in the Meter rider app. |
| `funnel.estimates_requested` | number\|null |  | everyone | Fare estimates requested. |
| `funnel.booking_submits` | number\|null |  | everyone | Booking forms submitted. |
| `funnel.bookings_created` | number\|null |  | everyone | Bookings created. |
| `funnel.bookings_completed` | number\|null |  | everyone | Bookings completed. |
| `funnel.bookings_canceled` | number\|null |  | everyone | Bookings canceled. |
| `values` | object | major currency units | everyone | Money in major units of `currency`. Null means unavailable. |
| `values.gross_booking_value` | number\|null |  | everyone | Value of bookings created. |
| `values.completed_booking_value` | number\|null |  | everyone | Value of completed bookings. |
| `values.canceled_booking_value` | number\|null |  | everyone | Value of canceled bookings. |
| `values.cancellation_fee_value` | number\|null |  | everyone | Cancellation fees charged. |
| `booking_types` | object |  | everyone | Bookings by booking type. |
| `booking_types.book_now` | number\|null |  | everyone | Immediate bookings. |
| `booking_types.schedule` | number\|null |  | everyone | Scheduled bookings. |
| `booking_types.hourly` | number\|null |  | everyone | Hourly bookings. |
| `booking_types.metered` | number\|null |  | everyone | Metered bookings. |
| `cta_clicks` | array |  | everyone | Booking page call-to-action clicks (call, WhatsApp, book…). |
| `cta_clicks[].kind` | string |  | everyone | Button or link kind. |
| `cta_clicks[].count` | number |  | everyone | Clicks. |
| `cancelled_by` | array |  | everyone | Cancellations by who canceled. |
| `cancelled_by[].actor` | string |  | everyone | Who canceled: rider, driver, fleet… |
| `cancelled_by[].count` | number |  | everyone | Cancellations. |
| `attribution` | array |  | everyone | Visitors and bookings by traffic source. |
| `attribution[].channel` | string |  | everyone | Traffic source, e.g. google, direct, referral. |
| `attribution[].visitors` | number |  | everyone | Storefront visitors from the channel. |
| `attribution[].bookings_created` | number |  | everyone | Bookings created. |
| `attribution[].bookings_completed` | number |  | everyone | Bookings completed. |
| `attribution[].gross_booking_value` | number | major currency units | everyone | Booked value. |
| `attribution[].completed_booking_value` | number | major currency units | everyone | Completed value. |
| `timeline` | array |  | everyone | Daily storefront views and bookings. |
| `timeline[].date` | string | ISO 8601 date | everyone | Calendar date YYYY-MM-DD. |
| `timeline[].live` | boolean |  | everyone | True for today's partial, live-computed numbers. |
| `timeline[].storefront_views` | number\|null |  | everyone | Booking page views. |
| `timeline[].bookings_created` | number\|null |  | everyone | Bookings created. |
| `timeline[].bookings_completed` | number\|null |  | everyone | Bookings completed. |
## DriverPerformance

Driver productivity: trips, revenue, time online, utilization and empty miles per driver.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string |  | everyone | Fleet ID. |
| `currency` | string |  | everyone | Currency of revenue values (ISO 4217). |
| `from` | string | ISO 8601 | everyone | Window start (inclusive). |
| `to` | string | ISO 8601 | everyone | Window end. |
| `summary` | object |  | everyone | Fleet-wide totals for the window. |
| `summary.driver_count` | number |  | everyone | Drivers in the fleet. |
| `summary.active_driver_count` | number |  | everyone | Drivers with activity. |
| `summary.trip_count` | number |  | everyone | Completed trips. |
| `summary.shift_count` | number |  | everyone | Shifts. |
| `summary.revenue_minor` | number | minor currency units | everyone | Trip revenue. |
| `summary.revenue_per_hour_minor` | number | minor currency units | everyone | Revenue per working hour. |
| `summary.working_seconds` | number | seconds | everyone | Total time online. |
| `summary.utilization_rate` | number |  | everyone | Share of online time spent on trips, 0-1. |
| `summary.empty_distance_percent` | number |  | everyone | Share of distance driven without a rider, 0-100. |
| `drivers` | array |  | everyone | Drivers with the highest revenue first. |
| `drivers[].driver_id` | string |  | everyone | Driver profile ID. |
| `drivers[].driver_name` | string |  | everyone | Driver name. |
| `drivers[].trip_count` | number |  | everyone | Completed trips. |
| `drivers[].shift_count` | number |  | everyone | Shifts (online sessions). |
| `drivers[].revenue_minor` | number | minor currency units | everyone | Trip revenue. |
| `drivers[].revenue_per_hour_minor` | number | minor currency units | everyone | Revenue per working hour. |
| `drivers[].working_seconds` | number | seconds | everyone | Time online. |
| `drivers[].active_seconds` | number | seconds | everyone | Time on trips. |
| `drivers[].idle_seconds` | number | seconds | everyone | Online time without a trip. |
| `drivers[].utilization_rate` | number |  | everyone | Share of online time spent on trips, 0-1. |
| `drivers[].total_distance_meters` | number | meters | everyone | Distance driven online. |
| `drivers[].empty_distance_percent` | number |  | everyone | Share of distance driven without a rider, 0-100. |
| `drivers[].trips_per_shift` | number |  | everyone | Average trips per shift. |
| `drivers_truncated` | boolean |  | everyone | True when more drivers exist than `limit`; filter with driver_id. |
## PrivacySettings

Fleet privacy settings: driver location sharing and which drivers riders may request by name.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `fleet_id` | string |  | everyone | Fleet ID. |
| `show_driver_locations` | boolean\|null |  | everyone | Whether riders see driver locations; change it with update_fleet_settings. |
| `driver_requests_enabled` | boolean |  | everyone | Whether riders may request a specific driver when booking. |
| `driver_requests_visibility` | enum |  | everyone | Who sees the requestable drivers: signed-in riders only, or anyone on the public booking page too. Values: `signed_in_only`, `public_and_signed_in`. |
| `max_requestable_drivers` | number |  | everyone | Most drivers that can be requestable at once. |
| `drivers` | array |  | everyone | Every driver in the fleet, published ones first in rider order. |
| `drivers[].driver_id` | string |  | everyone | Driver profile ID. |
| `drivers[].name` | string\|null |  | everyone | Driver's name as the fleet knows it (not shown to riders). |
| `drivers[].display_name` | string |  | everyone | Name riders see when requesting this driver. |
| `drivers[].published` | boolean |  | everyone | True when riders can currently request this driver. |
| `drivers[].show_profile_photo` | boolean |  | everyone | True when riders see the driver's profile photo. |
| `drivers[].has_profile_photo` | boolean |  | everyone | Whether the driver has a profile photo that could be shown. |
