# Safety rules for agents using Meter Rides

These rules apply to every skill in this plugin. A ride is a real car sent to a real address and usually a real payment, so the person sees and confirms each choice.

## Reading

1. **`whoami` first, once.** It tells you who is signed in. Do not call it in a loop.
2. **Never guess an id.** `fleet_id`, `booking_id` and `quote_id` come from earlier results. A `not_found` on a guessed id is not a hint to try another.
3. **A permission error is final for this person.** `forbidden` means they may not see or do that. Do not retry with other ids.
4. **Present in the ride's terms.** Currency from the result (values are minor units) and the pickup's local time.
5. **Respect the privacy boundary.** Results already exclude payment-provider ids, GPS traces, internal notes and other people's contact details. Do not try to infer them, and do not pass a driver's phone number on to anyone else.

## Writing

6. **Every write starts with a saved preview.** Pass `dry_run: true` explicitly. The result includes `status: preview`, a `proposal`, and `changes: [{ field, from, to }]`; show every part of it and stop. A first call without a live proposal writes nothing and returns `confirmation_required`.
7. **An explicit yes, on the concrete values.** Then repeat the intended arguments with the saved `proposal_id` and `dry_run: false`. If the proposal is stale or expired, show its fresh replacement and ask again. Never chain the two in one turn.
8. **Only for the signed-in person.** Rides are booked for the person who signed in, nobody else.
9. **Never retry a booking blind.** Check `list_bookings` first: a timeout after a booking call does not mean nothing happened.
10. **Payment happens on Meter.** Nothing is paid in the chat. Never ask for, accept or type card numbers, expiry dates or security codes. Say a ride is booked only when `list_bookings` or `get_ride_status` shows it.

## Sign-in

11. **Sign-in stays with the host.** On `unauthenticated`, the person reconnects the connector in their app; you never ask them to paste anything.

## When in doubt

Ask `describe_api` and `explain_data`, read `https://www.meterapp.co/llms-full.txt`, or tell the person what you could not verify and suggest `jonathan@welcome.meterapp.co`.
