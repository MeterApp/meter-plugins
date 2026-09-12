---
name: meter-fleet-onboarding
description: Guide a new fleet owner through Meter fleet setup with the get_onboarding_checklist tool and the settings tools (update_fleet_settings, update_booking_settings, update_ride_option, assign_vehicle), always previewing with dry_run: true and confirming before applying, and knowing when to send them to the web onboarding at meterapp.co/fleet/onboarding instead. Use when someone has just created a fleet, asks what is left to set up, or wants help getting their fleet to its first booking; do not use for day-to-day questions about an established fleet (meter-fleet-insights) or isolated settings edits (meter-settings-changes).
---

# Onboarding a fleet with Meter

A fleet becomes operational when onboarding is complete and billing is active (`is_operational` in `whoami` and `list_fleets`). Until then, fleet-wide read tools return `fleet_not_operational`, but `get_onboarding_checklist` works on fleets that are still onboarding. This skill turns "what do I still need to do?" into a guided checklist that ends with the first booking.

## Start

1. `whoami`. Confirm the person is `owner` (or `admin`) of the fleet. Drivers cannot onboard a fleet; tell them to ask the owner.
2. `get_onboarding_checklist` with the `fleet_id`. It returns `items` (fleet profile, brand icon, service area, a ride option with a fare, booking settings, a vehicle, a driver, payouts connected as a yes/no, the shareable booking link, the first booking), each saying whether it is done, whether riders can book without it, and how to complete it: the MCP tool to call or the web page to send the human to. It also returns `required_remaining`, `booking_page_status` and the public booking URL. Treat it as the source of truth for what is missing; do not invent steps.
3. `get_fleet` for the current settings so you can quote them back before changing anything.

## Work through the checklist

For each incomplete item, in the order the checklist gives:

- Explain the item in one or two sentences in plain language (what it is, why the fleet needs it, whether riders can book without it).
- Ask for the values you need. Do not fill in defaults the human did not choose, especially fares, cancellation terms and lead times.
- Call the settings tool the item names with `dry_run: true` and only those fields. `dry_run` defaults to false, so never omit it on the preview call. Show the returned `changes` (each `field`, `from`, `to`) verbatim.
- Only after an explicit yes, repeat the identical call without `dry_run`. Confirm `applied: true`, then re-run `get_onboarding_checklist` and continue.

Never batch several items into one apply. One item, one confirmation.

## Send them to the web when

Some items cannot be completed through tools and the checklist says so: it names the page instead of a tool. Send the person to `https://www.meterapp.co/fleet/onboarding` (signed in with the same account) for:

- Billing and subscription (payment method, plan) and connecting payouts (the checklist only reports connected yes/no)
- Uploading the brand icon
- Creating ride options (the tools edit existing ones) and adding vehicles or inviting drivers
- Anything involving documents, identity verification or phone number verification

Say exactly which item needs the web and why; do not attempt a workaround through unrelated tools.

## Fares and ride options

`update_ride_option` edits an existing ride option and the rates of its default fare (in major currency units as shown in the console). Changing a fare is a money decision: state `from` and `to` for the base fare, minimum fare, per-distance and per-minute rates with the currency, and require an explicit yes. If the fleet has an official tariff, prefer it; do not guess market rates.

## Vehicles and drivers

- `list_vehicles` shows the fleet's cars; `assign_vehicle` (dry run first) links a vehicle to a driver from `list_fleet_members`, replacing whoever drives it today, or unassigns with `member_id: null`.
- A fleet needs at least one driver besides the owner to dispatch. Drivers join from the app or the web join link; you cannot add them through tools.

## Finish

When `required_remaining` is empty and `booking_page_status` says riders can book, share the booking URL from the checklist, summarize what was set up (with the final values), and suggest the first insight: `list_bookings` for upcoming rides or `get_fleet` to review settings.

## References

- [Tool catalog](../../references/tools.md) (generated)
- [Data model](../../references/data-model.md) (generated; `OnboardingChecklist`)
- [Safety](../../references/safety.md)
