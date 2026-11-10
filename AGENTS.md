# AGENTS.md — the Meter cross-agent plugins

Two plugins, Meter for Drivers & Fleets and Meter Rides, each packaged natively
for Claude Code and Codex, plus the vendor-neutral Open Plugins manifest. This directory is the source of truth and
is published verbatim to the public `MeterApp/meter-plugins` repository, where
these files sit at the repository root. Everything here is customer- and
agent-visible.

## The shape

The repository root is the marketplace; each plugin is a folder bound to exactly
one hosted MCP server, so the directory can pair it with that server's connector.

| Path | Consumed by |
| --- | --- |
| `.claude-plugin/marketplace.json` | `/plugin marketplace add MeterApp/meter-plugins` |
| `.agents/plugins/marketplace.json` | `codex plugin marketplace add MeterApp/meter-plugins` |
| `fleet/` | The plugin `meter-fleet` (Meter for Drivers & Fleets), server `https://www.meterapp.co/api/mcp/fleet` |
| `rides/` | The plugin `meter-rides` (Meter Rides), server `https://www.meterapp.co/api/mcp/rider` |

Inside each plugin folder:

| Path | Consumed by |
| --- | --- |
| `.claude-plugin/plugin.json` | `/plugin install <plugin>@meterapp-meter`; also the Anthropic Directory listing (`privacyPolicyUrl`, `termsOfServiceUrl`, `supportUrl`) |
| `.codex-plugin/plugin.json` | `codex plugin add <plugin>@meterapp-meter` (also the directory listing) |
| `.plugin/plugin.json` | Open Plugins, and anything else that reads the portable schema |
| `.mcp.json` | Every client: that plugin's one hosted server. Sign-in is OAuth, handled by the host |
| `server.json` | The official MCP Registry entry (`co.meterapp/meter` for fleet, `co.meterapp/meter-rides` for rides), remote-only |
| `skills/` | All of the above, and `npx skills add MeterApp/meter-plugins` |
| `references/` | Deep material the skills link to; `tools.md` and `data-model.md` are generated, with only that server's tools and objects |

A plugin install copies only its own folder, so each one carries its own README,
LICENSE, CHANGELOG, icon and references, and links nothing outside itself.

## Rules

- **One plugin, one server.** Each `.mcp.json` lists exactly its own server, and
  no file in a plugin names the other plugin's server URL; refer to the other
  plugin by name. A skill depends only on its own plugin's server.
- **Versions move together.** All three `plugin.json` files and `server.json` of
  both plugins carry the same `version`, and each `CHANGELOG.md` gains a
  `## <version> ` heading in the same commit. The source repository's validator
  (`scripts/ops/validate-meter-plugin.py`) fails otherwise. A version published to the MCP Registry can never be changed, so
  publish it only from a released version.
- **Listing URLs are real pages on `https://www.meterapp.co`.** The Claude
  manifest's `privacyPolicyUrl`, `termsOfServiceUrl` and `supportUrl` match the
  Codex interface's `privacyPolicyURL`, `termsOfServiceURL` and `supportURL`.
  `/terms` redirects to `/privacy`, which carries the terms of use, so both
  name `/privacy`. Confirm a new URL resolves before using it. OpenAI's
  form caps `displayName` and `shortDescription` at 30 characters.
- **Keep those three Claude manifest fields.** The directory warns that it does
  not recognize them and says no action is needed; they feed the listing. Do
  not remove them to clear the warning.
- **The marketplace is `meterapp-meter`.** Claude Code and Codex identify
  marketplaces by name, so it must not share one with another Meter marketplace
  (Car Image's is `meterapp`, skillhook's `meterapp-skillhook`): whoever added
  one could not add the other. Both marketplace files and every install or
  update command use it; the validator fails otherwise, except in
  a `CHANGELOG.md`, whose migration notes give commands with the old names.
- **Generated references are not edited by hand.** `references/tools.md` and
  `references/data-model.md` and their linked `tools/part-*.md` and `data-model/part-*.md` files come from `pnpm run agent-docs:generate` in the
  source repository's `backend/`; a test there fails when they are stale.
- **Keep reference files below 200 KB.** Anthropic held v1.4.0 because its
  validator could not inspect the 367 KB data-model file (2026-10-27). The
  generator keeps complete DTO sections in smaller linked parts; the plugin
  validator checks the size budget before publication.
- **Product facts do not drift.** Tool names, roles and argument names come from
  the generated references; a skill that quotes them must match. The combined
  `/api/mcp` server was removed and now answers 410. Every published link uses
  `https://www.meterapp.co`.
- **Never link the private source repository.** It 404s for everyone outside
  the org. Link the docs, the generated references, or `jonathan@welcome.meterapp.co`.
- **Skill frontmatter is `name` and `description` only**, the name matches the
  folder, and the description says both when to use the skill *and* when not to;
  that text is the only thing the model routes on. The validator requires at
  least 120 characters.
- **`agents/openai.yaml` stays in sync with its skill.** Declare the MCP
  dependency only for skills that actually call MCP tools; the explainer skill
  reads documentation and must not.
- **OAuth is the only sign-in.** Each `.mcp.json` entry is `type` and `url` and
  nothing else: any added request field turns off the host's OAuth sign-in on a
  directory install. The plugin asks the person for nothing and takes nothing
  from their computer.
- **The directory's policy check is textual.** It holds a plugin over vocabulary
  about sign-in, even in a sentence that denies the thing, history included. So
  say what the plugin does ("signs in with your Meter account in the browser"),
  not what it does not do. The word list lives in the source repository
  (`scripts/ops/scan-meter-plugin.py`), which runs before every publish; keep
  it out of this directory.
- **Only allowed file types.** MeterApp is not a Verified organization, so the
  directory refuses any file but Markdown, text, JSON, YAML and PNG/JPEG/GIF/WebP/ICO
  images (SVG included), plus LICENSE and .gitignore, and refuses scripts and package
  manager files. Validators live in the source repository, and the logo is the PNG
  each Claude manifest names.
- **Never pipe a download into a shell or interpreter.** Anything a workflow runs
  is a committed file.
- **Write for the conversation as well as the terminal.** Claude.ai and ChatGPT
  load one skill and have no shell: say which tool to call, what to show the
  person and when to ask first, and keep CLI commands in their own section.

## Safety

- **Every write requires a saved preview and explicit confirmation.** Set
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
claude plugin validate . --strict
claude plugin validate ./fleet --strict
claude plugin validate ./rides --strict
CODEX_HOME="$(mktemp -d)" codex plugin marketplace add . --json
skills add . --list
```

CI runs all of these on every push. The source repository also runs
`scripts/ops/validate-meter-plugin.py` and `scripts/ops/scan-meter-plugin.py` before
each publish, and `scripts/ops/check-meter-plugin-endpoint.py` on a schedule.

## Releasing

Changes land in the private source repository and are published from there;
`node scripts/ops/publish-plugins.mjs` mirrors this directory to the public
repository. A pull request opened directly against the published repository
would be overwritten on the next release; redirect contributors to an issue.
