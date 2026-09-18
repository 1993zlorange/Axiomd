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

    def test_sr07_authenticated_browser_contract_is_explicit(self) -> None:
        skill = (ROOT / "skills" / "sr-search-strategy" / "SKILL.md").read_text(encoding="utf-8")
        reference = (ROOT / "skills" / "sr-research-shared" / "references" / "browser-skill-literature-search.md").read_text(encoding="utf-8")
        for required in ["bsk session", "bsk tab borrow", "bsk request-help", "bsk session stop", "L3"]:
            self.assertIn(required, skill + reference)
        for fallback_required in ["安装 BrowserSkill 后重试", "未经用户确认不得静默切换回退路径"]:
            self.assertIn(fallback_required, skill + reference)
        for forbidden in ["Cookie", "令牌", "密码", "localStorage"]:
            self.assertIn(forbidden, skill + reference)
        self.assertIn("authenticated_content_observed", skill + reference)

    def test_sr07_sr08_define_zotero_batch_exports(self) -> None:
        catalog = json.loads(
            (ROOT / "skills" / "sr-doctoral-research" / "catalog.json").read_text(encoding="utf-8")
        )
        by_id = {item["id"]: item for item in catalog["skills"]}
        reference_path = ROOT / "skills" / "sr-research-shared" / "references" / "zotero-batch-import.md"
        self.assertTrue(reference_path.is_file())

        for sr_id, skill_name in [("SR-07", "sr-search-strategy"), ("SR-08", "sr-literature-screening")]:
            export = by_id[sr_id]["bibliography_export"]
            self.assertEqual(export["default_format"], "RIS")
            self.assertIn("BibTeX", export["optional_formats"])
            self.assertEqual(export["reference"], "../sr-research-shared/references/zotero-batch-import.md")

            skill_root = ROOT / "skills" / skill_name
            skill_text = (skill_root / "SKILL.md").read_text(encoding="utf-8")
            template_text = (skill_root / "assets" / "output-template.md").read_text(encoding="utf-8")
            self.assertIn("zotero-batch-import.md", skill_text)
            self.assertIn("bibliography_exports:", template_text)
            self.assertIn("Zotero 实机导入", template_text)

    def test_installer_check_and_uninstall_in_temp_home(self) -> None:
        with tempfile.TemporaryDirectory(prefix="axiom-codex-") as temporary:
            codex_home = Path(temporary)
            untouched = codex_home / "skills" / "user-owned-skill"
            untouched.mkdir(parents=True)
            (untouched / "KEEP.txt").write_text("user asset\n", encoding="utf-8")

            install = run("scripts/install.py", "--profile", "ai4programming", "--codex-home", str(codex_home))
            self.assertEqual(install.returncode, 0, install.stderr)
            self.assertEqual(len(list((codex_home / "agents").glob("*.toml"))), 5)
            state = json.loads((codex_home / ".axiom-install.json").read_text(encoding="utf-8"))
            self.assertEqual(state["profile"], "ai4programming")
            self.assertEqual(len(state["skills"]), 18)

            check = run("scripts/install.py", "--profile", "ai4programming", "--codex-home", str(codex_home), "--check")
            self.assertEqual(check.returncode, 0, check.stderr)

            uninstall = run("scripts/install.py", "--profile", "ai4programming", "--codex-home", str(codex_home), "--uninstall")
            self.assertEqual(uninstall.returncode, 0, uninstall.stderr)
            self.assertFalse(list((codex_home / "agents").glob("*.toml")))
            self.assertFalse(list((codex_home / "skills").glob("pr-*")))
            self.assertTrue((untouched / "KEEP.txt").is_file())
            self.assertFalse((codex_home / ".axiom-install.json").exists())


if __name__ == "__main__":
    unittest.main()
