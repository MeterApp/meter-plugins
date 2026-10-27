# Safety rules for agents using Meter

These rules apply to every Meter skill. They exist because the data is a business's money and its customers' rides, and because the write tools can change what riders are charged.

## Reading

1. **`whoami` first, once.** It tells you the person's fleets and roles and which tools apply. Do not call it in a loop.
2. **Never guess an id.** `fleet_id`, `trip_id`, `booking_id`, `member_id` come from earlier results. A `not_found` on a guessed id is not a hint to try another.
3. **A permission error is final for this person.** `forbidden` means their role does not allow the view. Switch to a tool that fits (`driver: "me"`, `scope: "me"`, `scope: "driver"`), or explain who can see it.
4. **Say which tool produced a number.** `get_earnings` is card payouts only; `get_accounting_summary` is the full ledger; `list_trips` totals are what you summed. Do not blend them silently.
5. **Present in the fleet's terms.** Currency from the result (values are minor units), the fleet timezone for times, meters converted to the fleet's distance unit.
6. **Respect the privacy boundary.** Results already exclude payment-provider ids, GPS traces, internal notes and other people's contact details beyond what the role allows. Do not try to infer them, and do not build profiles of drivers or riders the human did not ask for.

## Writing

7. **Every write starts with a saved preview.** Pass `dry_run: true` explicitly. The result includes `status: preview`, a `proposal`, and `changes: [{ field, from, to }]`; show every change verbatim and stop. A first call without a live proposal writes nothing and returns `confirmation_required`.
8. **An explicit yes, on the concrete values.** Then repeat the intended arguments with the saved `proposal_id` and `dry_run: false`. Confirm `status: applied`; `applied: false` with no changes means no mutation was needed. If the proposal is stale or expired, show its fresh replacement and ask again. Never chain the two in one turn. A vague reply is not a yes for money fields.
9. **Only the fields the human named.** Do not pass extra fields, do not act on a dry-run warning without asking, and do not fix things the human did not mention.
10. **Fares and payout fractions are money.** Always state old and new values with the currency. Never change them in a batch the human did not enumerate, and never invent market rates.
11. **One target at a time.** Several fleets or several ride options mean several dry-run and confirm cycles.

## Credentials

12. **No tokens anywhere.** Not in prompts, files, URLs, tool arguments, screenshots or bug reports. On `unauthenticated`, the human reconnects the connector in their host; you do not ask for a token.
13. **Nothing to buy or subscribe to.** No tool changes billing. Billing and payout accounts are set up by the human in the web console.

## When in doubt

Ask `describe_api` and `explain_data`, read `https://www.meterapp.co/llms-full.txt`, or tell the human what you could not verify and suggest `hello@meterapp.co`.
