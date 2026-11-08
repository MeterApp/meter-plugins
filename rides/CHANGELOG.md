# Changelog

## 2.0.1 — 2026-11-08

- The plugin ships only file types the Claude plugin directory accepts from organizations that are not Verified: the SVG logo is gone, and Codex and the directory listing use a PNG logo instead. Tools, skills and sign-in did not change.

## 2.0.0 — 2026-11-05

Before 2.0.0 this marketplace offered one plugin, `meter`, connected to both Meter servers. The Anthropic Directory pairs a plugin with one connector, so there are now two plugins, one per server: `meter-fleet` (Meter for Drivers & Fleets) and `meter-rides` (Meter Rides). Sign-in, tools and what you can do have not changed.

If you installed `meter@meterapp-meter`, uninstall it and install one or both of the new plugins. Claude Code:

```text
/plugin uninstall meter@meterapp-meter
/plugin marketplace update meterapp-meter
/plugin install meter-fleet@meterapp-meter
/plugin install meter-rides@meterapp-meter
```

Codex:

```bash
codex plugin remove meter@meterapp-meter
codex plugin marketplace upgrade meterapp-meter
codex plugin add meter-fleet@meterapp-meter
codex plugin add meter-rides@meterapp-meter
```

This plugin is `meter-rides`: it connects only to `https://www.meterapp.co/api/mcp/rider`, and its references list only that server's tools.

- `meter-ride`, the skill for booking, following and cancelling your own ride, moved here from `meter`.
- New skill `meter-rider-personal`: looking back at your own rides and quotes, rating a ride and reporting a problem. A rider's past rides used to be part of `meter-driver-personal`.
- New MCP Registry entry `co.meterapp/meter-rides`.

Earlier history of the combined `meter` plugin is in the changelog of `meter-fleet`, in the same repository.
