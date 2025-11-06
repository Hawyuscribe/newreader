Heroku Smoke Test Checklist (ReasoningPal + Audio)

Prereqs
- Staff account on the deployed app.
- Heroku app deployed with config vars set (use scripts/heroku_reasoningpal_setup.sh).

Quick Checks
- Open /debug/openai-selftest/ while logged in as staff.
  - Expect JSON: client_initialized: true, chat_ok: true.

ReasoningPal Flow (Inline)
- Visit any MCQ page, answer, then click the ReasoningPal button.
- Step 2 should switch to “processing” briefly and then render results (within ~30–90s), not get stuck.
- Confirm the analysis includes:
  - Cognitive Bias section (names specific bias and quotes learner’s words)
  - “Guideline Evidence” with exact quotes or the “No direct guideline quotation available” line
  - An Algorithm list and a Comparative Table
  - 800–1200 words total output

Audio Transcription
- In the modal, record a short audio blurb and submit.
- Expect 200 OK with a { text: "..." } response; no 500.

If Still Stuck on Step 2
- Check browser console for /cognitive_session/<id>/status/ responses.
- Ensure REASONING_INLINE=true in Heroku config.
- If you prefer background tasks, add Redis + worker dyno, then unset REASONING_INLINE and verify again.

Optional: Background Tasks
- heroku addons:create heroku-redis:hobby-dev -a <APP>
- heroku ps:scale worker=1 -a <APP>
- heroku config:unset REASONING_INLINE CELERY_EAGER -a <APP>

