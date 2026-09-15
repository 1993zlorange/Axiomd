from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args: str, cwd: Path = ROOT) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        cwd=cwd,
        text=True,
        capture_output=True,
        encoding="utf-8",
    )


class RepositoryTests(unittest.TestCase):
    def test_validator_passes(self) -> None:
        result = run("scripts/validate.py")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_package_metadata_is_consistent(self) -> None:
        package = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        plugin = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(package["name"], plugin["name"])
        self.assertEqual(package["version"], plugin["version"])
        self.assertEqual(len(package["agents"]), 10)
        self.assertEqual(len(package["skills"]), 95)
        self.assertEqual(set(package["profiles"]), {"ai4programming", "ai4science", "all"})

    def test_installer_check_and_uninstall_in_temp_home(self) -> None:
        with tempfile.TemporaryDirectory(prefix="myagent-codex-") as temporary:
            codex_home = Path(temporary)
            untouched = codex_home / "skills" / "user-owned-skill"
            untouched.mkdir(parents=True)
            (untouched / "KEEP.txt").write_text("user asset\n", encoding="utf-8")

            install = run("scripts/install.py", "--profile", "ai4programming", "--codex-home", str(codex_home))
            self.assertEqual(install.returncode, 0, install.stderr)
            self.assertEqual(len(list((codex_home / "agents").glob("*.toml"))), 5)
            state = json.loads((codex_home / ".myagent-install.json").read_text(encoding="utf-8"))
            self.assertEqual(state["profile"], "ai4programming")
            self.assertEqual(len(state["skills"]), 18)

            check = run("scripts/install.py", "--profile", "ai4programming", "--codex-home", str(codex_home), "--check")
            self.assertEqual(check.returncode, 0, check.stderr)

            uninstall = run("scripts/install.py", "--profile", "ai4programming", "--codex-home", str(codex_home), "--uninstall")
            self.assertEqual(uninstall.returncode, 0, uninstall.stderr)
            self.assertFalse(list((codex_home / "agents").glob("*.toml")))
            self.assertFalse(list((codex_home / "skills").glob("pr-*")))
            self.assertTrue((untouched / "KEEP.txt").is_file())
            self.assertFalse((codex_home / ".myagent-install.json").exists())


if __name__ == "__main__":
    unittest.main()
