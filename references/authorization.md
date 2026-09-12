# Authorization

Meter has no API keys for agents. Every request to `https://www.meterapp.co/api/mcp` carries an OAuth 2.1 access token that belongs to a signed-in Meter user, and the server answers exactly what that person could see or do in the Meter apps.

## The flow, as hosts implement it

1. **Challenge.** An unauthenticated `POST /api/mcp` returns `401` with
   `WWW-Authenticate: Bearer resource_metadata="https://www.meterapp.co/.well-known/oauth-protected-resource", error="invalid_token"`.
2. **Protected-resource metadata (RFC 9728).** `GET https://www.meterapp.co/.well-known/oauth-protected-resource` returns the `resource`, `authorization_servers` (Supabase Auth, `https://<project>.supabase.co/auth/v1`), `bearer_methods_supported: ["header"]` and `scopes_supported` (`openid`, `email`, `profile`). The path-suffixed form `/.well-known/oauth-protected-resource/api/mcp` is also served.
3. **Authorization-server metadata.** `GET <issuer>/.well-known/oauth-authorization-server` lists the authorization, token and registration endpoints. PKCE with `S256` is required. Dynamic client registration is enabled so MCP hosts can register themselves.
4. **Consent.** The person's browser opens the authorization URL; they sign in to Meter and approve the connector at `https://www.meterapp.co/oauth/consent`.
5. **Tokens.** The host exchanges the code for an access token and a refresh token and sends `Authorization: Bearer <access_token>` on every request. Refresh is the host's job; the server never sees a refresh token.

Claude.ai and Claude Desktop connectors, ChatGPT connectors, Claude Code (`claude mcp add --transport http meter https://www.meterapp.co/api/mcp`), Cursor and Codex do all of this from the URL alone. The CLI (`npx @meterapp/meter login`) runs the same flow from a terminal and stores the session locally.

## Roles

A person's role comes from their fleet membership and is evaluated per call.

| Role (as the tool catalog names it) | Who |
| --- | --- |
| `anyone` | any signed-in Meter user, including riders and solo drivers |
| `fleet_member` | owner, admin or driver of the fleet passed as `fleet_id` |
| `fleet_admin` | owner or admin of a fleet that is operational (onboarded, billing active) |
| `participant` | a fleet owner or admin, or the driver or rider on that specific trip or booking |
| `self` | the signed-in person, acting on their own record |

Write tools follow the same roles: `update_fleet_settings`, `update_booking_settings`, `update_ride_option` and `assign_vehicle` need `fleet_admin`; `update_my_profile` and `update_my_availability` only ever touch the caller's own record. Every write is attributed to the signed-in person in Meter's audit trail (fare edits land in the fare audit log with them as the actor) exactly as if they had used the app.

Within a result, some fields are further restricted (`roles` in the data model): for example a booking's rider contact details appear only for fleet owners and admins, the assigned driver and the rider themselves.

## Errors an agent will meet

| `structuredContent.code` | Meaning | Do |
| --- | --- | --- |
| `unauthenticated` | no or expired token | ask the human to reconnect the connector; never ask them to paste a token |
| `forbidden` | the role does not allow this | switch to a tool that fits the role; do not retry with other ids |
| `not_found` | unknown id, or one this person may not see (indistinguishable on purpose) | take ids from earlier results |
| `fleet_required` | the person belongs to several fleets | `list_fleets`, ask which, pass `fleet_id` |
| `fleet_not_operational` | onboarding or billing incomplete | own-data tools still work; onboarding skill for the rest |
| `invalid_argument` | schema violation | `describe_api` with the tool name, fix, retry once |

## Disconnecting

Removing the connector in the host (or `logout` in the CLI) discards that host's token. Other devices and the Meter apps are unaffected.

## What never leaves the server

Every result is an allowlisted object validated against a public schema (see [data-model.md](data-model.md)). Payment-provider ids, GPS traces, internal notes, who-did-what attribution ids, join codes and invitation tokens, admin and test-account flags, and device or app-version fields are never returned to anyone.
