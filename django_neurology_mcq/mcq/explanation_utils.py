"""
Helpers for working with MCQ explanations.

Provides utilities to merge legacy structured explanation sections into a single
string as well as lightweight rendering helpers so the unified explanation can
be displayed as HTML without bringing in a full Markdown dependency.
"""

from __future__ import annotations

from typing import Mapping

from django.utils.html import escape
from django.utils.safestring import mark_safe

from .explanation_sections import EXPLANATION_SECTIONS, SECTION_LOOKUP


def merge_sections_to_text(sections: Mapping[str, str]) -> str:
    """
    Convert a structured explanation dictionary into a single markdown-like text block.

    Args:
        sections: Mapping of section keys to prose strings.

    Returns:
        Consolidated multi-section text with headings preserved.
    """
    if not sections:
        return ""

    ordered_keys = [section.key for section in EXPLANATION_SECTIONS]
    merged_blocks: list[str] = []

    # Add canonical sections first to preserve pedagogical order.
    for section in EXPLANATION_SECTIONS:
        content = sections.get(section.key)
        if isinstance(content, str):
            stripped = content.strip()
        else:
            stripped = str(content).strip() if content else ""

        if stripped:
            merged_blocks.append(f"### {section.title}\n\n{stripped}")

    # Include any legacy/unknown keys so historical data is not lost.
    for key, value in sections.items():
        if key in ordered_keys:
            continue

        if isinstance(value, str):
            stripped = value.strip()
        else:
            stripped = str(value).strip() if value else ""

        if not stripped:
            continue

        title = SECTION_LOOKUP.get(key, None)
        heading = title.title if title else key.replace("_", " ").title()
        merged_blocks.append(f"### {heading}\n\n{stripped}")

    return "\n\n".join(merged_blocks).strip()


def render_explanation_as_html(text: str) -> str:
    """
    Render a unified explanation string as safe HTML.

    Performs a lightweight markdown-to-HTML conversion supporting headings
    (###, ##, #), unordered lists (-, *), ordered lists (1.), and paragraphs.

    Args:
        text: Unified explanation text

    Returns:
        HTML fragment marked safe for template rendering.
    """
    if not text:
        return ""

    html_parts: list[str] = []
    in_ul = False
    in_ol = False
    list_index = 0

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            html_parts.append("</ul>")
            in_ul = False
        if in_ol:
            html_parts.append("</ol>")
            in_ol = False

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()

        if not stripped:
            close_lists()
            continue

        if stripped.startswith("### "):
            close_lists()
            html_parts.append(f"<h4>{escape(stripped[4:].strip())}</h4>")
            continue

        if stripped.startswith("## "):
            close_lists()
            html_parts.append(f"<h3>{escape(stripped[3:].strip())}</h3>")
            continue

        if stripped.startswith("# "):
            close_lists()
            html_parts.append(f"<h2>{escape(stripped[2:].strip())}</h2>")
            continue

        if stripped.startswith(("- ", "* ")):
            if in_ol:
                html_parts.append("</ol>")
                in_ol = False
            if not in_ul:
                html_parts.append("<ul>")
                in_ul = True
            html_parts.append(f"<li>{escape(stripped[2:].strip())}</li>")
            continue

        if stripped[:2].isdigit() and stripped[2:4] in {". ", ") "}:
            # Minimal ordered list detection (e.g., "1. " or "1) ")
            marker = stripped.split(maxsplit=1)[0]
            content = stripped[len(marker):].strip()
            if in_ul:
                html_parts.append("</ul>")
                in_ul = False
            if not in_ol:
                html_parts.append("<ol>")
                in_ol = True
                list_index = 0
            list_index += 1
            html_parts.append(f"<li>{escape(content)}</li>")
            continue

        close_lists()
        escaped = escape(stripped)
        formatted = escaped.replace("\n", "<br>")
        html_parts.append(f"<p>{formatted}</p>")

    close_lists()
    return mark_safe("\n".join(html_parts))
