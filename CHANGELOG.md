# Changelog

## 1.4.1 — 2026-10-27

- Split the generated tool and data-model references into smaller linked files so the directory validator can inspect every definition. Existing reference links remain indexes, with no tools or fields removed.
- Validate reference file sizes before publishing to prevent another directory inspection hold.

## 1.4.0 — 2026-10-14

The marketplace is now `meterapp-meter`, and the plugin installs as `meter@meterapp-meter`. It was `meterapp`, the name the Car Image marketplace (`MeterApp/car-image-plugins`) also uses, and Claude Code and Codex key marketplaces by name, so whoever had added one could not add the other. The new name follows skillhook's `meterapp-skillhook`.

If you installed `meter@meterapp`, your `meterapp` marketplace is this repository: move it to the new name, which also frees `meterapp` for Car Image. If your `meterapp` is Car Image's (it offers `car-image`, not `meter`), keep it and just add this marketplace.

Claude Code, where removing the marketplace also uninstalls `meter@meterapp`:

```text
/plugin marketplace remove meterapp
/plugin marketplace add MeterApp/meter-plugins
/plugin install meter@meterapp-meter
```

Codex:

```bash
codex plugin remove meter@meterapp
codex plugin marketplace remove meterapp
codex plugin marketplace add MeterApp/meter-plugins
codex plugin add meter@meterapp-meter
```

Until you move, `meter@meterapp` keeps working. Claude Code still updates it; Codex cannot, because `codex plugin marketplace upgrade meterapp` refuses a marketplace whose name changed.

Also new since 1.2.1, with no entry until now:

- `references/tools.md` and `references/data-model.md` cover 88 tools (41 of them writes), up from 21: bookings, fares, quotes, invoices, trip fees and discounts, fleet finances, website pages, metrics, reviews, reports and feedback among them.
- Every write needs a saved proposal: preview with `dry_run: true`, show every change, get an explicit yes, then repeat the intended arguments with `proposal_id` and `dry_run: false`. A first call without a live proposal writes nothing. The skills, `AGENTS.md` and `references/safety.md` describe this sequence.
- `describe_api` returns a domain index by default; pass `domain` to browse a domain's tools or `tool` for full detail.
- The README says how to keep the plugin up to date in each client.

## 1.3.0 — 2026-10-14

Ride booking for riders, and directory listing fields.

- New skill `meter-ride`: books a ride for the signed-in rider in a conversation. It finds the taxi company (saved fleets first, asks when several fit), confirms the exact pickup and drop-off from `search_places`, shows the ride options and prices from `estimate_ride`, previews the booking with `request_ride` and `dry_run: true` (price, pickup time, how it is paid, cancellation policy) and goes ahead only after an explicit yes with the saved `proposal_id`. Nothing is paid in the chat: when the ride needs paying for, the agent hands the rider a Meter checkout link (valid about 30 minutes, for that signed-in rider only), and confirms the booking with `list_bookings` and `get_ride_status` after the rider says they paid, never before. Rides paid to the driver after the trip, and free rides, are booked in the chat. It follows the ride with `get_ride_status`, cancels with the fee shown first, sends the person to the `add_payment_method`, `finish_ride_payment` and `track_ride` links when the app has to take over, never asks for card details, never books for someone else, and checks `list_bookings` before any retry so a lost response cannot book twice. Written for chat apps without a terminal as well as coding agents.
- `meter-driver-personal`, `meter-settings-changes` and `meter-fleet-insights` send ride booking, tracking and cancelling to `meter-ride` instead of claiming it.
- Listing fields for the Anthropic Directory and OpenAI review: `privacyPolicyUrl`, `termsOfServiceUrl` and `supportUrl` in `.claude-plugin/plugin.json`, `privacyPolicyURL` and `termsOfServiceURL` in the Codex interface. Descriptions, keywords and the Codex starter prompts now cover riders.
- `server.json`: the entry for the official MCP Registry, `co.meterapp/meter`, a remote-only Streamable HTTP server at `https://www.meterapp.co/api/mcp` with OAuth sign-in.
- `scripts/validate_repo.py` also fails on an `Authorization` header in any manifest or MCP file, on anything that reads a credential from the user's machine (an environment variable or a plugin option), on missing or mismatched listing URLs, on Codex listing text over OpenAI's limits, and on a `server.json` out of step with the manifests.
- Skill descriptions are quoted YAML. `meter-driver-personal`, `meter-fleet-onboarding` and `meter-settings-changes` had an unquoted `: ` in theirs, so `npx skills add MeterApp/meter-plugins` skipped them and installed only two of the five skills; the validator now refuses an unquoted `: `.

## 1.2.1 — 2026-09-30

- The generated references and the server instructions no longer claim that every write lands in an audit trail; a write runs as the signed-in person with their own permissions.
- The four fleet settings tools (`update_fleet_settings`, `update_booking_settings`, `update_ride_option`, `assign_vehicle`) now work while a fleet is still completing setup, so an agent can act on `get_onboarding_checklist` recommendations. A fleet whose billing has lapsed still gets `fleet_not_operational`.
- `list_bookings` with the default scope now returns a solo driver's own assigned rides instead of a permission error.

## 1.2.0 — 2026-09-24

- Simplify supported editor packaging to Claude Code and Codex plus the portable manifest.
- Keep agent instructions in AGENTS.md with a CLAUDE.md symlink.

## 1.1.0 — 2026-09-11

Write tools and the onboarding checklist.

- The hosted server now offers six settings write tools (`update_fleet_settings`, `update_booking_settings`, `update_ride_option`, `assign_vehicle`, `update_my_profile`, `update_my_availability`) and the read tool `get_onboarding_checklist`. Every write accepts `dry_run` (default false; pass `dry_run: true` to preview) and returns `{ applied, dry_run, changes: [{ field, from, to }], <object> }`.
- Skills and references describe the dry-run, confirm, apply sequence against that contract; `references/tools.md` and `references/data-model.md` regenerated.
- CLI: `npx @meterapp/meter call <tool> --dry-run` calls any tool with a preview.

## 1.0.0 — 2026-09-11

First public release.

- Five skills: `meter-fleet-insights`, `meter-fleet-onboarding`, `meter-settings-changes`, `meter-driver-personal`, `meter-api-explainer`.
- Hosted MCP server at `https://www.meterapp.co/api/mcp`, authenticated with the person's own Meter sign-in (OAuth 2.1 with PKCE; no API keys).
- Native manifests for Claude Code and Codex, plus the vendor-neutral Open Plugins manifest.
- Installable by name: `/plugin marketplace add MeterApp/meter-plugins` (Claude Code),
  `codex plugin marketplace add MeterApp/meter-plugins` (Codex),
  `npx skills add MeterApp/meter-plugins` (skills only, any agent).
- Generated references: `references/tools.md` and `references/data-model.md` are built from the server's tool catalog.
