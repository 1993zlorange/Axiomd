"""项目创建默认无副作用，拒绝旧模板和覆盖，不传播维护材料。"""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("create_project", ROOT / "scripts/create_project.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CreateProjectTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.template = self.root / "template"
        engine = self.template / "projectname/project"
        (engine / "scripts").mkdir(parents=True)
        (engine / "configs").mkdir()
        for p in [self.template / "AGENTS.md", engine / "AGENTS.md", engine / "PROGRAMMING_STANDARDS.md"]:
            p.write_text("projectname项目规则", encoding="utf-8")
        (engine / "scripts/f001_governance_validate.py").write_text("# 示例入口", encoding="utf-8")
        self.registry = engine / "configs/features.yaml"
        self.registry.write_text(json.dumps({"record_policy": {}, "technical_documents": {"profile": "reader"}, "achievement_layout": {"enabled": True, "roots": []}}), encoding="utf-8")
        history = self.template / "projectname/achieve/old.md"
        history.parent.mkdir(parents=True)
        history.write_text("模板维护历史不能复制", encoding="utf-8")

    def test_preview_creates_nothing(self):
        target = self.root / "new"
        MODULE.create("research", self.template, target, "new", "实际需求")
        self.assertFalse(target.exists())

    def test_creation_does_not_copy_history_or_fake_docs(self):
        target = self.root / "new"
        source = json.loads(self.registry.read_text(encoding="utf-8"))
        source["achievement_layout"] = {"enabled": True, "roots": [{"baseline_paths": ["old-maintenance.md"]}]}
        self.registry.write_text(json.dumps(source), encoding="utf-8")
        MODULE.create("research", self.template, target, "new", "实际需求", True)
        config = json.loads((target / "new/project/configs/features.yaml").read_text(encoding="utf-8"))
        self.assertEqual(config["achievement_layout"]["roots"][0]["baseline_paths"], [])
        self.assertEqual([p.name for p in (target / "new/project/docs").iterdir()], ["README.md"])
        self.assertFalse((target / "new/achieve/old.md").exists())
        self.assertFalse((target / "new/project/server").exists())
        with self.assertRaises(ValueError):
            MODULE.create("research", self.template, target, "new", "实际需求", True)

    def test_old_or_broken_source_is_rejected_before_creation(self):
        target = self.root / "new"
        self.registry.write_text('{"record_policy":{}}', encoding="utf-8")
        with self.assertRaises(ValueError):
            MODULE.create("research", self.template, target, "new", "实际需求", True)
        self.assertFalse(target.exists())
        self.registry.write_text('broken', encoding="utf-8")
        with self.assertRaises(ValueError):
            MODULE.create("research", self.template, target, "new", "实际需求", True)
        self.assertFalse(target.exists())
