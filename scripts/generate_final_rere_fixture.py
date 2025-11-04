#!/usr/bin/env python3
"""Generate sanitized MCQ fixture for RERE data."""

import argparse
import json
from pathlib import Path

EXTRA_SOURCES = [
    ("clinical_scenario", "Clinical Scenario"),
    ("keywords", "Keywords"),
    ("required_knowledge_areas", "Required Knowledge Areas"),
    ("board_exam_relevance", "Board Exam Relevance"),
    ("references", "References"),
]

SECTION_KEY_MAP = {
    "pathophysiological_mechanisms": "pathophysiology",
    "clinical_correlation": "clinical_manifestation",
    "current_evidence": "current_evidence",
    "option_analysis_detailed": "option_analysis_detailed",
    "summary": "summary",
}

ALLOWED_COPY_FIELDS = {
    "question_number",
    "question_text",
    "subspecialty",
    "source_file",
    "exam_type",
    "exam_year",
    "verification_confidence",
    "primary_category",
    "secondary_category",
    "key_concept",
    "difficulty_level",
    "image_url",
    "ai_generated",
}


def build_explanation(fields: dict) -> str | None:
    parts: list[str] = []
    base_explanation = fields.get("unified_explanation") or fields.get("explanation")
    if base_explanation and base_explanation.strip():
        parts.append(base_explanation.strip())

    for key, label in EXTRA_SOURCES:
        value = fields.get(key)
        if not value:
            continue
        if key == "keywords" and isinstance(value, list):
            text = ", ".join(value)
        elif isinstance(value, list):
            text = "\n".join(f"- {item}" for item in value)
        else:
            text = str(value)
        parts.append(f"**{label}:**\n{text}")

    return "\n\n".join(parts) if parts else None


def normalize_sections(sections: dict) -> dict:
    normalized: dict = {}
    for key, value in sections.items():
        if value in (None, "", [], {}):
            continue
        normalized[key] = value
        mapped = SECTION_KEY_MAP.get(key)
        if mapped and mapped not in normalized:
            normalized[mapped] = value
    return normalized


def sanitize_fixture(source: Path, destination: Path) -> int:
    raw = json.loads(source.read_text())
    sanitized: list[dict] = []

    for idx, item in enumerate(raw, start=1):
        fields = item.get("fields", {})
        new_fields: dict = {}

        for field in ALLOWED_COPY_FIELDS:
            value = fields.get(field)
            if value not in (None, "", [], {}):
                new_fields[field] = value

        options = fields.get("options") or {}
        if isinstance(options, list):
            options = {chr(65 + i): option for i, option in enumerate(options)}
        new_fields["options"] = options

        correct = fields.get("correct_answer")
        if correct:
            if isinstance(correct, list):
                letter_str = ", ".join(correct)
            else:
                letter_str = str(correct)
            new_fields["correct_answer"] = letter_str
            if isinstance(correct, str) and "," in correct:
                letters = [part.strip() for part in correct.split(",")]
                texts = [options.get(letter) for letter in letters if options.get(letter)]
                new_fields["correct_answer_text"] = "; ".join(texts)
            else:
                new_fields["correct_answer_text"] = options.get(letter_str.strip(), "")
        else:
            new_fields["correct_answer"] = ""
            new_fields["correct_answer_text"] = ""

        explanation = build_explanation(fields)
        if explanation:
            new_fields["unified_explanation"] = explanation
            new_fields["explanation"] = explanation

        sections = fields.get("explanation_sections") or {}
        normalized = normalize_sections(sections)
        if normalized:
            new_fields["explanation_sections"] = normalized

        sanitized.append({
            "model": "mcq.mcq",
            "pk": idx,
            "fields": new_fields,
        })

    destination.write_text(json.dumps(sanitized, ensure_ascii=False))
    return len(sanitized)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate sanitized RERE fixture")
    parser.add_argument("--source", default="final_rere_fixtures.json", help="Path to raw fixture")
    parser.add_argument(
        "--dest",
        default="/tmp/final_rere_fixtures_sanitized.json",
        help="Output path for sanitized fixture",
    )
    args = parser.parse_args()

    source = Path(args.source)
    if not source.exists():
        raise SystemExit(f"Source fixture not found: {source}")

    destination = Path(args.dest)
    count = sanitize_fixture(source, destination)
    print(f"Sanitized fixture written to {destination} with {count} MCQs")


if __name__ == "__main__":
    main()
