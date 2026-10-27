# Meter — plugin for Claude Code and Codex

[Meter](https://www.meterapp.co) is the taxi meter and fleet platform: drivers run a meter in the Meter app, fleets manage drivers, vehicles, fares, scheduled bookings and money, and riders book rides from fleets. This plugin gives your agent the view you already have in the Meter apps, through the hosted MCP server, with your own Meter sign-in. One repository, native packaging for each client, plus the vendor-neutral [Open Plugins](https://agent-plugins.org) manifest.

**No API keys.** The first time a tool is used, your agent opens a Meter sign-in in the browser (OAuth 2.1 with PKCE). The token it receives is exactly as powerful as you are: owners and admins see fleet-wide data, drivers and riders see their own.

## Install

### Claude Code

```text
/plugin marketplace add MeterApp/meter-plugins
/plugin install meter@meterapp-meter
```

### Codex

```bash
codex plugin marketplace add MeterApp/meter-plugins
codex plugin add meter@meterapp-meter
```

### Skills only, any agent

```bash
npx skills add MeterApp/meter-plugins
```

### Server only, no skills

```bash
claude mcp add --transport http meter https://www.meterapp.co/api/mcp
```

Start a new session, then try:

> "How much did my fleet earn last week, and which driver had the most trips?"

> "Book me a ride to the airport at 6am with my usual taxi company."

### Claude and ChatGPT (no terminal)

Add a custom connector with the URL `https://www.meterapp.co/api/mcp` in the app's connector settings and sign in to Meter when asked. The skills are optional there: the server explains its own tools and asks for a preview and your yes before anything changes.

### Keep it up to date

- **Claude Code** updates the plugin by itself at startup once auto-update is on for its marketplace, which Claude Code leaves off for marketplaces outside Anthropic's: open `/plugin`, go to **Marketplaces**, choose `meterapp-meter` and select **Enable auto-update**. By hand: `/plugin marketplace update meterapp-meter`, then `/plugin update meter@meterapp-meter`, then restart (or `/reload-plugins`).
- **Codex:** `codex plugin marketplace upgrade meterapp-meter`.
- **Skills only:** `npx skills update`.

Added this marketplace before 1.4.0, when it was called `meterapp`? [CHANGELOG.md](CHANGELOG.md) shows how to move your install to the new name.

The CLI, `@meterapp/meter`, installs its own new versions in the background, and `meter update` updates it now and refreshes this plugin wherever Claude Code or Codex has it installed.

## What you get

Six skills and the hosted MCP server.

| Skill | Job |
| --- | --- |
| `meter-ride` | Booking, following and cancelling your own taxi ride: confirmed addresses, the price first, your yes before booking |
| `meter-fleet-insights` | Questions about a fleet's trips, bookings, drivers, vehicles, earnings and accounting |
| `meter-fleet-onboarding` | Walking a new fleet owner through setup with the onboarding checklist and settings tools |
| `meter-settings-changes` | Changing fleet, booking, ride-option or personal settings: dry run, confirm, apply |
| `meter-driver-personal` | An individual driver's own trips, earnings, pay stubs, availability and profile, and a rider's past rides |
| `meter-api-explainer` | "How does this work / what does this field mean", and drafting integrations |

The MCP server at `https://www.meterapp.co/api/mcp` provides the tools listed in [references/tools.md](references/tools.md); the objects they return are in [references/data-model.md](references/data-model.md). Both files are generated from the server's own catalog. The server also describes itself: `describe_api` returns a domain index by default; pass `domain` to browse its tools or `tool` for full detail. `explain_data` explains any result field.

## Authentication

| Surface | Credential |
| --- | --- |
| Hosted MCP | OAuth 2.1 access token obtained by the host from your Meter sign-in |
| CLI | `npx @meterapp/meter login` (same sign-in, stored locally); `meter call <tool> --dry-run` previews any write |
| Browsers, config files, prompts | **Never a token** |

The host discovers the sign-in from the server's 401 challenge and the metadata at `https://www.meterapp.co/.well-known/oauth-protected-resource`. Nothing in this repository contains or expects a credential. Details in [references/authorization.md](references/authorization.md).

## Safety model

- Read first, ask second. `whoami` tells the agent who is signed in and which fleets and roles they have; ids come from results, never from guesses.
- Every settings change is a dry run first. `dry_run` defaults to false, so the agent passes `dry_run: true`, shows the exact `changes` (`field`, `from`, `to`), waits for an explicit yes, then repeats the call to apply. Fares are never changed without stating the from and to values.
- A permission error is final for that person. The agent switches to a tool that fits their role instead of retrying.
- Results never contain payment-provider ids, GPS traces, internal notes or other people's contact details beyond what the role allows. See [references/safety.md](references/safety.md).
- Rides are booked only for the signed-in rider, only after a preview of the price, pickup time, payment and cancellation policy, and only on an explicit yes. Nothing is paid in the chat: when a ride needs paying for, the agent gives you a Meter checkout link (valid about 30 minutes, only for you) and the ride is booked once you have paid on meterapp.co; it then checks the booking before saying so. Rides the company takes payment for after the trip, and free rides, are booked in the chat. The agent never asks for or types card details. Cancelling shows the fee first.

## What the plugin sends, and where

Everything goes to one place: the hosted Meter MCP server at `https://www.meterapp.co/api/mcp`, authenticated by your host with your own Meter sign-in. The agent sends the arguments of the tools it calls, which can include addresses you ask it to search or book, ride times and booking ids. Nothing in this plugin reads files, environment variables or credentials from your machine, and nothing is sent anywhere else. How Meter handles that data: [privacy policy](https://www.meterapp.co/privacy). To disconnect, remove the connector in your host or revoke it in Meter under Account, Connected apps.

## Development

```bash
python3 scripts/validate_repo.py
claude plugin validate . --strict
codex plugin marketplace add . --json
```

This repository is published from the Meter source repository. Please open an issue here, or write to [hello@meterapp.co](mailto:hello@meterapp.co), rather than sending a pull request; changes are overwritten on the next release.

## Links

[Docs](https://www.meterapp.co/docs) · [MCP](https://www.meterapp.co/docs/mcp) · [Plugins](https://www.meterapp.co/docs/plugins) · [Book rides](https://www.meterapp.co/docs/rides) · [Privacy and terms](https://www.meterapp.co/privacy) · [MCP Registry entry](server.json) · [agents.md](https://www.meterapp.co/agents.md) · [llms.txt](https://www.meterapp.co/llms.txt) · [openapi-mcp.json](https://www.meterapp.co/openapi-mcp.json) · [hello@meterapp.co](mailto:hello@meterapp.co)

## License

MIT
