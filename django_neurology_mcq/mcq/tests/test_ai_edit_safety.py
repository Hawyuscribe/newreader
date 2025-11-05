import unittest
from typing import List
from unittest.mock import patch

from django_neurology_mcq.mcq import openai_integration as integration


class DummyResponseBlock:
    def __init__(self, payload):
        self.type = "json_schema"
        self.json = payload


class DummyResponseItem:
    def __init__(self, payload):
        self.content = [DummyResponseBlock(payload)]


class DummyResponse:
    def __init__(self, payload):
        self.output = [DummyResponseItem(payload)]


class DummyMCQ:
    def __init__(self, question_text, options, correct="A", explanation="", subspecialty="General"):
        self.id = 123
        self.question_text = question_text
        self._options = options
        self.correct_answer = correct
        self.explanation = explanation
        self.subspecialty = subspecialty

    def get_options_dict(self):
        return dict(self._options)


class AiEditSafetyTests(unittest.TestCase):
    def setUp(self):
        self._api_key = integration.api_key
        self._client = integration.client
        integration.api_key = "test-key"
        integration.client = object()

    def tearDown(self):
        integration.api_key = self._api_key
        integration.client = self._client

    def test_prepare_editor_instructions_normalizes_whitespace(self):
        raw = "  Keep   it concise.\n\n* bullet one  \n  * bullet two\n\t"
        result = integration._prepare_editor_instructions(raw)
        self.assertEqual(result, "Keep it concise.\n* bullet one\n* bullet two")

    def test_validate_generated_options_detects_duplicates(self):
        errors = integration._validate_generated_options(
            generated={"C": "Same option", "D": "same option"},
            expected_letters=["C", "D"],
            existing_options={"A": "Correct choice"},
            correct_letter="A",
            correct_answer_text="Correct choice",
            forbidden_terms=[],
        )
        self.assertTrue(any("duplicates" in err for err in errors))

    def test_ai_edit_question_retries_with_sanitization(self):
        mcq = DummyMCQ(
            question_text="Original stem referencing restricted content.",
            options={"A": "Choice A", "B": "Choice B", "C": "Choice C", "D": "Choice D"},
            correct="B",
            explanation="",
        )

        call_state = {"count": 0}
        captured_prompts: List[str] = []

        def fake_responses_create(_model, messages, **_kwargs):
            call_state["count"] += 1
            if call_state["count"] == 1:
                raise ValueError("Invalid prompt: content policy violation")
            captured_prompts.append(messages[1]["content"][0]["text"])
            refined_stem = (
                "A 55-year-old man with diabetes and hypertension presents with progressive gait imbalance and distal numbness over "
                "six months. Neurologic examination shows length-dependent sensory loss, wide-based gait, and absent ankle reflexes. "
                "Laboratory studies reveal elevated hemoglobin A1c. What is the next best diagnostic evaluation to confirm the underlying neuropathy?"
            )
            return DummyResponse({"stem": refined_stem})

        with patch.object(integration, "_responses_create", side_effect=fake_responses_create), patch(
            "django_neurology_mcq.mcq.openai_integration.time.sleep", return_value=None
        ):
            result = integration.ai_edit_question(mcq, custom_instructions="")

        self.assertEqual(call_state["count"], 2)
        self.assertIn("55-year-old", result)
        self.assertTrue(captured_prompts)
        sanitized_prompt = captured_prompts[0]
        self.assertIn("sanitized for policy compliance", sanitized_prompt.lower())

    def test_ai_edit_options_retries_on_validation_errors(self):
        mcq = DummyMCQ(
            question_text="Neurology stem",
            options={"A": "Correct answer text", "B": "Existing option", "C": "", "D": ""},
            correct="A",
            explanation="Key rationale",
        )

        call_state = {"count": 0}

        def fake_responses_create(_model, messages, **_kwargs):
            call_state["count"] += 1
            if call_state["count"] == 1:
                return DummyResponse({"C": "duplicate", "D": "duplicate"})
            return DummyResponse({"C": "Hemiparesis due to lacunar infarct", "D": "Myasthenia gravis exacerbation"})

        with patch.object(integration, "_responses_create", side_effect=fake_responses_create), patch(
            "django_neurology_mcq.mcq.openai_integration.time.sleep", return_value=None
        ):
            final_options = integration.ai_edit_options(mcq, custom_instructions="")

        self.assertEqual(call_state["count"], 2)
        self.assertEqual(final_options["A"], "Correct answer text")
        self.assertNotEqual(final_options["C"], final_options["D"])
        self.assertTrue(final_options["C"].startswith("Hemiparesis"))

    def test_extract_json_from_text_handles_prefixed_logs(self):
        raw = "INFO: starting run\n{\"explanation\":\"Alpha reasoning\"}\ntrail"
        parsed = integration._extract_json_from_text(raw)
        self.assertIsInstance(parsed, dict)
        self.assertEqual(parsed.get("explanation"), "Alpha reasoning")

    def test_coerce_explanation_from_partial_json(self):
        raw = '{"explanation":"Segmented detail with newline\\nSecond line'
        explanation = integration._coerce_explanation_from_raw(raw)
        self.assertEqual(explanation, "Segmented detail with newline\nSecond line")


if __name__ == "__main__":
    unittest.main()
