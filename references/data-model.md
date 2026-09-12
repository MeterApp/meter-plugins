# Meter data model (public DTOs)

Generated from the `@meterapp/meter-sdk` DTO schemas; do not edit by hand. Every tool result is validated against one of these objects before it leaves the server, so a field that is not listed here is never returned. Money is in minor currency units (`*_minor`), distances in meters, durations in seconds, timestamps ISO 8601. `Visible to` narrows a field to certain viewers; everyone else gets null or no field.

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

Result of get_fleet. Drivers get public info; owners/admins also get settings.

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
| `booking_settings.cancellation_fee_fraction` | number |  | everyone | Cancellation fee as a fraction of the fare (0-1). |
| `booking_settings.cancellation_grace_period_seconds` | number | seconds | everyone | Free-cancellation window after booking. |
| `booking_settings.individual_passenger_capacity` | number |  | everyone | Default passenger capacity for individual bookings. |
| `admin_settings` | object\|null |  | owner, admin | Operational settings; null for drivers. |
| `admin_settings.default_driver_payout_fraction` | number\|null |  | everyone | Default share of each fare paid to the driver (0-1), or null when payouts are not configured. |
| `admin_settings.allow_fleet_custom_fares` | boolean |  | everyone | Whether drivers may use custom fares. |
| `admin_settings.show_driver_locations` | boolean |  | everyone | Whether riders see live driver locations on the public booking page. |
| `admin_settings.trip_collection_mode` | string\|null |  | everyone | How trip payments are collected (stored enum), or null. |
| `admin_settings.tip_split_behavior` | string\|null |  | everyone | How tips are split between fleet and driver (stored enum), or null. |
| `admin_settings.pass_credit_card_fees_to_customer` | boolean\|null |  | everyone | Whether card fees are added to the rider total. |

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
| `tip_minor` | number\|null | minor currency units | everyone | Tip included in the total, or null. |
| `fee_count` | number |  | everyone | Number of fees applied (tolls, airport fees, ...). |
| `discount_count` | number |  | everyone | Number of discounts applied. |
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
| `items[].tip_minor` | number\|null | minor currency units | everyone | Tip included in the total, or null. |
| `items[].fee_count` | number |  | everyone | Number of fees applied (tolls, airport fees, ...). |
| `items[].discount_count` | number |  | everyone | Number of discounts applied. |
| `items[].is_paid` | boolean |  | everyone | Whether the trip is marked paid. |
| `items[].payment_method` | string\|null |  | everyone | How the trip was paid: cash, card (Meter Pay), other, or null when not recorded. |
| `items[].void_status` | enum\|null |  | everyone | Set when the driver asked to void the trip (void_requested) or an admin voided it (voided). Values: `void_requested`, `voided`. |
| `items[].created_at` | string | ISO 8601 | everyone | When the trip was uploaded to Meter. |
| `next_cursor` | string\|null |  | everyone | Pass this back as `cursor` to fetch the next page. Null when there are no more results. |
| `has_more` | boolean |  | everyone | True when another page exists. |

## Booking

A booking (scheduled ride). No payment-provider ids, internal snapshots or dispatch internals.

| Field | Type | Unit | Visible to | Description |
| --- | --- | --- | --- | --- |
| `booking_id` | string |  | everyone | Opaque booking id (a scheduled ride). |
| `fleet_id` | string\|null |  | everyone | Fleet the ride was booked with, or null for a solo driver booking. |
| `status` | enum |  | everyone | Booking lifecycle: pending (awaiting a driver), confirmed (driver assigned), in_progress, completed, canceled, pending_payment (rider must pay before it is dispatched). Values: `pending`, `confirmed`, `in_progress`, `completed`, `canceled`, `pending_payment`. |
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
| `dispatch_mode` | enum |  | everyone | How new bookings reach drivers: NONE (dispatcher assigns manually), ALL_ONLINE_DRIVERS (offered to every online driver), AUTO_DISPATCH (nearest available driver). Values: `NONE`, `ALL_ONLINE_DRIVERS`, `AUTO_DISPATCH`. |
| `payment_mode` | enum |  | everyone | disabled: no card payments on bookings; payments_optional: riders may add a card; pre_payment_required: riders must authorize payment before dispatch. Values: `disabled`, `payments_optional`, `pre_payment_required`. |
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
| `applied` | boolean |  | everyone | True when the change was written. False on a dry run or when nothing differed from the current values. |
| `dry_run` | boolean |  | everyone | True when the call was a preview: values were validated and authorized but nothing was written. |
| `changes` | array |  | everyone | Field-level changes (empty when every requested value already matched). Summarize these back to the human. |
| `changes[].field` | string |  | everyone | Name of the changed argument, exactly as passed to the tool (e.g. "contact_phone", "fare.base"). |
| `changes[].from` | string\|number\|boolean\|null\|array\|array |  | everyone | Value before the change. |
| `changes[].to` | string\|number\|boolean\|null\|array\|array |  | everyone | Value after the change. |
| `booking_settings` | object\|null |  | everyone | The booking settings after the call. Null only on a dry run for a fleet that has no booking settings yet; the real call creates them. |
| `booking_settings.fleet_id` | string |  | everyone | The fleet these settings belong to. |
| `booking_settings.dispatch_mode` | enum |  | everyone | How new bookings reach drivers: NONE (dispatcher assigns manually), ALL_ONLINE_DRIVERS (offered to every online driver), AUTO_DISPATCH (nearest available driver). Values: `NONE`, `ALL_ONLINE_DRIVERS`, `AUTO_DISPATCH`. |
| `booking_settings.payment_mode` | enum |  | everyone | disabled: no card payments on bookings; payments_optional: riders may add a card; pre_payment_required: riders must authorize payment before dispatch. Values: `disabled`, `payments_optional`, `pre_payment_required`. |
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
