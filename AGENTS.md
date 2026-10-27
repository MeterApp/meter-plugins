# AGENTS.md — the Meter cross-agent plugin

One plugin, packaged natively for Claude Code and Codex, plus the
vendor-neutral Open Plugins manifest. This directory is the source of truth and
is published verbatim to the public `MeterApp/meter-plugins` repository, where
these files sit at the repository root. Everything here is customer- and
agent-visible.

## The shape

| Path | Consumed by |
| --- | --- |
| `.claude-plugin/marketplace.json` | `/plugin marketplace add MeterApp/meter-plugins` |
| `.claude-plugin/plugin.json` | `/plugin install meter@meterapp-meter`; also the Anthropic Directory listing (`privacyPolicyUrl`, `termsOfServiceUrl`, `supportUrl`) |
| `.agents/plugins/marketplace.json` | `codex plugin marketplace add MeterApp/meter-plugins` |
| `.codex-plugin/plugin.json` | `codex plugin add meter@meterapp-meter` (also the directory listing) |
| `.plugin/plugin.json` | Open Plugins, and anything else that reads the portable schema |
| `.mcp.json` | Every client: the hosted server. Sign-in is OAuth, handled by the host |
| `server.json` | The official MCP Registry entry (`co.meterapp/meter`, remote-only); published by a human with `mcp-publisher`, never by CI |
| `skills/` | All of the above, and `npx skills add MeterApp/meter-plugins` |
| `references/` | Deep material the skills link to; `tools.md` and `data-model.md` are generated |

The marketplace `source` is `"./"`: the repository *is* the plugin. There is no
nested plugin directory, which is why one repository serves all supported channels.

## Rules

- **Manifest versions move together.** All three `plugin.json` files and
  `server.json` carry the same `version`, and `CHANGELOG.md` gains a
  `## <version> ` heading in the same commit. `scripts/validate_repo.py` fails
  otherwise. A version published to the MCP Registry can never be changed, so
  publish it only from a released version.
- **Listing URLs are real pages on `https://www.meterapp.co`.** The Claude
  manifest's `privacyPolicyUrl`, `termsOfServiceUrl` and `supportUrl` match the
  Codex interface's `privacyPolicyURL`, `termsOfServiceURL` and `supportURL`.
  `/terms` redirects to `/privacy`, which carries the terms of use, so both
  name `/privacy`. Check a new URL with `curl -sIL` before using it. OpenAI's
  form caps `displayName` and `shortDescription` at 30 characters.
- **The marketplace is `meterapp-meter`.** Claude Code and Codex key
  marketplaces by name, so it must not share one with another Meter marketplace
  (Car Image's is `meterapp`, skillhook's `meterapp-skillhook`): whoever added
  one could not add the other. Both marketplace files and every install or
  update command use it; `scripts/validate_repo.py` fails otherwise, except in
  `CHANGELOG.md`, whose migration notes give commands with the old name.
- **Generated references are not edited by hand.** `references/tools.md` and
  `references/data-model.md` come from `pnpm run agent-docs:generate` in the
  source repository's `backend/`; a test there fails when they are stale.
- **Product facts do not drift.** Tool names, roles and argument names come from
  the generated references; a skill that quotes them must match. The MCP URL is
  `https://www.meterapp.co/api/mcp` and every published link uses
  `https://www.meterapp.co`.
- **Never link the private source repository.** It 404s for everyone outside
  the org. Link the docs, the generated references, or `hello@meterapp.co`.
- **Skill frontmatter is `name` and `description` only**, the name matches the
  folder, and the description says both when to use the skill *and* when not to;
  that text is the only thing the model routes on. The validator requires at
  least 120 characters.
- **`agents/openai.yaml` stays in sync with its skill.** Declare the MCP
  dependency only for skills that actually call MCP tools; the explainer skill
  reads documentation and must not.
- **No credential, ever.** There are no API keys in this product. Nothing here
  may contain a token, a `Bearer` header value, a Supabase key or a placeholder
  that looks like one, and no example may put a token in a URL, a file or a prompt.
- **No `Authorization` header and no credential read from the user's machine.**
  Any configured `Authorization` header disables Claude Code's OAuth sign-in on
  a directory install, whatever its value. The Anthropic Directory holds a
  plugin for review ("Uses a credential from the user's machine") when a skill,
  the README or a config reads a key from an environment variable, a file or a
  plugin option and sends it on, examples included. The validator enforces both.
- **Write for the conversation as well as the terminal.** Claude.ai and ChatGPT
  load one skill and have no shell: say which tool to call, what to show the
  person and when to ask first, and keep CLI commands in their own section.

## Safety

- **Every write requires a saved preview and explicit confirmation.** Pass
  `dry_run: true`, save the returned proposal, show every `changes` row
  (`field`, `from`, `to`), wait for an explicit yes, then repeat the intended
  arguments with `proposal_id` and `dry_run: false`. A first call without a live
  proposal writes nothing. Stale or expired proposals need fresh confirmation.
- **Fares and payout fractions are money.** No skill may suggest changing them
  without stating the old and the new value, and never in a batch the human did
  not enumerate.
- **A permission error is final.** Skills tell the agent to switch to a tool
  that fits the person's role, not to retry with other arguments or ids.
- **Rides are booked for the signed-in rider only**, after `search_places`
  results the person confirmed and a `request_ride` preview showing price,
  pickup time, payment and cancellation policy. In third-party hosts nothing is
  paid in the chat: a ride that needs paying for goes to the Meter checkout
  link, and a skill may call it booked only after `list_bookings` or
  `get_ride_status` shows it. Saved-card booking in chat exists only in Meter's
  own CLI and in-app assistant. No skill may ask for, accept or type card
  details, or retry a booking without checking `list_bookings` first.
- **Ids are never guessed.** They come from `whoami`, `list_fleets`,
  `list_trips`, `list_bookings` and `list_fleet_members`.

## Validation

```bash
python3 scripts/validate_repo.py
claude plugin validate . --strict
claude plugin validate .claude-plugin/plugin.json --strict
CODEX_HOME="$(mktemp -d)" codex plugin marketplace add . --json
npx -y skills@latest add . --list
```

CI runs all of these on every push, plus a scheduled check that the hosted MCP
URL in `.mcp.json` still answers with the OAuth challenge.

## Releasing

Changes land in the private source repository and are published from there;
`node scripts/ops/publish-plugins.mjs` mirrors this directory to the public
repository. A pull request opened directly against the published repository
would be overwritten on the next release; redirect contributors to an issue.
