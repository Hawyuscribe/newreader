"""Canonical definitions for MCQ structured explanation sections."""

from dataclasses import dataclass, asdict
from typing import List


@dataclass(frozen=True)
class ExplanationSection:
    key: str
    title: str
    icon: str
    required: bool = False
    description: str = ""
    ai_prompt: str = ""


EXPLANATION_SECTIONS: List[ExplanationSection] = [
    ExplanationSection(
        key="option_analysis",
        title="Option Analysis",
        icon="bi-clipboard2-check",
        required=True,
        description="Explain why the correct option is right and why others fall short.",
        ai_prompt=(
            "Provide a concise analysis of each answer option. Highlight why the correct answer "
            "is best and give short clinical reasoning for eliminating other choices."
        ),
    ),
    ExplanationSection(
        key="conceptual_foundation",
        title="Conceptual Foundation",
        icon="bi-diagram-3",
        description="Key foundational concepts or anatomy worth reviewing before tackling the problem.",
        ai_prompt="Summarise the foundational science or key definitions relevant to this case.",
    ),
    ExplanationSection(
        key="pathophysiology",
        title="Pathophysiology",
        icon="bi-activity",
        description="Mechanistic reasoning that links the vignette to underlying disease biology.",
        ai_prompt="Describe the pathophysiology or mechanism underlying the presentation.",
    ),
    ExplanationSection(
        key="clinical_manifestation",
        title="Clinical Manifestations",
        icon="bi-person-heart",
        description="How the disease typically presents, including red flags or distinguishing clues.",
        ai_prompt="Outline the hallmark history, exam, or lab findings that support the diagnosis.",
    ),
    ExplanationSection(
        key="diagnostic_approach",
        title="Diagnostic Approach",
        icon="bi-search",
        description="Tests, imaging, or decision rules that confirm or exclude the condition.",
        ai_prompt="Summarise the diagnostic work-up and how each modality guides management.",
    ),
    ExplanationSection(
        key="classification_and_nosology",
        title="Classification & Nosology",
        icon="bi-diagram-2",
        description="Pertinent subtypes, staging systems, or differential diagnoses to consider.",
        ai_prompt="List important subtypes or how the disorder fits into a broader classification scheme.",
    ),
    ExplanationSection(
        key="management_principles",
        title="Management Principles",
        icon="bi-clipboard2-pulse",
        required=True,
        description="Initial management, definitive treatment, and supportive care pearls.",
        ai_prompt="Outline acute management, definitive therapy, and avoidance of common pitfalls.",
    ),
    ExplanationSection(
        key="follow_up_guidelines",
        title="Follow-up & Safety",
        icon="bi-calendar3",
        description="Monitoring, recurrence prevention, or patient counselling tips.",
        ai_prompt="Describe follow-up strategy, monitoring, or patient education points.",
    ),
    ExplanationSection(
        key="clinical_pearls",
        title="Clinical Pearls",
        icon="bi-stars",
        description="Memorable take-home points or pattern recognition cues.",
        ai_prompt="Give high-yield bedside pearls or traps to avoid for learners.",
    ),
    ExplanationSection(
        key="current_evidence",
        title="Current Evidence",
        icon="bi-journal-medical",
        description="Guideline references, landmark trials, or citations for further reading.",
        ai_prompt="Provide recent guideline recommendations or key evidence supporting management.",
    ),
]


SECTION_LOOKUP = {section.key: section for section in EXPLANATION_SECTIONS}
EXPLANATION_SECTIONS_EXPORT = [asdict(section) for section in EXPLANATION_SECTIONS]
