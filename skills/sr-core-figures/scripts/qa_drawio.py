#!/usr/bin/env python3
"""Deterministic source QA for diagrams.net/draw.io files used by SR-53.

This checker validates uncompressed or compressed mxGraph XML and reports common
structural/layout defects. It does not replace diagrams.net visual inspection.

Exit codes:
  0 = no issues, or warnings without --strict
  1 = warnings with --strict
  2 = XML/parser errors or blocking source errors
"""

from __future__ import annotations

import argparse
import base64
import html
import math
import re
import sys
import urllib.parse
import xml.etree.ElementTree as ET
import zlib
from dataclasses import dataclass
from pathlib import Path


FORMULA_RE = re.compile(r"(\\\(|\\\[|\$\$|`[^`]+`|\\sqrt|sqrt\(|softmax|\\mathrm|\^[A-Za-z0-9{]|_[A-Za-z0-9{])")
TAG_RE = re.compile(r"<[^>]+>")
MAX_NODE_LABEL_CHARS = 86
MAX_TEXT_LABEL_CHARS = 150
MAX_EDGE_LABEL_CHARS = 34


@dataclass
class Page:
    index: int
    name: str
    model: ET.Element


@dataclass
class Box:
    cell_id: str
    page: int
    parent: str | None
    x: float
    y: float
    width: float
    height: float
    value: str
    style: str
    edge: bool = False
    source: str | None = None
    target: str | None = None
    waypoints: list[tuple[float, float]] | None = None

    @property
    def right(self) -> float:
        return self.x + self.width

    @property
    def bottom(self) -> float:
        return self.y + self.height

    @property
    def cx(self) -> float:
        return self.x + self.width / 2

    @property
    def cy(self) -> float:
        return self.y + self.height / 2

    @property
    def plain_label(self) -> str:
        value = (self.value or "").replace("<br>", " ").replace("<br/>", " ")
        return " ".join(html.unescape(TAG_RE.sub(" ", value)).split())


def number(value: str | None, default: float = 0.0) -> float:
    try:
        return float(value) if value is not None else default
    except ValueError:
        return default


def decode_drawio_payload(payload: str) -> str:
    data = base64.b64decode(payload, validate=False)
    try:
        raw = zlib.decompress(data, -15)
    except zlib.error:
        raw = zlib.decompress(data)
    return urllib.parse.unquote(raw.decode("utf-8"))


def load_pages(path: Path) -> list[Page]:
    root = ET.parse(path).getroot()
    direct = root.findall(".//mxGraphModel")
    if direct:
        return [Page(i, model.get("pageName", f"page-{i + 1}"), model) for i, model in enumerate(direct)]

    pages: list[Page] = []
    for i, diagram in enumerate(root.findall("./diagram")):
        payload = (diagram.text or "").strip()
        if not payload:
            continue
        try:
            decoded = decode_drawio_payload(payload)
            model = ET.fromstring(decoded)
        except (ValueError, ET.ParseError, zlib.error) as exc:
            raise ValueError(f"cannot decode compressed diagram {diagram.get('name', str(i + 1))}: {exc}") from exc
        if model.tag != "mxGraphModel":
            model = model.find(".//mxGraphModel")
            if model is None:
                raise ValueError(f"decoded diagram {diagram.get('name', str(i + 1))} has no mxGraphModel")
        pages.append(Page(i, diagram.get("name", f"page-{i + 1}"), model))
    return pages


def collect_boxes(pages: list[Page]) -> tuple[list[Box], dict[str, Box], list[str]]:
    boxes: list[Box] = []
    by_id: dict[str, Box] = {}
    errors: list[str] = []
    for page in pages:
        seen_ids: set[str] = set()
        cells = page.model.findall("./root/mxCell")
        if not cells:
            errors.append(f"page {page.name}: no root/mxCell elements")
            continue
        for cell in cells:
            cell_id = cell.get("id", "")
            if not cell_id:
                errors.append(f"page {page.name}: mxCell without id")
                continue
            if cell_id in seen_ids:
                errors.append(f"duplicate cell id: {cell_id}")
                continue
            seen_ids.add(cell_id)
            is_edge = cell.get("edge") == "1"
            is_vertex = cell.get("vertex") == "1"
            if not is_edge and not is_vertex:
                continue
            geometry = cell.find("mxGeometry")
            if geometry is None:
                errors.append(f"{cell_id}: { 'edge' if is_edge else 'vertex' } has no mxGeometry")
                continue
            points: list[tuple[float, float]] = []
            if is_edge:
                array = geometry.find("Array[@as='points']")
                if array is not None:
                    for point in array.findall("mxPoint"):
                        points.append((number(point.get("x")), number(point.get("y"))))
            box = Box(
                cell_id=cell_id,
                page=page.index,
                parent=cell.get("parent"),
                x=number(geometry.get("x")),
                y=number(geometry.get("y")),
                width=number(geometry.get("width")),
                height=number(geometry.get("height")),
                value=cell.get("value", ""),
                style=cell.get("style", ""),
                edge=is_edge,
                source=cell.get("source"),
                target=cell.get("target"),
                waypoints=points if is_edge else None,
            )
            boxes.append(box)
            by_id[cell_id] = box

    # Resolve mxGraph's parent-relative coordinates recursively.
    resolved: dict[str, tuple[float, float]] = {}
    visiting: set[str] = set()

    def origin(box: Box) -> tuple[float, float]:
        if box.cell_id in resolved:
            return resolved[box.cell_id]
        if box.cell_id in visiting:
            errors.append(f"parent cycle at cell: {box.cell_id}")
            return (0.0, 0.0)
        visiting.add(box.cell_id)
        value = (0.0, 0.0)
        if box.parent and box.parent in by_id:
            parent = by_id[box.parent]
            if parent.edge:
                errors.append(f"{box.cell_id}: vertex parent is an edge: {parent.cell_id}")
            else:
                value = origin(parent)
        resolved[box.cell_id] = value
        visiting.remove(box.cell_id)
        return value

    for box in boxes:
        dx, dy = origin(box)
        box.x += dx
        box.y += dy
    return boxes, by_id, errors


def is_text_cell(box: Box) -> bool:
    return bool(box.plain_label) and box.style.strip().startswith("text;")


def is_background_container(box: Box) -> bool:
    style = box.style.lower()
    return (
        "container=1" in style
        or (box.width >= 220 and box.height >= 140 and "align=left" in style and "verticalalign=top" in style)
    )


def overlaps(a: Box, b: Box, padding: float = 0.0) -> bool:
    return not (
        a.right <= b.x - padding
        or a.x >= b.right + padding
        or a.bottom <= b.y - padding
        or a.y >= b.bottom + padding
    )


def is_ancestor(candidate: str, box: Box, by_id: dict[str, Box]) -> bool:
    current: str | None = box.parent
    while current:
        if current == candidate:
            return True
        current = by_id[current].parent if current in by_id else None
    return False


def edge_points(edge: Box, by_id: dict[str, Box]) -> list[tuple[float, float]]:
    points: list[tuple[float, float]] = []
    if edge.source and edge.source in by_id:
        source = by_id[edge.source]
        points.append((source.cx, source.cy))
    points.extend(edge.waypoints or [])
    if edge.target and edge.target in by_id:
        target = by_id[edge.target]
        points.append((target.cx, target.cy))
    return points


def point_in_box(point: tuple[float, float], box: Box, padding: float = 0.0) -> bool:
    x, y = point
    return box.x - padding <= x <= box.right + padding and box.y - padding <= y <= box.bottom + padding


def segment_intersects_box(a: tuple[float, float], b: tuple[float, float], box: Box) -> bool:
    left, right, top, bottom = box.x, box.right, box.y, box.bottom
    # Fast reject.
    if max(a[0], b[0]) < left or min(a[0], b[0]) > right or max(a[1], b[1]) < top or min(a[1], b[1]) > bottom:
        return False

    def cross(p: tuple[float, float], q: tuple[float, float], r: tuple[float, float]) -> float:
        return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

    corners = [(left, top), (right, top), (right, bottom), (left, bottom)]
    sides = [(corners[i], corners[(i + 1) % 4]) for i in range(4)]
    for p, q in sides:
        d1 = cross(a, b, p)
        d2 = cross(a, b, q)
        d3 = cross(p, q, a)
        d4 = cross(p, q, b)
        if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
            return True
    return point_in_box(a, box) or point_in_box(b, box)


def qa(path: Path, grid: int, padding: float) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    pages = load_pages(path)
    if not pages:
        errors.append("no mxGraphModel page found")
        return errors, warnings
    boxes, by_id, parse_errors = collect_boxes(pages)
    errors.extend(parse_errors)
    if not any(box.cell_id == "0" for box in boxes) and not any(cell_id == "0" for cell_id in by_id):
        if not any(page.model.find('./root/mxCell[@id="0"]') is not None for page in pages): errors.append('graph root must contain mxCell id="0"')

    formulas_present = False
    for box in boxes:
        if FORMULA_RE.search(box.value or ""):
            formulas_present = True
            page = next((item for item in pages if item.index == box.page), None)
            if page and page.model.get("math") != "1":
                errors.append(f'{box.cell_id}: formula-like label requires mxGraphModel math="1"')

        if box.edge:
            if not box.source:
                errors.append(f"{box.cell_id}: edge has no source")
            elif box.source not in by_id:
                errors.append(f"{box.cell_id}: unknown source={box.source}")
            if not box.target:
                errors.append(f"{box.cell_id}: edge has no target")
            elif box.target not in by_id:
                errors.append(f"{box.cell_id}: unknown target={box.target}")
            label = box.plain_label
            if len(label) > MAX_EDGE_LABEL_CHARS:
                warnings.append(f"{box.cell_id}: edge label is {len(label)} chars; use a separate text cell")
            continue

        if box.width <= 0 or box.height <= 0:
            errors.append(f"{box.cell_id}: vertex width/height must be positive")
            continue
        for key, value in (("x", box.x), ("y", box.y), ("width", box.width), ("height", box.height)):
            if value % grid != 0:
                warnings.append(f"{box.cell_id}: {key}={value:g} is off the {grid}px grid")
        limit = MAX_TEXT_LABEL_CHARS if is_text_cell(box) else MAX_NODE_LABEL_CHARS
        if box.plain_label and not is_background_container(box) and len(box.plain_label) > limit:
            warnings.append(f"{box.cell_id}: label is {len(box.plain_label)} chars; split the node or move prose to caption")

    for page in pages:
        page_width = number(page.model.get("pageWidth"), 0)
        page_height = number(page.model.get("pageHeight"), 0)
        if page_width <= 0 or page_height <= 0:
            continue
        for box in boxes:
            if box.page != page.index or box.edge:
                continue
            if box.x < 0 or box.y < 0 or box.right > page_width or box.bottom > page_height:
                warnings.append(
                    f"{box.cell_id}: extends beyond page bounds {page_width:g}x{page_height:g}"
                )

    # Text-bearing vertices should not overlap unrelated visible vertices.
    text_boxes = [box for box in boxes if not box.edge and box.plain_label and not is_background_container(box)]
    for i, left in enumerate(text_boxes):
        for right in boxes[i + 1 :]:
            if right.edge or right.page != left.page or not right.plain_label or is_background_container(right):
                continue
            if is_ancestor(left.cell_id, right, by_id) or is_ancestor(right.cell_id, left, by_id):
                continue
            if overlaps(left, right, padding):
                warnings.append(f"{left.cell_id}: text-bearing box overlaps {right.cell_id}")

    # Conservative center-route probe for connector occlusion.
    for edge in (box for box in boxes if box.edge):
        points = edge_points(edge, by_id)
        if len(points) < 2:
            continue
        for box in boxes:
            if box.edge or box.page != edge.page or not box.plain_label or is_background_container(box):
                continue
            if box.cell_id in {edge.source, edge.target} or is_ancestor(box.cell_id, edge, by_id):
                continue
            for a, b in zip(points, points[1:]):
                if math.isclose(a[0], b[0]) and math.isclose(a[1], b[1]):
                    continue
                if segment_intersects_box(a, b, box):
                    warnings.append(f"{edge.cell_id}: route appears to cross text-bearing node {box.cell_id}")
                    break

    if formulas_present:
        print("formula_mode=required")
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("drawio", type=Path, help="Uncompressed or compressed .drawio file")
    parser.add_argument("--grid", type=int, default=10, help="Expected geometry grid (default: 10)")
    parser.add_argument("--padding", type=float, default=2.0, help="Overlap safety padding in px (default: 2)")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as blocking")
    args = parser.parse_args()
    if args.grid <= 0:
        parser.error("--grid must be positive")
    if not args.drawio.is_file():
        print(f"ERROR input file does not exist: {args.drawio}")
        return 2

    try:
        errors, warnings = qa(args.drawio, args.grid, args.padding)
    except (OSError, ET.ParseError, ValueError) as exc:
        print(f"ERROR cannot parse {args.drawio}: {exc}")
        return 2

    pages = len(load_pages(args.drawio))
    print(f"drawio={args.drawio}")
    print(f"pages={pages}")
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
