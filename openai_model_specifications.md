# OpenAI Model Specifications

The application now standardises every OpenAI call through `mcq.openai_integration`.  
`gpt-5-mini` is the default model for **all** completions and reasoning flows.  
Deployments can override the defaults with environment variables:

| Variable | Purpose | Default |
| --- | --- | --- |
| `OPENAI_MODEL` | Primary model for every helper | `gpt-5-mini` |
| `OPENAI_FALLBACK_MODEL` | Optional fallback model | `gpt-4o-mini` (if unset) |

## Runtime Behaviour

- `chat_completion()` automatically normalises parameters for GPT‑5 models (e.g. converts `max_tokens` → `max_completion_tokens` and drops legacy sampling arguments that GPT‑5 ignores).
- If a request fails and a distinct fallback model is configured, the helper retries exactly once with that fallback.
- All call sites (`mcq_case_converter`, `case_session_validator`, `generate_missing_questions`, `match_mcqs_with_gpt`, and the interactive case bot) now use the shared helper so that model changes propagate globally.

## Notes for Contributors

1. Prefer importing `DEFAULT_MODEL`, `FALLBACK_MODEL`, and `chat_completion` from `mcq.openai_integration` instead of hard-coding model IDs.
2. Scripts that previously referenced legacy models (e.g. `gpt-4.1-nano`) have been updated to the shared helper; mirror that approach for any new utilities.
3. When experimenting with alternate models, set `OPENAI_MODEL`/`OPENAI_FALLBACK_MODEL` in your environment rather than modifying code.
4. GPT‑5 models currently ignore `temperature`/`top_p` parameters; the helper strips them automatically. Behavioural tuning should therefore use prompt engineering rather than sampling controls.

This document replaces the older per-function inventory now that model selection is centralised.
