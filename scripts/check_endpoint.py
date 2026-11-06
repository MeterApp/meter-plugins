#!/usr/bin/env python3
"""Check that each plugin's hosted MCP server still offers OAuth sign-in.

The plugins hard-code their server URL in `.mcp.json`. If one moves or breaks,
every install silently stops working, so this runs on a schedule.

For each server: a POST without signing in must answer 401 with a challenge
that names `resource_metadata=` (hosts find the sign-in through it), and the
RFC 9728 metadata at `/.well-known/oauth-protected-resource<path>` must list
`authorization_servers`.

Usage: python3 scripts/check_endpoint.py [fleet] [rides]   (default: both)
"""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGINS = ("fleet", "rides")
TIMEOUT_SECONDS = 30
HEADERS = {"User-Agent": "meter-plugins-endpoint-check"}
REQUEST = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/list"}).encode()


def check_challenge(url: str) -> str | None:
    request = urllib.request.Request(
        url,
        data=REQUEST,
        method="POST",
        headers={
            **HEADERS,
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            return f"expected 401 before sign-in, got {response.status}"
    except urllib.error.HTTPError as answer:
        if answer.code != 401:
            return f"expected 401 before sign-in, got {answer.code}"
        if "resource_metadata=" not in answer.headers.get("WWW-Authenticate", ""):
            return "401 without a resource_metadata challenge"
        return None
    except urllib.error.URLError as failure:
        return f"could not reach the server: {failure.reason}"


def check_metadata(url: str) -> str | None:
    parts = urllib.parse.urlsplit(url)
    metadata = f"{parts.scheme}://{parts.netloc}/.well-known/oauth-protected-resource{parts.path}"
    request = urllib.request.Request(metadata, headers=HEADERS)
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            document = json.load(response)
    except (urllib.error.URLError, json.JSONDecodeError) as failure:
        return f"could not read {metadata}: {failure}"
    servers = document.get("authorization_servers")
    if not isinstance(servers, list) or not servers:
        return f"{metadata} lists no authorization_servers"
    return None


def main(plugins: list[str]) -> int:
    failed = False
    for plugin in plugins:
        if plugin not in PLUGINS:
            print(f"{plugin}: unknown plugin; expected one of {PLUGINS}", file=sys.stderr)
            failed = True
            continue
        config = json.loads((ROOT / plugin / ".mcp.json").read_text(encoding="utf-8"))
        for name, server in config["mcpServers"].items():
            problems = [p for p in (check_challenge(server["url"]), check_metadata(server["url"])) if p]
            for problem in problems:
                print(f"{plugin}/{name}: {problem}", file=sys.stderr)
            if problems:
                failed = True
            else:
                print(f"{plugin}/{name}: {server['url']} answers with the OAuth challenge")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:] or list(PLUGINS)))
