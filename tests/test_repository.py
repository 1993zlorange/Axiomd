from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import zipfile
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

    def test_sr53_has_drawio_authoring_and_source_qa(self) -> None:
        skill_root = ROOT / "skills" / "sr-core-figures"
        skill_text = (skill_root / "SKILL.md").read_text(encoding="utf-8")
        for required in [
            "## Draw.io scientific authoring",
            "references/drawio-authoring.md",
            "references/drawio-visual-language.md",
            "references/drawio-export-qa.md",
            "scripts/qa_drawio.py",
            "preview_export=blocked",
        ]:
            self.assertIn(required, skill_text)

        valid_drawio = """<mxfile><diagram id="d1" name="Figure"><mxGraphModel pageWidth="800" pageHeight="600"><root><mxCell id="0"/><mxCell id="1" parent="0"/><mxCell id="node-input" value="Input" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1"><mxGeometry x="40" y="80" width="160" height="60" as="geometry"/></mxCell><mxCell id="node-model" value="Model" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1"><mxGeometry x="320" y="80" width="160" height="60" as="geometry"/></mxCell><mxCell id="edge-input-model" value="" style="edgeStyle=orthogonalEdgeStyle;html=1;" edge="1" parent="1" source="node-input" target="node-model"><mxGeometry relative="1" as="geometry"/></mxCell></root></mxGraphModel></diagram></mxfile>"""
        invalid_drawio = valid_drawio.replace('value="Model"', r'value="Attention(x_i)"').replace(' target="node-model"', "")

        with tempfile.TemporaryDirectory(prefix="sr53-drawio-") as temporary:
            valid = Path(temporary) / "figure.drawio"
            invalid = Path(temporary) / "invalid.drawio"
            valid.write_text(valid_drawio, encoding="utf-8")
            invalid.write_text(invalid_drawio, encoding="utf-8")

            passed = run(str(skill_root / "scripts" / "qa_drawio.py"), str(valid))
            self.assertEqual(passed.returncode, 0, passed.stdout + passed.stderr)
            self.assertIn("QA=pass", passed.stdout)

            failed = run(str(skill_root / "scripts" / "qa_drawio.py"), str(invalid))
            self.assertEqual(failed.returncode, 2, failed.stdout + failed.stderr)
            self.assertIn("edge has no target", failed.stdout)
            self.assertIn("math=\"1\"", failed.stdout)

    def test_sr58_document_to_ppt_contract_and_qa(self) -> None:
        skill_root = ROOT / "skills" / "sr-talk-open-source"
        skill_text = (skill_root / "SKILL.md").read_text(encoding="utf-8")
        standard_text = (skill_root / "references" / "group-meeting-ppt-standard.md").read_text(encoding="utf-8")
        for required in [
            "## Document-to-PPT bridge",
            "references/document-to-ppt.md",
            "references/group-meeting-ppt-standard.md",
            "assets/ppt-page-plan.md",
            "scripts/qa_group_meeting_pptx.py",
            "one complete, visible `SR58-SUMMARY` sentence on every page",
            "red+bold+underline",
            "body ≥18pt",
        ]:
            self.assertIn(required, skill_text)
        for required in [
            "## One-sentence summary contract",
            "summary_sentence:",
            "summary_shape: \"SR58-SUMMARY\"",
            "Target 20–60 Chinese characters",
            "20–22pt bold Microsoft YaHei",
        ]:
            self.assertIn(required, standard_text)

        summary_shape = r"""<p:sp><p:nvSpPr><p:cNvPr id="4" name="SR58-SUMMARY"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr><p:spPr/><p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:rPr sz="2000" b="1"><a:solidFill><a:srgbClr val="0070C0"/></a:solidFill><a:latin typeface="Microsoft YaHei"/><a:ea typeface="Microsoft YaHei"/></a:rPr><a:t>本页证明结论成立。</a:t></a:r></a:p></p:txBody></p:sp>"""
        slide_prefix = r"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"><p:cSld><p:spTree><p:sp><p:nvSpPr><p:cNvPr id="2" name="Title"/><p:cNvSpPr/><p:nvPr><p:ph type="title"/></p:nvPr></p:nvSpPr><p:spPr/><p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:rPr sz="2000" b="1"><a:solidFill><a:srgbClr val="000000"/></a:solidFill><a:latin typeface="Microsoft YaHei"/><a:ea typeface="Microsoft YaHei"/></a:rPr><a:t>结论</a:t></a:r></a:p></p:txBody></p:sp>""" + summary_shape + r"""<p:sp><p:nvSpPr><p:cNvPr id="3" name="Content"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr><p:spPr/><p:txBody><a:bodyPr/><a:lstStyle/>"""
        slide_suffix = "</p:txBody></p:sp></p:spTree></p:cSld></p:sld>"

        def xml_run(text: str, size: int, color: str, bold: bool = False, underline: bool = False, font: str = "Microsoft YaHei") -> str:
            attrs = f'sz="{size}"'
            if bold:
                attrs += ' b="1"'
            if underline:
                attrs += ' u="sng"'
            return (
                '<a:p><a:r><a:rPr ' + attrs + '><a:solidFill><a:srgbClr val="' + color
                + '"/></a:solidFill><a:latin typeface="' + font + '"/><a:ea typeface="' + font
                + '"/></a:rPr><a:t>' + text + '</a:t></a:r></a:p>'
            )

        valid_body = (
            xml_run("一般结果", 1800, "000000")
            + xml_run("重要结果", 1800, "0070C0", bold=True)
            + xml_run("关键结论", 1800, "FF0000", bold=True, underline=True)
        )
        invalid_body = (
            xml_run("太小", 1200, "000000", font="Arial")
            + xml_run("蓝色未加粗", 1800, "0070C0")
            + xml_run("红一", 1800, "FF0000")
            + xml_run("红二", 1800, "FF0000")
            + xml_run("红三", 1800, "FF0000")
            + xml_run("红四", 1800, "FF0000")
        )

        with tempfile.TemporaryDirectory(prefix="sr58-pptx-") as temporary:
            valid = Path(temporary) / "valid.pptx"
            invalid = Path(temporary) / "invalid.pptx"
            missing = Path(temporary) / "missing-summary.pptx"
            for target, body in [(valid, valid_body), (invalid, invalid_body), (missing, valid_body)]:
                with zipfile.ZipFile(target, "w") as package:
                    theme = '<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:themeElements><a:fontScheme name="SR58"><a:majorFont><a:latin typeface="Microsoft YaHei"/><a:ea typeface="Microsoft YaHei"/><a:cs typeface=""/></a:majorFont><a:minorFont><a:latin typeface="Microsoft YaHei"/><a:ea typeface="Microsoft YaHei"/><a:cs typeface=""/></a:minorFont></a:fontScheme></a:themeElements></a:theme>'
                    package.writestr("ppt/theme/theme1.xml", theme)
                    prefix = slide_prefix if target is not missing else slide_prefix.replace(summary_shape, "")
                    package.writestr("ppt/slides/slide1.xml", prefix + body + slide_suffix)

            passed = run(str(skill_root / "scripts" / "qa_group_meeting_pptx.py"), str(valid))
            self.assertEqual(passed.returncode, 0, passed.stdout + passed.stderr)
            self.assertIn("QA=pass", passed.stdout)

            self.assertIn("summary_shapes=1", passed.stdout)

            failed = run(str(skill_root / "scripts" / "qa_group_meeting_pptx.py"), str(invalid))
            self.assertEqual(failed.returncode, 2, failed.stdout + failed.stderr)
            self.assertIn("red runs exceed the limit of 3", failed.stdout)
            self.assertIn("below the 14pt minimum", failed.stdout)
            self.assertIn("non-Microsoft-YaHei font", failed.stdout)

            no_summary = run(str(skill_root / "scripts" / "qa_group_meeting_pptx.py"), str(missing))
            self.assertEqual(no_summary.returncode, 2, no_summary.stdout + no_summary.stderr)
            self.assertIn("requires exactly one visible SR58-SUMMARY", no_summary.stdout)

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
