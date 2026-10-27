#!/usr/bin/env python3
"""Validate the cross-agent Meter plugin without modifying anything.

Runs against this directory in the source repository and, unchanged, against
the published `MeterApp/meter-plugins` repository, where these files sit at
the root. Anything that would break an install (a manifest that drifted out
of sync, a skill missing its Codex interface, a relative path pointing at
nothing, a credential-shaped string) fails here rather than for a user.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []

PLUGIN_NAME = "meter"
# Claude Code and Codex key marketplaces by name, so this one must not share
# a name with another Meter marketplace: Car Image's is `meterapp`, skillhook's
# `meterapp-skillhook`.
MARKETPLACE_NAME = "meterapp-meter"
ORIGIN = "https://www.meterapp.co"
MCP_URL = f"{ORIGIN}/api/mcp"
# The source repository is private: a link there 404s for everyone outside the
# org, and `/plugin marketplace add` of a private repo simply fails. Assembled
# from parts so this file is not itself a violation.
PRIVATE_REPO = "/".join(("MeterApp", "meter-repo"))
PUBLIC_REPO = "https://github.com/MeterApp/meter-plugins"

SKILLS = [
    "meter-fleet-insights",
    "meter-fleet-onboarding",
    "meter-settings-changes",
    "meter-driver-personal",
    "meter-api-explainer",
    "meter-ride",
]
# Skills that tell the agent to call an MCP tool must declare the dependency so
# Codex can offer to connect the server when the skill is invoked. The
# explainer reads documentation and must not.
MCP_DEPENDENT = {
    "meter-fleet-insights",
    "meter-fleet-onboarding",
    "meter-settings-changes",
    "meter-driver-personal",
    "meter-ride",
}
# Skills that teach a write must teach the dry_run preview that comes first.
WRITE_SKILLS = {"meter-settings-changes", "meter-fleet-onboarding", "meter-ride"}
# The official MCP Registry entry (registry.modelcontextprotocol.io). The name is
# reverse-DNS for meterapp.co, which the registry verifies before publishing.
REGISTRY_NAME = "co.meterapp/meter"
REGISTRY_SCHEMA = "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json"
# Directory listing pages. https://www.meterapp.co/terms permanently redirects
# to /privacy, which carries the terms of use, so both listings name the final URL.
LISTING_URLS = {
    "privacyPolicyUrl": ("privacyPolicyURL", f"{ORIGIN}/privacy"),
    "termsOfServiceUrl": ("termsOfServiceURL", f"{ORIGIN}/privacy"),
    "supportUrl": ("supportURL", None),
}
GENERATED_REFERENCES = {"references/tools.md", "references/data-model.md"}
GENERATED_REFERENCES.update(
    str(path.relative_to(ROOT))
    for directory in ("data-model", "tools")
    for path in (ROOT / "references" / directory).glob("part-*.md")
)


def error(message: str) -> None:
    ERRORS.append(message)


def load_json(relative: str) -> dict:
    path = ROOT / relative
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        error(f"{relative}: invalid or unreadable JSON: {exc}")
        return {}


def check_path(owner: str, value: object) -> None:
    """A manifest path must be relative, stay inside the plugin, and exist."""
    if not isinstance(value, str) or not value.startswith("./"):
        error(f"{owner}: expected a ./-prefixed relative path, got {value!r}")
        return
    target = (ROOT / value[2:]).resolve()
    try:
        target.relative_to(ROOT.resolve())
    except ValueError:
        error(f"{owner}: path escapes the plugin root")
        return
    if not target.exists():
        error(f"{owner}: referenced path does not exist: {value}")


# --- manifests -------------------------------------------------------------

MANIFESTS = {
    "open": ".plugin/plugin.json",
    "claude": ".claude-plugin/plugin.json",
    "codex": ".codex-plugin/plugin.json",
}
manifests = {surface: load_json(path) for surface, path in MANIFESTS.items()}

versions = {surface: manifest.get("version") for surface, manifest in manifests.items()}
if len(set(versions.values())) != 1 or None in versions.values():
    error(f"manifest versions are not synchronized: {versions}")
else:
    version = next(iter(versions.values()))
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    if f"## {version} " not in changelog:
        error(f"CHANGELOG.md has no entry for {version}")

for surface, manifest in manifests.items():
    if manifest.get("name") != PLUGIN_NAME:
        error(f"{surface} manifest name must be {PLUGIN_NAME}")
    if manifest.get("repository") not in (None, PUBLIC_REPO):
        error(f"{surface} manifest repository must be {PUBLIC_REPO}")
    if len(manifest.get("description", "")) < 120:
        error(f"{surface} manifest description is too short for directory listings")
    for field in ("skills", "mcpServers", "logo"):
        if isinstance(manifest.get(field), str):
            check_path(f"{surface}.{field}", manifest[field])
    interface = manifest.get("interface", {})
    if isinstance(interface, dict):
        for field in ("composerIcon", "logo", "logoDark"):
            if field in interface:
                check_path(f"{surface}.interface.{field}", interface[field])

# OpenAI's plugin submission refuses longer listing text.
codex_interface = manifests["codex"].get("interface", {})
for field, limit in (("displayName", 30), ("shortDescription", 30), ("longDescription", 4000)):
    value = codex_interface.get(field, "")
    if not value or len(value) > limit:
        error(f"codex interface {field} must be 1-{limit} characters, got {len(value)}")

# --- directory listing -----------------------------------------------------

# The Anthropic Directory reads these from the Claude manifest and warns when the
# privacy policy is missing; OpenAI requires them for review. Both listings name
# the same pages.
for field, (codex_field, required) in LISTING_URLS.items():
    value = manifests["claude"].get(field)
    if not isinstance(value, str) or not value.startswith(f"{ORIGIN}/") or (required and value != required):
        error(f"claude manifest {field} must be {required or 'a page on ' + ORIGIN}, got {value!r}")
    elif value != codex_interface.get(codex_field):
        error(f"claude manifest {field} must match the codex interface {codex_field}")

# --- marketplaces ----------------------------------------------------------

claude_marketplace = load_json(".claude-plugin/marketplace.json")
if claude_marketplace.get("name") != MARKETPLACE_NAME:
    error(f".claude-plugin/marketplace.json name must be {MARKETPLACE_NAME}")
claude_plugins = claude_marketplace.get("plugins", [])
if len(claude_plugins) != 1 or claude_plugins[0].get("name") != PLUGIN_NAME:
    error(f".claude-plugin/marketplace.json must list exactly one plugin named {PLUGIN_NAME}")
elif claude_plugins[0].get("source") != "./":
    error('.claude-plugin/marketplace.json source must be "./" (the repository is the plugin)')

agents_marketplace = load_json(".agents/plugins/marketplace.json")
if agents_marketplace.get("name") != MARKETPLACE_NAME:
    error(f".agents/plugins/marketplace.json name must be {MARKETPLACE_NAME}")
agents_plugins = agents_marketplace.get("plugins", [])
if len(agents_plugins) != 1 or agents_plugins[0].get("name") != PLUGIN_NAME:
    error(f".agents/plugins/marketplace.json must list exactly one plugin named {PLUGIN_NAME}")

# --- MCP server ------------------------------------------------------------

server = load_json(".mcp.json").get("mcpServers", {}).get(PLUGIN_NAME, {})
# OAuth is negotiated by the host from the server's 401 challenge, so the
# entry is URL-only: a `headers` block would mean someone pasted a credential.
expected = {"type": "http", "url": MCP_URL}
if server != expected:
    error(f".mcp.json must configure the hosted server exactly as {expected}, got {server}")

# Any configured Authorization header disables Claude Code's OAuth sign-in on a
# directory install, whatever its value, even when the variable it names is
# unset. Nothing here may configure one, in any manifest or MCP file.
def authorization_headers(node: object, owner: str) -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "headers":
                if isinstance(value, dict):
                    names = list(value)
                elif isinstance(value, list):
                    names = [item.get("name", "") for item in value if isinstance(item, dict)]
                else:
                    names = []
                if any(str(name).lower() == "authorization" for name in names):
                    error(f"{owner}: an Authorization header disables OAuth sign-in")
            authorization_headers(value, owner)
    elif isinstance(node, list):
        for item in node:
            authorization_headers(item, owner)


for relative in [*MANIFESTS.values(), ".mcp.json", "server.json"]:
    authorization_headers(load_json(relative), relative)

# --- MCP Registry entry ----------------------------------------------------

registry = load_json("server.json")
if registry.get("$schema") != REGISTRY_SCHEMA:
    error(f"server.json $schema must be {REGISTRY_SCHEMA}")
if registry.get("name") != REGISTRY_NAME:
    error(f"server.json name must be {REGISTRY_NAME}")
# A published registry version can never change, so it moves with the plugin.
if registry.get("version") != manifests["claude"].get("version"):
    error("server.json version must match the manifest version")
if not 1 <= len(registry.get("description", "")) <= 100:
    error("server.json description must be 1-100 characters")
if registry.get("remotes") != [{"type": "streamable-http", "url": MCP_URL}]:
    error(f"server.json remotes must be exactly one streamable-http remote at {MCP_URL}")
if "packages" in registry:
    error("server.json must not list packages: the server is remote-only")
for icon in registry.get("icons", []):
    if not str(icon.get("src", "")).startswith(f"{ORIGIN}/"):
        error(f"server.json icons must be served from {ORIGIN}")

# --- skills ----------------------------------------------------------------

skills_root = ROOT / "skills"
found = sorted(path.name for path in skills_root.iterdir() if path.is_dir())
if found != sorted(SKILLS):
    error(f"skills/ must contain exactly {sorted(SKILLS)}, found {found}")

frontmatter = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
for name in found:
    skill_dir = skills_root / name
    skill_file = skill_dir / "SKILL.md"
    openai_file = skill_dir / "agents" / "openai.yaml"

    if not skill_file.is_file():
        error(f"{name}: missing SKILL.md")
        continue
    if not openai_file.is_file():
        error(f"{name}: missing agents/openai.yaml")
        continue

    content = skill_file.read_text(encoding="utf-8")
    match = frontmatter.match(content)
    if not match:
        error(f"{name}: invalid YAML frontmatter boundary")
        continue

    metadata: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        key, separator, value = line.partition(":")
        if not separator:
            error(f"{name}: malformed frontmatter line: {line}")
            continue
        value = value.strip()
        # An unquoted value containing ": " is not valid YAML. Claude Code
        # tolerates it, but the skills CLI silently skips the skill.
        if ": " in value and not (value.startswith('"') and value.endswith('"')):
            error(f"{name}: quote the {key.strip()} value; it contains ': '")
        metadata[key.strip()] = value.strip("\"'")

    if set(metadata) != {"name", "description"}:
        error(f"{name}: frontmatter must contain only name and description")
    if metadata.get("name") != name:
        error(f"{name}: frontmatter name does not match the folder")
    # A short description is the single biggest cause of a skill never being
    # picked: the model routes on this text alone.
    if len(metadata.get("description", "")) < 120:
        error(f"{name}: description is too short for reliable discovery")
    if "do not use" not in metadata.get("description", "").lower():
        error(f"{name}: description must say when NOT to use the skill")

    openai = openai_file.read_text(encoding="utf-8")
    if f"${name}" not in openai:
        error(f"{name}: default_prompt must mention ${name}")
    if name in MCP_DEPENDENT:
        if MCP_URL not in openai:
            error(f"{name}: must declare the hosted MCP dependency")
    elif "dependencies:" in openai:
        error(f"{name}: declares an MCP dependency it does not need")

    # Writes without a dry run are the one thing a skill must never teach.
    body = content[match.end() :]
    if name in WRITE_SKILLS and "dry_run" not in body:
        error(f"{name}: a skill that changes settings must describe the dry_run sequence")

# --- generated references --------------------------------------------------

for relative in GENERATED_REFERENCES:
    path = ROOT / relative
    if not path.is_file():
        error(f"{relative}: missing generated reference (run agent-docs:generate)")
    elif "Generated from the `@meterapp/meter-sdk`" not in path.read_text(encoding="utf-8"):
        error(f"{relative}: does not look generated; do not edit by hand")

# --- local links -----------------------------------------------------------

# The directory could not inspect the former 367 KB data-model reference.
# Keep readable references below a conservative 200 KB per-file budget.
for reference in (ROOT / "references").rglob("*.md"):
    if reference.stat().st_size > 200_000:
        error(f"{reference.relative_to(ROOT)}: split generated references below 200 KB for directory inspection")

link = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
for markdown in ROOT.rglob("*.md"):
    if ".git" in markdown.parts:
        continue
    for target in link.findall(markdown.read_text(encoding="utf-8")):
        target = target.strip().strip("<>").split("#", 1)[0]
        if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.IGNORECASE):
            continue
        if not (markdown.parent / target).resolve().exists():
            error(f"{markdown.relative_to(ROOT)}: broken local link {target}")

# --- things that must never ship -------------------------------------------

FORBIDDEN = {
    PRIVATE_REPO: "a link to the private source repository",
    "vercel.app": "a deployment URL (use www.meterapp.co)",
    "https://meterapp.co": "the non-canonical origin (use https://www.meterapp.co)",
    "[TODO": "an unresolved placeholder",
    "Authorization: Bearer ey": "something shaped like a real token",
}
# Anything shaped like a credential. Deliberately broad: a false positive costs
# a reworded example; a true positive published is a leaked secret.
SECRET_PATTERNS = {
    re.compile(r"\beyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}"): "a JWT",
    re.compile(r"\bsb_(?:secret|publishable)_[A-Za-z0-9_-]{10,}"): "a Supabase API key",
    re.compile(r"\b(?:sk|rk)_(?:live|test)_[A-Za-z0-9]{16,}"): "a Stripe key",
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}"): "a GitHub token",
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"): "an AWS access key",
    re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"): "a Google API key",
    re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}"): "a Slack token",
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"): "a private key",
    re.compile(r"(?i)\b(?:api[_-]?key|secret|password|token)\s*[:=]\s*[\"'][A-Za-z0-9_\-./+]{16,}[\"']"): "an assigned credential",
}
# An install or update command that names another marketplace fails for
# whoever copies it. CHANGELOG.md keeps the old name in its migration notes.
MARKETPLACE_REFERENCES = (
    re.compile(rf"(?<![\w/@.-]){PLUGIN_NAME}@([a-z0-9][a-z0-9-]*)"),
    re.compile(r"\bmarketplace (?:update|upgrade) ([a-z0-9][a-z0-9-]*)"),
)

# The Anthropic Directory holds a plugin for review ("Uses a credential from the
# user's machine") when anything in it reads a key or secret from environment
# variables or files and sends it on, examples included. An agent uses the
# connection the host authenticated; the CLI signs in with `meter login`.
CREDENTIAL_READS = re.compile(
    r"\$\{?[A-Z][A-Z0-9_]*(?:KEY|SECRET|TOKEN|PASSWORD)\b"  # $METER_API_KEY, ${GITHUB_TOKEN}
    r"|process\.env(?:\.|\[\s*['\"])[A-Z0-9_]*(?:KEY|SECRET|TOKEN|PASSWORD)\b"
    r"|\bos\.(?:environ|getenv)\b"
    r"|Deno\.env\.get\("
    r"|import\.meta\.env\.[A-Z0-9_]*(?:KEY|SECRET|TOKEN|PASSWORD)\b"
    r"|\$\{user_config\."  # Meter takes no key, not even an optional one
)

for path in sorted(ROOT.rglob("*")):
    if not path.is_file() or ".git" in path.parts or path.suffix in {".svg", ".pyc"}:
        continue
    if path.resolve() == Path(__file__).resolve():
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    relative = path.relative_to(ROOT)
    for needle, label in FORBIDDEN.items():
        if needle in text:
            error(f"{relative}: contains {label}: {needle}")
    for pattern, label in SECRET_PATTERNS.items():
        if pattern.search(text):
            error(f"{relative}: contains {label}")
    for match in CREDENTIAL_READS.finditer(text):
        line = text.count("\n", 0, match.start()) + 1
        error(f"{relative}:{line}: reads a credential from the user's machine: {match.group(0)}")
    if relative != Path("CHANGELOG.md"):
        for pattern in MARKETPLACE_REFERENCES:
            for name in pattern.findall(text):
                if name != MARKETPLACE_NAME:
                    error(f"{relative}: names the marketplace {name}; it is {MARKETPLACE_NAME}")

if ERRORS:
    print("Plugin validation failed:", file=sys.stderr)
    for item in ERRORS:
        print(f"- {item}", file=sys.stderr)
    raise SystemExit(1)

print(f"Plugin validation passed: {len(manifests)} manifests, {len(found)} skills")
