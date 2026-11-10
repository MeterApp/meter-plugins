# Meter for Drivers & Fleets — plugin for Claude Code and Codex

[Meter](https://www.meterapp.co) is the taxi meter and fleet platform: drivers run a meter in the Meter app, and fleets manage drivers, vehicles, fares, scheduled bookings and money. This plugin gives your agent the view you already have in the Meter apps, through the hosted Meter for Drivers & Fleets MCP server, with your own Meter sign-in. Booking rides as a rider is a separate plugin, Meter Rides, in the same marketplace.

**Sign in with your Meter account.** The first time a tool is used, your agent opens a Meter sign-in in the browser (OAuth 2.1 with PKCE). The connection it gets is exactly as powerful as you are: owners and admins see fleet-wide data, drivers see their own.

## Install

### Claude Code

```text
/plugin marketplace add MeterApp/meter-plugins
/plugin install meter-fleet@meterapp-meter
```

### Codex

```bash
codex plugin marketplace add MeterApp/meter-plugins
codex plugin add meter-fleet@meterapp-meter
```

### Server only, no skills

```bash
claude mcp add --transport http meter-fleet https://www.meterapp.co/api/mcp/fleet
```

Start a new session, then try:

> "How much did my fleet earn last week, and which driver had the most trips?"

### Claude and ChatGPT (no terminal)

Add a connector with the URL `https://www.meterapp.co/api/mcp/fleet` in the app's connector settings and sign in to Meter when asked. The skills are optional there: the server explains its own tools and asks for a preview and your yes before anything changes.

### Keep it up to date

- **Claude Code** updates the plugin by itself at startup once auto-update is on for its marketplace, which Claude Code leaves off for marketplaces outside Anthropic's: open `/plugin`, go to **Marketplaces**, choose `meterapp-meter` and select **Enable auto-update**. By hand: `/plugin marketplace update meterapp-meter`, then `/plugin update meter-fleet@meterapp-meter`, then restart (or `/reload-plugins`).
- **Codex:** `codex plugin marketplace upgrade meterapp-meter`.

Installed the `meter` plugin before 2.0.0? [CHANGELOG.md](CHANGELOG.md) shows how to move to this one.

## What you get

Five skills and the hosted MCP server.

| Skill | Job |
| --- | --- |
| `meter-fleet-insights` | Questions about a fleet's trips, bookings, drivers, vehicles, earnings and accounting |
| `meter-fleet-onboarding` | Walking a new fleet owner through setup with the onboarding checklist and settings tools |
| `meter-settings-changes` | Changing fleet and driver settings, including service areas, fares, booking rules, website pages and custom domains |
| `meter-driver-personal` | An individual driver's own trips, earnings, pay stubs, availability and profile |
| `meter-api-explainer` | "How does this work / what does this field mean", and drafting integrations |

The MCP server at `https://www.meterapp.co/api/mcp/fleet` provides the tools listed in [references/tools.md](references/tools.md); the objects they return are in [references/data-model.md](references/data-model.md). Both files are generated from the server's own catalog. The server also describes itself: `describe_api` returns a domain index by default; name a `domain` to browse its tools or a `tool` for full detail. `explain_data` explains any result field.

## Sign-in

Your host opens the Meter sign-in (OAuth 2.1) and keeps the connection. The host finds the sign-in from the server's 401 answer and its metadata at `https://www.meterapp.co/.well-known/oauth-protected-resource/api/mcp/fleet`. The plugin itself asks you for nothing: you only ever sign in on meterapp.co. Choose **Look and change** to make settings changes. To update an existing connection, go to [Connected apps](https://www.meterapp.co/app/account/connected-apps), change its access, then start a new session to refresh the tools. See [authorization details](references/authorization.md).

## Safety model

- Read first, ask second. `whoami` tells the agent who is signed in and which fleets and roles they have; ids come from results, never from guesses.
- Every settings change is a dry run first. `dry_run` defaults to false, so the agent sets `dry_run: true`, shows the exact `changes` (`field`, `from`, `to`), waits for an explicit yes, then repeats the call to apply. Fares are never changed without stating the from and to values.
- A permission error is final for that person. The agent switches to a tool that fits their role instead of retrying.
- Results never contain payment-provider ids, GPS traces, internal notes or other people's contact details beyond what the role allows. See [references/safety.md](references/safety.md).

## What the plugin sends, and where

Everything goes to Meter's hosted MCP server, `https://www.meterapp.co/api/mcp/fleet`, through your host and your own Meter sign-in. The agent sends the arguments of the tools it calls, which can include fleet settings, dates and ids. The plugin is instructions and one server address: it runs no code of its own and sends nothing anywhere else. How Meter handles that data: [privacy policy](https://www.meterapp.co/privacy). To disconnect, remove the connector in your host or revoke it in Meter under Account, Connected apps.

## Links

[Docs](https://www.meterapp.co/docs) · [MCP](https://www.meterapp.co/docs/mcp) · [Plugins](https://www.meterapp.co/docs/plugins) · [Privacy and terms](https://www.meterapp.co/privacy) · [MCP Registry entry](server.json) · [agents.md](https://www.meterapp.co/agents.md) · [llms.txt](https://www.meterapp.co/llms.txt) · [openapi-mcp.json](https://www.meterapp.co/openapi-mcp.json) · [jonathan@welcome.meterapp.co](mailto:jonathan@welcome.meterapp.co)

## License

MIT
