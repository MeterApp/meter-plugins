# Meter Rides — plugin for Claude Code and Codex

[Meter](https://www.meterapp.co) riders book rides from local taxi companies that use Meter. This plugin lets your agent do that in a conversation, through the hosted Meter Rides MCP server, with your own Meter sign-in. Driving or running a fleet is a separate plugin, Meter for Drivers & Fleets, in the same marketplace.

**Sign in with your Meter account.** The first time a tool is used, your agent opens a Meter sign-in in the browser (OAuth 2.1 with PKCE). The agent acts only for you and sees only your own rides.

## Install

### Claude Code

```text
/plugin marketplace add MeterApp/meter-plugins
/plugin install meter-rides@meterapp-meter
```

### Codex

```bash
codex plugin marketplace add MeterApp/meter-plugins
codex plugin add meter-rides@meterapp-meter
```

### Server only, no skills

```bash
claude mcp add --transport http meter-rides https://www.meterapp.co/api/mcp/rider
```

Start a new session, then try:

> "Book me a ride to the airport at 6am with my usual taxi company."

### Claude and ChatGPT (no terminal)

Add a connector with the URL `https://www.meterapp.co/api/mcp/rider` in the app's connector settings and sign in to Meter when asked. The skills are optional there: the server explains its own tools and asks for a preview and your yes before anything is booked.

### Keep it up to date

- **Claude Code** updates the plugin by itself at startup once auto-update is on for its marketplace, which Claude Code leaves off for marketplaces outside Anthropic's: open `/plugin`, go to **Marketplaces**, choose `meterapp-meter` and select **Enable auto-update**. By hand: `/plugin marketplace update meterapp-meter`, then `/plugin update meter-rides@meterapp-meter`, then restart (or `/reload-plugins`).
- **Codex:** `codex plugin marketplace upgrade meterapp-meter`.

Installed the `meter` plugin before 2.0.0? [CHANGELOG.md](CHANGELOG.md) shows how to move to this one.

## What you get

Two skills and the hosted MCP server.

| Skill | Job |
| --- | --- |
| `meter-ride` | Booking, following and cancelling your own taxi ride: confirmed addresses, the price first, your yes before booking |
| `meter-rider-personal` | Looking back at your own rides, answering a company's quote, rating a ride and reporting a problem |

The MCP server at `https://www.meterapp.co/api/mcp/rider` provides the tools listed in [references/tools.md](references/tools.md); the objects they return are in [references/data-model.md](references/data-model.md). Both files are generated from the server's own catalog. `describe_api` and `explain_data` describe the server from inside a conversation.

## Sign-in

Your host opens the Meter sign-in (OAuth 2.1) and keeps the connection. It finds the sign-in from the server's 401 answer and its metadata at `https://www.meterapp.co/.well-known/oauth-protected-resource/api/mcp/rider`. The plugin itself asks you for nothing: you only ever sign in on meterapp.co. Details in [references/authorization.md](references/authorization.md).

## Safety model

- Rides are booked only for the signed-in rider, only after a preview of the price, pickup time, payment and cancellation policy, and only on an explicit yes.
- Nothing is paid in the chat. When a ride needs paying for, the agent gives you a Meter checkout link (valid about 30 minutes, only for you) and the ride is booked once you have paid on meterapp.co; it then checks the booking before saying so. Rides the company takes payment for after the trip, and free rides, are booked in the chat.
- The agent never asks for or types card details. Cancelling shows the fee first.
- Before any second booking the agent checks your bookings, so a lost response cannot book twice. See [references/safety.md](references/safety.md).

## What the plugin sends, and where

Everything goes to Meter's hosted MCP server, `https://www.meterapp.co/api/mcp/rider`, through your host and your own Meter sign-in. The agent sends the arguments of the tools it calls, which can include addresses you ask it to search or book, ride times and booking ids. The plugin is instructions and one server address: it runs no code of its own and sends nothing anywhere else. How Meter handles that data: [privacy policy](https://www.meterapp.co/privacy). To disconnect, remove the connector in your host or revoke it in Meter under Account, Connected apps.

## Links

[Book rides](https://www.meterapp.co/docs/rides) · [Docs](https://www.meterapp.co/docs) · [Plugins](https://www.meterapp.co/docs/plugins) · [Privacy and terms](https://www.meterapp.co/privacy) · [MCP Registry entry](server.json) · [jonathan@welcome.meterapp.co](mailto:jonathan@welcome.meterapp.co)

## License

MIT
