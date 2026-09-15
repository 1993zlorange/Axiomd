#!/usr/bin/env python3
"""Validate MyAgent package structure, metadata, profiles, hashes, and portability."""
from __future__ import annotations

import hashlib
import json
import re
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAFE_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
SECRET_PATTERNS = [
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\bghp_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
]
FORBIDDEN_TEXT = ["E:/" + "zl", "E:" + "\\" + "zl", "C:/Users/" + "PC", "C:" + "\\" + "Users\\" + "PC"]
TEXT_SUFFIXES = {".md", ".py", ".toml", ".yaml", ".yml", ".json", ".txt", ".sh", ".ps1"}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def tree_hash(path: Path) -> str:
    if path.is_file() and not path.is_symlink():
        return file_hash(path)
    digest = hashlib.sha256()
    for item in sorted(p for p in path.rglob("*") if p.is_file() and not p.is_symlink()):
        rel = item.relative_to(path).as_posix().encode("utf-8")
        digest.update(len(rel).to_bytes(8, "big"))
        digest.update(rel)
        digest.update(file_hash(item).encode("ascii"))
    return digest.hexdigest()


def validate_json(errors: list[str]) -> dict:
    try:
        manifest = read_json(ROOT / "manifest.json")
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, f"invalid JSON manifest.json: {exc}")
        manifest = {}
    for path in [ROOT / "plugin.json", ROOT / ".codex-plugin/plugin.json", ROOT / ".agents/plugins/marketplace.json"]:
        try:
            read_json(path)
        except (OSError, json.JSONDecodeError) as exc:
            fail(errors, f"invalid JSON {path.relative_to(ROOT)}: {exc}")
    return manifest


def validate_profiles(errors: list[str], manifest: dict) -> dict[str, dict]:
    profile_files = sorted((ROOT / "profiles").glob("*.json"))
    profiles: dict[str, dict] = {}
    expected = set(manifest.get("profiles", {}))
    actual = {path.stem for path in profile_files}
    if expected != actual:
        fail(errors, f"profile files and manifest differ: files={sorted(actual)}, manifest={sorted(expected)}")
    for path in profile_files:
        try:
            profile = read_json(path)
        except (OSError, json.JSONDecodeError) as exc:
            fail(errors, f"invalid profile {path.relative_to(ROOT)}: {exc}")
            continue
        profiles[path.stem] = profile
        if profile.get("schema_version") != 1:
            fail(errors, f"{path.name} has unsupported schema_version")
        for field in ("agents", "skills", "optional_skills"):
            values = profile.get(field, [])
            if not isinstance(values, list) or not all(isinstance(x, str) for x in values):
                fail(errors, f"{path.name}:{field} must be a string list")
                continue
            if len(values) != len(set(values)):
                fail(errors, f"{path.name}:{field} contains duplicates")
            for name in values:
                if not SAFE_NAME.fullmatch(name):
                    fail(errors, f"{path.name}:{field} has unsafe name {name!r}")
        for name in profile.get("agents", []):
            if not (ROOT / "agents" / f"{name}.toml").is_file():
                fail(errors, f"{path.name} references missing agent {name}")
        for field in ("skills", "optional_skills"):
            for name in profile.get(field, []):
                if not (ROOT / "skills" / name / "SKILL.md").is_file():
                    fail(errors, f"{path.name} references missing skill {name}")
        summary = manifest.get("profiles", {}).get(path.stem, {})
        for field in ("agents", "skills", "optional_skills"):
            if summary.get(field) != len(profile.get(field, [])):
                fail(errors, f"manifest profile summary mismatch: {path.stem}.{field}")
    if "all" in profiles:
        all_profile = profiles["all"]
        expected_agents = sorted({a for p in profiles.values() for a in p.get("agents", [])})
        expected_skills = sorted(set(all_profile.get("skills", [])))
        if sorted(all_profile.get("agents", [])) != expected_agents:
            fail(errors, "all profile does not contain the union of profile agents")
        known_skills = sorted(p.name for p in (ROOT / "skills").iterdir() if p.is_dir())
        if expected_skills != known_skills:
            fail(errors, "all profile does not contain every skill in skills/")
    return profiles


def validate_agents(errors: list[str], profiles: dict[str, dict], manifest: dict) -> set[str]:
    known_skills = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
    agent_files = sorted((ROOT / "agents").glob("*.toml"))
    manifest_agents = set(manifest.get("agents", {}))
    if manifest_agents != {path.stem for path in agent_files}:
        fail(errors, "manifest agents do not exactly match agents/*.toml")
    for path in agent_files:
        try:
            data = tomllib.loads(path.read_text(encoding="utf-8"))
        except (OSError, tomllib.TOMLDecodeError, UnicodeDecodeError) as exc:
            fail(errors, f"invalid TOML {path.relative_to(ROOT)}: {exc}")
            continue
        if data.get("name") != path.stem:
            fail(errors, f"{path.name} TOML name must equal file stem")
        if not str(data.get("description", "")).strip():
            fail(errors, f"{path.name} missing description")
        configured = []
        for item in data.get("skills", {}).get("config", []):
            raw = item.get("path", "")
            match = re.fullmatch(r"\.\./skills/([A-Za-z0-9._-]+)", raw)
            if not match or match.group(1) not in known_skills:
                fail(errors, f"{path.name} has invalid skill path {raw!r}")
                continue
            configured.append(match.group(1))
        record = manifest.get("agents", {}).get(path.stem, {})
        actual_hash = tree_hash(path)
        if record.get("hash") != actual_hash:
            fail(errors, f"manifest hash mismatch for agent {path.stem}")
        memberships = record.get("profiles", [])
        expected_memberships = [name for name, profile in profiles.items() if path.stem in profile.get("agents", [])]
        if sorted(memberships) != sorted(expected_memberships):
            fail(errors, f"manifest profile membership mismatch for agent {path.stem}")
        for skill in configured:
            if skill not in known_skills:
                fail(errors, f"{path.name} config references missing skill {skill}")
            for profile_name in memberships:
                if skill not in profiles[profile_name].get("skills", []):
                    fail(errors, f"{profile_name} includes {path.stem} but omits configured skill {skill}")
        instructions = str(data.get("developer_instructions", ""))
        for skill in known_skills:
            if re.search(r"(?<![A-Za-z0-9_-])" + re.escape(skill) + r"(?![A-Za-z0-9_-])", instructions):
                if skill not in known_skills:
                    fail(errors, f"{path.name} references missing skill {skill}")
    return known_skills


def validate_skills(errors: list[str], profiles: dict[str, dict], manifest: dict) -> None:
    skill_dirs = sorted(path for path in (ROOT / "skills").iterdir() if path.is_dir())
    manifest_skills = set(manifest.get("skills", {}))
    if manifest_skills != {path.name for path in skill_dirs}:
        fail(errors, "manifest skills do not exactly match skills/* directories")
    for directory in skill_dirs:
        skill_file = directory / "SKILL.md"
        if not skill_file.is_file():
            fail(errors, f"missing SKILL.md for {directory.name}")
            continue
        try:
            text = skill_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            fail(errors, f"cannot read {skill_file.relative_to(ROOT)}: {exc}")
            continue
        match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", text, re.DOTALL)
        if not match:
            fail(errors, f"{directory.name}/SKILL.md missing closed frontmatter")
            continue
        frontmatter = match.group(1)
        name_match = re.search(r"^name:\s*[\"']?([A-Za-z0-9._-]+)[\"']?\s*$", frontmatter, re.MULTILINE)
        if not name_match:
            fail(errors, f"{directory.name}/SKILL.md missing valid name")
        elif name_match.group(1) != directory.name:
            fail(errors, f"{directory.name}/SKILL.md name mismatch: {name_match.group(1)}")
        if not re.search(r"^description:\s*\S", frontmatter, re.MULTILINE):
            fail(errors, f"{directory.name}/SKILL.md missing description")
        record = manifest.get("skills", {}).get(directory.name, {})
        if record.get("hash") != tree_hash(directory):
            fail(errors, f"manifest hash mismatch for skill {directory.name}")
        expected = [name for name, profile in profiles.items() if directory.name in profile.get("skills", [])]
        if sorted(record.get("profiles", [])) != sorted(expected):
            fail(errors, f"manifest profile membership mismatch for skill {directory.name}")
        expected_optional = [name for name, profile in profiles.items() if directory.name in profile.get("optional_skills", [])]
        if sorted(record.get("optional_profiles", [])) != sorted(expected_optional):
            fail(errors, f"manifest optional-profile mismatch for skill {directory.name}")


def validate_plugin_and_docs(errors: list[str], manifest: dict) -> None:
    try:
        plugin = read_json(ROOT / "plugin.json")
        overlay = read_json(ROOT / ".codex-plugin/plugin.json")
        marketplace = read_json(ROOT / ".agents/plugins/marketplace.json")
    except (OSError, json.JSONDecodeError):
        return
    for path, data in [(ROOT / "plugin.json", plugin), (ROOT / ".codex-plugin/plugin.json", overlay)]:
        if data.get("name") != "myagent" or data.get("version") != manifest.get("version"):
            fail(errors, f"package identity/version mismatch in {path.relative_to(ROOT)}")
        if data.get("skills") != "./skills/":
            fail(errors, f"{path.relative_to(ROOT)} must point skills to ./skills/")
    plugins = marketplace.get("plugins", [])
    if not isinstance(plugins, list) or len(plugins) != 1 or plugins[0].get("name") != "myagent":
        fail(errors, "marketplace must contain exactly one myagent plugin")
    elif plugins[0].get("source", {}).get("path") != "./":
        fail(errors, "marketplace myagent source path must be ./")
    readme = ROOT / "README.md"
    if not readme.is_file():
        fail(errors, "README.md is missing")
    else:
        text = readme.read_text(encoding="utf-8")
        for required in ["## 一键安装", "## 安装档案", "docs/asset-index.md", "python scripts/install.py --profile all"]:
            if required not in text:
                fail(errors, f"README.md missing required text: {required}")
    asset_index = (ROOT / "docs/asset-index.md").read_text(encoding="utf-8", errors="replace")
    for name in manifest.get("skills", {}):
        if name not in asset_index:
            fail(errors, f"docs/asset-index.md missing skill {name}")
    for name in manifest.get("agents", {}):
        if name not in asset_index:
            fail(errors, f"docs/asset-index.md missing agent {name}")


def validate_portability(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        rel = path.relative_to(ROOT).as_posix()
        for term in FORBIDDEN_TEXT:
            if term in text:
                fail(errors, f"machine-specific path in {rel}: {term}")
        for pattern in SECRET_PATTERNS:
            match = pattern.search(text)
            if match:
                fail(errors, f"possible credential in {rel}: {match.group(0)[:8]}...")


def main() -> int:
    errors: list[str] = []
    manifest = validate_json(errors)
    profiles = validate_profiles(errors, manifest)
    validate_agents(errors, profiles, manifest)
    validate_skills(errors, profiles, manifest)
    validate_plugin_and_docs(errors, manifest)
    validate_portability(errors)
    if errors:
        print(f"Validation failed with {len(errors)} error(s):", file=__import__("sys").stderr)
        for error in errors:
            print(f"- {error}", file=__import__("sys").stderr)
        return 1
    print(f"Validation passed: {len(manifest.get('agents', {}))} agents, {len(manifest.get('skills', {}))} skills, {len(profiles)} profiles.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
