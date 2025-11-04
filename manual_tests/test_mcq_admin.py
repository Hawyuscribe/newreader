#!/usr/bin/env python
"""Test MCQ admin functionality"""

import os
import sys
import django


def _ensure_django_setup():
    project_root = os.path.join(os.path.dirname(__file__), "django_neurology_mcq")
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
    django.setup()


def _print_field_snapshot(form, field_name, label):
    field = form.fields.get(field_name)
    if not field:
        print(f"{label}: (field missing)")
        return
    value = field.initial or ""
    snippet = value[:50] + "..." if value else "(empty)"
    print(f"{label}: {snippet}")


def main():
    _ensure_django_setup()

    from mcq.models import MCQ
    from mcq.admin import MCQAdminForm

    mcq = MCQ.objects.filter(explanation_sections__isnull=False).first()
    if not mcq:
        mcq = MCQ.objects.filter(explanation__isnull=False).first()

    if not mcq:
        print("No MCQ with explanation found in database.")
        return

    print(f"Testing with MCQ #{mcq.question_number}")
    print(f"Has explanation_sections: {bool(mcq.explanation_sections)}")
    print(f"Has explanation: {bool(mcq.explanation)}")

    form = MCQAdminForm(instance=mcq)

    print("\nForm initial values:")
    _print_field_snapshot(form, 'conceptual_foundation', 'Conceptual Foundation')
    _print_field_snapshot(form, 'option_analysis', 'Option Analysis')
    _print_field_snapshot(form, 'clinical_context', 'Clinical Context')
    _print_field_snapshot(form, 'key_insight', 'Key Insight')
    _print_field_snapshot(form, 'quick_reference', 'Quick Reference')
    _print_field_snapshot(form, 'application_and_recall', 'Application and Recall')

    print("\nForm setup successful!")


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(f"Error: {exc}")
        import traceback
        traceback.print_exc()
