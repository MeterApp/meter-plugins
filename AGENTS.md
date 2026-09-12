# AGENTS.md — the Meter cross-agent plugin

One plugin, packaged natively for Claude Code, Codex and Cursor, plus the
vendor-neutral Open Plugins manifest. This directory is the source of truth and
is published verbatim to the public `MeterApp/meter-plugins` repository, where
these files sit at the repository root. Everything here is customer- and
agent-visible.

## The shape

| Path | Consumed by |
| --- | --- |
| `.claude-plugin/marketplace.json` | `/plugin marketplace add MeterApp/meter-plugins` |
| `.claude-plugin/plugin.json` | `/plugin install meter@meterapp` |
| `.agents/plugins/marketplace.json` | `codex plugin marketplace add MeterApp/meter-plugins` |
| `.codex-plugin/plugin.json` | `codex plugin add meter@meterapp` (also the directory listing) |
| `.cursor-plugin/plugin.json` | Cursor |
| `.plugin/plugin.json` | Open Plugins, and anything else that reads the portable schema |
| `.mcp.json` | Every client: the hosted server. Sign-in is OAuth, handled by the host |
| `skills/` | All of the above, and `npx skills add MeterApp/meter-plugins` |
| `references/` | Deep material the skills link to; `tools.md` and `data-model.md` are generated |

The marketplace `source` is `"./"`: the repository *is* the plugin. There is no
nested plugin directory, which is why one repository serves all four channels.

## Rules

- **Manifest versions move together.** All four `plugin.json` files carry the
  same `version`, and `CHANGELOG.md` gains a `## <version> ` heading in the same
  commit. `scripts/validate_repo.py` fails otherwise.
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

## Safety

- **Every write is a dry run first.** `dry_run` defaults to false on the
  server, so a skill that changes settings must tell the agent to pass
  `dry_run: true` explicitly, show the returned `changes` (`field`, `from`,
  `to`) to the human, wait for an explicit yes, then repeat the call to apply.
- **Fares and payout fractions are money.** No skill may suggest changing them
  without stating the old and the new value, and never in a batch the human did
  not enumerate.
- **A permission error is final.** Skills tell the agent to switch to a tool
  that fits the person's role, not to retry with other arguments or ids.
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
