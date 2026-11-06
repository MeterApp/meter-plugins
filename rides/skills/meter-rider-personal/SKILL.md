---
name: meter-rider-personal
description: "Help a Meter rider look back at their own rides through the Meter Rides MCP tools: past and upcoming bookings (list_bookings scope \"rider\", get_booking, get_booking_audit_log), quotes a company sent them (list_quotes scope \"rider\", get_quote, respond_to_quote), rating a finished ride (get_rating_prompt, rate_ride) and reporting a problem (report_ride_issue). Use when the signed-in person asks about \"my past rides\", \"what did I pay\", a quote or a ride that went wrong; do not use to book, follow or cancel a ride (meter-ride), or for a driver's trips and pay or a fleet's data (the Meter for Drivers & Fleets plugin)."
---

# A rider's own rides

This skill looks back: what the signed-in rider booked, what it cost, what happened to it. To book, follow or cancel a ride, use `meter-ride`.

## Start with `whoami`

Call it once. `is_rider: true` means the person has booked rides. `profile` is their own name, email and phone, never anyone else's.

## Rides and what happened to them

| Ask | Call |
| --- | --- |
| "My past rides" | `list_bookings` with `scope: "rider"` and `before` set to now; page with `cursor` |
| "My upcoming rides" | `list_bookings` with `scope: "rider"`, `after` set to now, `sort: "asc"` |
| "That ride last Tuesday" | `list_bookings` for that day, then `get_booking` with the id it returned |
| "What happened to that booking" | `get_booking_audit_log`: a timeline that gives roles, never names |

Money in results is in minor units: divide by 100 for most currencies and show the currency. Times are ISO 8601; say them in the pickup's local time. Ids come from these results, never from a guess. A `not_found` is not a hint to try another id.

Bookings waiting for payment are hidden unless you ask: pass `status` with `pending_payment` when the person is looking for a ride they have not paid for yet.

## Quotes

`list_quotes` and `get_quote` with `scope: "rider"` show the quotes a company sent the person. Stored prices and dates are facts about the quote; they do not prove it was paid.

To answer a quote, call `respond_to_quote` with `dry_run: true`, show the route, time, price, expiry and how it is paid, and wait for an explicit yes. Then repeat the call with the saved `proposal_id` and `dry_run: false`. Accepting books the ride, and declining is final and tells the company. When the result sends the person to Meter's quote page, give them the `action_link` as returned: they accept and pay there, never in the chat.

## Rating and problems

Both are writes, so both follow the same order: `dry_run: true`, show the preview, an explicit yes, then the saved `proposal_id` with `dry_run: false`.

- `get_rating_prompt` returns the newest finished ride still waiting for a rating, and the reasons `rate_ride` accepts. `rate_ride` takes the person's own stars and reasons, within 30 days of the ride; rating again replaces the earlier rating. Do not choose stars for them. The result can carry a `tip_link`: tipping happens on that Meter page, never in the chat.
- `report_ride_issue` sends a problem with one of the person's own bookings to Meter support, in their words, and returns a reference number. It does not change a rating and the driver does not see it.
- A refund goes through `get_action_link` with `action: "request_refund"`. Never say a refund has gone through.

## What this skill does not do

- Book, follow or cancel a ride; `meter-ride` does, with its own preview and confirmation.
- Show anyone else's rides, or a driver's trips and pay.
- Take payment in the chat, or ask for card details.

## References

- [Safety](../../references/safety.md)
- [Tool catalog](../../references/tools.md) (generated)
- [Data model](../../references/data-model.md) (generated; `Booking`, `QuoteDetail`, `RatingPrompt`)
