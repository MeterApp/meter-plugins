# Meter data-model reference

Generated from the `@meterapp/meter-sdk` catalog and DTO schemas; do not edit by hand. See the [reference index](../data-model.md) for all definitions.

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
| `required_remaining` | array |  | everyone | Ids of required items still open, in recommended order. |
| `items` | array |  | everyone | Checklist items in recommended order. |
| `items[].key` | enum |  | everyone | Stable identifier of the setup step. Values: `fleet_profile`, `brand_icon`, `service_area`, `ride_option_with_fare`, `booking_settings`, `vehicle`, `driver`, `payouts_connected`, `booking_link`, `first_booking`. |
| `items[].title` | string |  | everyone | Short human title of the step. |
| `items[].done` | boolean |  | everyone | True when the step is complete. |
| `items[].required` | boolean |  | everyone | True when riders cannot book until this step is done. |
| `items[].how_to` | string |  | everyone | What to do next: the MCP tool that completes the step when one exists, otherwise the web page. |
| `items[].tool` | string\|null |  | everyone | Name of the MCP tool that completes this step, or null when it needs the web console. |
| `items[].url` | string\|null |  | everyone | Absolute web URL where a human completes the step, or null. |
