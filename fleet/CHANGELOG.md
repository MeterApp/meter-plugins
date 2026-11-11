# Changelog

## 2.0.5 (2026-11-11)

Configure personal booking policies, driver websites and notification preferences. Manage booking blocks and pauses on personal and fleet calendars, update existing fleet webhooks, and remove unused service zones.

## 2.0.4 (2026-11-10)

Fleet admins can connect an existing custom domain, check its DNS status, or disconnect it after confirmation. Settings guidance now covers service boundaries, fares and websites, and explains how to enable changes.

## 2.0.3 — 2026-11-08

- Reworded the skills and references for the directory's automatic check. Tools, skills and sign-in did not change.

## 2.0.2 — 2026-11-08

- The README and this changelog are shorter, and now match Meter Rides: the README covers only the plugin, and this file starts at 2.0.0. Tools, skills and sign-in did not change.

## 2.0.1 — 2026-11-08

- The plugin ships only file types the Claude plugin directory accepts from organizations that are not Verified: the SVG logo is gone, and Codex and the directory listing use a PNG logo instead. Tools, skills and sign-in did not change. The README no longer lists the separate command-line package.

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

This plugin is `meter-fleet`: it connects only to `https://www.meterapp.co/api/mcp/fleet`, and its references list only that server's tools. The `meter-ride` skill and the rider parts of `meter-driver-personal` moved to `meter-rides`.

Earlier releases are the `v1.5.3` tag and older in this repository.
