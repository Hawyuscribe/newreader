"""
Template filters for exam type display.
"""

from django import template

register = template.Library()


@register.filter
def display_exam_type(exam_type):
    """
    Convert exam type to display name.
    Maps old names to new names for consistency.
    """
    if not exam_type:
        return ''
    
    # Define the mapping
    exam_type_mapping = {
        # Old names
        'Promotion': 'Basic level',
        'promotion': 'Basic level',
        'Part I': 'Advanced',
        'Part 1': 'Advanced',
        'PartI': 'Advanced',
        'part i': 'Advanced',
        'Part II': 'Board-level',
        'Part 2': 'Board-level',
        'PartII': 'Board-level',
        'part ii': 'Board-level',
        # New names (return as is)
        'Basic level': 'Basic level',
        'Advanced': 'Advanced',
        'Board-level': 'Board-level',
        'Other': 'Other',
    }
    
    # Return mapped value or original if not in mapping
    return exam_type_mapping.get(exam_type, exam_type)


@register.filter
def exam_type_badge_class(exam_type):
    """
    Return appropriate badge class for exam type.
    """
    display_type = display_exam_type(exam_type)
    
    badge_classes = {
        'Basic level': 'bg-success',
        'Advanced': 'bg-primary',
        'Board-level': 'bg-danger',
        'Other': 'bg-secondary',
    }
    
    return badge_classes.get(display_type, 'bg-secondary')