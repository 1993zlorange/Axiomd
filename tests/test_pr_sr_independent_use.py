"""验证自然语言入口、本地资源、生成一致性和已合并入口的升级行为。"""
from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, "-X", "utf8", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")


class IndependentSkillTests(unittest.TestCase):
    def test_all_entries_are_chinese_automatically_available_and_local(self) -> None:
        for root in sorted((ROOT / "skills").iterdir()):
            if not root.name.startswith(("pr-", "sr-")):
                continue
            with self.subTest(skill=root.name):
                entry = (root / "SKILL.md").read_text(encoding="utf-8")
                ui = (root / "agents/openai.yaml").read_text(encoding="utf-8")
                self.assertIn("allow_implicit_invocation: true", ui)
                self.assertRegex(entry, r"description:.*[\u4e00-\u9fff]")
                for section in ("什么时候用", "先看什么", "怎么做", "交付什么", "怎么检查"):
                    self.assertIn("## " + section, entry)
                self.assertNotRegex(entry, r"\$[a-z][a-z0-9-]+")
                self.assertNotIn("Recommended optional adapters", entry)
                self.assertNotIn("Before starting", entry)
                for target in re.findall(r"\]\(([^)]+)\)", entry):
                    if re.match(r"https?://|#", target):
                        continue
                    resolved = (root / target.split("#")[0]).resolve()
                    self.assertTrue(resolved.is_relative_to(root.resolve()), target)
                    self.assertTrue(resolved.is_file(), target)

    def test_generation_checks_and_role_coverage(self) -> None:
        for command in [
            ("skills/sr-doctoral-research/scripts/generate_leaf_skills.py", "--repo-root", ".", "--check"),
            ("scripts/generate_sr_record_templates.py", "--check"),
            ("scripts/generate_pr_sr_interaction_guides.py", "--check"),
            ("skills/sr-doctoral-research/scripts/validate_sr_skills.py", "--repo-root", "."),
        ]:
            with self.subTest(command=command):
                result = run(*command)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_project_skill_factory_keeps_natural_language_default(self) -> None:
        script = ROOT / "skills/pr-ps-00-project-supervision/scripts/ps_02_create_project_skill.py"
        with tempfile.TemporaryDirectory(prefix="pr-skill-factory-") as temporary:
            root = Path(temporary)
            (root / "AGENTS.md").write_text(
                '```project-supervision\nproject_skills_root = "skills"\nproject_management_root = "records"\nskills_dir = "skills"\n```\n',
                encoding="utf-8",
            )
            result = run(str(script), "--project-root", str(root), "--code", "test-01", "--name", "sample", "--display-name", "样例技能", "--description", "根据实际输入完成一个可检查的中文任务。", "--write")
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            ui = (root / "skills/test-01-sample/agents/openai.yaml").read_text(encoding="utf-8")
            self.assertIn("allow_implicit_invocation: true", ui)
            self.assertIn("## 怎么做", (root / "skills/test-01-sample/SKILL.md").read_text(encoding="utf-8"))

    def test_special_templates_match_task_ids_and_reach_the_output(self) -> None:
        items = json.loads((ROOT / "skills/sr-doctoral-research/catalog.json").read_text(encoding="utf-8"))["skills"]
        names = {item["id"].lower(): item["name"] for item in items}
        for path in (ROOT / "skills/sr-research-shared/references/record-templates/special").glob("*.md"):
            match = re.fullmatch(r"(sr-\d+)-(.+)\.md", path.name)
            self.assertIsNotNone(match, path.name)
            name = names[match.group(1)]
            self.assertEqual(name, "sr-" + match.group(2), path.name)
            output = (ROOT / "skills" / name / "assets/output-template.md").read_text(encoding="utf-8")
            self.assertIn(path.read_text(encoding="utf-8").strip(), output, path.name)

    def test_prune_merged_entry_preserves_backup_and_user_files(self) -> None:
        # Model an earlier managed install, including its exact recorded hash.
        spec = importlib.util.spec_from_file_location("axiom_inventory_test", ROOT / "scripts/build_inventory.py")
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory(prefix="pr-sr-upgrade-") as temporary:
            home = Path(temporary)
            installed = run("scripts/install.py", "--profile", "ai4science", "--codex-home", str(home))
            self.assertEqual(installed.returncode, 0, installed.stderr)
            old = home / "skills/sr-weekly-meeting"
            old.mkdir()
            (old / "SKILL.md").write_text("旧组会技能\n", encoding="utf-8")
            state_file = home / ".axiom-install.json"
            state = json.loads(state_file.read_text(encoding="utf-8"))
            state["skills"][old.name] = {"hash": module.tree_hash(old)}
            state_file.write_text(json.dumps(state), encoding="utf-8")
            user_file = home / "skills/user-notes.txt"
            user_file.write_text("用户内容", encoding="utf-8")
            upgraded = run("scripts/install.py", "--profile", "ai4science", "--codex-home", str(home), "--prune")
            self.assertEqual(upgraded.returncode, 0, upgraded.stdout + upgraded.stderr)
            self.assertFalse(old.exists())
            self.assertEqual(user_file.read_text(encoding="utf-8"), "用户内容")
            self.assertTrue(list((home / ".axiom-backups").glob("*/skills/sr-weekly-meeting/SKILL.md")))
            checked = run("scripts/install.py", "--profile", "ai4science", "--codex-home", str(home), "--check")
            self.assertEqual(checked.returncode, 0, checked.stderr)


if __name__ == "__main__":
    unittest.main()
