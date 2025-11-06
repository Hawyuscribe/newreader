# Manual Test Scripts

This directory contains ad-hoc verification scripts that were previously stored in
the repository root. They remain executable for operational vetting, but are no
longer picked up by Django's automated test discovery. Each script should be run
explicitly, for example:

```bash
python manual_tests/test_mcq_admin.py
```

If you intend to promote any of these workflows to automated coverage, port the
logic into Django test cases under the relevant app (e.g., `django_neurology_mcq/mcq/tests/`)
and wrap external integrations (OpenAI, Redis, etc.) with deterministic mocks.
