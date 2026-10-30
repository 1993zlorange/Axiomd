"""技能指纹不应依赖本机字节码缓存。"""
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

class HashPortabilityTests(unittest.TestCase):
    def test_cache_does_not_change_asset_identity(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "SKILL.md").write_text("技能正文", encoding="utf-8")
            modules = []
            for name in ["build_inventory", "install", "validate"]:
                spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                modules.append(mod)
            before = [mod.tree_hash(root) for mod in modules]
            (root / "__pycache__").mkdir()
            (root / "__pycache__/example.cpython.pyc").write_bytes(b"local cache")
            (root / "other.pyc").write_bytes(b"local bytecode")
            self.assertEqual([mod.tree_hash(root) for mod in modules], before)
            self.assertEqual(len(set(before)), 1)
            (root / "SKILL.md").write_text("真实正文变更", encoding="utf-8")
            self.assertTrue(all(mod.tree_hash(root) != before[i] for i, mod in enumerate(modules)))
