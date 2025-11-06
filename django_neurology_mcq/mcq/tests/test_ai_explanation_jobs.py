import json
from typing import Any, Dict
from unittest import TestCase
from unittest.mock import patch

from django_neurology_mcq.mcq import openai_integration as integration


class DummyContentBlock:
    def __init__(self, payload: Dict[str, Any]):
        self.type = "json_schema"
        self.json = payload


class DummyOutputItem:
    def __init__(self, payload: Dict[str, Any]):
        self.content = [DummyContentBlock(payload)]


class DummyResponsesPayload:
    def __init__(self, payload: Dict[str, Any]):
        self.output = [DummyOutputItem(payload)]


class DummyChatMessage:
    def __init__(self, content: str):
        self.content = content


class DummyChatChoice:
    def __init__(self, content: str):
        self.message = DummyChatMessage(content)


class DummyChatPayload:
    def __init__(self, raw_text: str):
        self.output = []
        self.choices = [DummyChatChoice(raw_text)]


class DummyMCQ:
    def __init__(self):
        self.id = 999
        self.question_text = (
            "A 45-year-old man with poorly controlled diabetes presents with progressive distal numbness, "
            "burning pain, and absent ankle reflexes over eight months."
        )
        self.correct_answer = "B"
        self.subspecialty = "Neuro-infectious"
        self.unified_explanation = "Existing explanation text that ensures adequate baseline length." * 8
        self.explanation = self.unified_explanation
        self._options = {
            "A": "Alcoholic neuropathy",
            "B": "Diabetic neuropathy",
            "C": "Guillain-Barré syndrome",
            "D": "Chronic inflammatory demyelinating polyneuropathy",
        }

    def get_options_dict(self):
        return dict(self._options)


class AIExplanationParsingTests(TestCase):
    def setUp(self):
        self._api_key = integration.api_key
        self._client = integration.client
        self._agent_enabled = integration.AGENT_ENABLED_DEFAULT
        integration.api_key = "test-key"
        integration.client = object()
        integration.AGENT_ENABLED_DEFAULT = False

    def tearDown(self):
        integration.api_key = self._api_key
        integration.client = self._client
        integration.AGENT_ENABLED_DEFAULT = self._agent_enabled

    def test_ai_edit_explanation_uses_json_schema_payload(self):
        explanation_text = "### Enhanced Explanation\n" + ("Supporting detail. " * 140)
        dummy_response = DummyResponsesPayload({"explanation": explanation_text})

        with patch.object(integration, "_responses_create", return_value=dummy_response):
            result = integration.ai_edit_explanation_text(DummyMCQ())

        self.assertTrue(result.startswith("### Enhanced Explanation"))
        self.assertGreater(len(result), 600)

    def test_ai_edit_explanation_recovers_from_noisy_json(self):
        explanation_text = "### Differential diagnosis\n" + ("Evidence-based comparison. " * 90)
        raw_payload = json.dumps({"explanation": explanation_text})
        noisy_text = f"INFO: start\n{raw_payload}\n-- end"
        dummy_response = DummyChatPayload(noisy_text)

        with patch.object(integration, "_responses_create", return_value=dummy_response):
            result = integration.ai_edit_explanation_text(DummyMCQ())

        self.assertTrue(result.startswith("### Differential diagnosis"))
        self.assertIn("Evidence-based comparison.", result)
