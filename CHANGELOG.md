# Changelog

## 1.1.0 — 2026-09-11

Write tools and the onboarding checklist.

- The hosted server now offers six settings write tools (`update_fleet_settings`, `update_booking_settings`, `update_ride_option`, `assign_vehicle`, `update_my_profile`, `update_my_availability`) and the read tool `get_onboarding_checklist`. Every write accepts `dry_run` (default false; pass `dry_run: true` to preview) and returns `{ applied, dry_run, changes: [{ field, from, to }], <object> }`.
- Skills and references describe the dry-run, confirm, apply sequence against that contract; `references/tools.md` and `references/data-model.md` regenerated.
- CLI: `npx @meterapp/meter call <tool> --dry-run` calls any tool with a preview.

## 1.0.0 — 2026-09-11

First public release.

- Five skills: `meter-fleet-insights`, `meter-fleet-onboarding`, `meter-settings-changes`, `meter-driver-personal`, `meter-api-explainer`.
- Hosted MCP server at `https://www.meterapp.co/api/mcp`, authenticated with the person's own Meter sign-in (OAuth 2.1 with PKCE; no API keys).
- Native manifests for Claude Code, Codex and Cursor, plus the vendor-neutral Open Plugins manifest.
- Installable by name: `/plugin marketplace add MeterApp/meter-plugins` (Claude Code),
  `codex plugin marketplace add MeterApp/meter-plugins` (Codex),
  `npx skills add MeterApp/meter-plugins` (skills only, any agent).
- Generated references: `references/tools.md` and `references/data-model.md` are built from the server's tool catalog.
