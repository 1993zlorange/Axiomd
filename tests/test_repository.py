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
                "Adaptive reasoning policy:",
                "Light path:",
                "Standard path:",
                "Deep path:",
                "Deep triggers for this role:",
            ]:
                self.assertIn(required, instructions, f"{path.name} missing {required!r}")

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
            "## Human revision retrospective",
            "references/document-to-ppt.md",
            "references/group-meeting-ppt-standard.md",
            "references/ppt-layout-system.md",
            "references/logic-diagram-style.md",
            "references/human-revision-retrospective.md",
            "assets/ppt-page-plan.md",
            "scripts/qa_group_meeting_pptx.py",
            "one complete, visible `SR58-SUMMARY` sentence on every page",
            "one primary `cognitive_type` per page",
            "red+bold+underline",
            "body ≥18pt",
        ]:
            self.assertIn(required, skill_text)
        for required in [
            "## One-sentence summary contract",
            "## Cognitive-object and layout gate",
            "## Structured titles and logic diagrams",
            "## Human revision retrospective",
            "summary_sentence:",
            "summary_shape: \"SR58-SUMMARY\"",
            "Target 20–60 Chinese characters",
            "20–22pt bold Microsoft YaHei",
        ]:
            self.assertIn(required, standard_text)
        document_text = (skill_root / "references" / "document-to-ppt.md").read_text(encoding="utf-8")
        for required in [
            "group-meeting-process-review",
            "Evidence coverage matrix",
            "Cognitive-object extraction",
            "Split by cognitive object before considering word count",
            "ppt-layout-system.md",
            "logic-diagram-style.md",
            "human-revision-retrospective.md",
        ]:
            self.assertIn(required, document_text)
        page_plan_text = (skill_root / "assets" / "ppt-page-plan.md").read_text(encoding="utf-8")
        for required in [
            "presentation_mode:",
            "Evidence coverage matrix",
            "cognitive_type:",
            "layout_pattern:",
            "split_check:",
            "Human revision feedback",
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
            self.assertEqual(export["reference"], "../sr-research-shared/references/zotero-batch-import.md")

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
        catalog = json.loads(
            (ROOT / "skills" / "sr-doctoral-research" / "catalog.json").read_text(encoding="utf-8")
        )
        items = catalog["skills"]
        self.assertEqual(len(items), 68)
        aspects = {item["aspect_key"] for item in items}
        self.assertEqual(
            aspects,
            {"problem", "literature", "idea", "method", "experiment", "analysis", "paper", "progress"},
        )
        for item in items:
            template = ROOT / "skills" / item["name"] / "assets" / "output-template.md"
            text = template.read_text(encoding="utf-8")
            for required in [
                "# 一句话结论",
                "## 1. 原来遇到什么问题",
                "## 2. 问题原因分析",
                "## 3. 当时有哪些可能做法",
                "## 4. 本阶段做了什么",
                "## 5. 遇到的困难和处理方式",
                "## 6. 当前结果",
                "## 7. 本阶段没有解决的问题",
                "## 8. 下一步计划",
                "## 9. 专业补充",
                "## 附录A：支撑材料",
                "## 附录B：系统记录",
                f'sr_id: "{item["id"]}"',
            ]:
                self.assertIn(required, text, f"{item['name']} missing {required!r}")

        for aspect in sorted(aspects):
            self.assertTrue(
                (ROOT / "skills" / "sr-research-shared" / "references" / "record-templates" / "aspects" / f"{aspect}.md").is_file()
            )
        for special in [
            "sr-07-search-strategy.md",
            "sr-08-literature-screening.md",
            "sr-53-core-figures.md",
            "sr-58-talk-open-source.md",
            "sr-68-stage-archive.md",
        ]:
            path = ROOT / "skills" / "sr-research-shared" / "references" / "record-templates" / "special" / special
            self.assertTrue(path.is_file(), f"missing special template {path}")
        for handoff in ["explore.md", "execute.md", "express.md"]:
            path = ROOT / "skills" / "sr-research-shared" / "references" / "record-templates" / "handoffs" / handoff
            self.assertTrue(path.is_file(), f"missing handoff template {path}")
        for stage in ["explore", "execute", "express"]:
            path = ROOT / "skills" / "sr-research-shared" / "assets" / f"workflow-handoff-{stage}-template.md"
            self.assertTrue(path.is_file(), f"missing assembled handoff template {path}")

        generated = run("scripts/generate_sr_record_templates.py", "--check")
        self.assertEqual(generated.returncode, 0, generated.stdout + generated.stderr)
        self.assertIn("PASS: 68 SR record templates", generated.stdout)

        base = (ROOT / "skills" / "sr-research-shared" / "assets" / "achievement-card-template.md").read_text(encoding="utf-8")
        valid = base
        replacements = {
            "<这一阶段解决了什么问题，做到什么程度，还有什么没解决。>": "文献筛选已完成，核心文献从70篇收敛到10篇，全文复筛仍未完成。",
            "|  |  | 是 / 否 / 待定 |  |": "| 检索词过宽 | 初筛发现大量无关主题 | 是 | 需要补充排除标准 |",
            "| 方案A |  |  | 推荐 / 不推荐 |": "| 只按标题筛 | 速度快 | 可能漏掉相关论文 | 推荐 |",
            "| 方案B |  |  | 推荐 / 不推荐 |": "| 直接全文复筛 | 判断更准 | 阅读时间约8小时 | 不推荐 |",
            "推荐方案及原因：": "推荐方案及原因：先按标题摘要筛，因为当前文献量较大且主题边界清楚。",
            "|  |  |  | 已解决 / 部分解决 / 未解决 |": "| 检索结果重复 | 影响计数 | 按 DOI 和题名去重 | 已解决 |",
            "|  |  |  |  |": "| 全文获取受限 | 部分论文无法下载 | 需要馆际互借 | 影响复筛 |",
            "- 下一步先做什么：": "- 下一步先做什么：补齐10篇核心文献全文。",
            "- 做到什么程度算完成：": "- 做到什么程度算完成：每篇都有保留或排除理由。",
            "<按本工作包所属研究阶段和专业需要填写，不作为领导阅读的主文。>": "### 文献调研补充\n- 数据库：Web of Science\n",
        }
        for old, new in replacements.items():
            valid = valid.replace(old, new, 1)
        bad = valid.replace("## 7. 本阶段没有解决的问题", "## 7. 遗留内容", 1)
        bad = bad.replace("只按标题筛", "冻结后只按标题筛", 1)

        with tempfile.TemporaryDirectory(prefix="sr-record-qa-") as temporary:
            valid_path = Path(temporary) / "valid.md"
            bad_path = Path(temporary) / "bad.md"
            valid_path.write_text(valid, encoding="utf-8")
            bad_path.write_text(bad, encoding="utf-8")
            validator = ROOT / "skills" / "sr-research-shared" / "scripts" / "validate_sr_record.py"

            passed = run(str(validator), str(valid_path))
            self.assertEqual(passed.returncode, 0, passed.stdout + passed.stderr)
            self.assertIn("QA=pass", passed.stdout)

            failed = run(str(validator), str(bad_path))
            self.assertEqual(failed.returncode, 2, failed.stdout + failed.stderr)
            self.assertIn("missing section: ## 7. 本阶段没有解决的问题", failed.stdout)
            self.assertIn("internal management term", failed.stdout)

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
