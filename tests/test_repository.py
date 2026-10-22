from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import zipfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args: str, cwd: Path = ROOT) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-X", "utf8", *args],
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

    def test_sr_pr_agents_use_adaptive_reasoning_policy(self) -> None:
        import tomllib

        agent_names = sorted(path.stem for path in (ROOT / "agents").glob("*.toml"))
        self.assertEqual(len(agent_names), 10)
        for path in sorted((ROOT / "agents").glob("*.toml")):
            data = tomllib.loads(path.read_text(encoding="utf-8"))
            self.assertNotIn(
                "model_reasoning_effort",
                data,
                f"{path.name} must inherit runtime reasoning instead of fixing an effort level",
            )
            instructions = data["developer_instructions"]
            for required in [
                "分析深度：",
                "简单任务：",
                "常规任务：",
                "复杂任务：",
                "需要深入检查的情形：",
            ]:
                self.assertIn(required, instructions, f"{path.name} missing {required!r}")

    def test_sr07_authenticated_browser_contract_is_explicit(self) -> None:
        skill = (ROOT / "skills" / "sr-search-strategy" / "SKILL.md").read_text(encoding="utf-8")
        reference = (ROOT / "skills" / "sr-research-shared" / "references" / "browser-skill-literature-search.md").read_text(encoding="utf-8")
        for required in ["现有会话", "来源 URL", "检索时间", "归还借用标签页", "验证码"]:
            self.assertIn(required, skill + reference)
        for forbidden in ["Cookie", "令牌", "密码", "localStorage", "认证头"]:
            self.assertIn(forbidden, skill)
        self.assertIn("不绕过", skill)
        self.assertNotIn("调用 $browser-skill", skill)
        self.assertNotIn("安装 BrowserSkill 后重试", skill + reference)

    def test_sr53_has_drawio_authoring_and_source_qa(self) -> None:
        skill_root = ROOT / "skills" / "sr-core-figures"
        skill_text = (skill_root / "SKILL.md").read_text(encoding="utf-8")
        for required in [
            "### 数据图",
            "references/scientific-figure-authoring.md",
            "references/advisor-figure-patterns.md",
            "references/paper-figure-patterns.md",
            "references/figure-pattern-exemplars.md",
            "assets/figure-contract-template.md",
            "scripts/qa_scientific_figure.py",
            "### 可编辑示意图",
            "references/drawio-authoring.md",
            "references/drawio-visual-language.md",
            "references/drawio-export-qa.md",
            "scripts/qa_drawio.py",
            "preview_export=blocked",
        ]:
            self.assertIn(required, skill_text)
        self.assertNotIn("nature-figure", skill_text)

        special = (
            ROOT
            / "skills"
            / "sr-research-shared"
            / "references"
            / "record-templates"
            / "special"
            / "sr-53-core-figures.md"
        ).read_text(encoding="utf-8")
        for required in [
            "数据版本与复核方式（哈希写附录）",
            "样本量、重复次数、布局数或分箱数",
            "不确定性类型",
            "图例样式、覆盖对象和间距检查",
            "多面板编号与直接比较理由",
            "脱敏参考图及其借鉴边界",
            "绘图脚本或可编辑源文件核对结果（路径写附录）",
            "这张图不能支持的结论",
            "数据不变量检查",
        ]:
            self.assertIn(required, special)

        exemplar_dir = skill_root / "assets" / "figure-pattern-exemplars"
        expected_exemplars = {
            "method-framework.png",
            "domain-configuration.png",
            "cost-evidence.png",
            "comparison-signed-difference.png",
            "prediction-residual.png",
            "field-snapshots.png",
            "long-time-stability.png",
        }
        exemplar_guide = (skill_root / "references" / "figure-pattern-exemplars.md").read_text(encoding="utf-8")
        self.assertEqual({path.name for path in exemplar_dir.glob("*.png")}, expected_exemplars)
        self.assertLessEqual(sum(path.stat().st_size for path in exemplar_dir.glob("*.png")), 768 * 1024)
        for path in exemplar_dir.glob("*.png"):
            self.assertEqual(path.read_bytes()[:8], b"\x89PNG\r\n\x1a\n")
            self.assertIn(path.name, exemplar_guide)
        self.assertIn("不含私有项目数值", exemplar_guide)
        self.assertIn("合成数据", exemplar_guide)

        with tempfile.TemporaryDirectory(prefix="sr53-figure-") as temporary:
            temporary_path = Path(temporary)
            svg = temporary_path / "figure.svg"
            svg.write_text("<svg xmlns=\"http://www.w3.org/2000/svg\"><rect width=\"10\" height=\"10\"/></svg>", encoding="utf-8")
            digest = "0" * 64
            valid_contract = temporary_path / "figure-contract.md"
            valid_contract.write_text(
                f"""# Contract\n```yaml\nfigure_id: "20261011-test"\nfigure_version: "v1"\nclaim: "Method A is faster under the stated condition"\nevidence_role: "cost"\ndata_source:\n  - "data/test.csv"\nsource_data_sha256:\n  - '{digest}'\nstyle_exemplars:\n  - "assets/figure-pattern-exemplars/cost-evidence.png"\nsample_size: "n=4"\ncomparison: "Method A versus Method B"\nencoding: "black circle=raw run; gray bar=mean"\nunits: "wall time (s); dimensionless count"\nuncertainty: "range over two repeats"\nlegend: "white boxed legend with black border and clear spacing"\npanel_logic: "single panel"\nboundary: "does not prove accuracy"\ncaption: "Conditions, encodings, result, and boundary."\nexport_status: "passed"\nexport_files:\n  - "figure.svg"\nadvisor_review: "accepted"\n```\n""",
                encoding="utf-8",
            )
            passed = run(
                str(skill_root / "scripts" / "qa_scientific_figure.py"),
                str(valid_contract),
                "--figure",
                str(svg),
            )
            self.assertEqual(passed.returncode, 0, passed.stdout + passed.stderr)
            self.assertIn("QA=pass", passed.stdout)

            # A technically checked figure does not need a named or accepted human verdict.
            unsigned = temporary_path / "without-review.md"
            unsigned.write_text(valid_contract.read_text(encoding="utf-8").replace('advisor_review: "accepted"\n', ""), encoding="utf-8")
            unsigned_result = run(str(skill_root / "scripts" / "qa_scientific_figure.py"), str(unsigned), "--figure", str(svg), "--strict")
            self.assertEqual(unsigned_result.returncode, 0, unsigned_result.stdout + unsigned_result.stderr)

            invalid_contract = temporary_path / "invalid-contract.md"
            invalid_text = valid_contract.read_text(encoding="utf-8").replace('data_source:\n  - "data/test.csv"', 'data_source:\n  - "E:\\private\\test.csv"').replace("- '" + digest + "'", "- 'not-a-hash'")
            invalid_contract.write_text(invalid_text, encoding="utf-8")
            failed = run(str(skill_root / "scripts" / "qa_scientific_figure.py"), str(invalid_contract))
            self.assertEqual(failed.returncode, 2, failed.stdout + failed.stderr)
            self.assertIn("absolute path", failed.stdout)
            self.assertIn("source_data_sha256", failed.stdout)

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
            "### 从材料到演示文稿",
            "用户提供修改稿",
            "references/document-to-ppt.md",
            "references/group-meeting-ppt-standard.md",
            "references/ppt-layout-system.md",
            "references/logic-diagram-style.md",
            "references/human-revision-retrospective.md",
            "references/group-meeting-ppt-template-patterns.md",
            "assets/sr58-group-meeting-v8-style-template.pptx",
            "assets/ppt-page-plan.md",
            "assets/ppt-page-plan.md",
            "scripts/qa_group_meeting_pptx.py",
            "每页只有一个独立的 `SR58-SUMMARY` 总结句",
            "页面的主要内容类型为 `cognitive_type`",
            "红色加粗下划线",
            "不低于 18pt",
        ]:
            self.assertIn(required, skill_text)
        for required in [
            "## 每页一句总结",
            "## 内容与拆页",
            "## 标题、字体和颜色",
            "## 修改与检查",
            "summary_sentence:",
            "summary_shape: \"SR58-SUMMARY\"",
            "20–60 个汉字",
            "20–22pt 加粗微软雅黑",
        ]:
            self.assertIn(required, standard_text)
        document_text = (skill_root / "references" / "document-to-ppt.md").read_text(encoding="utf-8")
        for required in [
            "group-meeting-process-review",
            "材料覆盖表",
            "主要问题拆页",
            "按主要问题拆页，再调整字数",
            "ppt-layout-system.md",
            "logic-diagram-style.md",
            "human-revision-retrospective.md",
            "20260830 v8 组会风格",
            "激励、几何、介质、边界四要素",
        ]:
            self.assertIn(required, document_text)
        template_path = skill_root / "assets" / "sr58-group-meeting-v8-style-template.pptx"
        template_plan = skill_root / "assets" / "sr58-group-meeting-v8-style-template-page-plan.md"
        template_patterns = (skill_root / "references" / "group-meeting-ppt-template-patterns.md").read_text(encoding="utf-8")
        contact_sheet = skill_root / "assets" / "sr58-group-meeting-v8-style-contact-sheet.png"
        self.assertTrue(template_path.is_file())
        self.assertLess(template_path.stat().st_size, 128 * 1024)
        for obsolete in [
            "sr58-group-meeting-template.pptx",
            "sr58-group-meeting-template-page-plan.md",
            "sr58-group-meeting-template-contact-sheet.png",
            "sr58-group-meeting-v8-template.pptx",
            "sr58-group-meeting-v8-template-page-plan.md",
            "sr58-group-meeting-v8-contact-sheet.png",
        ]:
            self.assertFalse((skill_root / "assets" / obsolete).exists())
        self.assertTrue(contact_sheet.is_file())
        self.assertLess(contact_sheet.stat().st_size, 512 * 1024)
        self.assertEqual(contact_sheet.read_bytes()[:8], b"\x89PNG\r\n\x1a\n")
        self.assertIn("没有原始研究图", template_patterns)
        self.assertIn("原始幻灯片截图", template_patterns)
        for forbidden in ["朱凌", "浙江大学", "file:///", "reference-folder/"]:
            self.assertNotIn(forbidden, template_patterns)
            self.assertNotIn(forbidden, template_plan.read_text(encoding="utf-8"))
        with zipfile.ZipFile(template_path) as package:
            slide_names = [name for name in package.namelist() if name.startswith("ppt/slides/slide") and name.endswith(".xml")]
            self.assertEqual(len(slide_names), 20)
            self.assertFalse(any(name.startswith("ppt/media/") for name in package.namelist()))
            native_table_slides = [name for name in package.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", name) and b"graphicFrame" in package.read(name)]
            self.assertTrue({"ppt/slides/slide11.xml", "ppt/slides/slide12.xml", "ppt/slides/slide13.xml"}.issubset(native_table_slides))
            package_text = " ".join(package.read(name).decode("utf-8") for name in slide_names)
            for forbidden in ["朱凌", "浙江大学", "file:///", "reference-folder/", "①", "②", "③", "④"]:
                self.assertNotIn(forbidden, package_text)
            for reference_color in ["003399", "D9E2F3", "C00000", "262626", "BFBFBF"]:
                self.assertIn(reference_color, package_text)
            for v8_required in ["激励", "几何", "介质", "边界", "网格", "未知量", "坐标", "图例", "colorbar", "24号"]:
                self.assertIn(v8_required, package_text)
            self.assertIn("不用圆圈序号", template_patterns)
            self.assertIn("20260830 v8 组会模式", standard_text)
            self.assertIn("模型四要素：激励、几何、介质、边界", template_plan.read_text(encoding="utf-8"))
            self.assertIn("通栏标题", template_patterns)
            self.assertIn("四类视图", template_patterns)
            self.assertIn("资源统计", template_patterns)
            self.assertIn("20pt", template_patterns)
            self.assertIn("关键内容红色加粗下划线", template_patterns)
            self.assertIn("重复模块突出变化部分", template_patterns)
            self.assertIn("配色规则｜按重要度红蓝黑分级", package_text)
            self.assertIn("结果页规则", package_text)
            self.assertIn("重复模块规则", package_text)
            self.assertIn("表格规则", package_text)
            for reference_color in ["#003399", "#D9E2F3", "#C00000", "#262626", "#BFBFBF"]:
                self.assertIn(reference_color, template_patterns)
            for forbidden in ["①", "②", "③", "④"]:
                self.assertNotIn(forbidden, template_patterns)
        template_qa = run(
            str(skill_root / "scripts" / "qa_group_meeting_pptx.py"),
            str(template_path),
            "--page-plan",
            str(template_plan),
            "--strict",
        )
        self.assertEqual(template_qa.returncode, 0, template_qa.stdout + template_qa.stderr)
        self.assertIn("QA=pass", template_qa.stdout)

        page_plan_text = (skill_root / "assets" / "ppt-page-plan.md").read_text(encoding="utf-8")
        for required in [
            "presentation_mode:",
            "材料覆盖表",
            "cognitive_type:",
            "layout_pattern:",
            "split_check:",
            "用户修改反馈",
        ]:
            self.assertIn(required, page_plan_text)

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
            + xml_run("①错误编号", 1800, "000000")
        )
        pending_body = xml_run("此内容待验证", 1800, "000000")
        valid_plan = (
            "# Page plan\n\n## Slide 1 — Claim\n\n"
            "kicker: \"0.1 成果\"\n"
            "title: \"结论\"\n"
            "cognitive_type: \"claim\"\n"
            "layout_pattern: \"claim\"\n"
            "summary_sentence: \"本页证明结论成立。\"\n"
            "one_cognitive_object: true\n"
            "needs_two_summaries: false\n"
            "split_recommended: false\n"
            "density_exception_reason: \"\"\n"
        )
        invalid_plan = (
            "# Page plan\n\n## Slide 1 — Mixed\n\n"
            "kicker: \"2.2 机制②\"\n"
            "title: \"结论\"\n"
            "cognitive_type: \"mechanism\"\n"
            "layout_pattern: \"claim\"\n"
            "summary_sentence: \"另一句总结。\"\n"
            "one_cognitive_object: false\n"
            "needs_two_summaries: true\n"
            "split_recommended: true\n"
            "density_exception_reason: \"\"\n"
        )

        with tempfile.TemporaryDirectory(prefix="sr58-pptx-") as temporary:
            valid = Path(temporary) / "valid.pptx"
            invalid = Path(temporary) / "invalid.pptx"
            missing = Path(temporary) / "missing-summary.pptx"
            pending = Path(temporary) / "pending.pptx"
            good_plan = Path(temporary) / "valid-plan.md"
            bad_plan = Path(temporary) / "invalid-plan.md"
            good_plan.write_text(valid_plan, encoding="utf-8")
            bad_plan.write_text(invalid_plan, encoding="utf-8")
            for target, body in [(valid, valid_body), (invalid, invalid_body), (missing, valid_body), (pending, pending_body)]:
                with zipfile.ZipFile(target, "w") as package:
                    theme = '<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:themeElements><a:fontScheme name="SR58"><a:majorFont><a:latin typeface="Microsoft YaHei"/><a:ea typeface="Microsoft YaHei"/><a:cs typeface=""/></a:majorFont><a:minorFont><a:latin typeface="Microsoft YaHei"/><a:ea typeface="Microsoft YaHei"/><a:cs typeface=""/></a:minorFont></a:fontScheme></a:themeElements></a:theme>'
                    package.writestr("ppt/theme/theme1.xml", theme)
                    prefix = slide_prefix if target is not missing else slide_prefix.replace(summary_shape, "")
                    package.writestr("ppt/slides/slide1.xml", prefix + body + slide_suffix)

            passed = run(str(skill_root / "scripts" / "qa_group_meeting_pptx.py"), str(valid), "--page-plan", str(good_plan))
            self.assertEqual(passed.returncode, 0, passed.stdout + passed.stderr)
            self.assertIn("QA=pass", passed.stdout)

            self.assertIn("summary_shapes=1", passed.stdout)

            failed = run(str(skill_root / "scripts" / "qa_group_meeting_pptx.py"), str(invalid), "--page-plan", str(bad_plan))
            self.assertEqual(failed.returncode, 2, failed.stdout + failed.stderr)
            self.assertIn("red runs exceed the limit of 3", failed.stdout)
            self.assertIn("below the 14pt minimum", failed.stdout)
            self.assertIn("non-Microsoft-YaHei font", failed.stdout)
            self.assertIn("small-circle numeral", failed.stdout)

            no_summary = run(str(skill_root / "scripts" / "qa_group_meeting_pptx.py"), str(missing), "--page-plan", str(good_plan))
            self.assertEqual(no_summary.returncode, 2, no_summary.stdout + no_summary.stderr)
            self.assertIn("requires exactly one visible SR58-SUMMARY", no_summary.stdout)

            pending_result = run(str(skill_root / "scripts" / "qa_group_meeting_pptx.py"), str(pending), "--page-plan", str(good_plan))
            self.assertEqual(pending_result.returncode, 2, pending_result.stdout + pending_result.stderr)
            self.assertIn("should move to backup or next-plan context", pending_result.stdout)
            self.assertIn("page plan admits multiple cognitive objects", failed.stdout)
            self.assertIn("page needs two summaries", failed.stdout)
            self.assertIn("split_recommended is true", failed.stdout)
            self.assertIn("SR58-SUMMARY does not match the page plan sentence", failed.stdout)
            self.assertIn("page_plan_records=1", passed.stdout)

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
            self.assertEqual(export["reference"], "references/zotero-batch-import.md")

            skill_root = ROOT / "skills" / skill_name
            skill_text = (skill_root / "SKILL.md").read_text(encoding="utf-8")
            template_text = (skill_root / "assets" / "output-template.md").read_text(encoding="utf-8")
            self.assertIn("zotero-batch-import.md", skill_text)
            self.assertIn("bibliography_exports:", template_text)
            self.assertIn("Zotero 实机导入", template_text)

    def test_pr_sr_skills_have_plain_interaction_guides(self) -> None:
        skill_dirs = sorted(path for path in (ROOT / "skills").iterdir() if path.is_dir() and path.name.startswith(("pr-", "sr-")))
        self.assertEqual(len(skill_dirs), 89)
        canonical = (ROOT / "docs" / "pr-sr-interaction-standard.md").read_text(encoding="utf-8")
        for directory in skill_dirs:
            guide = directory / "AGENTS.md"
            self.assertTrue(guide.is_file(), f"missing {guide}")
            self.assertEqual(guide.read_text(encoding="utf-8"), canonical)
            skill_text = (directory / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("[AGENTS.md](AGENTS.md)", skill_text)

        checked = run("scripts/generate_pr_sr_interaction_guides.py", "--check")
        self.assertEqual(checked.returncode, 0, checked.stdout + checked.stderr)
        self.assertIn("PASS: 89 PR/SR interaction guides", checked.stdout)

    def test_sr_record_templates_and_plain_language_validation(self) -> None:
        items = json.loads((ROOT / "skills/sr-doctoral-research/catalog.json").read_text(encoding="utf-8"))["skills"]
        self.assertEqual(len(items), 68)
        self.assertEqual(len({item["aspect_key"] for item in items}), 8)
        for item in items:
            text = (ROOT / "skills" / item["name"] / "assets/output-template.md").read_text(encoding="utf-8")
            for heading in ["一句话结论", "要解决的问题", "做法与结果", "专业内容", "依据与检查", "适用范围与未解决问题", "下一步"]:
                self.assertIn(heading, text)
            self.assertIn(f'sr_id: "{item["id"]}"', text)
            self.assertNotIn('owner: "<', text)
            self.assertNotIn("human_verdict:", text)
        generated = run("scripts/generate_sr_record_templates.py", "--check")
        self.assertEqual(generated.returncode, 0, generated.stdout + generated.stderr)
        valid = """# 一句话结论
样本中的两个重复标识已定位，尚未修改原始数据。

## 要解决的问题
检查重复标识是否影响分析。

## 做法与结果
读取样例文件并按标识分组，发现两条重复记录。

## 依据与检查
| 结果 | 来源 | 检查 |
|---|---|---|
| 两条重复记录 | samples.csv 第 2、4 行 | 分组结果与原始记录一致 |

## 适用范围与未解决问题
这些结果不能支持全量数据无其他问题的结论。

## 下一步
核查全量数据；做到什么程度算完成：每个标识的重复次数有记录。
"""
        with tempfile.TemporaryDirectory(prefix="sr-record-qa-") as temporary:
            good = Path(temporary) / "good.md"
            bad = Path(temporary) / "bad.md"
            good.write_text(valid, encoding="utf-8")
            bad.write_text(valid.replace("| 两条重复记录 | samples.csv 第 2、4 行 | 分组结果与原始记录一致 |", "| | | |"), encoding="utf-8")
            validator = str(ROOT / "skills/sr-research-shared/scripts/validate_sr_record.py")
            passed = run(validator, str(good), "--strict")
            self.assertEqual(passed.returncode, 0, passed.stdout + passed.stderr)
            failed = run(validator, str(bad))
            self.assertEqual(failed.returncode, 2, failed.stdout + failed.stderr)
            self.assertIn("需要具体来源", failed.stdout)
            bad.write_text(valid.replace("## 适用范围与未解决问题", "## 省略限制"), encoding="utf-8")
            failed = run(validator, str(bad))
            self.assertEqual(failed.returncode, 2)

    def test_sr_progress_narrative_covers_weekly_and_timeline_without_deck_duplication(self) -> None:
        skill = (ROOT / "skills/sr-progress-narrative/SKILL.md").read_text(encoding="utf-8")
        for required in ["周报", "时间线", "不能支持的结论", "渲染检查", "不制作 PPT"]:
            self.assertIn(required, skill)
        self.assertFalse((ROOT / "skills/sr-weekly-meeting").exists())
        for profile_name in ("ai4science", "all"):
            profile = json.loads((ROOT / "profiles" / f"{profile_name}.json").read_text(encoding="utf-8"))
            self.assertIn("sr-progress-narrative", profile["skills"])
            self.assertNotIn("sr-weekly-meeting", profile["skills"])

    def test_pr_management_writing_standard_and_tools(self) -> None:
        ps_root = ROOT / "skills" / "pr-ps-00-project-supervision"
        standard = (ps_root / "references" / "20260929-管理文档写作标准-管理规范.md").read_text(encoding="utf-8")
        for required in [
            "Status: approved",
            "## 1. 文档分级",
            "## 2. A 级结构",
            "## 3. B 级结构",
            "## 4. C 级结构",
            "## 5. 公文词映射表",
            "## 6. 编号规则",
            "## 7. 表格证据列",
            "## 8. 安全网",
            "## 9. 句式",
            "## 10. 命名",
        ]:
            self.assertIn(required, standard)

        expected_levels = {
            "20260912-用户需求-需求记录模板.md": "A",
            "20260912-项目工作-日志模板.md": "A",
            "20260912-项目操作监督-监督记录模板.md": "B",
            "20260912-项目变更-变更记录模板.md": "B",
            "20260912-问题缺陷-反思模板.md": "B",
            "20260912-质量门禁-检查模板.md": "C",
            "20260912-成本时间-统计模板.md": "C",
        }
        for name, level in expected_levels.items():
            text = (ps_root / "assets" / name).read_text(encoding="utf-8")
            self.assertIn(f'writing_level: "{level}"', text)
        for name in ["20260912-用户需求-需求记录模板.md", "20260912-项目工作-日志模板.md"]:
            text = (ps_root / "assets" / name).read_text(encoding="utf-8")
            for required in [
                "## 1. 背景一句话",
                "## 2. 研究内容",
                "## 3. 研究影响",
                "## 附录：管理信息",
                "### 正文编号对照",
                "### 原记录对照",
            ]:
                self.assertIn(required, text)

        api = (ps_root / "references" / "20260912-项目监理脚本工具-API说明.md").read_text(encoding="utf-8")
        self.assertIn("ps_04_validate_management_document.py", api)
        ps01 = (ROOT / "skills" / "pr-ps-01-project-governance" / "SKILL.md").read_text(encoding="utf-8")
        ps03 = (ROOT / "skills" / "pr-ps-03-project-logging" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("需求记录按 A 级生成", ps01)
        self.assertIn("项目日志按 A 级生成", ps03)

        with tempfile.TemporaryDirectory(prefix="pr-management-doc-") as temporary:
            project = Path(temporary)
            management = project / "00-项目管理"
            (management / "requirements").mkdir(parents=True)
            (management / "supervision").mkdir(parents=True)
            (project / "AGENTS.md").write_text(
                "# Pilot\n\n```project-supervision\nproject_management_root = \"00-项目管理\"\nrequirements_dir = \"requirements\"\nsupervision_dir = \"supervision\"\n```\n",
                encoding="utf-8",
            )
            creator = ps_root / "scripts" / "ps_01_create_governance_document.py"
            created_requirement = run(
                str(creator), "--project-root", str(project), "--type", "requirement", "--summary", "写作标准试点", "--write"
            )
            self.assertEqual(created_requirement.returncode, 0, created_requirement.stdout + created_requirement.stderr)
            created_supervision = run(
                str(creator), "--project-root", str(project), "--type", "supervision", "--summary", "写作标准试点", "--write"
            )
            self.assertEqual(created_supervision.returncode, 0, created_supervision.stdout + created_supervision.stderr)

            requirement_file = next((management / "requirements").glob("*-写作标准试点-需求记录.md"))
            supervision_file = next((management / "supervision").glob("*-写作标准试点-监督记录.md"))
            self.assertIn('writing_level: "A"', requirement_file.read_text(encoding="utf-8"))
            self.assertIn('writing_level: "B"', supervision_file.read_text(encoding="utf-8"))

            validator = ps_root / "scripts" / "ps_04_validate_management_document.py"
            for target in (requirement_file, supervision_file):
                result = run(str(validator), str(target), "--strict")
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn("QA=pass", result.stdout)

            invalid = project / "invalid.md"
            invalid.write_text(
                "---\nwriting_level: \"A\"\n---\n\n# Bad\n\nREQ-1 见 a/b.md，`code`，具名。\n",
                encoding="utf-8",
            )
            failed = run(str(validator), str(invalid))
            self.assertEqual(failed.returncode, 2, failed.stdout + failed.stderr)
            for required in [
                "A级缺少必需结构",
                "A级正文出现治理编号",
                "A级正文出现路径",
                "A级正文出现反引号",
                "A级正文出现公文词",
            ]:
                self.assertIn(required, failed.stdout)

            baseline = project / "baseline.md"
            revised = project / "revised.md"
            common = "---\nid: \"REQ-1\"\nwriting_level: \"A\"\n---\n\n# Test\n\nREQ-1 a/b.md\n\n> 用户原话必须保留\n"
            baseline.write_text(common + "\n旧句。\n", encoding="utf-8")
            revised.write_text(common + "\n新句。\n", encoding="utf-8")
            compared = run(str(validator), "--baseline", str(baseline), "--revised", str(revised), "--strict")
            self.assertEqual(compared.returncode, 0, compared.stdout + compared.stderr)
            self.assertIn("QA=pass", compared.stdout)

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
