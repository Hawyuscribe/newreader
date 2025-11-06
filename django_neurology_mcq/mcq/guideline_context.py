"""
Guideline Context Retrieval for Clinical Reasoning Modal (Generic)

Purpose
- Provide exact quotations (if any) drawn from existing MCQ content to avoid hallucinations.
- Work generically across all specialties and question types without condition-specific prompts.

How it works
- Scans the MCQ's explanation text and structured explanation_sections for quoted sentences.
- Returns a plain multi-line string of exact quotes only; no fabrication.
- If no quotes are discoverable, returns an empty string, prompting the UI to state
  “No direct guideline quotation available.”

Notes
- This module intentionally avoids condition-specific mappings. If you later wire a
  full guideline RAG index, plug its outputs here.
"""

from __future__ import annotations

import json
from typing import Dict, List, Any
import re


QUOTE_RE = re.compile(r'“(.{10,300}?)”|"(.{10,300}?)"')


def _extract_quotes_from_text(text: str) -> List[str]:
    if not text:
        return []
    quotes = []
    for m in QUOTE_RE.finditer(text):
        q = m.group(1) or m.group(2)
        q = (q or "").strip()
        if q and q not in quotes:
            quotes.append(q)
    return quotes


def _walk_sections_and_collect_quotes(sections: Any) -> List[str]:
    quotes: List[str] = []
    if isinstance(sections, dict):
        for v in sections.values():
            if isinstance(v, str):
                quotes.extend(_extract_quotes_from_text(v))
            elif isinstance(v, list):
                for item in v:
                    if isinstance(item, str):
                        quotes.extend(_extract_quotes_from_text(item))
                    elif isinstance(item, dict):
                        quotes.extend(_walk_sections_and_collect_quotes(item))
            elif isinstance(v, dict):
                quotes.extend(_walk_sections_and_collect_quotes(v))
    return list(dict.fromkeys(quotes))  # dedupe preserve order


def build_guideline_context(
    question_text: str,
    options_texts: List[str],
    explanation_sections: Any = None,
    explanation_text: str | None = None,
) -> str:
    """Return a plain text block of exact quotes discovered in existing MCQ content.

    The returned string is injected into the model prompt under GuidelineContext.
    If empty, the model is instructed to state no direct quotation is available.
    """
    quotes: List[str] = []

    # 1) Prefer structured sections
    quotes.extend(_walk_sections_and_collect_quotes(explanation_sections))

    # 2) Fall back to raw explanation text
    quotes.extend(_extract_quotes_from_text(explanation_text or ""))

    # Keep the context small
    quotes = [q for q in quotes if 10 <= len(q) <= 300][:4]

    if not quotes:
        return ""

    # Render as lines; do not fabricate sources
    # Each line is "Quote" (source if present in original text)
    return "\n".join([f'"{q}"' for q in quotes])
