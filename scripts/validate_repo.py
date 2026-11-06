#!/usr/bin/env python3
"""Validate the cross-agent Meter plugins without modifying anything.

Runs against this directory in the source repository and, unchanged, against
the published `MeterApp/meter-plugins` repository, where these files sit at
the root. Anything that would break an install (a manifest that drifted out
of sync, a skill missing its Codex interface, a relative path pointing at
nothing, a plugin bound to the wrong server) fails here rather than for a user.
The source repository also runs `scripts/ops/scan-meter-plugin.py` before
publishing, which is not published.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []

# Claude Code and Codex identify marketplaces by name, so this one must not share
# a name with another Meter marketplace: Car Image's is `meterapp`, skillhook's
# `meterapp-skillhook`.
MARKETPLACE_NAME = "meterapp-meter"
ORIGIN = "https://www.meterapp.co"
# The source repository is private: a link there 404s for everyone outside the
# org, and `/plugin marketplace add` of a private repo simply fails. Assembled
# from parts so this file is not itself a violation.
PRIVATE_REPO = "/".join(("MeterApp", "meter-repo"))
PUBLIC_REPO = "https://github.com/MeterApp/meter-plugins"
REGISTRY_SCHEMA = "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json"
# Directory listing pages. https://www.meterapp.co/terms permanently redirects
# to /privacy, which carries the terms of use, so both listings name the final URL.
LISTING_URLS = {
    "privacyPolicyUrl": ("privacyPolicyURL", f"{ORIGIN}/privacy"),
    "termsOfServiceUrl": ("termsOfServiceURL", f"{ORIGIN}/privacy"),
    "supportUrl": ("supportURL", None),
}


@dataclass(frozen=True)
class Plugin:
    folder: str
    name: str
    display_name: str
    server_url: str
    # The official MCP Registry entry (registry.modelcontextprotocol.io). The name
    # is reverse-DNS for meterapp.co, which the registry verifies before publishing.
    registry_name: str
    # Skills that tell the agent to call an MCP tool declare the plugin's server
    # so Codex can offer to connect it. The explainer reads documentation and must not.
    skills: frozenset[str]
    documentation_skills: frozenset[str] = frozenset()
    # Skills that teach a write must teach the dry_run preview that comes first.
    write_skills: frozenset[str] = frozenset()


# One plugin, one hosted server: the directory pairs each with its own connector.
PLUGINS = (
    Plugin(
        folder="fleet",
        name="meter-fleet",
        display_name="Meter for Drivers & Fleets",
        server_url=f"{ORIGIN}/api/mcp/fleet",
        registry_name="co.meterapp/meter",
        skills=frozenset({"meter-fleet-insights", "meter-fleet-onboarding", "meter-settings-changes", "meter-driver-personal"}),
        documentation_skills=frozenset({"meter-api-explainer"}),
        write_skills=frozenset({"meter-settings-changes", "meter-fleet-onboarding"}),
    ),
    Plugin(
        folder="rides",
        name="meter-rides",
        display_name="Meter Rides",
        server_url=f"{ORIGIN}/api/mcp/rider",
        registry_name="co.meterapp/meter-rides",
        skills=frozenset({"meter-ride", "meter-rider-personal"}),
        write_skills=frozenset({"meter-ride", "meter-rider-personal"}),
    ),
)
MANIFESTS = {
    "open": ".plugin/plugin.json",
    "claude": ".claude-plugin/plugin.json",
    "codex": ".codex-plugin/plugin.json",
}
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def error(message: str) -> None:
    ERRORS.append(message)


def load_json(relative: str) -> dict:
    path = ROOT / relative
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        error(f"{relative}: invalid or unreadable JSON: {exc}")
        return {}


def check_path(owner: str, plugin_root: Path, value: object) -> None:
    """A manifest path must be relative, stay inside the plugin, and exist."""
    if not isinstance(value, str) or not value.startswith("./"):
        error(f"{owner}: expected a ./-prefixed relative path, got {value!r}")
        return
    target = (plugin_root / value[2:]).resolve()
    try:
        target.relative_to(plugin_root.resolve())
    except ValueError:
        error(f"{owner}: path escapes the plugin root")
        return
    if not target.exists():
        error(f"{owner}: referenced path does not exist: {value}")


def check_manifests(plugin: Plugin, version: object) -> dict[str, dict]:
    root = ROOT / plugin.folder
    manifests = {surface: load_json(f"{plugin.folder}/{path}") for surface, path in MANIFESTS.items()}
    for surface, manifest in manifests.items():
        owner = f"{plugin.folder} {surface} manifest"
        if manifest.get("version") != version:
            error(f"{owner}: version must be {version}, got {manifest.get('version')}")
        if manifest.get("name") != plugin.name:
            error(f"{owner}: name must be {plugin.name}")
        if manifest.get("repository") not in (None, PUBLIC_REPO):
            error(f"{owner}: repository must be {PUBLIC_REPO}")
        if len(manifest.get("description", "")) < 120:
            error(f"{owner}: description is too short for directory listings")
        for field in ("skills", "mcpServers", "logo"):
            if isinstance(manifest.get(field), str):
                check_path(f"{owner}.{field}", root, manifest[field])
        interface = manifest.get("interface", {})
        if isinstance(interface, dict):
            for field in ("composerIcon", "logo", "logoDark"):
                if field in interface:
                    check_path(f"{owner}.interface.{field}", root, interface[field])

    if manifests["claude"].get("displayName") != plugin.display_name:
        error(f"{plugin.folder}: claude manifest displayName must be {plugin.display_name}")

    changelog = root / "CHANGELOG.md"
    if not changelog.is_file() or f"## {version} " not in changelog.read_text(encoding="utf-8"):
        error(f"{plugin.folder}/CHANGELOG.md has no entry for {version}")
    for required in ("README.md", "LICENSE", "assets/logo.svg"):
        if not (root / required).is_file():
            error(f"{plugin.folder}/{required} is missing; an install copies only the plugin folder")

    # OpenAI's plugin submission refuses longer listing text.
    codex_interface = manifests["codex"].get("interface", {})
    if codex_interface.get("displayName") != plugin.display_name:
        error(f"{plugin.folder}: codex interface displayName must be {plugin.display_name}")
    for field, limit in (("displayName", 30), ("shortDescription", 30), ("longDescription", 4000)):
        value = codex_interface.get(field, "")
        if not value or len(value) > limit:
            error(f"{plugin.folder}: codex interface {field} must be 1-{limit} characters, got {len(value)}")

    # The Anthropic Directory reads these from the Claude manifest and warns when
    # the privacy policy is missing; OpenAI requires them for review. Both listings
    # name the same pages.
    for field, (codex_field, required) in LISTING_URLS.items():
        value = manifests["claude"].get(field)
        if not isinstance(value, str) or not value.startswith(f"{ORIGIN}/") or (required and value != required):
            error(f"{plugin.folder}: claude manifest {field} must be {required or 'a page on ' + ORIGIN}, got {value!r}")
        elif value != codex_interface.get(codex_field):
            error(f"{plugin.folder}: claude manifest {field} must match the codex interface {codex_field}")
    return manifests


def check_server(plugin: Plugin, version: object) -> None:
    # OAuth is negotiated by the host from the server's 401 answer, so the entry
    # is URL-only, and each plugin is bound to exactly its own server.
    servers = load_json(f"{plugin.folder}/.mcp.json").get("mcpServers", {})
    expected = {plugin.name: {"type": "http", "url": plugin.server_url}}
    if servers != expected:
        error(f"{plugin.folder}/.mcp.json must configure exactly {expected}, got {servers}")

    registry = load_json(f"{plugin.folder}/server.json")
    owner = f"{plugin.folder}/server.json"
    if registry.get("$schema") != REGISTRY_SCHEMA:
        error(f"{owner}: $schema must be {REGISTRY_SCHEMA}")
    if registry.get("name") != plugin.registry_name:
        error(f"{owner}: name must be {plugin.registry_name}")
    if registry.get("title") != plugin.display_name:
        error(f"{owner}: title must be {plugin.display_name}")
    # A published registry version can never change, so it moves with the plugin.
    if registry.get("version") != version:
        error(f"{owner}: version must match the manifest version")
    if not 1 <= len(registry.get("description", "")) <= 100:
        error(f"{owner}: description must be 1-100 characters")
    if registry.get("remotes") != [{"type": "streamable-http", "url": plugin.server_url}]:
        error(f"{owner}: remotes must be exactly one streamable-http remote at {plugin.server_url}")
    if "packages" in registry:
        error(f"{owner}: must not list packages: the server is remote-only")
    for icon in registry.get("icons", []):
        if not str(icon.get("src", "")).startswith(f"{ORIGIN}/"):
            error(f"{owner}: icons must be served from {ORIGIN}")


def check_skills(plugin: Plugin) -> int:
    skills_root = ROOT / plugin.folder / "skills"
    expected = sorted(plugin.skills | plugin.documentation_skills)
    found = sorted(path.name for path in skills_root.iterdir() if path.is_dir()) if skills_root.is_dir() else []
    if found != expected:
        error(f"{plugin.folder}/skills must contain exactly {expected}, found {found}")

    for name in found:
        owner = f"{plugin.folder}/{name}"
        skill_dir = skills_root / name
        skill_file = skill_dir / "SKILL.md"
        openai_file = skill_dir / "agents" / "openai.yaml"

        if not skill_file.is_file():
            error(f"{owner}: missing SKILL.md")
            continue
        if not openai_file.is_file():
            error(f"{owner}: missing agents/openai.yaml")
            continue

        content = skill_file.read_text(encoding="utf-8")
        match = FRONTMATTER.match(content)
        if not match:
            error(f"{owner}: invalid YAML frontmatter boundary")
            continue

        metadata: dict[str, str] = {}
        for line in match.group(1).splitlines():
            if not line.strip():
                continue
            field, separator, value = line.partition(":")
            if not separator:
                error(f"{owner}: malformed frontmatter line: {line}")
                continue
            value = value.strip()
            # An unquoted value containing ": " is not valid YAML. Claude Code
            # tolerates it, but the skills CLI silently skips the skill.
            if ": " in value and not (value.startswith('"') and value.endswith('"')):
                error(f"{owner}: quote the {field.strip()} value; it contains ': '")
            metadata[field.strip()] = value.strip("\"'")

        if set(metadata) != {"name", "description"}:
            error(f"{owner}: frontmatter must contain only name and description")
        if metadata.get("name") != name:
            error(f"{owner}: frontmatter name does not match the folder")
        # A short description is the single biggest cause of a skill never being
        # picked: the model routes on this text alone.
        if len(metadata.get("description", "")) < 120:
            error(f"{owner}: description is too short for reliable discovery")
        if "do not use" not in metadata.get("description", "").lower():
            error(f"{owner}: description must say when NOT to use the skill")

        openai = openai_file.read_text(encoding="utf-8")
        if f"${name}" not in openai:
            error(f"{owner}: default_prompt must mention ${name}")
        if name in plugin.skills:
            if f'value: "{plugin.name}"' not in openai or plugin.server_url not in openai:
                error(f"{owner}: must declare the {plugin.name} MCP dependency")
            if openai.count('type: "mcp"') != 1:
                error(f"{owner}: must depend on {plugin.name} only")
        elif "dependencies:" in openai:
            error(f"{owner}: declares an MCP dependency it does not need")

        # Writes without a dry run are the one thing a skill must never teach.
        if name in plugin.write_skills and "dry_run" not in content[match.end() :]:
            error(f"{owner}: a skill that changes settings must describe the dry_run sequence")
    return len(found)


def check_references(plugin: Plugin) -> None:
    references = ROOT / plugin.folder / "references"
    generated = [references / "tools.md", references / "data-model.md"]
    for directory in ("data-model", "tools"):
        generated.extend((references / directory).glob("part-*.md"))
    for path in generated:
        relative = path.relative_to(ROOT)
        if not path.is_file():
            error(f"{relative}: missing generated reference (run agent-docs:generate)")
        elif "Generated from the `@meterapp/meter-sdk`" not in path.read_text(encoding="utf-8"):
            error(f"{relative}: does not look generated; do not edit by hand")
    # The directory could not inspect the former 367 KB data-model reference.
    # Keep readable references below a conservative 200 KB per-file budget.
    for reference in references.rglob("*.md"):
        if reference.stat().st_size > 200_000:
            error(f"{reference.relative_to(ROOT)}: split generated references below 200 KB for directory inspection")


# --- plugins ---------------------------------------------------------------

version = load_json(f"{PLUGINS[0].folder}/.claude-plugin/plugin.json").get("version")
if not version:
    error("fleet/.claude-plugin/plugin.json has no version")
skill_count = 0
for plugin in PLUGINS:
    check_manifests(plugin, version)
    check_server(plugin, version)
    skill_count += check_skills(plugin)
    check_references(plugin)

# --- marketplaces ----------------------------------------------------------

claude_marketplace = load_json(".claude-plugin/marketplace.json")
if claude_marketplace.get("name") != MARKETPLACE_NAME:
    error(f".claude-plugin/marketplace.json name must be {MARKETPLACE_NAME}")
listed = {entry.get("name"): entry.get("source") for entry in claude_marketplace.get("plugins", [])}
expected_listed = {plugin.name: f"./{plugin.folder}" for plugin in PLUGINS}
if listed != expected_listed:
    error(f".claude-plugin/marketplace.json must list exactly {expected_listed}, got {listed}")

agents_marketplace = load_json(".agents/plugins/marketplace.json")
if agents_marketplace.get("name") != MARKETPLACE_NAME:
    error(f".agents/plugins/marketplace.json name must be {MARKETPLACE_NAME}")
listed = {entry.get("name"): entry.get("source", {}).get("path") for entry in agents_marketplace.get("plugins", [])}
if listed != expected_listed:
    error(f".agents/plugins/marketplace.json must list exactly {expected_listed}, got {listed}")

# --- local links -----------------------------------------------------------

link = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
for markdown in ROOT.rglob("*.md"):
    if ".git" in markdown.parts:
        continue
    for target in link.findall(markdown.read_text(encoding="utf-8")):
        target = target.strip().strip("<>").split("#", 1)[0]
        if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.IGNORECASE):
            continue
        resolved = (markdown.parent / target).resolve()
        if not resolved.exists():
            error(f"{markdown.relative_to(ROOT)}: broken local link {target}")
            continue
        # An install copies only the plugin folder, so a link out of it dies there.
        for plugin in PLUGINS:
            plugin_root = (ROOT / plugin.folder).resolve()
            if markdown.resolve().is_relative_to(plugin_root) and not resolved.is_relative_to(plugin_root):
                error(f"{markdown.relative_to(ROOT)}: local link {target} leaves the plugin folder")

# --- things that must never ship -------------------------------------------

FORBIDDEN = {
    PRIVATE_REPO: "a link to the private source repository",
    "vercel.app": "a deployment URL (use www.meterapp.co)",
    "https://meterapp.co": "the non-canonical origin (use https://www.meterapp.co)",
    "[TODO": "an unresolved placeholder",
}
# An install or update command that names another marketplace fails for
# whoever copies it. A CHANGELOG.md keeps old names in its migration notes.
PLUGIN_NAMES = "|".join(plugin.name for plugin in PLUGINS)
MARKETPLACE_REFERENCES = (
    re.compile(rf"(?<![\w/@.-])(?:{PLUGIN_NAMES}|meter)@([a-z0-9][a-z0-9-]*)"),
    re.compile(r"\bmarketplace (?:update|upgrade) ([a-z0-9][a-z0-9-]*)"),
)
# Each plugin names only its own server; the other is a separate plugin.
OTHER_SERVER = {
    plugin.folder: [other.server_url for other in PLUGINS if other is not plugin]
    for plugin in PLUGINS
}

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
    for url in OTHER_SERVER.get(relative.parts[0], []):
        if url in text:
            error(f"{relative}: names the other plugin's server {url}")
    if relative.name != "CHANGELOG.md":
        for pattern in MARKETPLACE_REFERENCES:
            for name in pattern.findall(text):
                if name != MARKETPLACE_NAME:
                    error(f"{relative}: names the marketplace {name}; it is {MARKETPLACE_NAME}")

if ERRORS:
    print("Plugin validation failed:", file=sys.stderr)
    for item in ERRORS:
        print(f"- {item}", file=sys.stderr)
    raise SystemExit(1)

print(f"Plugin validation passed: {len(PLUGINS)} plugins, {skill_count} skills")
