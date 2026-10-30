"""按实际能力建立干净项目；默认预览、拒绝覆盖，不复制维护历史。"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

VERSION = "reader-delivery/2.1.0-rc1"
READER_FILES = ["README.md", "项目技术说明.md", "使用指南.md", "结果说明与适用范围.md"]


def create(kind: str, template: Path, destination: Path, name: str, requirement: str, write: bool = False) -> Path:
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]{0,47}", name):
        raise ValueError("项目名须为字母开头的稳定名称")
    if kind not in {"research", "software"} or not requirement.strip():
        raise ValueError("请选择项目性质并填写真实初始要求")
    template, destination = template.resolve(), destination.resolve()
    if destination.exists() or destination.is_relative_to(template):
        raise ValueError("目标须不存在且不能位于模板内部")
    source = template / "projectname/project"
    registry_name = "configs/features.yaml" if kind == "research" else "config/feature-registry.yaml"
    for p in [template / "AGENTS.md", source / "AGENTS.md", source / "PROGRAMMING_STANDARDS.md", source / registry_name, source / "scripts/f001_governance_validate.py"]:
        if not p.is_file():
            raise ValueError("模板缺少必要规则或配置：" + p.name)
    source_config = json.loads((source / registry_name).read_text(encoding="utf-8-sig"))
    if source_config.get("technical_documents", {}).get("profile") != "reader":
        raise ValueError("模板不是受支持的读者交付版本；请使用推荐版本组合")
    if not source_config.get("achievement_layout", {}).get("enabled"):
        raise ValueError("模板缺少新版成果归属规则，请使用同一推荐组合")
    if not write:
        return destination
    engine = destination / name / "project"
    records = destination / name / "achieve/00-项目管理/requirements"
    records.mkdir(parents=True)
    for rel in ["AGENTS.md", "PROGRAMMING_STANDARDS.md", "scripts/f001_governance_validate.py"]:
        target = engine / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text((source / rel).read_text(encoding="utf-8-sig").replace("projectname", name), encoding="utf-8")
    (destination / "AGENTS.md").write_text((template / "AGENTS.md").read_text(encoding="utf-8-sig").replace("projectname", name), encoding="utf-8")
    config = json.loads((source / registry_name).read_text(encoding="utf-8-sig"))
    config = json.loads(json.dumps(config, ensure_ascii=False).replace("projectname", name))
    config["features"] = [{"feature_id": "F001", "feature_code": "PROJECT_RULES", "feature_name": "项目规则与文档", "owner": "项目维护者", "implementation_paths": ["../../AGENTS.md", "AGENTS.md", "PROGRAMMING_STANDARDS.md", registry_name, "scripts/f001_governance_validate.py", "docs/README.md"], "test_paths": ["tests/test_project_setup.py"], "status": "active", "validate_paths": True}]
    if kind == "software":
        config["features"][0]["implementation_paths"].remove("../../AGENTS.md")
    policy = config["record_policy"]
    policy.update(project_id=name, profile="research" if kind == "research" else "software", process_record_profile="minimal", enabled_daily_types=["requirement", "log"], legacy_paths=[], historical_views=[], historical_requirement_views=[], exports=[], current_entries={}, current_artifacts={})
    config["technical_documents"] = {"enabled": True, "profile": "reader", "delivery_state": "not_started", "root": "docs", "root_entries": READER_FILES, "stable_directories": [], "baseline_paths": [], "pinned_paths": {}}
    config["artifact_policy"] = {}
    for spec in config.get("achievement_layout", {}).get("roots", []):
        spec["baseline_paths"] = []
    source_digest = hashlib.sha256(b"".join(p.read_bytes() for p in [template / "AGENTS.md", source / registry_name, source / "scripts/f001_governance_validate.py"])).hexdigest()
    config["project_origin"] = {"standard": VERSION, "kind": kind, "capabilities": ["script"], "template_digest": source_digest}
    if "allowed_engineering_top_level" in config:
        config["allowed_engineering_top_level"] = ["docs", "scripts", "config", "data", "var", "src", "tests"]
    target = engine / registry_name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (target.parent / "skill-promotion.yaml").write_text('{"version":1,"promotions":[]}', encoding="utf-8")
    docs = engine / "docs"
    docs.mkdir()
    (docs / "README.md").write_text("# " + name + "\n\n初始目标：" + requirement + "\n\n成果尚未建立。当前不声明方法已经完成或取得结果；实际成果形成后再补充技术说明、使用指南及结果范围。\n", encoding="utf-8")
    (engine / "README.md").write_text("# 项目入口\n\n[项目说明](docs/README.md)\n", encoding="utf-8")
    (destination / "README.md").write_text("# " + name + "\n\n[项目说明](" + name + "/project/docs/README.md)\n", encoding="utf-8")
    tests = engine / "tests"
    tests.mkdir()
    root_arg = "engine" if kind == "research" else "engine.parent.parent"
    (tests / "test_project_setup.py").write_text('import subprocess\nimport sys\nfrom pathlib import Path\nimport unittest\n\nclass ProjectSetupTests(unittest.TestCase):\n    def test_initial_project_checks(self):\n        engine = Path(__file__).resolve().parents[1]\n        result = subprocess.run([sys.executable, str(engine / "scripts/f001_governance_validate.py"), "--project-root", str(' + root_arg + ')], capture_output=True)\n        self.assertEqual(result.returncode, 0, result.stdout.decode("utf-8", errors="replace"))\n', encoding="utf-8")
    now = datetime.now(timezone(timedelta(hours=8))).isoformat()
    day = now[:10]
    entry = {"entry_id": name + "-initial", "event_key": "initial-requirement", "attempt_id": "1", "recorded_at": now, "occurred_at": now, "status": "requested"}
    header = {"schema_version": "daily-record/1.0", "project_id": name, "record_date": day, "record_type": "requirement", "record_profile": policy["profile"], "timezone": "Asia/Shanghai", "writing_level": "A"}
    (records / (day.replace("-", "") + "-用户要求-需求记录.md")).write_text("---\n" + "".join(k + ": " + json.dumps(v, ensure_ascii=False) + "\n" for k, v in header.items()) + "---\n\n<!-- daily-entry " + json.dumps(entry, ensure_ascii=False) + " -->\n<a id=\"entry-" + entry["entry_id"] + "\"></a>\n## 初始要求\n\n" + requirement + "\n\n完成标准：产出可读、可用且结果有依据的实际成果；未完成部分如实说明。\n", encoding="utf-8")
    return destination


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kind", choices=["research", "software"], required=True)
    parser.add_argument("--template-root", type=Path, required=True)
    parser.add_argument("--destination", type=Path, required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--requirement", required=True)
    parser.add_argument("--capability", choices=["script"], default="script")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    try:
        target = create(args.kind, args.template_root, args.destination, args.name, args.requirement, args.write)
    except (ValueError, OSError) as error:
        parser.exit(2, "无法创建项目：" + str(error) + "\n")
    print(("已创建：" if args.write else "仅预览：") + str(target))


if __name__ == "__main__":
    main()
