"""日记录的路径、幂等、并发、跨日和失败恢复行为。"""

from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "skills/pr-ps-00-project-supervision/scripts"
SPEC = importlib.util.spec_from_file_location("daily_records_test_module", SCRIPTS / "daily_records.py")
daily = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(daily)


class DailyRecordTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.config = {"project_management_root": "achieve/00-项目管理", "record_profile": "software",
                       "logs_dir": "logs", "requirements_dir": "requirements", "supervision_dir": "supervision"}
        self.now = datetime(2026, 10, 29, 8, tzinfo=timezone.utc)

    def payload(self, identifier="one", **extra):
        value = {"entry_id": identifier, "event_key": "task-" + identifier, "content": "完成当前任务，已保存实际结果。",
                 "impact": "用户可以按要求继续使用。", "requirement_id": "TASK-1", "status": "completed"}
        value.update(extra)
        return value

    def append(self, identifier="one", **kwargs):
        return daily.append_record(self.root, self.config, "log", "任务" + identifier,
                                   self.payload(identifier), now=self.now, write=True, **kwargs)

    def test_preview_and_no_content_never_create_directories(self):
        daily.append_record(self.root, self.config, "log", "标题", self.payload(), now=self.now)
        self.assertEqual(list(self.root.iterdir()), [])
        with self.assertRaises(daily.RecordError):
            daily.append_record(self.root, self.config, "log", "标题", {}, now=self.now, write=True)
        self.assertEqual(list(self.root.iterdir()), [])

    def test_summary_alias_and_event_retry_use_one_file_without_duplicate(self):
        first, _ = self.append()
        second, _ = daily.append_record(self.root, self.config, "项目日志", "另一个任务",
                                       self.payload("two"), now=self.now, write=True)
        self.assertEqual(first, second)
        before = first.read_bytes()
        _, changed = self.append()
        self.assertFalse(changed)
        self.assertEqual(first.read_bytes(), before)
        self.assertEqual(len(daily.entry_blocks(before.decode())), 2)
        self.assertEqual(first.name, "20261029-项目进度-日志.md")

    def test_same_event_changed_content_requires_explicit_revision(self):
        path, _ = self.append()
        old = path.read_bytes()
        with self.assertRaises(daily.RecordError):
            daily.append_record(self.root, self.config, "log", "任务one", self.payload(content="不同结果"), now=self.now, write=True)
        self.assertEqual(path.read_bytes(), old)
        daily.append_record(self.root, self.config, "log", "修订说明",
                            self.payload("revision", revision_of="one"), now=self.now, write=True)
        self.assertEqual(len(daily.entry_blocks(path.read_text(encoding="utf-8"))), 2)

    def test_different_attempt_is_real_new_entry(self):
        path, _ = self.append()
        payload = self.payload("retry", event_key="task-one", attempt_id="2")
        daily.append_record(self.root, self.config, "log", "真实重试", payload, now=self.now, write=True)
        self.assertEqual(len(daily.entry_blocks(path.read_text(encoding="utf-8"))), 2)

    def test_shanghai_midnight_and_cross_day_revision(self):
        first = datetime(2026, 10, 29, 15, 59, tzinfo=timezone.utc)
        second = datetime(2026, 10, 29, 16, 1, tzinfo=timezone.utc)
        a, _ = daily.append_record(self.root, self.config, "log", "当天进展", self.payload(), now=first, write=True)
        reference = a.relative_to(self.root).as_posix() + "#entry-one"
        b, _ = daily.append_record(self.root, self.config, "log", "次日更正",
                                  self.payload("two", revision_of=reference, occurred_at=first.isoformat()), now=second, write=True)
        self.assertTrue(a.name.startswith("20261029"))
        self.assertTrue(b.name.startswith("20261030"))
        self.assertFalse(daily.validate_daily(b.read_text(encoding="utf-8")))

    def test_duplicate_active_file_in_other_directory_blocks_append(self):
        path, _ = self.append()
        other = self.root / "other/20261029-AgentB-项目日志.md"
        other.parent.mkdir()
        other.write_text(path.read_text(encoding="utf-8").replace('record_type: "log"', 'record_type: "科研日志"'), encoding="utf-8")
        before = path.read_bytes()
        with self.assertRaises(daily.RecordError):
            self.append("two")
        self.assertEqual(path.read_bytes(), before)

    def test_schema_inside_output_and_unusual_extension_is_not_hidden(self):
        path, _ = self.append()
        hidden = self.root / "output/trace/second.notes"
        hidden.parent.mkdir(parents=True)
        hidden.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
        with self.assertRaises(daily.RecordError):
            self.append("two")

    def test_cross_midnight_replay_returns_original_file(self):
        path, _ = self.append()
        later = datetime(2026, 10, 30, 8, tzinfo=timezone.utc)
        returned, changed = daily.append_record(self.root, self.config, "log", "任务one", self.payload(), now=later, write=True)
        self.assertFalse(changed)
        self.assertEqual(returned, path)
        self.assertEqual(len(list(path.parent.glob("*.md"))), 1)

    def test_readonly_export_does_not_duplicate_the_writable_source(self):
        path, _ = self.append()
        exported = self.root / "export.md"
        text = path.read_text(encoding="utf-8").replace('writing_level: "A"',
            'writing_level: "A"\nderived_from: ' + json.dumps(path.relative_to(self.root).as_posix(), ensure_ascii=False))
        exported.write_text(text, encoding="utf-8")
        self.append("two")
        self.assertEqual(len(daily.entry_blocks(path.read_text(encoding="utf-8"))), 2)

    def test_fake_export_source_is_not_a_daily_master(self):
        path, _ = self.append()
        fields = daily.frontmatter(path.read_text(encoding="utf-8"))
        fake = self.root / "README.md"
        fake.write_text('---\n' + ''.join(k + ': ' + json.dumps(fields[k]) + '\n' for k in ["project_id", "record_date", "record_type"]) + '---\n', encoding="utf-8")
        exported = self.root / "second.notes"
        exported.write_text(path.read_text(encoding="utf-8").replace('writing_level: "A"', 'writing_level: "A"\nderived_from: "README.md"'), encoding="utf-8")
        with self.assertRaises(daily.RecordError):
            self.append("two")

    def test_idempotent_replay_does_not_accept_corrupt_body_or_changed_profile(self):
        path, _ = self.append()
        original = path.read_text(encoding="utf-8")
        path.write_text(original.replace('<a id="entry-one"></a>', ''), encoding="utf-8")
        with self.assertRaises(daily.RecordError):
            self.append()
        path.write_text(original.replace('record_profile: "software"', 'record_profile: "research"'), encoding="utf-8")
        with self.assertRaises(daily.RecordError):
            self.append()

    def test_scientific_handoff_preserves_verdict_and_validates_read_anchor(self):
        self.config["record_profile"] = "research"
        source, _ = daily.append_record(self.root, self.config, "achievement", "研究结果",
            self.payload("card-one", sr_id="SR-34"), now=self.now, write=True)
        reference = source.relative_to(self.root).as_posix() + "#entry-card-one"
        payload = self.payload("handoff-one", cards_read=[reference], handoffs_read=[], human_verdict="pending", scientific_accepted=False)
        target, _ = daily.append_record(self.root, self.config, "handoff", "真实交接", payload, now=self.now, write=True)
        item = daily.entry_blocks(target.read_text(encoding="utf-8"))[0][0]
        self.assertEqual(item["cards_read"], [reference])
        self.assertEqual(item["human_verdict"], "pending")
        self.assertFalse(item["scientific_accepted"])
        with self.assertRaises(daily.RecordError):
            daily.append_record(self.root, self.config, "handoff", "错误来源",
                self.payload("handoff-bad", cards_read=[reference.replace('card-one', 'absent')]), now=self.now, write=True)

    def test_directory_legacy_exemption_is_rejected(self):
        (self.root / "history").mkdir()
        policy = {"record_policy": {"project_id": "portable", "profile": "software", "types": {}, "legacy_paths": ["history"]}}
        (self.root / "registry.json").write_text(json.dumps(policy), encoding="utf-8")
        self.config["record_policy_registry"] = "registry.json"
        with self.assertRaises(daily.RecordError):
            self.append()

    def test_each_entry_is_validated_not_only_first(self):
        path, _ = self.append()
        self.append("two")
        text = path.read_text(encoding="utf-8").replace('"requirement_id": "TASK-1"', '"requirement_id": ""', 1)
        self.assertTrue(any("需求" in e for e in daily.validate_daily(text)))
        text = path.read_text(encoding="utf-8").replace('"entry_id": "two"', '"entry_id": "one"')
        self.assertTrue(any("重复" in e for e in daily.validate_daily(text)))

    def test_research_log_requires_point_and_source_and_cards_use_shared_home(self):
        self.config["record_profile"] = "research"
        with self.assertRaises(daily.RecordError):
            daily.append_record(self.root, self.config, "log", "没有要点", self.payload(), now=self.now, write=True)
        payload = self.payload(research_point="方法效率", research_source="研究目标第1项")
        path, _ = daily.append_record(self.root, self.config, "log", "有要点", payload, now=self.now, write=True)
        self.assertEqual(path.name, "20261029-科研进度-日志.md")
        card, _ = daily.append_record(self.root, self.config, "成果卡", "研究结果",
                                     self.payload("card", sr_id="SR-34"), now=self.now, write=True)
        self.assertEqual(card.parent.name, "08-项目推进与下一步计划")

    def test_path_escape_and_boundary_injection_are_rejected(self):
        self.config["logs_dir"] = "../../outside"
        with self.assertRaises(daily.RecordError):
            self.append()
        self.config["logs_dir"] = "logs"
        with self.assertRaises(daily.RecordError):
            daily.append_record(self.root, self.config, "log", "标题",
                                self.payload(content='<!-- daily-entry {} -->'), now=self.now, write=True)

    def test_atomic_failure_keeps_old_bytes_and_cleans_temporary(self):
        path, _ = self.append()
        old = path.read_bytes()
        with mock.patch.object(daily.os, "replace", side_effect=OSError("disk unavailable")):
            with self.assertRaises(OSError):
                self.append("two")
        self.assertEqual(path.read_bytes(), old)
        self.assertEqual(list(path.parent.glob(".daily-*.tmp")), [])

    @unittest.skipUnless(os.name == "nt", "Windows路径表示回归")
    def test_windows_extended_prefix_does_not_create_false_escape(self):
        resolve = Path.resolve
        def extended(path, *args, **kwargs):
            result = resolve(path, *args, **kwargs)
            return Path("\\\\?\\" + str(result)) if path.name == "logs" else result
        with mock.patch.object(Path, "resolve", autospec=True, side_effect=extended):
            result = daily.inside(self.root, "logs")
        self.assertEqual(result, self.root / "logs")

    def test_registry_configuration_is_project_relative_and_controls_unique_path(self):
        policy = {"record_policy": {"enabled": True, "project_id": "portable", "profile": "software",
            "timezone": "Asia/Shanghai", "types": {"log": {"directory": "records/progress", "filename_body": "项目进度", "label": "日志"}}}}
        (self.root / "registry.json").write_text(json.dumps(policy), encoding="utf-8")
        self.config["record_policy_registry"] = "registry.json"
        path, _ = self.append()
        self.assertEqual(path.parent, self.root / "records/progress")
        self.assertEqual(daily.frontmatter(path.read_text(encoding="utf-8"))["project_id"], "portable")

    def test_sr_validator_checks_evidence_in_every_daily_entry(self):
        self.config["record_profile"] = "research"
        validator_spec = importlib.util.spec_from_file_location("sr_daily_validator",
            ROOT / "skills/sr-research-shared/scripts/validate_sr_record.py")
        validator = importlib.util.module_from_spec(validator_spec)
        validator_spec.loader.exec_module(validator)
        content = ("# 一句话结论\n样本结果已整理，范围限于当前样本。\n\n"
            "## 要解决的问题\n比较当前样本中的结果差异。\n\n"
            "## 做法与结果\n按相同条件整理已保存结果。\n\n"
            "## 依据与检查\n已有样本表第二行说明本次结果。\n\n"
            "## 适用范围与未解决问题\n这些结果不能支持未测试对象。\n\n"
            "## 下一步\n补充必要比较，范围保持不变。\n")
        path, _ = daily.append_record(self.root, self.config, "achievement", "样本分析",
            self.payload("sr-one", sr_id="SR-41", content=content), now=self.now, write=True)
        self.assertEqual(validator.validate(path)[0], [])
        bad = content.replace("已有样本表第二行说明本次结果。", "")
        daily.append_record(self.root, self.config, "achievement", "另一项分析",
            self.payload("sr-two", sr_id="SR-42", content=bad), now=self.now, write=True)
        errors = validator.validate(path)[0]
        self.assertTrue(any("sr-two" in e and "具体来源" in e for e in errors), errors)

    def test_concurrent_cli_writers_keep_all_entries_and_replay_is_idempotent(self):
        config_text = '\n'.join(k + ' = ' + json.dumps(v, ensure_ascii=False) for k, v in self.config.items())
        (self.root / "AGENTS.md").write_text('# 项目\n```project-supervision\n' + config_text + '\n```\n', encoding="utf-8")
        processes = []
        commands = []
        for index in range(4):
            payload = self.root / f"input-{index}.json"
            payload.write_text(json.dumps(self.payload(str(index))), encoding="utf-8")
            cmd = [sys.executable, str(SCRIPTS / "ps_01_create_governance_document.py"), "--project-root", str(self.root),
                   "--type", "log", "--summary", "并发实际任务", "--entry-file", str(payload), "--write"]
            commands.append(cmd)
            processes.append(subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE))
        completed = []
        for process in processes:
            stdout, stderr = process.communicate(timeout=15)
            completed.append((process.returncode, (stdout + stderr).decode("utf-8")))
        for returncode, output in completed:
            self.assertEqual(returncode, 0, output)
        files = list((self.root / "achieve/00-项目管理/logs").glob("*.md"))
        self.assertEqual(len(files), 1)
        self.assertEqual(len(daily.entry_blocks(files[0].read_text(encoding="utf-8"))), 4)
        replay = subprocess.run(commands[0], capture_output=True)
        self.assertEqual(replay.returncode, 0, replay.stderr)
        self.assertEqual(len(daily.entry_blocks(files[0].read_text(encoding="utf-8"))), 4)


if __name__ == "__main__":
    unittest.main()
