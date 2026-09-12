# Meter — plugin for Claude Code, Codex and Cursor

[Meter](https://www.meterapp.co) is the taxi meter and fleet platform: drivers run a meter in the Meter app, fleets manage drivers, vehicles, fares, scheduled bookings and money, and riders book rides from fleets. This plugin gives your agent the view you already have in the Meter apps, through the hosted MCP server, with your own Meter sign-in. One repository, native packaging for each client, plus the vendor-neutral [Open Plugins](https://agent-plugins.org) manifest.

**No API keys.** The first time a tool is used, your agent opens a Meter sign-in in the browser (OAuth 2.1 with PKCE). The token it receives is exactly as powerful as you are: owners and admins see fleet-wide data, drivers and riders see their own.

## Install

### Claude Code

```text
/plugin marketplace add MeterApp/meter-plugins
/plugin install meter@meterapp
```

### Codex

```bash
codex plugin marketplace add MeterApp/meter-plugins
codex plugin add meter@meterapp
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

## What you get

Five skills and the hosted MCP server.

| Skill | Job |
| --- | --- |
| `meter-fleet-insights` | Questions about a fleet's trips, bookings, drivers, vehicles, earnings and accounting |
| `meter-fleet-onboarding` | Walking a new fleet owner through setup with the onboarding checklist and settings tools |
| `meter-settings-changes` | Changing fleet, booking, ride-option or personal settings: dry run, confirm, apply |
| `meter-driver-personal` | An individual driver's or rider's own trips, earnings, pay stubs, availability and profile |
| `meter-api-explainer` | "How does this work / what does this field mean", and drafting integrations |

The MCP server at `https://www.meterapp.co/api/mcp` provides the tools listed in [references/tools.md](references/tools.md); the objects they return are in [references/data-model.md](references/data-model.md). Both files are generated from the server's own catalog. The server also describes itself: `describe_api` lists every tool and `explain_data` explains any result field.

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

## Development

```bash
python3 scripts/validate_repo.py
claude plugin validate . --strict
codex plugin marketplace add . --json
```

This repository is published from the Meter source repository. Please open an issue here, or write to [hello@meterapp.co](mailto:hello@meterapp.co), rather than sending a pull request; changes are overwritten on the next release.

## Links

[Docs](https://www.meterapp.co/docs) · [MCP](https://www.meterapp.co/docs/mcp) · [Plugins](https://www.meterapp.co/docs/plugins) · [agents.md](https://www.meterapp.co/agents.md) · [llms.txt](https://www.meterapp.co/llms.txt) · [openapi-mcp.json](https://www.meterapp.co/openapi-mcp.json) · [hello@meterapp.co](mailto:hello@meterapp.co)

## License

MIT
