# Authorization

Agents sign in to Meter the same way people do. Every request to `https://www.meterapp.co/api/mcp/rider` carries an OAuth 2.1 access grant that belongs to a signed-in Meter user, issued to the host after the person approves it, and the server answers only for that person.

## The flow, as hosts implement it

1. **Challenge.** A `POST /api/mcp/rider` before signing in returns `401` with a challenge that names the server's metadata document, `https://www.meterapp.co/.well-known/oauth-protected-resource/api/mcp/rider`.
2. **Protected-resource metadata (RFC 9728).** That document returns the `resource`, `authorization_servers` (Supabase Auth, `https://<project>.supabase.co/auth/v1`) and `scopes_supported` (`openid`, `email`, `profile`).
3. **Authorization-server metadata.** `GET <issuer>/.well-known/oauth-authorization-server` lists the authorization server's endpoints, including dynamic registration. PKCE with `S256` is required.
4. **Consent.** The person's browser opens the authorization URL; they sign in to Meter and approve the connector at `https://www.meterapp.co/oauth/consent`.
5. **Access grant.** The host exchanges the code for an access grant, sends it with every request as RFC 6750 describes, and renews it itself.

Claude.ai and Claude Desktop connectors, ChatGPT connectors, Claude Code (`claude mcp add --transport http meter-rides https://www.meterapp.co/api/mcp/rider`) and Codex do all of this from the URL alone.

## Who can see what

The server always acts as the signed-in rider. Bookings, quotes and ratings are that person's own; a booking made by someone else answers `not_found`. A driver's or fleet owner's own work is on the Meter for Drivers & Fleets server, with its own plugin.

## Errors an agent will meet

| `structuredContent.code` | Meaning | Do |
| --- | --- | --- |
| `unauthenticated` | not signed in, or the sign-in expired | ask the person to reconnect the connector; never ask them to paste anything |
| `forbidden` | this person may not do that | stop; do not retry with other ids |
| `not_found` | unknown id, or one this person may not see (indistinguishable on purpose) | take ids from earlier results |
| `invalid_argument` | schema violation | `describe_api` with the tool name, fix, retry once |

## Disconnecting

Removing the connector in the host ends that host's sign-in. Other devices and the Meter apps are unaffected.

## What never leaves the server

Every result is an allowlisted object validated against a public schema (see [data-model.md](data-model.md)). Payment-provider ids, GPS traces, internal notes and device fields are never returned to anyone.
