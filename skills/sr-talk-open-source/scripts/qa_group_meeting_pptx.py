#!/usr/bin/env python3
"""QA the SR-58 academic/group-meeting PPTX contract.

Reads Office XML directly and has no third-party Python dependency. When a page
plan is supplied, it also checks cognitive-object splitting, layout metadata,
structured kickers, planned summary sentences, and density exceptions. The
script cannot inspect text rasterized inside PNG/JPEG figures or judge
scientific correctness; rendered-slide inspection remains required.

Exit codes:
  0 = pass, or warnings without --strict
  1 = warnings with --strict
  2 = unreadable package, invalid page plan, or blocking style errors
"""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from dataclasses import dataclass
from pathlib import Path


A = "http://schemas.openxmlformats.org/drawingml/2006/main"
P = "http://schemas.openxmlformats.org/presentationml/2006/main"
NS = {"a": A, "p": P}
FONT_RE = re.compile(r"^(microsoft yahei|微软雅黑)$", re.IGNORECASE)
RED_RGB = {"FF0000", "C00000", "D93025", "B71C1C"}
BLUE_RGB = {"0000FF", "0070C0", "1F4E79", "0F4D92", "003399"}
COGNITIVE_TYPES = {
    "claim", "context", "artifact", "mechanism", "role", "process",
    "architecture", "case", "metric", "risk", "reflection", "decision", "backup",
}
LAYOUT_PATTERNS = {
    "claim", "evidence-screenshot", "mechanism-map", "process-flow",
    "architecture", "case", "reflection",
}
PENDING_RE = re.compile(r"(待验证|待定|待补充|尚未确认|不做汇报|未验证)")


@dataclass
class Run:
    slide: int
    context: str
    text: str
    size_pt: float | None
    bold: bool
    underline: bool
    color: str | None
    latin_font: str | None = None
    ea_font: str | None = None


@dataclass
class Page:
    no: int
    runs: list[Run]
    summaries: list[str]
    title_texts: list[str]
    image_count: int
    drawing_count: int

    @property
    def chars(self) -> int:
        return sum(len(run.text.strip()) for run in self.runs)

    @property
    def all_text(self) -> str:
        return " ".join(run.text.strip() for run in self.runs if run.text.strip())


def truthy(value: str | None) -> bool:
    return str(value).lower() in {"1", "true", "yes"}


def falsy(value: str | None) -> bool:
    return str(value).lower() in {"0", "false", "no"}


def clean_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1].strip()
    return value


def color_kind(rpr: ET.Element) -> str | None:
    rgb = rpr.find("a:solidFill/a:srgbClr", NS)
    if rgb is not None and rgb.get("val"):
        value = rgb.get("val", "").upper()
        if len(value) != 6:
            return None
        red, green, blue = (int(value[i : i + 2], 16) for i in (0, 2, 4))
        if value in RED_RGB or (red >= 170 and green <= 80 and blue <= 80):
            return "red"
        if value in BLUE_RGB or (blue >= 130 and red <= 80 and green <= 110):
            return "blue"
        if red + green + blue <= 240:
            return "black"
        return f"#{value}"
    scheme = rpr.find("a:solidFill/a:schemeClr", NS)
    if scheme is not None and scheme.get("val") in {"tx1", "dk1", "black"}:
        return "black"
    return None


def shape_name(sp: ET.Element) -> str:
    node = sp.find("p:nvSpPr/p:cNvPr", NS)
    return node.get("name", "").strip() if node is not None else ""


def context_of(sp: ET.Element) -> str:
    if shape_name(sp).upper() == "SR58-SUMMARY":
        return "summary"
    ph = sp.find("p:nvSpPr/p:nvPr/p:ph", NS)
    return "title" if ph is not None and ph.get("type") in {"title", "ctrTitle"} else "body"


def shape_text(sp: ET.Element) -> str:
    parts: list[str] = []
    for paragraph in sp.findall(".//a:p", NS):
        paragraph_text = "".join(
            "".join(run.find("a:t", NS).itertext())
            for run in paragraph.findall("a:r", NS)
            if run.find("a:t", NS) is not None
        )
        if paragraph_text.strip():
            parts.append(paragraph_text.strip())
    return " ".join(parts).strip()


def make_run(slide: int, context: str, text: str, rpr: ET.Element | None) -> Run:
    if rpr is None:
        return Run(slide, context, text, None, False, False, None)
    size = float(rpr.get("sz")) / 100 if rpr.get("sz") else None
    latin_node = rpr.find("a:latin", NS)
    ea_node = rpr.find("a:ea", NS)
    return Run(
        slide,
        context,
        text,
        size,
        truthy(rpr.get("b")),
        rpr.get("u", "").lower() in {"sng", "dbl"},
        color_kind(rpr),
        latin_node.get("typeface") if latin_node is not None else None,
        ea_node.get("typeface") if ea_node is not None else None,
    )


def parse_page(path: ET.Element, no: int) -> Page:
    runs: list[Run] = []
    summaries: list[str] = []
    titles: list[str] = []
    for sp in page_shapes(path):
        context = context_of(sp)
        text = shape_text(sp)
        if context == "summary" and text:
            summaries.append(text)
        if context == "title" and text:
            titles.append(text)
        for run in sp.findall(".//a:p/a:r", NS):
            text_node = run.find("a:t", NS)
            run_text = "".join(text_node.itertext()) if text_node is not None else ""
            if run_text.strip():
                runs.append(make_run(no, context, run_text, run.find("a:rPr", NS)))

    for frame in path.findall(".//p:cSld/p:spTree//p:graphicFrame", NS):
        if frame.find(".//a:tbl", NS) is None:
            continue
        for run in frame.findall(".//a:r", NS):
            text_node = run.find("a:t", NS)
            run_text = "".join(text_node.itertext()) if text_node is not None else ""
            if run_text.strip():
                runs.append(make_run(no, "table", run_text, run.find("a:rPr", NS)))

    return Page(
        no=no,
        runs=runs,
        summaries=summaries,
        title_texts=titles,
        image_count=len(path.findall(".//p:pic", NS)),
        drawing_count=0,
    )


def page_shapes(root: ET.Element) -> list[ET.Element]:
    return root.findall(".//p:cSld/p:spTree//p:sp", NS)


def parse_page_plan(path: Path) -> dict[int, dict[str, str]]:
    plans: dict[int, dict[str, str]] = {}
    current: dict[str, str] | None = None
    tracked = {
        "no", "kicker", "title", "cognitive_type", "layout_pattern",
        "summary_sentence", "summary_style", "one_cognitive_object",
        "needs_two_summaries", "split_recommended", "density_exception_reason",
    }
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        heading = re.match(r"^##\s+Slide\s+(\d+)", line, re.IGNORECASE)
        if heading:
            number = int(heading.group(1))
            current = {"no": str(number)}
            plans[number] = current
            continue
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if not match:
            continue
        key, value = match.groups()
        if key == "no":
            try:
                number = int(clean_scalar(value))
            except ValueError as exc:
                raise ValueError(f"page plan has invalid slide no: {value}") from exc
            current = {"no": str(number)}
            plans[number] = current
            continue
        if current is not None and key in tracked and clean_scalar(value):
            current[key] = clean_scalar(value)
    return plans


def check_theme(package: zipfile.ZipFile, warnings: list[str]) -> None:
    theme_names = sorted(
        name for name in package.namelist() if re.fullmatch(r"ppt/theme/theme\d+\.xml", name)
    )
    if not theme_names:
        warnings.append("no PPTX theme found; inherited fonts could not be checked")
        return
    for name in theme_names:
        root = ET.fromstring(package.read(name))
        for scheme in root.findall(".//a:fontScheme", NS):
            for kind in ("a:majorFont", "a:minorFont"):
                node = scheme.find(kind, NS)
                if node is None:
                    continue
                for tag in ("a:latin", "a:ea"):
                    font = node.find(tag, NS)
                    typeface = font.get("typeface", "") if font is not None else ""
                    if typeface and not (
                        FONT_RE.fullmatch(typeface)
                        or typeface.startswith("+mn")
                        or typeface.startswith("+mj")
                    ):
                        warnings.append(
                            f"{name}: theme {kind}/{tag} uses '{typeface}'; set Microsoft YaHei explicitly on visible runs"
                        )


def normalized_text(value: str) -> str:
    value = re.sub(r"\s+", "", value)
    return value.replace("：", ":").replace("；", ";").replace("，", ",").replace("。", ".").lower()


def qa(
    path: Path, page_plan_path: Path | None
) -> tuple[list[str], list[str], int, int, int, int, int]:
    errors: list[str] = []
    warnings: list[str] = []
    plans = parse_page_plan(page_plan_path) if page_plan_path else {}
    if page_plan_path and not plans:
        errors.append("page plan contains no slide records")
    if not page_plan_path:
        warnings.append("no page plan supplied; cognitive-object/layout metadata was not checked")

    with zipfile.ZipFile(path) as package:
        slide_names = sorted(
            (
                name
                for name in package.namelist()
                if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)
            ),
            key=lambda name: int(re.search(r"(\d+)", name).group(1)),
        )
        if not slide_names:
            errors.append("PPTX contains no ppt/slides/slideN.xml")
            return errors, warnings, 0, 0, 0, 0, 0

        check_theme(package, warnings)
        pages: list[Page] = []
        for name in slide_names:
            no = int(re.search(r"(\d+)", name).group(1))
            root = ET.fromstring(package.read(name))
            pages.append(parse_page(root, no))

        title_counts: dict[str, list[int]] = {}
        previous_watch = False
        for page in pages:
            no = page.no
            if len(page.summaries) != 1:
                errors.append(
                    f"slide {no}: requires exactly one visible SR58-SUMMARY text shape; found {len(page.summaries)}"
                )
            for summary in page.summaries:
                compact = " ".join(summary.split())
                if len(compact) > 80:
                    errors.append(
                        f"slide {no}: summary has {len(compact)} chars; split the page at the 80-char limit"
                    )
                if not re.search(r"[.。!！?？]$", compact):
                    errors.append(
                        f"slide {no}: summary is not one complete sentence: '{compact[:50]}'"
                    )

            red_count = sum(run.color == "red" for run in page.runs)
            if red_count > 3:
                errors.append(f"slide {no}: {red_count} red runs exceed the limit of 3")
            if not page.title_texts:
                warnings.append(f"slide {no}: no nonempty title placeholder text detected")
            for title in page.title_texts:
                title_counts.setdefault(normalized_text(title), []).append(no)

            plan = plans.get(no)
            if page_plan_path:
                if plan is None:
                    errors.append(f"slide {no}: page plan record is missing")
                else:
                    if not plan.get("kicker"):
                        errors.append(f"slide {no}: page plan kicker is missing")
                    cognitive = plan.get("cognitive_type", "")
                    if not cognitive:
                        errors.append(f"slide {no}: page plan cognitive_type is missing")
                    elif cognitive not in COGNITIVE_TYPES:
                        errors.append(
                            f"slide {no}: invalid cognitive_type '{cognitive}'; choose one primary object"
                        )
                    layout = plan.get("layout_pattern", "")
                    if not layout:
                        errors.append(f"slide {no}: page plan layout_pattern is missing")
                    elif layout not in LAYOUT_PATTERNS:
                        errors.append(f"slide {no}: invalid layout_pattern '{layout}'")
                    if falsy(plan.get("one_cognitive_object", "")):
                        errors.append(f"slide {no}: page plan admits multiple cognitive objects; split the page")
                    if truthy(plan.get("needs_two_summaries", "")):
                        errors.append(f"slide {no}: page needs two summaries; split the page")
                    if truthy(plan.get("split_recommended", "")):
                        errors.append(f"slide {no}: split_recommended is true; split before delivery")
                    planned_summary = plan.get("summary_sentence", "")
                    if planned_summary and page.summaries and normalized_text(planned_summary) not in {
                        normalized_text(item) for item in page.summaries
                    }:
                        errors.append(f"slide {no}: SR58-SUMMARY does not match the page plan sentence")

            density_exception = bool(plan and plan.get("density_exception_reason"))
            if page.chars > 320:
                message = f"slide {no}: {page.chars} visible characters exceed the 320 cognitive-density limit; split the page"
                if density_exception:
                    warnings.append(message + " (exception recorded)")
                else:
                    errors.append(message)
            elif page.chars >= 220:
                warnings.append(
                    f"slide {no}: {page.chars} visible characters are in the 220-320 watch band; review splitting/layout"
                )
            if page.chars >= 220 and previous_watch and not density_exception:
                errors.append(f"slide {no}: consecutive watch/blocked density pages require a split or layout change")
            previous_watch = page.chars >= 220

            cognitive = plan.get("cognitive_type", "") if plan else ""
            pending = PENDING_RE.search(page.all_text)
            if pending:
                message = f"slide {no}: unverified/pending language '{pending.group(0)}' should move to backup or next-plan context"
                if page_plan_path and cognitive not in {"backup", "decision", "risk"}:
                    errors.append(message)
                elif not page_plan_path:
                    warnings.append(message)

            for run in page.runs:
                prefix = f"slide {no}: '{run.text[:40]}'"
                if run.color == "red" and not (run.bold and run.underline):
                    errors.append(f"{prefix} red text must be bold and underlined")
                if run.color == "blue" and not run.bold:
                    errors.append(f"{prefix} blue text must be bold")
                if run.context == "title" and not run.bold:
                    errors.append(f"{prefix} title text must be bold")
                if run.context == "summary":
                    if not run.bold:
                        errors.append(f"{prefix} summary text must be bold")
                    if not (
                        (run.color == "blue")
                        or (run.color == "red" and run.underline)
                    ):
                        errors.append(
                            f"{prefix} summary style must be blue+bold or red+bold+underline"
                        )
                    if run.size_pt is not None and run.size_pt < 18:
                        errors.append(f"{prefix} summary size is below the 18pt hard minimum")
                    elif run.size_pt is not None and run.size_pt < 20:
                        warnings.append(
                            f"{prefix} summary is {run.size_pt:g}pt; the reference standard prefers 20-22pt"
                        )
                if run.size_pt is None:
                    warnings.append(f"{prefix} has inherited size; set an explicit pt value")
                elif run.size_pt < 14:
                    errors.append(f"{prefix} is {run.size_pt:g}pt, below the 14pt minimum")
                elif run.size_pt < 18 and run.context not in {"table"}:
                    warnings.append(
                        f"{prefix} is {run.size_pt:g}pt non-table text, below the 18pt body target"
                    )
                explicit_fonts = [font for font in (run.latin_font, run.ea_font) if font]
                if len(explicit_fonts) < 2:
                    warnings.append(
                        f"{prefix} has incomplete explicit Latin/East-Asian font; set both to Microsoft YaHei"
                    )
                bad = sorted(
                    font
                    for font in explicit_fonts
                    if not (
                        FONT_RE.fullmatch(font)
                        or font.startswith("+mn")
                        or font.startswith("+mj")
                    )
                )
                if bad:
                    errors.append(
                        f"{prefix} uses non-Microsoft-YaHei font {', '.join(sorted(set(bad)))}"
                    )
                if run.color is None:
                    warnings.append(
                        f"{prefix} has inherited color; set explicit black/blue/red for semantic QA"
                    )
                elif run.color not in {"red", "blue", "black"}:
                    errors.append(
                        f"{prefix} uses non-semantic color {run.color}; use only red/blue/black"
                    )

        for title, numbers in title_counts.items():
            if len(numbers) > 1:
                warnings.append(
                    "generic/repeated title detected across slides "
                    + ", ".join(map(str, numbers))
                    + f": '{title[:40]}'"
                )

        if plans:
            missing = sorted(set(plans) - {page.no for page in pages})
            if missing:
                errors.append("page plan has records without slides: " + ", ".join(map(str, missing)))

        all_runs = [run for page in pages for run in page.runs]
        red_total = sum(run.color == "red" for run in all_runs)
        summary_total = sum(len(page.summaries) for page in pages)

    return (
        errors,
        warnings,
        len(pages),
        len(all_runs),
        red_total,
        summary_total,
        len(plans),
    )


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--page-plan", type=Path, help="SR-58 Markdown page plan with per-slide metadata")
    parser.add_argument("--strict", action="store_true", help="treat warnings as blocking")
    args = parser.parse_args()
    if not args.pptx.is_file():
        print(f"ERROR input PPTX does not exist: {args.pptx}")
        return 2
    if args.page_plan is not None and not args.page_plan.is_file():
        print(f"ERROR page plan does not exist: {args.page_plan}")
        return 2
    try:
        result = qa(args.pptx, args.page_plan)
    except (OSError, zipfile.BadZipFile, ET.ParseError, ValueError) as exc:
        print(f"ERROR cannot inspect PPTX/page plan: {exc}")
        return 2

    errors, warnings, slide_count, run_count, red_total, summary_count, plan_count = result
    print(f"pptx={args.pptx}")
    print(
        f"slides={slide_count} text_runs={run_count} summary_shapes={summary_count} "
        f"page_plan_records={plan_count} red_runs_total={red_total}"
    )
    print(f"errors={len(errors)} warnings={len(warnings)}")
    for item in errors:
        print(f"ERROR {item}")
    for item in warnings:
        print(f"WARN {item}")
    if errors:
        return 2
    if warnings:
        print("QA=warnings")
        return 1 if args.strict else 0
    print("QA=pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
