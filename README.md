# Meter plugins for Claude Code and Codex

[Meter](https://www.meterapp.co) is the taxi meter and fleet platform. This repository is a marketplace with two plugins, one for each of Meter's hosted MCP servers. Each plugin has native packaging for each client, plus the vendor-neutral [Open Plugins](https://agent-plugins.org) manifest.

| Plugin | For | Server | Folder |
| --- | --- | --- | --- |
| **Meter for Drivers & Fleets** (`meter-fleet`) | Drivers and fleet owners: trips, bookings, drivers, vehicles, earnings, accounting, onboarding and settings | `https://www.meterapp.co/api/mcp/fleet` | [fleet](fleet/README.md) |
| **Meter Rides** (`meter-rides`) | Riders: book, follow and cancel your own taxi rides, and look back at them | `https://www.meterapp.co/api/mcp/rider` | [rides](rides/README.md) |

Sign in with your Meter account the first time a tool is used. Your agent then sees exactly what you see in the Meter apps.

## Install

### Claude Code

```text
/plugin marketplace add MeterApp/meter-plugins
/plugin install meter-fleet@meterapp-meter
/plugin install meter-rides@meterapp-meter
```

### Codex

```bash
codex plugin marketplace add MeterApp/meter-plugins
codex plugin add meter-fleet@meterapp-meter
codex plugin add meter-rides@meterapp-meter
```

Install the one you need, or both.

### Skills only, any agent

```bash
npx skills add MeterApp/meter-plugins
```

### Claude and ChatGPT (no terminal)

Add a connector with one of the server URLs above in the app's connector settings and sign in to Meter when asked.

### Moving from the `meter` plugin

Before 2.0.0 this repository offered one plugin, `meter`, with both servers. Uninstall it and install one or both of the plugins above; [the changelog](fleet/CHANGELOG.md) has the commands.

## Development

```bash
python3 scripts/validate_repo.py
python3 scripts/check_endpoint.py
claude plugin validate . --strict
claude plugin validate ./fleet --strict
claude plugin validate ./rides --strict
```

This repository is published from the Meter source repository. Please open an issue here, or write to [jonathan@welcome.meterapp.co](mailto:jonathan@welcome.meterapp.co), rather than sending a pull request; changes are overwritten on the next release.

## License

MIT
