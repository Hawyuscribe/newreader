from collections import deque

from django.test import SimpleTestCase

from unittest.mock import patch

from django_neurology_mcq.mcq.services.case_learning_service import (
    CaseLearningService,
    CasePreparationResult,
    CaseStartResult,
)


TEST_CASE_STATES = {
    'INITIAL': 0,
    'HISTORY_TAKING': 1,
    'HISTORY_FEEDBACK': 2,
    'EXAMINATION': 3,
    'EXAMINATION_FEEDBACK': 4,
    'LOCALIZATION_PROMPT': 5,
    'LOCALIZATION_FEEDBACK': 6,
    'LOCALIZATION': 7,
    'INVESTIGATIONS_PROMPT': 8,
    'INVESTIGATIONS_FEEDBACK': 9,
    'INVESTIGATIONS': 10,
    'DIFFERENTIAL_PROMPT': 11,
    'DIFFERENTIAL_FEEDBACK': 12,
    'DIFFERENTIAL_DIAGNOSIS': 13,
    'MANAGEMENT_PROMPT': 14,
    'MANAGEMENT_FEEDBACK': 15,
    'MANAGEMENT': 16,
    'CONCLUSION': 17,
    'FOLLOWUP': 18,
}


class StubbedApiCall:
    def __init__(self, response="stubbed response"):
        self.response = response
        self.calls = []

    def __call__(self, messages, **kwargs):
        self.calls.append({"messages": messages, "kwargs": kwargs})
        return self.response


class SequencedApiCall:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def __call__(self, messages, **kwargs):
        if not self.responses:
            raise AssertionError("SequencedApiCall exhausted — add more stub responses")
        response = self.responses.pop(0)
        self.calls.append({
            "messages": messages,
            "kwargs": kwargs,
            "response": response,
        })
        return response


class CaseLearningServiceTests(SimpleTestCase):
    def setUp(self):
        self.service = CaseLearningService(TEST_CASE_STATES)
        self.session_id = self.service.session_manager.create_session(
            user_id=1,
            specialty='Headache',
            difficulty='moderate',
        )
        self.session = self.service.session_manager.get_session(self.session_id)
        self.session['specialty'] = 'Headache'
        self.session['difficulty'] = 'moderate'
        self.session['case_data'] = {
            'condition': 'Migraine with aura',
            'age': 32,
            'gender': 'female',
            'difficulty': 'moderate',
            'description': '32-year-old woman with recurrent throbbing headaches',
            'case_hash': 'hash123',
            'custom_request': '',
        }
        # Ensure message history exists for deterministic assertions
        self.session['messages'] = deque(maxlen=100)

    def _screening_exam_generator(self, case_data):
        self.screening_exam_invocations.append(case_data)
        return "Screening neurological examination output"

    def test_missing_exam_triggers_feedback_before_localization(self):
        self.session['state'] = TEST_CASE_STATES['EXAMINATION']
        self.session['examination_findings'] = []

        api_stub = StubbedApiCall()
        self.screening_exam_invocations = []

        critical_elements = {
            'history': {},
            'examination': {'Headache': ['Fundoscopy']},
        }

        result = self.service.process_user_turn(
            self.session_id,
            self.session,
            'Proceed to localization now',
            critical_elements=critical_elements,
            make_api_call=api_stub,
            screening_exam_generator=self._screening_exam_generator,
        )

        self.assertTrue(result.handled)
        self.assertIsNotNone(result.response)
        self.assertEqual(result.response['state'], 'EXAMINATION_FEEDBACK')
        self.assertEqual(
            self.session['state'],
            TEST_CASE_STATES['EXAMINATION_FEEDBACK'],
        )
        self.assertIn('Fundoscopy', self.session['critical_exam_missed'])
        self.assertEqual(api_stub.calls, [])  # Early feedback should avoid AI call

    def test_proceed_to_examination_inserts_screening_exam(self):
        self.session['state'] = TEST_CASE_STATES['HISTORY_TAKING']
        self.session['history_gathered'] = ['Asked about onset']
        self.session['screening_exam_done'] = False

        api_stub = StubbedApiCall()
        self.screening_exam_invocations = []

        critical_elements = {
            'history': {},
            'examination': {},
        }

        result = self.service.process_user_turn(
            self.session_id,
            self.session,
            'Proceed to examination now',
            critical_elements=critical_elements,
            make_api_call=api_stub,
            screening_exam_generator=self._screening_exam_generator,
        )

        self.assertTrue(result.handled)
        self.assertIsNotNone(result.response)
        self.assertEqual(result.response['state'], 'EXAMINATION')
        self.assertTrue(self.session['screening_exam_done'])
        self.assertEqual(self.session['state'], TEST_CASE_STATES['EXAMINATION'])
        self.assertEqual(len(self.screening_exam_invocations), 1)

        assistant_messages = [msg for msg in self.session['messages'] if msg['role'] == 'assistant']
        self.assertEqual(len(assistant_messages), 1)
        self.assertIn('Screening neurological examination output', assistant_messages[0]['content'])

    def test_localization_prompt_captures_user_input(self):
        self.session['state'] = TEST_CASE_STATES['LOCALIZATION_PROMPT']
        self.session['case_laterality'] = 'right'  # deterministic prompt additions

        api_stub = StubbedApiCall(response='Constructive localization feedback')
        self.screening_exam_invocations = []

        critical_elements = {
            'history': {},
            'examination': {},
        }

        result = self.service.process_user_turn(
            self.session_id,
            self.session,
            'Lesion localized to the left thalamus based on findings',
            critical_elements=critical_elements,
            make_api_call=api_stub,
            screening_exam_generator=self._screening_exam_generator,
        )

        self.assertFalse(result.handled)
        self.assertEqual(
            self.session['state'],
            TEST_CASE_STATES['LOCALIZATION_FEEDBACK'],
        )
        self.assertEqual(self.session['user_localization'], 'Lesion localized to the left thalamus based on findings')
        self.assertIsNotNone(result.bot_response)
        self.assertIn('Constructive localization feedback', result.bot_response)
        self.assertEqual(len(api_stub.calls), 1)

        prompt_messages = api_stub.calls[0]['messages']
        self.assertIn('Provide constructive feedback on the resident\'s localization', prompt_messages[0]['content'])
        self.assertNotIn('phase_transitioned', self.session)

    def test_initialize_case_conversation_general_flow(self):
        case_payload = {
            'condition': 'Migraine with aura',
            'age': 32,
            'gender': 'female',
            'difficulty': 'moderate',
            'description': '32-year-old woman with throbbing headaches',
            'custom_request': '',
        }

        preparation = CasePreparationResult(
            session=self.session,
            case_data=case_payload,
            specialty='Headache',
            difficulty='moderate',
            custom_request='',
            is_mcq_case=False,
            starting_state=TEST_CASE_STATES['HISTORY_TAKING'],
            requires_ai_intro=True,
        )

        api_stub = StubbedApiCall(response='Chief complaint response')

        with patch.object(self.service, 'prepare_case_for_session', return_value=preparation):
            result = self.service.initialize_case_conversation(
                self.session_id,
                self.session,
                user_id=1,
                requested_specialty='Headache',
                difficulty='moderate',
                case_pools={},
                critical_elements={'history': {}, 'examination': {}},
                make_api_call=api_stub,
                general_prompt_builder=None,
                mcq_message_builder=None,
                mcq_case_data=None,
                ai_call_kwargs={'temperature': 0.8},
            )

        self.assertFalse(result.is_mcq_case)
        self.assertEqual(result.bot_response, 'Chief complaint response')
        self.assertEqual(result.state_name, 'HISTORY_TAKING')
        self.assertEqual(self.session['chief_complaint'], 'Chief complaint response')
        self.assertEqual(len(api_stub.calls), 1)
        self.assertEqual(api_stub.calls[0]['kwargs']['temperature'], 0.8)
        system_msg = api_stub.calls[0]['messages'][0]['content']
        self.assertIn('You are an expert neurologist presenting a case in Headache', system_msg)
        self.assertIn('USE PATIENT-FRIENDLY LANGUAGE', system_msg)
        assistant_messages = [msg for msg in self.session['messages'] if msg['role'] == 'assistant']
        self.assertEqual(assistant_messages[-1]['content'], 'Chief complaint response')

    def test_initialize_case_conversation_mcq_flow_with_enhancer(self):
        case_payload = {
            'condition': 'Migraine with aura',
            'clinical_presentation': 'Pulsating headache with aura',
            'patient_demographics': {'age': 32, 'gender': 'female'},
            'difficulty': 'moderate',
            'question_type': 'diagnosis',
            'source_mcq_id': 99,
        }

        preparation = CasePreparationResult(
            session=self.session,
            case_data=case_payload,
            specialty='Headache',
            difficulty='moderate',
            custom_request='',
            is_mcq_case=True,
            starting_state=TEST_CASE_STATES['DIFFERENTIAL_PROMPT'],
            requires_ai_intro=False,
        )

        enhancer_calls = []

        def enhancer(payload):
            enhancer_calls.append(payload)
            updated = dict(payload)
            updated['enhanced'] = True
            return updated

        def mcq_builder(payload, starting_state):
            self.assertEqual(starting_state, TEST_CASE_STATES['DIFFERENTIAL_PROMPT'])
            return 'MCQ intro'

        api_stub = StubbedApiCall(response='UNUSED')

        with patch.object(self.service, 'prepare_case_for_session', return_value=preparation):
            result = self.service.initialize_case_conversation(
                self.session_id,
                self.session,
                user_id=1,
                requested_specialty='Headache',
                difficulty='moderate',
                case_pools={},
                critical_elements={'history': {}, 'examination': {}},
                make_api_call=api_stub,
                mcq_message_builder=mcq_builder,
                mcq_case_data=case_payload,
                mcq_case_enhancer=enhancer,
            )

        self.assertTrue(result.is_mcq_case)
        self.assertEqual(result.bot_response, 'MCQ intro')
        self.assertEqual(result.state_name, 'DIFFERENTIAL_PROMPT')
        self.assertEqual(len(api_stub.calls), 0)
        self.assertEqual(len(enhancer_calls), 1)
        self.assertTrue(self.session['case_data']['enhanced'])
        assistant_messages = [msg for msg in self.session['messages'] if msg['role'] == 'assistant']
        self.assertEqual(assistant_messages[-1]['content'], 'MCQ intro')

    def test_skip_case_appends_hash_and_retries_mcq_payload(self):
        self.session['specialty'] = 'Headache'
        self.session['difficulty'] = 'moderate'
        self.session['case_hash'] = 'hash123'
        self.session['skipped_cases'] = ['existing']

        mcq_payload = {
            'condition': 'Migraine with aura',
            'clinical_presentation': 'Aura with headache',
            'difficulty': 'moderate',
        }
        unique_payload = {
            'condition': 'Cluster headache',
            'clinical_presentation': 'Severe unilateral headache',
            'difficulty': 'hard',
        }

        mcq_result = CaseStartResult(
            session=self.session,
            session_id=self.session_id,
            bot_response='MCQ intro',
            state_name='DIFFERENTIAL_PROMPT',
            specialty='Headache',
            difficulty='moderate',
            custom_request='',
            case_data=mcq_payload,
            is_mcq_case=True,
        )
        unique_result = CaseStartResult(
            session=self.session,
            session_id=self.session_id,
            bot_response='Unique intro',
            state_name='HISTORY_TAKING',
            specialty='Headache',
            difficulty='moderate',
            custom_request='',
            case_data=unique_payload,
            is_mcq_case=False,
        )

        with patch.object(
            self.service,
            'initialize_case_conversation',
            side_effect=[mcq_result, unique_result],
        ) as init_mock:
            result = self.service.skip_case(
                self.session_id,
                self.session,
                user_id=1,
                case_pools={},
                critical_elements={'history': {}, 'examination': {}},
                make_api_call=lambda *args, **kwargs: 'unused',
                mcq_message_builder=None,
                custom_request='',
                ai_call_kwargs={'temperature': 0.7},
            )

        self.assertIs(result, unique_result)
        self.assertEqual(self.session['skipped_cases'], ['existing', 'hash123'])
        self.assertEqual(init_mock.call_count, 2)
        first_call_kwargs = init_mock.call_args_list[0].kwargs
        self.assertIn('skip_list', first_call_kwargs)
        self.assertEqual(first_call_kwargs['skip_list'], ['existing', 'hash123'])
        self.assertFalse(result.is_mcq_case)

    def test_process_user_turn_generates_screening_exam_via_service_default(self):
        self.session['state'] = TEST_CASE_STATES['EXAMINATION']
        self.session['screening_exam_done'] = False
        self.session['examination_findings'] = []

        api_stub = StubbedApiCall(response='**Screening Neurological Examination:**\n- generated via stub')
        self.screening_exam_invocations = []

        critical_elements = {'history': {}, 'examination': {}}

        result = self.service.process_user_turn(
            self.session_id,
            self.session,
            'Please perform a screening neurological exam',
            critical_elements=critical_elements,
            make_api_call=api_stub,
        )

        self.assertFalse(result.handled)
        self.assertIn('Screening Neurological Examination', result.bot_response)
        self.assertTrue(self.session['screening_exam_done'])
        self.assertIn('screening_neurological_exam', self.session['examination_findings'])
        self.assertEqual(len(api_stub.calls), 1)
        system_msg = api_stub.calls[0]['messages'][0]['content']
        self.assertIn('SCREENING neurological examination', system_msg)

    def test_process_user_turn_screening_exam_fallback_on_api_error(self):
        self.session['state'] = TEST_CASE_STATES['EXAMINATION']
        self.session['screening_exam_done'] = False
        self.session['examination_findings'] = []

        def failing_api_call(messages, **kwargs):  # pragma: no cover - invoked in test
            raise RuntimeError('API failure')

        critical_elements = {'history': {}, 'examination': {}}

        result = self.service.process_user_turn(
            self.session_id,
            self.session,
            'Need a basic screening exam please',
            critical_elements=critical_elements,
            make_api_call=failing_api_call,
        )

        self.assertFalse(result.handled)
        self.assertIn('*This is a screening examination. Specific abnormalities would require targeted testing.*', result.bot_response)
        self.assertTrue(self.session['screening_exam_done'])
        self.assertIn('screening_neurological_exam', self.session['examination_findings'])

    def test_headache_elderly_case_transcript(self):
        """End-to-end transcript covering the giant cell arteritis scenario."""

        self.session['state'] = TEST_CASE_STATES['HISTORY_TAKING']
        self.session['specialty'] = 'Headache'
        self.session['difficulty'] = 'hard'
        self.session['history_gathered'] = []
        self.session['examination_findings'] = []
        self.session['messages'] = deque(maxlen=100)
        self.session['screening_exam_done'] = False

        case_data = {
            'condition': 'Giant cell arteritis',
            'age': 87,
            'gender': 'female',
            'difficulty': 'hard',
            'description': 'An 87-year-old female with a severe right temporal headache and jaw claudication.',
            'symptom_onset': 'five days ago',
            'symptom_course': 'have been worsening over the past 48 hours',
            'function_impact': 'limit her ability to chew meals and perform daily tasks',
            'patient_concern': 'worry her about permanent vision loss',
            'history_summary': (
                "The patient reports a new severe right temporal headache accompanied by jaw fatigue while chewing. "
                "Symptoms began five days ago and have been worsening over the past 48 hours. "
                "The problem limits her daily routines, and it worries her about permanent vision loss."
            ),
        }
        self.session['case_data'] = case_data

        critical_elements = {
            'history': {
                'Headache': ['blurry vision episodes', 'jaw claudication details'],
            },
            'examination': {
                'Headache': ['Temporal artery palpation', 'Fundoscopy', 'Trigger points'],
            },
        }

        screening_calls = []

        def screening_stub(case_payload):
            screening_calls.append(case_payload)
            return (
                "**Screening Neurological Examination:**\n"
                "**Mental Status & Language:** Alert, fluent speech with subtle word-finding pauses.\n"
                "**Cranial Nerves:** Pupils equal/reactive; extraocular movements full; facial strength symmetric.\n"
                "**Motor:** 5/5 strength throughout, no drift.\n"
                "**Reflexes:** 2+ and symmetric; plantar responses flexor.\n"
                "**Sensory:** Light touch intact in all limbs.\n"
                "**Coordination:** Finger-to-nose intact; heel-to-shin slightly cautious.\n"
                "**Gait:** Steady but guarded."
            )

        api_responses = [
            "**Examination Findings Provided:**\n- Temporal artery is tender and thickened.\n- Fundoscopy shows blurred disc margins.\n- Trigger points absent.",
            "Feedback: localization leans toward cranial branch arteritis consistent with giant cell arteritis.",
            "Expert localization: Inflammation of the right superficial temporal artery causing ischemic optic neuropathy.",
            "Investigations feedback: ESR, CRP, CBC with platelets, temporal artery biopsy, and urgent ophthalmology consult are appropriate.",
            "Investigations synthesis: Prioritize same-day steroids, arrange biopsy within 24 hours, baseline labs, and rheumatology input.",
            "Differential prompt: Summarize the key differentials for an elderly patient with temporal headache and jaw claudication.",
            "Differential feedback: Giant cell arteritis is most likely; consider trigeminal neuralgia and TMJ disease but they lack systemic findings.",
            "Differential synthesis: Giant cell arteritis best fits; trigeminal neuralgia and primary stabbing headache are less consistent.",
            "Management prompt: Outline your acute and chronic management steps for this patient.",
            "Management feedback: Start IV methylprednisolone then transition to high-dose oral prednisone with calcium/vitamin D and PPI prophylaxis.",
            "Management synthesis: Continue taper with steroid-sparing tocilizumab if relapse, schedule ophthalmology and vascular follow-up.",
            "Conclusion summary: Presentation aligns with giant cell arteritis; rapid steroids preserved vision and biopsy confirmed diagnosis.",
        ]
        api_stub = SequencedApiCall(api_responses)

        # History phase - request full HPI
        hpi_result = self.service.process_user_turn(
            self.session_id,
            self.session,
            'give me full HPI',
            critical_elements=critical_elements,
            make_api_call=api_stub,
            screening_exam_generator=screening_stub,
        )

        self.assertTrue(hpi_result.handled)
        self.assertEqual(hpi_result.response['message'], case_data['history_summary'])
        self.assertEqual(self.session['state'], TEST_CASE_STATES['HISTORY_TAKING'])
        self.assertIn(case_data['history_summary'], self.session['history_gathered'])

        # Clarify onset timing
        onset_result = self.service.process_user_turn(
            self.session_id,
            self.session,
            'when did the symptoms start?',
            critical_elements=critical_elements,
            make_api_call=api_stub,
            screening_exam_generator=screening_stub,
        )

        expected_onset = 'Symptoms began five days ago and have been worsening over the past 48 hours.'
        self.assertTrue(onset_result.handled)
        self.assertEqual(onset_result.response['message'], expected_onset)
        self.assertIn(expected_onset, self.session['history_gathered'])

        # Move to examination (auto screening exam should trigger)
        exam_transition = self.service.process_user_turn(
            self.session_id,
            self.session,
            'proceed to examination',
            critical_elements=critical_elements,
            make_api_call=api_stub,
            screening_exam_generator=screening_stub,
        )

        self.assertTrue(exam_transition.handled)
        self.assertEqual(self.session['state'], TEST_CASE_STATES['EXAMINATION'])
        self.assertEqual(len(screening_calls), 1)
        self.assertIn('Screening Neurological Examination', exam_transition.response['message'])

        # Attempt to localize too early -> should flag missing exam
        localization_block = self.service.process_user_turn(
            self.session_id,
            self.session,
            'proceed to localization',
            critical_elements=critical_elements,
            make_api_call=api_stub,
            screening_exam_generator=screening_stub,
        )

        self.assertTrue(localization_block.handled)
        self.assertEqual(self.session['state'], TEST_CASE_STATES['EXAMINATION_FEEDBACK'])
        self.assertIn('Temporal artery palpation', localization_block.response['message'])
        self.assertEqual(len(api_stub.calls), 0)

        # Provide missing examination data (first AI call)
        missing_exam = self.service.process_user_turn(
            self.session_id,
            self.session,
            'provide missing examination',
            critical_elements=critical_elements,
            make_api_call=api_stub,
            screening_exam_generator=screening_stub,
        )

        self.assertTrue(missing_exam.handled)
        self.assertEqual(self.session['state'], TEST_CASE_STATES['LOCALIZATION_PROMPT'])
        self.assertIn('Temporal artery is tender and thickened', missing_exam.response['message'])
        self.assertEqual(len(api_stub.calls), 1)
        self.assertIn('Missing examination', api_stub.calls[0]['messages'][0]['content'])

        # Provide localization attempt (feedback)
        localization_feedback = self.service.process_user_turn(
            self.session_id,
            self.session,
            'Localization is large vessel vasculitis involving the temporal artery',
            critical_elements=critical_elements,
            make_api_call=api_stub,
            screening_exam_generator=screening_stub,
        )

        self.assertFalse(localization_feedback.handled)
        self.assertIn('Feedback: localization leans toward', localization_feedback.bot_response)
        self.assertEqual(self.session['state'], TEST_CASE_STATES['LOCALIZATION_FEEDBACK'])
        self.assertEqual(len(api_stub.calls), 2)

        # Request complete localization analysis
        localization_complete = self.service.process_user_turn(
            self.session_id,
            self.session,
            'proceed to complete localization analysis',
            critical_elements=critical_elements,
            make_api_call=api_stub,
            screening_exam_generator=screening_stub,
        )

        self.assertFalse(localization_complete.handled)
        self.assertIn('Expert localization', localization_complete.bot_response)
        self.assertEqual(self.session['state'], TEST_CASE_STATES['LOCALIZATION'])
        self.assertEqual(len(api_stub.calls), 3)

        # Transition to investigations prompt
        investigations_prompt = self.service.process_user_turn(
            self.session_id,
            self.session,
            'proceed to investigations',
            critical_elements=critical_elements,
            make_api_call=api_stub,
            screening_exam_generator=screening_stub,
        )

        self.assertTrue(investigations_prompt.handled)
        self.assertIn('How would you like to structure the diagnostic workup?', investigations_prompt.response['message'])
        self.assertEqual(self.session['state'], TEST_CASE_STATES['INVESTIGATIONS_PROMPT'])
        self.assertEqual(len(api_stub.calls), 3)

        investigations_mode = self.service.process_user_turn(
            self.session_id,
            self.session,
            'full plan',
            critical_elements=critical_elements,
            make_api_call=api_stub,
            screening_exam_generator=screening_stub,
        )

        self.assertTrue(investigations_mode.handled)
        self.assertIn('outline your full investigation plan', investigations_mode.response['message'])
        self.assertEqual(self.session['state'], TEST_CASE_STATES['INVESTIGATIONS_PROMPT'])
        self.assertEqual(len(api_stub.calls), 3)

        # Provide minimal investigation plan (skip phrase)
        investigations_feedback = self.service.process_user_turn(
            self.session_id,
            self.session,
            'none more',
            critical_elements=critical_elements,
            make_api_call=api_stub,
            screening_exam_generator=screening_stub,
        )

        self.assertFalse(investigations_feedback.handled)
        self.assertTrue(investigations_feedback.bot_response.startswith('**[Phase: Investigations Feedback]**'))
        self.assertIn('Investigations feedback', investigations_feedback.bot_response)
        self.assertEqual(self.session['state'], TEST_CASE_STATES['INVESTIGATIONS_FEEDBACK'])
        self.assertEqual(len(api_stub.calls), 4)

        # Ask for expert investigation synthesis
        investigations_complete = self.service.process_user_turn(
            self.session_id,
            self.session,
            'proceed to complete investigations',
            critical_elements=critical_elements,
            make_api_call=api_stub,
            screening_exam_generator=screening_stub,
        )

        self.assertFalse(investigations_complete.handled)
        self.assertIn('Investigations synthesis', investigations_complete.bot_response)
        self.assertEqual(self.session['state'], TEST_CASE_STATES['INVESTIGATIONS'])
        self.assertEqual(len(api_stub.calls), 5)

        # Advance to differential prompt
        differential_prompt = self.service.process_user_turn(
            self.session_id,
            self.session,
            'proceed to differential',
            critical_elements=critical_elements,
            make_api_call=api_stub,
            screening_exam_generator=screening_stub,
        )

        self.assertFalse(differential_prompt.handled)
        self.assertTrue(differential_prompt.bot_response.startswith('**[Phase: Differential Diagnosis - Your Turn]**'))
        self.assertIn('Differential prompt', differential_prompt.bot_response)
        self.assertEqual(self.session['state'], TEST_CASE_STATES['DIFFERENTIAL_PROMPT'])
        self.assertEqual(len(api_stub.calls), 6)

        # Share differential diagnosis
        differential_feedback = self.service.process_user_turn(
            self.session_id,
            self.session,
            'Giant cell arteritis is most likely with trigeminal neuralgia and TMJ disorders as alternatives',
            critical_elements=critical_elements,
            make_api_call=api_stub,
            screening_exam_generator=screening_stub,
        )

        self.assertFalse(differential_feedback.handled)
        self.assertIn('Differential feedback', differential_feedback.bot_response)
        self.assertEqual(self.session['state'], TEST_CASE_STATES['DIFFERENTIAL_FEEDBACK'])
        self.assertEqual(self.session['user_differential'], 'Giant cell arteritis is most likely with trigeminal neuralgia and TMJ disorders as alternatives')
        self.assertEqual(len(api_stub.calls), 7)

        # Request complete differential analysis
        differential_complete = self.service.process_user_turn(
            self.session_id,
            self.session,
            'proceed to complete differential',
            critical_elements=critical_elements,
            make_api_call=api_stub,
            screening_exam_generator=screening_stub,
        )

        self.assertFalse(differential_complete.handled)
        self.assertIn('Differential synthesis', differential_complete.bot_response)
        self.assertEqual(self.session['state'], TEST_CASE_STATES['DIFFERENTIAL_DIAGNOSIS'])
        self.assertEqual(len(api_stub.calls), 8)

        # Move to management prompt
        management_prompt = self.service.process_user_turn(
            self.session_id,
            self.session,
            'proceed to management',
            critical_elements=critical_elements,
            make_api_call=api_stub,
            screening_exam_generator=screening_stub,
        )

        self.assertFalse(management_prompt.handled)
        self.assertTrue(management_prompt.bot_response.startswith('**[Phase: Management Plan - Your Turn]**'))
        self.assertIn('Management prompt', management_prompt.bot_response)
        self.assertEqual(self.session['state'], TEST_CASE_STATES['MANAGEMENT_PROMPT'])
        self.assertEqual(len(api_stub.calls), 9)

        # Provide management plan
        management_feedback = self.service.process_user_turn(
            self.session_id,
            self.session,
            'Start IV methylprednisolone followed by a high-dose oral taper with a steroid sparing agent',
            critical_elements=critical_elements,
            make_api_call=api_stub,
            screening_exam_generator=screening_stub,
        )

        self.assertFalse(management_feedback.handled)
        self.assertIn('Management feedback', management_feedback.bot_response)
        self.assertEqual(self.session['state'], TEST_CASE_STATES['MANAGEMENT_FEEDBACK'])
        self.assertEqual(self.session['user_management'], 'Start IV methylprednisolone followed by a high-dose oral taper with a steroid sparing agent')
        self.assertEqual(len(api_stub.calls), 10)

        # Request complete management plan
        management_complete = self.service.process_user_turn(
            self.session_id,
            self.session,
            'proceed to complete management',
            critical_elements=critical_elements,
            make_api_call=api_stub,
            screening_exam_generator=screening_stub,
        )

        self.assertFalse(management_complete.handled)
        self.assertIn('Management synthesis', management_complete.bot_response)
        self.assertEqual(self.session['state'], TEST_CASE_STATES['MANAGEMENT'])
        self.assertEqual(len(api_stub.calls), 11)

        # Conclude the case
        conclusion_result = self.service.process_user_turn(
            self.session_id,
            self.session,
            'proceed to conclusion',
            critical_elements=critical_elements,
            make_api_call=api_stub,
            screening_exam_generator=screening_stub,
        )

        self.assertFalse(conclusion_result.handled)
        self.assertTrue(conclusion_result.bot_response.startswith('**[Phase: Case Conclusion]**'))
        self.assertIn('Conclusion summary', conclusion_result.bot_response)
        self.assertEqual(self.session['state'], TEST_CASE_STATES['CONCLUSION'])
        self.assertEqual(len(api_stub.calls), 12)

        # All stubbed responses consumed and screening exam invoked once
        self.assertEqual(len(api_stub.responses), 0)
        self.assertEqual(len(screening_calls), 1)

    def test_investigation_result_request_transitions_and_records(self):
        self.session['state'] = TEST_CASE_STATES['INVESTIGATIONS_FEEDBACK']
        self.session['user_investigations'] = 'CT brain without contrast; CTA head/neck; baseline labs.'
        self.session['messages'] = deque(maxlen=100)

        api_stub = SequencedApiCall(['CT brain shows no acute hemorrhage.'])

        critical_elements = {'history': {}, 'examination': {}}

        result = self.service.process_user_turn(
            self.session_id,
            self.session,
            'What is the CT brain result?',
            critical_elements=critical_elements,
            make_api_call=api_stub,
        )

        self.assertFalse(result.handled)
        self.assertEqual(self.session['state'], TEST_CASE_STATES['INVESTIGATIONS'])
        self.assertEqual(result.state_name, 'INVESTIGATIONS')
        self.assertIn('**[Phase: Investigation Results]**', result.bot_response)
        self.assertIn('CT brain shows no acute hemorrhage.', result.bot_response)
        self.assertIn('Learner\'s latest request', api_stub.calls[0]['messages'][0]['content'])
        self.assertIn('What is the CT brain result?', api_stub.calls[0]['messages'][0]['content'])
        self.assertIn('investigation results', api_stub.calls[0]['messages'][0]['content'].lower())
        self.assertEqual(self.session['investigation_results'], ['CT brain shows no acute hemorrhage.'])
        self.assertTrue(self.session['investigations_completed'])
        self.assertEqual(self.session.get('latest_investigation_query'), '')
        self.assertIn('specific_investigation_requests', self.session)
        self.assertNotIn('state_transition_msg', self.session)

    def test_extract_onset_phrase_prefers_description(self):
        description = 'A 70-year-old patient reports a severe headache that began suddenly about three hours ago.'
        onset = self.service._extract_onset_phrase(description)
        self.assertEqual(onset, 'about 3 hours ago')

    def test_staged_investigations_collect_stages(self):
        self.session['state'] = TEST_CASE_STATES['INVESTIGATIONS_PROMPT']
        self.session['needs_investigation_mode'] = True
        self.session['investigation_stage'] = 1
        self.session['messages'] = deque(maxlen=100)

        critical_elements = {'history': {}, 'examination': {}}

        mode_result = self.service.process_user_turn(
            self.session_id,
            self.session,
            'staged plan',
            critical_elements=critical_elements,
            make_api_call=StubbedApiCall(),
        )

        self.assertTrue(mode_result.handled)
        self.assertEqual(self.session.get('investigation_mode'), 'staged')
        self.assertFalse(self.session.get('needs_investigation_mode'))
        self.assertEqual(self.session.get('investigation_stage'), 1)

        api_stub = SequencedApiCall(['Stage 1 feedback'])

        stage_result = self.service.process_user_turn(
            self.session_id,
            self.session,
            'CBC, ESR, CRP',
            critical_elements=critical_elements,
            make_api_call=api_stub,
        )

        self.assertFalse(stage_result.handled)
        self.assertEqual(self.session['state'], TEST_CASE_STATES['INVESTIGATIONS_FEEDBACK'])
        self.assertIn('Stage 1: CBC, ESR, CRP', self.session['user_investigations'])
        self.assertEqual(self.session.get('investigation_stage'), 2)
        self.assertEqual(self.session.get('staged_investigations')[0]['stage'], 1)
        self.assertEqual(self.session.get('staged_investigations')[0]['plan'], 'CBC, ESR, CRP')
        self.assertEqual(self.session.get('last_stage_submitted'), 1)
        self.assertEqual(len(api_stub.calls), 1)

    def test_provide_all_examination_satisfies_requirement(self):
        self.session['state'] = TEST_CASE_STATES['EXAMINATION_FEEDBACK']
        self.session['critical_exam_missed'] = ['Visuospatial testing']
        self.session['examination_findings'] = []
        self.session['messages'] = deque(maxlen=100)

        api_stub = SequencedApiCall(['Visuospatial testing reveals left-sided inattention.'])

        result = self.service.process_user_turn(
            self.session_id,
            self.session,
            'Could you please provide all exam findings before localization?',
            critical_elements={'history': {}, 'examination': {}},
            make_api_call=api_stub,
        )

        self.assertTrue(result.handled)
        self.assertEqual(self.session['state'], TEST_CASE_STATES['LOCALIZATION_PROMPT'])
        self.assertEqual(self.session['critical_exam_missed'], [])
        self.assertIn('Visuospatial testing', self.session['examination_findings'][0])
        self.assertEqual(len(api_stub.calls), 1)

    def test_provide_all_history_satisfies_requirement(self):
        self.session['state'] = TEST_CASE_STATES['HISTORY_FEEDBACK']
        self.session['critical_history_missed'] = ['Onset timing']
        self.session['history_gathered'] = []
        self.session['messages'] = deque(maxlen=100)

        api_stub = SequencedApiCall(['Symptoms began 10 hours ago after sudden onset.'])

        result = self.service.process_user_turn(
            self.session_id,
            self.session,
            'Please provide the missing history details.',
            critical_elements={'history': {}, 'examination': {}},
            make_api_call=api_stub,
        )

        self.assertTrue(result.handled)
        self.assertEqual(self.session['state'], TEST_CASE_STATES['EXAMINATION'])
        self.assertEqual(self.session['critical_history_missed'], [])
        self.assertIn('Symptoms began 10 hours ago', self.session['history_gathered'][0])
        self.assertEqual(len(api_stub.calls), 1)
