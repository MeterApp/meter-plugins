---
name: meter-api-explainer
description: "Explain how Meter's agent surface works and what its data means, using the self-documenting describe_api and explain_data tools and the machine-readable docs (llms.txt, llms-full.txt, agents.md, openapi-mcp.json). Covers \"how do I connect\", \"which tool answers X\", \"what does this field mean\", OAuth sign-in, roles, and drafting an integration or client against the MCP server. Use for questions about the API, its tools, fields, authentication or integration code; do not use to actually answer a fleet question (meter-fleet-insights), change settings (meter-settings-changes) or onboard a fleet (meter-fleet-onboarding)."
---

# Explaining the Meter API

Meter's agent surface is one remote MCP server, `https://www.meterapp.co/api/mcp`, secured with OAuth 2.1 (PKCE). It is self-documenting, and the same documentation is published as static files. Use both.

## Ask the server

When the `meter` MCP server is connected:

- `describe_api` with no arguments returns a compact domain index with tool counts and listed tool names. Use `domain: "<domain>"` to browse its tools, access, risk and sensitive-field escalations; use `tool: "<name>"` for full detail including arguments, an example call and result fields. Choose one selector. Responses are capped at 64 KB; if truncated, request a tool or use `explain_data` for a specific field.
- `explain_data` with `tool` (and optionally `field`, a name or dot path like `items.pickup.address`) returns the meaning, JSON type, unit, allowed values and role visibility of result fields, generated from the schemas the server validates against.
- `whoami` shows what the signed-in person can do here.

Quote these results rather than paraphrasing from memory; they are the current truth for the connected server version.

## Read the published docs

Without a connection, or when drafting code, read the published files. They are generated from the same catalog:

| File | Use it for |
| --- | --- |
| `https://www.meterapp.co/llms.txt` | one-page index: endpoint, integrations, one line per tool, rules |
| `https://www.meterapp.co/llms-full.txt` | everything: OAuth flow, transport, every tool with arguments and result fields, error codes, data model |
| `https://www.meterapp.co/agents.md` | tool table (name, roles, writes?), authorization model, safety rules, the dry_run convention |
| `https://www.meterapp.co/openapi-mcp.json` | OpenAPI 3.1: the JSON-RPC envelope, the `oauth2` security scheme, JSON Schemas for every tool under `x-mcp` and `components.schemas` |
| `https://www.meterapp.co/.well-known/oauth-protected-resource` | which authorization server issues tokens (RFC 9728) |

Human pages: `https://www.meterapp.co/docs`, `/docs/mcp`, `/docs/cli`, `/docs/plugins`, `/docs/authentication`, `/docs/data`.

## Explaining authentication

There are no API keys. Describe the flow in these terms:

1. The client POSTs to `/api/mcp` without a token and gets 401 with `WWW-Authenticate: Bearer resource_metadata="https://www.meterapp.co/.well-known/oauth-protected-resource"`.
2. That document names the authorization server (Supabase Auth) and scopes; `<issuer>/.well-known/oauth-authorization-server` lists its endpoints. PKCE is required; dynamic client registration is available.
3. The person signs in and approves the connector at `https://www.meterapp.co/oauth/consent`; the client exchanges the code for tokens and sends `Authorization: Bearer <access_token>`.

Tokens carry the person's own permissions: owners and admins see fleet-wide data, drivers and riders their own. See [references/authorization.md](../../references/authorization.md).

## Drafting an integration

- Transport: one JSON-RPC 2.0 message per POST, `Accept: application/json, text/event-stream`, JSON responses, stateless (no session id). Methods `initialize`, `tools/list`, `tools/call`, `ping`.
- Prefer an MCP client library. In TypeScript, `@meterapp/meter-sdk` (`MeterMcpClient`) speaks this protocol and ships the same zod schemas and typed tool inputs; the CLI `npx @meterapp/meter` wraps it for terminals (`meter call <tool> --<field> <value> [--dry-run]` calls any tool, `meter describe` prints the offline catalog reference and `meter explain` prints field documentation, `meter mcp` is a local stdio bridge).
- Write tools (`update_fleet_settings`, `update_booking_settings`, `update_ride_option`, `assign_vehicle`, `update_my_profile`, `update_my_availability`) require a saved proposal and return `{ status, applied, dry_run, changes: [{ field, from, to }], proposal?, <object> }`; `get_onboarding_checklist` is the read tool that names which of them completes each setup step. Explain preview with `dry_run: true`, display of all changes, explicit human confirmation, and repetition of intended arguments with `proposal_id` and `dry_run: false`. A first call without a live proposal writes nothing; stale or expired proposals need fresh confirmation.
- Validate arguments against the tool's `inputSchema` from `openapi-mcp.json` before calling; handle the error codes listed in `llms-full.txt` (`unauthenticated`, `forbidden`, `not_found`, `invalid_argument`, `fleet_required`, `fleet_not_operational`, `internal_error`) using the `Next:` guidance the server returns.
- Never hardcode ids, and never store tokens in code or config files. Point at the OAuth flow instead.

## Boundaries

- This skill explains; it does not run fleet queries or make changes. Hand over to the other Meter skills for that.
- Do not invent tools, arguments or fields. If a question cannot be answered from `describe_api`, `explain_data` or the published files, say so and suggest `hello@meterapp.co`.

## References

- [Tool catalog](../../references/tools.md) (generated)
- [Data model](../../references/data-model.md) (generated)
- [Authorization](../../references/authorization.md)
- [Safety](../../references/safety.md)
