from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from mcq.models import MCQ


class AiEditFlowsTests(TestCase):
    def setUp(self):
        self.staff = User.objects.create_user(
            username="editor",
            password="pass1234",
            is_staff=True,
            is_superuser=True,
        )
        self.client = Client()
        assert self.client.login(username="editor", password="pass1234")

        self.mcq = MCQ.objects.create(
            question_number="TEST-001",
            question_text="Baseline stem content that meets validation criteria.",
            options={"A": "Opt A", "B": "Opt B", "C": "Opt C", "D": "Opt D"},
            correct_answer="A",
            subspecialty="Neuromuscular",
            exam_type="Board-level",
            exam_year="2024",
        )

    @patch("mcq.openai_integration.ai_edit_explanation_text", return_value="")
    def test_ai_edit_explanation_rejects_empty_response(self, mock_edit):
        url = reverse("ai_edit_mcq_explanation", args=[self.mcq.id])
        payload = {
            "current_content": "Existing explanation",
            "custom_instructions": "",
        }
        response = self.client.post(url, data=payload, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()["success"])
        mock_edit.assert_called_once()

    @patch("mcq.openai_integration.ai_edit_options")
    def test_ai_edit_options_honors_override_payload(self, mock_ai_edit_options):
        mock_ai_edit_options.side_effect = lambda mcq_obj, *_args, **_kwargs: {
            "A": mcq_obj.question_text,
            "B": mcq_obj.correct_answer,
            "C": "C text",
            "D": "D text",
        }

        url = reverse("ai_edit_mcq_options", args=[self.mcq.id])
        new_question = "Updated vignette coming from editor textarea."
        payload = {
            "mode": "fill_missing",
            "custom_instructions": "",
            "question_text": new_question,
            "current_options": {"A": "", "B": "", "C": "", "D": ""},
            "correct_answer": "B",
        }
        response = self.client.post(url, data=payload, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertTrue(body["success"])
        self.assertEqual(body["options"]["A"], new_question)
        self.assertEqual(body["options"]["B"], "B")
        mock_ai_edit_options.assert_called_once()
