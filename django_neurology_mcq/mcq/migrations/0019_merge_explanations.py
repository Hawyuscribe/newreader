from django.db import migrations


def merge_explanations(apps, schema_editor):
    MCQ = apps.get_model("mcq", "MCQ")
    try:
        from django_neurology_mcq.mcq.explanation_utils import merge_sections_to_text
    except Exception:
        # Fallback: if the utility cannot be imported (during certain migration workflows)
        def merge_sections_to_text(sections):
            if not sections:
                return ""
            parts = []
            for key, value in sections.items():
                if not value:
                    continue
                parts.append(str(value).strip())
            return "\n\n".join(parts).strip()

    batch_size = 500
    qs = MCQ.objects.all().order_by("id")
    start = 0
    total = qs.count()

    while start < total:
        for mcq in qs[start : start + batch_size]:
            sections = getattr(mcq, "explanation_sections", None)
            if not sections:
                continue

            if isinstance(sections, str):
                # Attempt to coerce JSON string into dict
                try:
                    import json

                    parsed = json.loads(sections)
                    sections = parsed if isinstance(parsed, dict) else {}
                except (TypeError, ValueError):
                    sections = {}

            if not isinstance(sections, dict) or not sections:
                continue

            unified_text = merge_sections_to_text(sections)
            if not unified_text:
                continue

            # Prefer existing unified text if it already contains merged content
            current_unified = (mcq.unified_explanation or "").strip()
            current_plain = (mcq.explanation or "").strip()

            # Avoid duplicating content if already present
            target_text = current_unified or current_plain
            if target_text:
                if unified_text not in target_text:
                    if target_text.endswith("\n"):
                        target_text = f"{target_text}\n\n{unified_text}"
                    else:
                        target_text = f"{target_text}\n\n{unified_text}"
            else:
                target_text = unified_text

            mcq.unified_explanation = target_text
            mcq.explanation = target_text
            mcq.explanation_sections = None
            mcq.save(
                update_fields=[
                    "unified_explanation",
                    "explanation",
                    "explanation_sections",
                ]
            )
        start += batch_size


def noop_reverse(apps, schema_editor):
    # No-op reverse migration; original section data has been consolidated.
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("mcq", "0018_mcqcaseconversionsession"),
    ]

    operations = [
        migrations.RunPython(merge_explanations, noop_reverse),
    ]
