"""项目日记录：规范类型、上海日期、独立条目和安全幂等追加。仅使用标准库。"""

from __future__ import annotations

import contextlib
import hashlib
import json
import os
import re
import tempfile
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

SCHEMA = "daily-record/1.0"
SHANGHAI = timezone(timedelta(hours=8), "Asia/Shanghai")
SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,79}\Z")
MARKER = re.compile(r"^<!-- daily-entry (\{.*\}) -->\s*$", re.MULTILINE)
SKIP_DIRS = {".git", ".venv", "node_modules", "__pycache__"}
# canonical: directory key, fixed body, label, level, aliases
TYPES = {
    "requirement": ("requirements_dir", "用户要求", "需求记录", "A", ["需求", "需求记录"]),
    "supervision": ("supervision_dir", "项目监督", "监督记录", "B", ["监督记录", "监督简报"]),
    "log": ("logs_dir", "项目进度", "日志", "A", ["日志", "项目日志", "科研日志"]),
    "reflection": ("reflections_dir", "问题改进", "反思", "B", ["反思", "问题反思"]),
    "change": ("changes_dir", "项目变更", "变更记录", "B", ["变更", "变更记录"]),
    "cost": ("costs_dir", "资源消耗", "成本记录", "C", ["成本记录", "成本时间统计", "统计"]),
    "quality": ("quality_dir", "质量检查", "质量记录", "C", ["质量记录", "质量检查", "质量门禁"]),
    "achievement": (None, "科研结果", "成果卡", "B", ["成果卡", "科研成果卡"]),
    "work-contract": (None, "科研工作", "工作契约", "B", ["工作契约", "工作约定"]),
    "handoff": (None, "科研交接", "交接书", "B", ["交接书", "交接记录"]),
    "decision": (None, "科研决定", "人工决定", "A", ["人工决定", "决定记录"]),
    "skill-proposal": ("skills_dir", "技能提案", "技能提案", "B", ["技能提案"]),
    "document-type": ("templates_dir", "类型登记", "文档类型登记", "B", ["文档类型登记"]),
    "placement": ("supervision_dir", "文件放置", "放置决策", "B", ["放置决策"]),
}


class RecordError(ValueError):
    """拒绝无内容、重复身份、错误路径或并发冲突。"""


def canonical_path(path: Path) -> Path:
    """并发建目录时Windows解析可能返回扩展前缀；统一表示再做边界比较。"""
    resolved = path.resolve()
    value = str(resolved)
    if os.name == "nt":
        if value.startswith("\\\\?\\UNC\\"):
            return Path("\\\\" + value[8:])
        if value.startswith("\\\\?\\"):
            return Path(value[4:])
    return resolved


def inside(root: Path, value: str) -> Path:
    """解析受控项目路径，拒绝绝对路径、驱动器、穿越和链接越界。"""
    if not isinstance(value, str) or not value or Path(value).is_absolute() or re.match(r"^[A-Za-z]:", value):
        raise RecordError("记录路径必须是非空项目相对路径")
    target = canonical_path(root / value)
    if not target.is_relative_to(canonical_path(root)):
        raise RecordError("记录路径越出项目根：" + value)
    return target


def policy_from_config(root: Path, config: dict) -> dict:
    """读取可选的既有功能注册表策略；无注册表时沿用项目目录配置。"""
    policy = {"project_id": str(config.get("project_id", root.name)),
              "profile": str(config.get("record_profile", "software")), "types": {}}
    reference = config.get("record_policy_registry")
    if reference:
        data = json.loads(inside(root, reference).read_text(encoding="utf-8-sig"))
        provided = data.get("record_policy")
        if not isinstance(provided, dict) or not provided.get("enabled", True):
            raise RecordError("注册表缺少启用的record_policy")
        policy.update(provided)
    if policy.get("timezone", "Asia/Shanghai") != "Asia/Shanghai":
        raise RecordError("日记录时区必须为Asia/Shanghai")
    if not isinstance(policy.get("types"), dict) or not isinstance(policy.get("legacy_paths", []), list):
        raise RecordError("record_policy的types/legacy_paths无效")
    if not str(policy.get("project_id", "")).strip():
        raise RecordError("日记录缺少project_id")
    for relative in policy.get("legacy_paths", []):
        if not isinstance(relative, str) or not inside(root, relative).is_file():
            raise RecordError("legacy_paths只能登记精确存在的历史文件，不能豁免目录")
    return policy


def canonical_type(value: str, policy: dict) -> str:
    matches = []
    for name, definition in TYPES.items():
        custom = policy.get("types", {}).get(name, {})
        aliases = [name, *definition[4], *custom.get("aliases", [])]
        if value in aliases:
            matches.append(name)
    if len(matches) != 1:
        raise RecordError("未知或冲突的记录类型：" + value)
    return matches[0]


def record_target(root: Path, config: dict, policy: dict, kind: str, now: datetime) -> Path:
    if now.tzinfo is None:
        raise RecordError("记录时间必须包含时区")
    directory_key, body, label, _, _ = TYPES[kind]
    custom = policy.get("types", {}).get(kind, {})
    if custom.get("directory"):
        directory = inside(root, custom["directory"])
    else:
        management = inside(root, str(config.get("project_management_root", "")))
        if directory_key:
            directory = inside(management, str(config.get(directory_key, "")))
        elif policy["profile"] == "research":
            directory = inside(root, str(config.get("research_records_root",
                (management.parent / "08-项目推进与下一步计划").relative_to(root).as_posix())))
        else:
            raise RecordError("软件项目须显式配置该记录类型目录：" + kind)
    body = custom.get("filename_body", "科研进度" if kind == "log" and policy["profile"] == "research" else body)
    label = custom.get("label", label)
    if any(not isinstance(v, str) or not v or re.search(r"[\\/:*?\"<>|\r\n]", v) for v in [body, label]):
        raise RecordError("日记录固定文件名主体无效")
    filename = now.astimezone(SHANGHAI).strftime("%Y%m%d") + f"-{body}-{label}.md"
    return inside(root, (directory / filename).relative_to(root).as_posix())


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}
    fields = {}
    for line in match[1].splitlines():
        key, sep, value = line.partition(":")
        if sep:
            value = value.strip()
            try:
                fields[key.strip()] = json.loads(value)
            except json.JSONDecodeError:
                fields[key.strip()] = value.strip("\"'")
    return fields


def entry_blocks(text: str) -> list[tuple[dict, str]]:
    """按机器边界逐条解析，禁止让后一个条目补齐前一个缺项。"""
    matches = list(MARKER.finditer(text))
    result = []
    for index, match in enumerate(matches):
        try:
            metadata = json.loads(match.group(1))
        except json.JSONDecodeError as exc:
            raise RecordError("条目JSON无效") from exc
        if not isinstance(metadata, dict):
            raise RecordError("条目元数据必须为对象")
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        result.append((metadata, text[match.end():end].strip()))
    return result


def validate_daily(text: str) -> list[str]:
    """仅检验日文件结构和每条真实内容，不作科学正确性裁决。"""
    errors = []
    fields = frontmatter(text)
    for key in ["project_id", "record_date", "record_type", "timezone"]:
        if not fields.get(key):
            errors.append("日文件缺少" + key)
    if fields.get("schema_version") != SCHEMA or fields.get("timezone") != "Asia/Shanghai":
        errors.append("日记录schema/时区无效")
    try:
        kind = canonical_type(str(fields.get("record_type", "")), {})
    except RecordError:
        kind = ""
        errors.append("日记录类型无效")
    if fields.get("record_profile") not in {"software", "research"}:
        errors.append("日记录项目用途无效")
    try:
        datetime.strptime(str(fields.get("record_date")), "%Y-%m-%d")
    except ValueError:
        errors.append("记录日期无效")
    try:
        blocks = entry_blocks(text)
    except RecordError as exc:
        return errors + [str(exc)]
    if not blocks:
        errors.append("日文件没有真实条目")
    if text.count("<!-- daily-entry ") != len(blocks):
        errors.append("条目边界不完整或JSON格式损坏")
    ids, events = set(), set()
    for item, body in blocks:
        identifier = str(item.get("entry_id", ""))
        event = (str(item.get("event_key", "")), str(item.get("attempt_id", "1")))
        prefix = identifier or "无ID条目"
        if not SAFE_ID.fullmatch(identifier) or identifier in ids:
            errors.append(prefix + "：条目ID无效或重复")
        if not event[0] or event in events:
            errors.append(prefix + "：事件身份缺失或重复")
        ids.add(identifier)
        events.add(event)
        if f'<a id="entry-{identifier}"></a>' not in body:
            errors.append(prefix + "：缺少独立锚点")
        if len(body.replace(f'<a id="entry-{identifier}"></a>', "").strip()) < 20:
            errors.append(prefix + "：条目正文为空")
        for key in ["recorded_at", "occurred_at", "status"]:
            if not item.get(key):
                errors.append(prefix + "：缺少" + key)
        for key in ["recorded_at", "occurred_at"]:
            try:
                stamp = datetime.fromisoformat(str(item.get(key, "")))
                if stamp.tzinfo is None:
                    raise ValueError()
                if key == "recorded_at" and stamp.astimezone(SHANGHAI).date().isoformat() != fields.get("record_date"):
                    errors.append(prefix + "：记录日与时间不一致")
            except ValueError:
                errors.append(prefix + "：时间缺少有效时区")
        if kind == "log":
            if fields.get("record_profile") == "research":
                if not item.get("research_point") or not item.get("research_source"):
                    errors.append(prefix + "：科研日志缺研究要点及出处")
            elif not item.get("requirement_id"):
                errors.append(prefix + "：项目日志缺需求/任务对应")
        if kind == "achievement" and not item.get("sr_id"):
            errors.append(prefix + "：科研结果缺SR身份")
    return errors


def find_daily(root: Path, policy: dict, kind: str | None, day: str | None) -> list[Path]:
    found = []
    legacy = set(policy.get("legacy_paths", []))
    for base, dirs, names in os.walk(root, followlinks=False):
        dirs[:] = [n for n in dirs if n not in SKIP_DIRS and not (Path(base) / n).is_symlink()]
        for name in names:
            path = Path(base) / name
            if path.is_symlink() or name == ".daily-records.lock" or (name.startswith(".daily-") and name.endswith(".tmp")):
                continue
            # 只读取头部；大型专题正文不必整体加载。
            with path.open(encoding="utf-8-sig", errors="replace") as stream:
                header = stream.read(4096)
            fields = frontmatter(header)
            if fields.get("schema_version") != SCHEMA:
                continue
            if fields.get("project_id") != policy["project_id"]:
                continue
            relative = path.relative_to(root).as_posix()
            if relative in legacy:
                continue
            if fields.get("record_state") == "archived":
                raise RecordError("归档日文件未登记精确legacy路径：" + relative)
            if fields.get("derived_from"):
                reference = str(fields["derived_from"]).split("#", 1)[0]
                source = inside(root, reference)
                if source == path.resolve() or not source.is_file():
                    raise RecordError("只读导出没有有效母版：" + relative)
                with source.open(encoding="utf-8-sig", errors="replace") as stream:
                    source_text = stream.read()
                    parent = frontmatter(source_text)
                if (parent.get("schema_version") != SCHEMA or parent.get("derived_from")
                    or validate_daily(source_text)
                    or parent.get("record_profile") != policy["profile"]
                    or any(parent.get(k) != fields.get(k) for k in ["project_id", "record_date", "record_type", "record_profile", "timezone"])):
                    raise RecordError("导出文件与母版身份不符：" + relative)
                continue
            try:
                normalized = canonical_type(str(fields.get("record_type", "")), policy)
            except RecordError as exc:
                raise RecordError("日文件记录类型不合法：" + relative) from exc
            if (day is None or fields.get("record_date") == day) and (kind is None or normalized == kind):
                found.append(path.resolve())
    return found


@contextlib.contextmanager
def writer_lock(root: Path, config: dict, timeout: float = 5):
    """操作系统锁随进程退出释放；稳定锁文件不能unlink造成双写窗口。"""
    directory = inside(root, str(config["project_management_root"]))
    directory.mkdir(parents=True, exist_ok=True)
    path = inside(root, (directory / ".daily-records.lock").relative_to(root).as_posix())
    with path.open("a+b") as stream:
        if path.stat().st_size == 0:
            stream.write(b"0")
            stream.flush()
        started = time.monotonic()
        while True:
            try:
                stream.seek(0)
                if os.name == "nt":
                    import msvcrt
                    msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except OSError:
                if time.monotonic() - started >= timeout:
                    raise RecordError("日记录写入者忙；重试前重新读取，不能另开文件")
                time.sleep(0.05)
        try:
            yield
        finally:
            stream.seek(0)
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl
                fcntl.flock(stream.fileno(), fcntl.LOCK_UN)


def prepare_entry(summary: str, payload: dict, now: datetime) -> tuple[dict, str]:
    for key in ["entry_id", "event_key", "content", "impact", "status"]:
        if not isinstance(payload.get(key), str) or not payload[key].strip():
            raise RecordError("条目必须提供真实的" + key)
    if not SAFE_ID.fullmatch(payload["entry_id"]):
        raise RecordError("entry_id只允许字母数字、点、下划线、连字符")
    if not summary.strip() or any(x in summary for x in ["\n", "\r", "<!--", "-->"]):
        raise RecordError("条目标题为空或含边界字符")
    for key in ["background", "content", "impact"]:
        value = payload.get(key, "未单独记录背景。")
        if not isinstance(value, str) or "<!-- daily-entry" in value or re.search(r'<a\s+id=[\"\']entry-', value):
            raise RecordError("条目正文不能注入日记录边界")
    metadata = {key: payload[key] for key in ["entry_id", "event_key", "status", "sr_id", "agent", "workflow", "workflow_id",
        "requirement_id", "research_point", "research_source", "revision_of", "cards_read", "handoffs_read",
        "human_verdict", "scientific_accepted"] if key in payload}
    metadata["attempt_id"] = str(payload.get("attempt_id", "1"))
    metadata["recorded_at"] = now.astimezone(SHANGHAI).isoformat()
    metadata["occurred_at"] = str(payload.get("occurred_at", metadata["recorded_at"]))
    # 记录生成时刻不参与内容身份；同一事件再次提交可以真正幂等。
    encoded = json.dumps({"summary": summary, "payload": payload}, ensure_ascii=False, sort_keys=True)
    metadata["content_sha256"] = hashlib.sha256(encoded.encode()).hexdigest()
    body = f'<a id="entry-{payload["entry_id"]}"></a>\n## {summary}\n\n'
    body += '### 1. 背景一句话\n\n' + payload.get("background", "未单独记录背景。") + '\n\n'
    body += '### 2. 研究内容\n\n' + payload["content"] + '\n\n'
    body += '### 3. 研究影响\n\n' + payload["impact"] + '\n\n'
    body += '### 附录：管理信息\n\n'
    evidence = payload.get("evidence", [])
    if not isinstance(evidence, list) or not all(isinstance(x, str) for x in evidence):
        raise RecordError("evidence必须是来源路径列表")
    if any("<!-- daily-entry" in x or '<a id="entry-' in x for x in evidence):
        raise RecordError("证据不能注入日记录边界")
    body += '\n'.join('- ' + x for x in evidence) + '\n'
    return metadata, body


def append_record(root: Path, config: dict, kind: str, summary: str, payload: dict, *,
                  write: bool = False, now: datetime | None = None) -> tuple[Path, bool]:
    now = now or datetime.now(SHANGHAI)
    policy = policy_from_config(root, config)
    kind = canonical_type(kind, policy)
    target = record_target(root, config, policy, kind, now)
    day = now.astimezone(SHANGHAI).date().isoformat()
    metadata, body = prepare_entry(summary, payload, now)
    header = {"schema_version": SCHEMA, "project_id": policy["project_id"], "record_date": day,
              "record_type": kind, "record_profile": policy["profile"], "timezone": "Asia/Shanghai",
              "writing_level": TYPES[kind][3]}

    def prior_event() -> Path | None:
        for path in find_daily(root, policy, None, None):
            content = path.read_text(encoding="utf-8")
            fields = frontmatter(content)
            previous_kind = canonical_type(str(fields.get("record_type", "")), policy)
            if (validate_daily(content) or fields.get("record_profile") != policy["profile"]
                or fields.get("timezone") != "Asia/Shanghai"):
                raise RecordError("项目中已有损坏或策略身份不符的日记录，不能幂等返回：" + path.relative_to(root).as_posix())
            stamp = datetime.fromisoformat(str(fields["record_date"])).replace(tzinfo=SHANGHAI)
            if record_target(root, config, policy, previous_kind, stamp) != path:
                raise RecordError("项目已有日记录不在规范落点，不能另开母版")
            for previous, _ in entry_blocks(content):
                event = (previous.get("event_key"), str(previous.get("attempt_id", "1")))
                current_event = (metadata["event_key"], metadata["attempt_id"])
                if event == current_event:
                    if previous_kind == kind and previous.get("content_sha256") == metadata["content_sha256"]:
                        return path
                    raise RecordError("同一事件已在项目中记录但内容不同；请使用明确修订/真实新尝试")
                if previous.get("entry_id") == metadata["entry_id"]:
                    raise RecordError("条目ID已在项目其它日文件使用")
        return None

    def proposed() -> tuple[str, str | None, bool]:
        found = find_daily(root, policy, kind, day)
        if any(p != target for p in found):
            raise RecordError("同日同类型已有其它目录/名称母版，须先处理冲突")
        old = target.read_text(encoding="utf-8") if target.exists() else None
        if target.is_symlink():
            raise RecordError("拒绝把链接作为日记录写入目标")
        if old is None:
            text = '---\n' + ''.join(k + ': ' + json.dumps(v, ensure_ascii=False) + '\n' for k, v in header.items()) + '---\n\n# ' + day + ' ' + TYPES[kind][2] + '\n\n'
        else:
            if any(frontmatter(old).get(k) != v for k, v in header.items()):
                raise RecordError("目标元数据不匹配，不能覆盖旧记录或另一类型")
            if validate_daily(old):
                raise RecordError("原日文件结构损坏，拒绝追加")
            for previous, _ in entry_blocks(old):
                same_event = (previous.get("event_key"), previous.get("attempt_id", "1")) == (metadata["event_key"], metadata["attempt_id"])
                if same_event and previous.get("content_sha256") == metadata["content_sha256"]:
                    return old, old, False
                if same_event or previous.get("entry_id") == metadata["entry_id"]:
                    raise RecordError("事件或条目ID已存在但内容不同；请追加带revision_of的新修订条目")
            text = old.rstrip() + '\n\n'
        revision = metadata.get("revision_of")
        if revision:
            if not isinstance(revision, str):
                raise RecordError("revision_of必须是条目ID或项目相对文件#entry-ID")
            if "#" in revision:
                reference, anchor = revision.rsplit("#", 1)
                source = inside(root, reference)
                previous_ids = {p.get("entry_id") for p, _ in entry_blocks(source.read_text(encoding="utf-8"))}
                if anchor.removeprefix("entry-") not in previous_ids:
                    raise RecordError("修订来源锚点不存在")
            elif not old or revision not in {p["entry_id"] for p, _ in entry_blocks(old)}:
                raise RecordError("revision_of未指向已有条目；跨日修订须给出文件#锚点")
        for field in ["cards_read", "handoffs_read"]:
            references = metadata.get(field, [])
            if not isinstance(references, list) or not all(isinstance(x, str) for x in references):
                raise RecordError(field + "必须是项目相对文件/锚点列表")
            for reference in references:
                relative, sep, anchor = reference.partition("#")
                source = inside(root, relative)
                if not source.is_file():
                    raise RecordError(field + "引用文件不存在")
                if sep and not re.search(r'id=[\"\']' + re.escape(anchor) + r'[\"\']', source.read_text(encoding="utf-8")):
                    raise RecordError(field + "引用条目锚点不存在")
        text += '<!-- daily-entry ' + json.dumps(metadata, ensure_ascii=False, sort_keys=True) + ' -->\n' + body + '\n'
        errors = validate_daily(text)
        if errors:
            raise RecordError('；'.join(errors))
        return text, old, True

    if not write:
        existing = prior_event()
        if existing:
            return existing, False
        _, _, changed = proposed()
        return target, changed
    with writer_lock(root, config):
        # 锁内重新定位并读取；不能用预览时的旧文本覆盖另一个写入者。
        target = record_target(root, config, policy, kind, now)
        existing = prior_event()
        if existing:
            return existing, False
        text, old, changed = proposed()
        if not changed:
            return target, False
        target.parent.mkdir(parents=True, exist_ok=True)
        descriptor, temporary = tempfile.mkstemp(prefix='.daily-', suffix='.tmp', dir=target.parent)
        try:
            with os.fdopen(descriptor, 'w', encoding='utf-8', newline='\n') as stream:
                stream.write(text)
                stream.flush()
                os.fsync(stream.fileno())
            current = target.read_text(encoding='utf-8') if target.exists() else None
            if current != old:
                raise RecordError("文件被其它写入者修改，拒绝覆盖；请重读后追加")
            os.replace(temporary, target)
        finally:
            Path(temporary).unlink(missing_ok=True)
    return target, True
