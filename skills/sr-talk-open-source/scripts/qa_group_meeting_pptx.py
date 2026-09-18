#!/usr/bin/env python3
"""QA the fixed typography/color contract for SR-58 academic/group-meeting PPTX files.

Reads Office XML directly and has no third-party Python dependency. It cannot
inspect text rasterized inside PNG/JPEG figures or judge scientific correctness;
rendered-slide inspection remains required.

Exit codes:
  0 = pass, or warnings without --strict
  1 = warnings with --strict
  2 = unreadable package or blocking style errors
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
BLUE_RGB = {"0000FF", "0070C0", "1F4E79", "0F4D92"}


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


def truthy(value: str | None) -> bool:
    return str(value).lower() in {"1", "true"}


def color_kind(rpr: ET.Element) -> str | None:
    rgb = rpr.find("a:solidFill/a:srgbClr", NS)
    if rgb is not None and rgb.get("val"):
        value = rgb.get("val", "").upper()
        if len(value) != 6:
            return None
        red, green, blue = (int(value[i : i + 2], 16) for i in (0, 2, 4))
        if value in RED_RGB or (red >= 170 and green <= 80 and blue <= 80):
            return "red"
        if value in BLUE_RGB or (blue >= 150 and red <= 80 and green <= 110):
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
    return (node.get("name", "").strip() if node is not None else "")


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


def collect_runs(root: ET.Element, slide: int) -> list[Run]:
    runs: list[Run] = []
    for sp in root.findall(".//p:cSld/p:spTree//p:sp", NS):
        context = context_of(sp)
        for run in sp.findall(".//a:p/a:r", NS):
            text_node = run.find("a:t", NS)
            text = "".join(text_node.itertext()) if text_node is not None else ""
            if text.strip():
                runs.append(make_run(slide, context, text, run.find("a:rPr", NS)))

    for frame in root.findall(".//p:cSld/p:spTree//p:graphicFrame", NS):
        if frame.find(".//a:tbl", NS) is None:
            continue
        for run in frame.findall(".//a:r", NS):
            text_node = run.find("a:t", NS)
            text = "".join(text_node.itertext()) if text_node is not None else ""
            if text.strip():
                runs.append(make_run(slide, "table", text, run.find("a:rPr", NS)))
    return runs


def check_theme(package: zipfile.ZipFile, warnings: list[str]) -> None:
    theme_names = sorted(name for name in package.namelist() if re.fullmatch(r"ppt/theme/theme\d+\.xml", name))
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
                    if typeface and not (FONT_RE.fullmatch(typeface) or typeface.startswith("+mn") or typeface.startswith("+mj")):
                        warnings.append(
                            f"{name}: theme {kind}/{tag} uses '{typeface}'; set Microsoft YaHei explicitly on all visible runs"
                        )


def summary_shapes(root: ET.Element) -> list[str]:
    return [
        text
        for sp in root.findall(".//p:cSld/p:spTree//p:sp", NS)
        if shape_name(sp).upper() == "SR58-SUMMARY"
        for text in [shape_text(sp)]
        if text
    ]


def qa(path: Path) -> tuple[list[str], list[str], int, int, int, int]:
    errors: list[str] = []
    warnings: list[str] = []
    with zipfile.ZipFile(path) as package:
        slide_names = sorted(
            (name for name in package.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)),
            key=lambda name: int(re.search(r"(\d+)", name).group(1)),
        )
        if not slide_names:
            errors.append("PPTX contains no ppt/slides/slideN.xml")
            return errors, warnings, 0, 0, 0, 0
        check_theme(package, warnings)
        all_runs: list[Run] = []
        summary_shapes_total = 0
        for name in slide_names:
            no = int(re.search(r"(\d+)", name).group(1))
            root = ET.fromstring(package.read(name))
            runs = collect_runs(root, no)
            all_runs.extend(runs)
            summaries = summary_shapes(root)
            summary_shapes_total += len(summaries)
            if len(summaries) != 1:
                errors.append(f"slide {no}: requires exactly one visible SR58-SUMMARY text shape; found {len(summaries)}")
            for summary in summaries:
                compact = " ".join(summary.split())
                if len(compact) > 80:
                    errors.append(f"slide {no}: summary has {len(compact)} chars; split the page at the 80-char limit")
                if not re.search(r"[.。!！?？]$", compact):
                    errors.append(f"slide {no}: summary is not one complete sentence: '{compact[:50]}'")
            red_count = sum(run.color == "red" for run in runs)
            if red_count > 3:
                errors.append(f"slide {no}: {red_count} red runs exceed the limit of 3")
            if not any(run.context == "title" for run in runs):
                warnings.append(f"slide {no}: no nonempty title placeholder run detected")
            chars = sum(len(run.text) for run in runs)
            if chars > 1200:
                warnings.append(f"slide {no}: {chars} visible characters may be text-dense; split or delete")
            for run in runs:
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
                    if not ((run.color == "blue") or (run.color == "red" and run.underline)):
                        errors.append(f"{prefix} summary style must be blue+bold or red+bold+underline")
                    if run.size_pt is not None and run.size_pt < 18:
                        errors.append(f"{prefix} summary size is below the 18pt hard minimum")
                    elif run.size_pt is not None and run.size_pt < 20:
                        warnings.append(f"{prefix} summary is {run.size_pt:g}pt; the reference standard prefers 20-22pt")
                if run.size_pt is None:
                    warnings.append(f"{prefix} has inherited size; set an explicit pt value")
                elif run.size_pt < 14:
                    errors.append(f"{prefix} is {run.size_pt:g}pt, below the 14pt minimum")
                elif run.size_pt < 18 and run.context not in {"table"}:
                    warnings.append(f"{prefix} is {run.size_pt:g}pt non-table text, below the 18pt body target")
                explicit_fonts = [font for font in (run.latin_font, run.ea_font) if font]
                if len(explicit_fonts) < 2:
                    warnings.append(f"{prefix} has incomplete explicit Latin/East-Asian font; set both to Microsoft YaHei")
                bad = sorted(font for font in explicit_fonts if not (FONT_RE.fullmatch(font) or font.startswith("+mn") or font.startswith("+mj")))
                if bad:
                    errors.append(f"{prefix} uses non-Microsoft-YaHei font {', '.join(sorted(set(bad)))}")
                if run.color is None:
                    warnings.append(f"{prefix} has inherited color; set explicit black/blue/red for semantic QA")
                elif run.color not in {"red", "blue", "black"}:
                    errors.append(f"{prefix} uses non-semantic color {run.color}; use only red/blue/black")

        red_total = sum(run.color == "red" for run in all_runs)
    return errors, warnings, len(slide_names), len(all_runs), red_total, summary_shapes_total


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--strict", action="store_true", help="treat warnings as blocking")
    args = parser.parse_args()
    if not args.pptx.is_file():
        print(f"ERROR input PPTX does not exist: {args.pptx}")
        return 2
    try:
        errors, warnings, slide_count, run_count, red_total, summary_count = qa(args.pptx)
    except (OSError, zipfile.BadZipFile, ET.ParseError) as exc:
        print(f"ERROR cannot inspect PPTX: {exc}")
        return 2

    print(f"pptx={args.pptx}")
    print(f"slides={slide_count} text_runs={run_count} summary_shapes={summary_count} red_runs_total={red_total}")
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
