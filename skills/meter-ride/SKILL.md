---
name: meter-ride
description: "Book, track or cancel a taxi ride for the signed-in rider through the Meter MCP rider tools (find_fleets, search_places, estimate_ride, request_ride, get_ride_status, list_bookings, get_booking, cancel_booking, get_action_link). Covers choosing the taxi company, confirming the exact pickup and drop-off, showing prices, the dry run and explicit yes, the Meter checkout link the rider pays on, confirming the booking afterwards, duplicates and cancellation fees, in a chat app or a terminal. Use when the person wants a ride for themselves (\"book me a taxi to the airport at 6am\", \"where is my driver\", \"cancel my ride\"); do not use for a fleet's bookings or dispatch (meter-fleet-insights, meter-settings-changes), a driver's own assigned rides or pay (meter-driver-personal), or booking for someone else."
---

# Booking a ride for the signed-in rider

Meter riders book rides from taxi companies (fleets) that use Meter. This skill lets an agent do that in a conversation: find the company, pin down the addresses, show the price, get the person's yes, and hand them Meter's checkout when the ride has to be paid for. Afterwards it helps them follow or cancel the ride. It works the same in a chat app with no terminal (Claude, ChatGPT) and in a coding agent.

A ride is a real car sent to a real address, and usually a real payment. Every step below exists so that the person never gets a car, a time or a price they did not choose, and never pays anywhere but on Meter.

## The rules that never bend

- **Only for the signed-in person.** The rider is whoever signed in to Meter. Do not book for a friend, a guest or a customer, and do not put someone else's name or phone on a ride. If they ask, tell them the other person can book in the Meter app or on the company's booking page, or a fleet owner can dispatch the ride from Meter.
- **Never guess an address.** Every pickup and drop-off comes from `search_places` and is confirmed by the person in their own words ("Yes, Terminal B departures").
- **Never go ahead without an explicit yes** to the full preview from `request_ride` with `dry_run: true`. "Sounds good" about a price you mentioned earlier is not a yes to the booking.
- **Payment happens on Meter, not in the chat.** In Claude, ChatGPT and the plugins, `request_ride` does not charge anyone. When the ride needs paying for, it returns a Meter checkout link that the rider opens, confirms and pays on `meterapp.co`. Never ask for, accept or type card numbers, expiry dates, security codes or bank details. If the person pastes one, tell them to delete it and use the checkout link.
- **Never say a ride is booked until a tool says so.** After a checkout link, the ride exists only once `list_bookings` or `get_ride_status` shows it.
- **Never retry a booking blind.** Before any second `request_ride`, check `list_bookings` (see "Avoiding a double booking").

## The flow

### 1. Who is booking

Call `whoami` once. Use the person's own name from `profile` when you talk to them. A driver or fleet owner can book a ride as a rider too; this skill only ever books as the rider.

### 2. Which taxi company

Call `find_fleets` with what the person said: a company name ("my usual taxi company", "Yellow Cab"), or the pickup place so it can find companies serving it. Saved fleets come first.

| `find_fleets` says | Do |
| --- | --- |
| One saved fleet and the person said "my usual" or named it | Use it, and say its name in your next message |
| Several plausible fleets | List them by name (and area, if shown) and ask which one |
| None near the pickup | Say no Meter company serves that place yet; do not book with a company far away |

Never pick between two companies on the person's behalf. The `fleet_id` comes from the result, never from memory or a guess.

### 3. Exactly where

Call `search_places` for the pickup and again for the drop-off (and every stop). Then confirm:

- One clear match: read the full address back and ask "Pick you up at 1200 Main St, Springfield?"
- Several matches (two Starbucks, "the airport" with several terminals): list the options and ask. Do not choose the closest one yourself.
- No match: ask for a street address, a postcode or a landmark, and search again.
- "Home", "work" or "my hotel": search for what the person tells you; do not assume an address from an earlier conversation unless they confirm it now.

### 4. When and how many

A ride now has no `pickup_time`. A ride later needs an ISO 8601 time with the offset of the pickup's local time (`2026-10-15T06:00:00-04:00`). Resolve "tomorrow at 6am" against the pickup's time zone and say the date back: "Thursday 15 October at 6:00 am". Ask how many passengers if it matters for the vehicle, and pass `passengers`.

### 5. Price options

Call `estimate_ride` with the `fleet_id`, `pickup`, `dropoff`, and any `stops`, `pickup_time` and `passengers`. Present each ride option the way the result gives it: name, price or price range, currency, and anything it says about the estimate (for example that the final fare runs on the meter). Money in results is in minor units: divide by 100 for most currencies and show the currency. Mention the cancellation policy it returns.

If the person picks an option, keep its `ride_option_id` and the `estimate_id`. If they want something the company does not offer (a larger car, a child seat), say so; do not substitute.

### 6. Preview the booking

Call `request_ride` with `dry_run: true` and exactly the choices the person made (the `estimate_id` and `ride_option_id`, the confirmed places, the time, the passengers). Save the returned proposal. Show every part of the preview, in plain words:

- the taxi company
- pickup and drop-off (and stops), as confirmed
- the pickup time with its date, or "as soon as possible"
- the ride option and the price or price range, with currency
- how it will be paid, as the preview says: on Meter's checkout page before the ride, to the driver after the trip, or nothing (a free ride)
- the cancellation policy: when a fee starts and how much it is
- any warning the preview returns

When the payment is checkout, say so before asking: "After you say yes, I'll give you a Meter link to confirm and pay. The ride is booked once you've paid there." Then ask one clear question: "Go ahead with this ride? (yes/no)". Stop and wait.

### 7. Confirm, then check out or book

Only after an explicit yes, call `request_ride` again with the same arguments, the saved `proposal_id` and `dry_run: false`. What happens next depends on the result, not on what you expect:

| The result says | Do |
| --- | --- |
| Checkout needed, with a Meter checkout link | Give the link exactly as returned and tell the person: open it, check the ride, and pay on meterapp.co; it works for about 30 minutes and only when they are signed in to Meter as themselves. Say plainly that the ride is **not booked yet**. Then wait |
| Booked (the fleet takes payment after the trip, or the ride is free) | Tell the person it is booked and what happens next (the company confirms and assigns a driver). Share the tracking link if there is one, or get one with `get_action_link` and `action: "track_ride"` |
| No saved payment method and the company needs one before checkout | Give the `add_payment_method` link from the result (or `get_action_link` with that action) and say you will continue once they have added it |
| The proposal expired or the price changed | Show the fresh preview and ask again. Never go ahead with a preview the person did not see |

If the result has a checkout requirement but no link, get one with `get_action_link` and `action: "finish_ride_payment"`. Never build or edit a link yourself.

### 8. After checkout

When the person says they have paid (or comes back later):

1. Call `list_bookings` with `scope: "rider"`, `status: ["pending", "confirmed", "pending_payment"]` and an `after` a little before the pickup time, and find the ride by company, pickup and time.
2. Call `get_ride_status` on it.
3. Report what the tools say:
   - Confirmed or pending (waiting for the company): it is booked. Share the tracking link.
   - Still `pending_payment`: payment has not gone through. Say so, and offer the checkout link again if it is still valid (about 30 minutes), or a fresh one from `get_action_link` with `finish_ride_payment`.
   - Not there: nothing was booked. Offer to start again with a fresh preview.

Never tell the person the ride is booked, paid or confirmed from their word alone or from the checkout link having been sent.

## Avoiding a double booking

A timeout, an error or a lost connection after `request_ride` with `dry_run: false` does not mean nothing happened, and neither does an unused checkout link. Before you call `request_ride` again:

1. Call `list_bookings` as in step 8.
2. If a matching ride is there, report it and stop. If it is waiting for payment, send the person back to its checkout instead of creating a second ride.
3. If none is there, show the preview again and ask before going ahead.

Do the same when the person asks "did it go through?" or asks for the same ride twice.

## While the ride is on its way

`get_ride_status` with the booking returns the status, the driver's first name, the vehicle and plate, a phone number to reach the driver, an ETA when there is one, what cancelling would cost right now, and the receipt link after the trip. Give the person what they asked for; do not pass the driver's phone number on to anyone else. If the person asks "where is my ride" and you do not have the booking id, `list_bookings` with `scope: "rider"` first.

## Cancelling

1. Find the ride with `list_bookings` (`scope: "rider"`) or the id you already have, and confirm which ride: "Your 6:00 am ride to the airport with City Cabs?"
2. `get_ride_status` tells you the fee if they cancel now. Call `cancel_booking` with `dry_run: true` and `cancellation_reason: "rider_request"`.
3. Show the preview, including the fee and currency, in one line: "Cancelling now costs 5.00 USD. Cancel the ride? (yes/no)". A fee of zero is worth saying too.
4. Only after a yes, repeat with the saved `proposal_id` and `dry_run: false`.

Never say a refund or a charge has gone through; say the ride is cancelled and that any fee or refund follows the company's policy. A ride already in progress cannot be cancelled here: send the person to the Meter app.

## Errors

| Code | Means | Do |
| --- | --- | --- |
| `unauthenticated` | Not signed in, or the sign-in expired | Ask the person to connect Meter again in their app's connector settings (or `/mcp` in Claude Code). Never ask for a password or token |
| `forbidden` | This person cannot do that | Stop. Do not retry with another fleet or booking id |
| `not_found` | A fleet, place or booking that is not theirs or does not exist | Take ids from earlier results; ask the person |
| `402` / payment required | A payment step is needed | The checkout or `add_payment_method` link, as in step 7 |
| `invalid_argument` | A field is wrong | Fix it once (check `describe_api` for the tool), then ask the person if it fails again |

If a rider tool is not in the host's tool list, `find_tools` with a query such as `ride` lists it and `run_read_tool` / `run_write_tool` run it, with the same dry run and confirmation inside `arguments`.

## From a terminal

The CLI runs the same tools: `npx @meterapp/meter rides --help` lists the ride commands. Writes follow the same order there: a preview (`--dry-run`), the person's yes, then the apply with the returned proposal. Meter's own CLI may book with the rider's saved card instead of a checkout link; whichever it is, the result says so, and the rules above about saying "booked" only when a tool says so still apply.

## What this skill does not do

- Book for anyone except the signed-in person, or change who the rider is.
- Take payment in the chat, or take, store or repeat card numbers.
- Choose a company, address, time or ride option the person did not confirm.
- Promise a pickup time, a driver or a final fare beyond what the tools return.
- Dispatch rides as a fleet (that is the fleet's console), or show other riders' rides.

## References

- [Safety](../../references/safety.md)
- [Authorization](../../references/authorization.md)
- [Tool catalog](../../references/tools.md) (generated)
