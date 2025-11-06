from django import template

from ..explanation_sections import EXPLANATION_SECTIONS, SECTION_LOOKUP

register = template.Library()

@register.filter
def split(value, arg):
    """
    Splits the value by the argument and returns a list.
    Usage: {{ value|split:"," }}
    """
    return value.split(arg)


@register.filter
def get_item(dictionary, key):
    """
    Get an item from a dictionary using a variable as key.
    Usage: {{ dict|get_item:key }}
    """
    if dictionary and key:
        # Don't convert to lowercase - use the key as-is
        return dictionary.get(key, 0)
    return 0


@register.filter
def has_real_explanation_sections(explanation_sections):
    """Check if MCQ has real explanation sections or just placeholders."""
    if not isinstance(explanation_sections, dict):
        return False
    
    def is_substantial(content: str) -> bool:
        """Heuristic to detect substantive prose (not placeholders)."""
        if not content or not isinstance(content, str):
            return False
        text = content.strip()
        if len(text) < 50:
            return False
        lower_text = text.lower()
        if 'unified explanation' in lower_text:
            return False
        if 'placeholder' in lower_text and 'explanation' in lower_text:
            return False
        return True

    structured_hits = sum(
        1 for section in EXPLANATION_SECTIONS
        if is_substantial(explanation_sections.get(section.key, ''))
    )

    if structured_hits >= max(3, len(EXPLANATION_SECTIONS) // 2):
        return True

    legacy_hits = sum(
        1
        for key, value in explanation_sections.items()
        if key not in SECTION_LOOKUP and is_substantial(value)
    )

    return legacy_hits >= 3


@register.filter
def get_unified_explanation(explanation_sections):
    """Get the first non-empty section as unified explanation."""
    if not explanation_sections:
        return ""
    
    ordered_keys = [section.key for section in EXPLANATION_SECTIONS]
    legacy_fallbacks = [
        'pathophysiological_mechanisms',
        'clinical_correlation',
        'why_other_options_are_incorrect',
        'summary',
    ]

    for key in ordered_keys + legacy_fallbacks:
        value = explanation_sections.get(key, '')
        if isinstance(value, str) and len(value.strip()) > 50:
            return value

    # Final fallback: return the longest textual section
    longest_value = ""
    for value in explanation_sections.values():
        if isinstance(value, str) and len(value.strip()) > len(longest_value):
            longest_value = value.strip()

    return longest_value
