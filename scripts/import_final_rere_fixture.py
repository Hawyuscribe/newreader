#!/usr/bin/env python3
"""Sanitize and import the final RERE fixture into the MCQ table."""

import argparse
import json
import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = ROOT_DIR / "django_neurology_mcq"
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

import django
from django.db import transaction

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "neurology_mcq.settings")
django.setup()

from mcq.models import MCQ  # noqa: E402

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
    base = fields.get("unified_explanation") or fields.get("explanation")
    if base and base.strip():
        parts.append(base.strip())
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


def normalize_sections(sections: dict | None) -> dict:
    if not sections:
        return {}
    normalized: dict = {}
    for key, value in sections.items():
        if value in (None, "", [], {}):
            continue
        normalized[key] = value
        mapped = SECTION_KEY_MAP.get(key)
        if mapped and mapped not in normalized:
            normalized[mapped] = value
    return normalized


def sanitize_records(raw_records: list[dict]) -> list[MCQ]:
    mcqs: list[MCQ] = []
    for record in raw_records:
        fields = record.get("fields", {})
        mcq_data: dict = {}

        for field in ALLOWED_COPY_FIELDS:
            value = fields.get(field)
            if value not in (None, "", [], {}):
                mcq_data[field] = value

        options = fields.get("options") or {}
        if isinstance(options, list):
            options = {chr(65 + i): option for i, option in enumerate(options)}
        mcq_data["options"] = options

        correct = fields.get("correct_answer")
        if correct:
            if isinstance(correct, list):
                letter_str = ", ".join(correct)
            else:
                letter_str = str(correct)
            mcq_data["correct_answer"] = letter_str
            if isinstance(correct, str) and "," in correct:
                letters = [part.strip() for part in correct.split(",")]
                texts = [options.get(letter) for letter in letters if options.get(letter)]
                mcq_data["correct_answer_text"] = "; ".join(texts)
            else:
                mcq_data["correct_answer_text"] = options.get(letter_str.strip(), "")
        else:
            mcq_data["correct_answer"] = ""
            mcq_data["correct_answer_text"] = ""

        explanation = build_explanation(fields)
        if explanation:
            mcq_data["unified_explanation"] = explanation
            mcq_data["explanation"] = explanation

        sections = normalize_sections(fields.get("explanation_sections"))
        if sections:
            mcq_data["explanation_sections"] = sections

        mcqs.append(MCQ(**mcq_data))

    return mcqs


def main() -> None:
    parser = argparse.ArgumentParser(description="Import sanitized RERE MCQs")
    parser.add_argument(
        "--source",
        default="final_rere_fixtures.json",
        help="Path to the raw fixture JSON",
    )
    parser.add_argument(
        "--truncate",
        action="store_true",
        help="Delete existing MCQs before import",
    )
    args = parser.parse_args()

    source_path = Path(args.source)
    if not source_path.exists():
        raise SystemExit(f"Source fixture not found: {source_path}")

    raw_records = json.loads(source_path.read_text())
    mcqs = sanitize_records(raw_records)

    if args.truncate:
        deleted = MCQ.objects.all().delete()[0]
        print(f"Deleted {deleted} existing MCQs")

    with transaction.atomic():
        MCQ.objects.bulk_create(mcqs, batch_size=100)

    print(f"Imported {len(mcqs)} MCQs from {source_path}")


if __name__ == "__main__":
    main()
