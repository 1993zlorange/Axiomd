#!/usr/bin/env python3
"""Install MyAgent Codex agents and skills safely.

The installer uses staged copies, transactional activation, SHA-256 verification,
and timestamped backups. It only manages asset names declared by this repository.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_MANIFEST = REPO_ROOT / "manifest.json"
INSTALL_STATE_NAME = ".myagent-install.json"
SAFE_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


class InstallError(RuntimeError):
    pass


def read_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise InstallError(f"required JSON file not found: {path}") from exc
    except (OSError, json.JSONDecodeError) as exc:
        raise InstallError(f"cannot read JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise InstallError(f"expected a JSON object in {path}")
    return value


def safe_name(name: str) -> str:
    if not SAFE_NAME.fullmatch(name) or name in {".", ".."}:
        raise InstallError(f"unsafe asset name: {name!r}")
    return name


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_files(root: Path) -> list[Path]:
    if root.is_symlink() or any(parent.is_symlink() for parent in root.parents if parent != root):
        raise InstallError(f"symlinked asset is not supported: {root}")
    return sorted(p for p in root.rglob("*") if p.is_file() and not p.is_symlink())


def tree_hash(root: Path) -> str:
    if root.is_file() and not root.is_symlink():
        return file_hash(root)
    digest = hashlib.sha256()
    for path in iter_files(root):
        rel = path.relative_to(root).as_posix().encode("utf-8")
        digest.update(len(rel).to_bytes(8, "big"))
        digest.update(rel)
        digest.update(file_hash(path).encode("ascii"))
    return digest.hexdigest()


def copy_asset(src: Path, dst: Path) -> None:
    if src.is_file() and not src.is_symlink():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    elif src.is_dir() and not src.is_symlink():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(src, dst)
    else:
        raise InstallError(f"missing or unsupported source asset: {src}")
    if tree_hash(src) != tree_hash(dst):
        raise InstallError(f"staged copy verification failed: {dst.name}")


def name_from_asset(path: Path) -> str:
    return path.name


def asset_path(root: Path, kind: str, name: str) -> Path:
    filename = f"{name}.toml" if kind == "agents" else name
    return root / kind / filename


def ensure_within(child: Path, parent: Path, label: str) -> Path:
    child = child.resolve()
    parent = parent.resolve()
    try:
        child.relative_to(parent)
    except ValueError as exc:
        raise InstallError(f"{label} escapes destination root: {child}") from exc
    return child


def remove_managed_tree(path: Path, root: Path) -> None:
    path = ensure_within(path, root, "removal target")
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    elif path.exists() or path.is_symlink():
        path.unlink()


def move_tree(src: Path, dst: Path, destination_root: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst = ensure_within(dst, destination_root, "move destination")
    if dst.exists() or dst.is_symlink():
        raise InstallError(f"move destination already exists: {dst}")
    shutil.move(str(src), str(dst))


def default_codex_home() -> Path:
    configured = os.environ.get("CODEX_HOME")
    return Path(configured).expanduser() if configured else Path.home() / ".codex"


def package_manifest() -> dict:
    data = read_json(PACKAGE_MANIFEST)
    if data.get("name") != "myagent":
        raise InstallError("manifest.json is not a myagent package manifest")
    for key in ("agents", "skills", "profiles"):
        if not isinstance(data.get(key), dict):
            raise InstallError(f"manifest.json missing valid {key} section")
    return data


def profile_names(manifest: dict) -> list[str]:
    return sorted(manifest["profiles"])


def load_profile(name: str) -> tuple[str, dict]:
    manifest = package_manifest()
    if name not in manifest["profiles"]:
        raise InstallError(f"unknown profile {name!r}; available: {', '.join(profile_names(manifest))}")
    path = REPO_ROOT / "profiles" / f"{name}.json"
    data = read_json(path)
    if data.get("schema_version") != 1:
        raise InstallError(f"unsupported profile schema in {path}")
    for key in ("agents", "skills", "optional_skills"):
        if not isinstance(data.get(key), list) or not all(isinstance(x, str) for x in data[key]):
            raise InstallError(f"profile {name!r} has invalid {key}")
    return name, data


def selected_profile(profile: str, include_optional: bool) -> tuple[str, dict, dict[str, list[str]]]:
    name, data = load_profile(profile)
    agents = sorted({safe_name(x) for x in data["agents"]})
    skills = sorted({safe_name(x) for x in data["skills"]})
    optional = sorted({safe_name(x) for x in data.get("optional_skills", [])})
    if include_optional:
        skills = sorted(set(skills) | set(optional))
    overlap = set(agents) & set(skills)
    if overlap:
        raise InstallError(f"agent and skill names collide: {sorted(overlap)}")
    return name, data, {"agents": agents, "skills": skills}


def validate_sources(selection: dict[str, list[str]]) -> dict[tuple[str, str], str]:
    manifest = package_manifest()
    hashes: dict[tuple[str, str], str] = {}
    for kind, names in selection.items():
        source_root = REPO_ROOT / kind
        manifest_section = manifest[kind]
        for name in names:
            if name not in manifest_section:
                raise InstallError(f"{kind}/{name} is not listed in manifest.json")
            expected = manifest_section[name].get("hash")
            source = asset_path(REPO_ROOT, kind, name)
            actual = tree_hash(source)
            if actual != expected:
                raise InstallError(f"{kind}/{name} does not match manifest.json (expected {expected}, got {actual})")
            hashes[(kind, name)] = actual
    return hashes


def state_path(codex_home: Path) -> Path:
    return codex_home / INSTALL_STATE_NAME


def read_state(codex_home: Path) -> dict:
    path = state_path(codex_home)
    if not path.is_file():
        raise InstallError(f"No MyAgent install state found at {path}")
    state = read_json(path)
    if state.get("package") != "myagent":
        raise InstallError(f"{path} was not written by myagent")
    return state


def git_commit() -> str | None:
    if not (REPO_ROOT / ".git").exists():
        return None
    try:
        result = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout.strip()


def timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def print_plan(profile: str, include_optional: bool, codex_home: Path) -> tuple[dict[str, list[str]], dict[tuple[str, str], str]]:
    name, data, selection = selected_profile(profile, include_optional)
    hashes = validate_sources(selection)
    print(f"Profile:        {name}")
    print(f"Description:    {data['description']}")
    print(f"Agents:         {len(selection['agents'])}")
    print(f"Skills:         {len(selection['skills'])}")
    print(f"Optional added: {'yes' if include_optional else 'no'}")
    print(f"Source:         {REPO_ROOT}")
    print(f"Codex home:     {codex_home}")
    for kind in ("agents", "skills"):
        print(f"\n{kind.capitalize()}:")
        for asset in selection[kind]:
            print(f"  {asset}")
    return selection, hashes


def check_install(profile: str, include_optional: bool, codex_home: Path) -> int:
    _, _, selection = selected_profile(profile, include_optional)
    validate_sources(selection)
    failures: list[str] = []
    for kind, names in selection.items():
        for name in names:
            destination = asset_path(codex_home, kind, name)
            if not destination.exists():
                failures.append(f"MISSING {kind}/{name}")
                continue
            expected = tree_hash(asset_path(REPO_ROOT, kind, name))
            actual = tree_hash(destination)
            if expected != actual:
                failures.append(f"DIFF   {kind}/{name}")
    state_file = state_path(codex_home)
    if not state_file.is_file():
        failures.append(f"MISSING install state {state_file}")
    else:
        state = read_json(state_file)
        if state.get("profile") != profile or bool(state.get("include_optional")) != include_optional:
            failures.append(f"PROFILE state={state.get('profile')!r}, optional={state.get('include_optional')!r}")
    if failures:
        for failure in failures:
            print(failure)
        raise InstallError("installed assets do not match the selected profile")
    print(f"OK {len(selection['agents'])} agents and {len(selection['skills'])} skills match {profile!r}.")
    return 0


def backup_existing(destination: Path, backup_root: Path, kind: str) -> Path | None:
    if not destination.exists() and not destination.is_symlink():
        return None
    target = backup_root / kind / destination.name
    if target.exists():
        raise InstallError(f"backup destination already exists: {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(destination), str(target))
    return target


def install(profile: str, include_optional: bool, codex_home: Path, prune: bool, force: bool, dry_run: bool) -> int:
    _, _, selection = selected_profile(profile, include_optional)
    hashes = validate_sources(selection)
    previous_state = read_state(codex_home) if state_path(codex_home).is_file() else None

    if dry_run:
        print("Dry run only; no files were changed.")
        return 0

    codex_home.mkdir(parents=True, exist_ok=True)
    stage_root = Path(tempfile.mkdtemp(prefix=".myagent-stage-", dir=codex_home))
    backup_name = f".myagent-backups/{timestamp()}-{uuid.uuid4().hex[:8]}"
    backup_root = codex_home / backup_name
    activated: list[tuple[str, Path]] = []
    state_tmp: Path | None = None
    try:
        print(f"==> Staging {len(selection['agents'])} agents and {len(selection['skills'])} skills")
        for kind, names in selection.items():
            for name in names:
                copy_asset(asset_path(REPO_ROOT, kind, name), asset_path(stage_root, kind, name))

        print(f"==> Activating staged assets in {codex_home}")
        for kind, names in selection.items():
            for name in names:
                destination = asset_path(codex_home, kind, name)
                backup_existing(destination, backup_root, kind)
                move_tree(asset_path(stage_root, kind, name), destination, codex_home)
                activated.append((kind, destination))
                print(f"    activated {kind}/{name}")

        print("==> Verifying installed assets")
        for (kind, name), expected in hashes.items():
            destination = asset_path(codex_home, kind, name)
            actual = tree_hash(destination)
            if actual != expected:
                raise InstallError(f"verification failed for {kind}/{name}")

        pruned: list[str] = []
        if prune and previous_state:
            for kind in ("agents", "skills"):
                previous_names = previous_state.get(kind, {})
                for name in sorted(set(previous_names) - set(selection[kind])):
                    destination = asset_path(codex_home, kind, name)
                    if not destination.exists():
                        continue
                    expected = previous_names.get(name, {}).get("hash")
                    modified = expected is not None and tree_hash(destination) != expected
                    if modified and not force:
                        print(f"    SKIP modified stale asset {kind}/{name}")
                        continue
                    backup_existing(destination, backup_root, kind)
                    pruned.append(f"{kind}/{name}")
                    print(f"    pruned {kind}/{name}")

        state = {
            "schema_version": 1,
            "package": "myagent",
            "package_version": package_manifest().get("version"),
            "profile": profile,
            "include_optional": include_optional,
            "source_commit": git_commit(),
            "installed_at": datetime.now(timezone.utc).isoformat(),
            "backup": backup_name,
            "agents": {name: {"hash": hashes[("agents", name)]} for name in selection["agents"]},
            "skills": {name: {"hash": hashes[("skills", name)]} for name in selection["skills"]},
        }
        state_tmp = stage_root / INSTALL_STATE_NAME
        state_tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        os.replace(state_tmp, state_path(codex_home))
        state_tmp = None

        print("==> Install verified")
        if (backup_root / "agents").exists() or (backup_root / "skills").exists() or pruned:
            print(f"    backup: {backup_root}")
        if pruned:
            print(f"    pruned: {len(pruned)}")
        print("==> Done. Start a new Codex session before invoking the agents or skills.")
        return 0
    except Exception:
        # Roll back assets activated during this run.
        for _kind, destination in reversed(activated):
            if destination.exists():
                move_tree(destination, stage_root / "rollback" / destination.parent.name / destination.name, codex_home)
        if backup_root.exists():
            for kind in ("agents", "skills"):
                backup_dir = backup_root / kind
                if not backup_dir.exists():
                    continue
                for old in sorted(backup_dir.iterdir(), reverse=True):
                    restore = codex_home / kind / old.name
                    if restore.exists():
                        continue
                    move_tree(old, restore, codex_home)
        if state_path(codex_home).exists() and previous_state is None:
            state_path(codex_home).unlink()
        raise
    finally:
        if stage_root.exists():
            shutil.rmtree(stage_root, ignore_errors=True)


def uninstall(codex_home: Path, force: bool, profile: str | None, include_optional: bool | None) -> int:
    state = read_state(codex_home)
    selected_name = profile or state["profile"]
    use_optional = include_optional if include_optional is not None else bool(state.get("include_optional"))
    _, _, selection = selected_profile(selected_name, use_optional)
    validate_sources(selection)
    backup_name = f".myagent-backups/{timestamp()}-{uuid.uuid4().hex[:8]}"
    backup_root = codex_home / backup_name
    removed: list[str] = []
    try:
        for kind in ("agents", "skills"):
            for name in sorted(selection[kind]):
                destination = asset_path(codex_home, kind, name)
                if not destination.exists():
                    continue
                expected = state.get(kind, {}).get(name, {}).get("hash")
                modified = expected is not None and tree_hash(destination) != expected
                if modified and not force:
                    raise InstallError(f"{kind}/{name} was modified after install; use --force to back it up and remove it")
                backup_existing(destination, backup_root, kind)
                removed.append(f"{kind}/{name}")
                print(f"    removed {kind}/{name}")
        state_path(codex_home).unlink()
        print(f"==> Removed {len(removed)} managed assets; backup: {backup_root}")
        print("    Other files in your Codex home were untouched.")
        return 0
    except Exception:
        if backup_root.exists():
            for kind in ("agents", "skills"):
                backup_dir = backup_root / kind
                if not backup_dir.exists():
                    continue
                for old in sorted(backup_dir.iterdir(), reverse=True):
                    restore = codex_home / kind / old.name
                    if not restore.exists():
                        shutil.move(str(old), str(restore))
        raise


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", help="ai4programming, ai4science, or all (default: all)")
    parser.add_argument("--codex-home", type=Path, default=None, help="Codex home (default: $CODEX_HOME or ~/.codex)")
    parser.add_argument("--include-optional", action="store_true", help="also install the profile's optional compatibility skills")
    parser.add_argument("--core-only", action="store_true", help="with --check/--uninstall, use only the profile's core skills")
    parser.add_argument("--prune", action="store_true", help="after a successful install, remove stale assets managed by the previous MyAgent install")
    parser.add_argument("--force", action="store_true", help="allow removal or pruning of assets changed after installation (they are backed up)")
    parser.add_argument("--check", action="store_true", help="verify an existing installation without changing files")
    parser.add_argument("--uninstall", action="store_true", help="back up and remove only assets managed by MyAgent")
    parser.add_argument("--dry-run", action="store_true", help="show validation and intended operations without changing files")
    parser.add_argument("--list-profiles", action="store_true", help="list available profiles")
    args = parser.parse_args(argv)
    if args.core_only and args.include_optional:
        parser.error("--core-only conflicts with --include-optional")
    if args.uninstall and (args.prune or args.include_optional and False):
        parser.error("--uninstall cannot be combined with --prune")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    codex_home = args.codex_home.expanduser().resolve() if args.codex_home else default_codex_home().resolve()
    try:
        if args.list_profiles:
            for name in profile_names(package_manifest()):
                profile = read_json(REPO_ROOT / "profiles" / f"{name}.json")
                print(f"{name:16} agents={len(profile['agents']):2} skills={len(profile['skills']):2} optional={len(profile.get('optional_skills', []))}")
            return 0

        state = None
        if args.check or args.uninstall:
            state = read_state(codex_home)
        profile = args.profile or (state["profile"] if state else "all")
        if args.core_only:
            include_optional = False
        elif args.include_optional:
            include_optional = True
        elif state:
            include_optional = bool(state.get("include_optional"))
        else:
            include_optional = False

        if args.uninstall:
            return uninstall(codex_home, args.force, args.profile, None if args.profile is None else include_optional)
        if args.check:
            return check_install(profile, include_optional, codex_home)
        return install(profile, include_optional, codex_home, args.prune, args.force, args.dry_run)
    except InstallError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
