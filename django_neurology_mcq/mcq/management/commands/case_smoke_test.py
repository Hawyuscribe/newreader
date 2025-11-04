import json
import os
import re
import time
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Sequence
from urllib.parse import urljoin

import requests
from django.core.management.base import BaseCommand, CommandError


class CaseSmokeError(RuntimeError):
    """Raised when the smoke test cannot proceed."""


@dataclass(frozen=True)
class CaseStep:
    name: str
    prompt: str
    required_groups: Sequence[Sequence[str]]
    min_hits: int
    forbidden_terms: Sequence[str] = ()
    min_words: int = 0
    min_chars: int = 0


INTRO_GROUPS: Sequence[Sequence[str]] = (
    ("chief complaint", "presenting", "presents"),
    ("ask", "begin", "history"),
)

INTRO_FORBIDDEN: Sequence[str] = (
    "diagnosis",
    "diagnostic",
    "final diagnosis",
    "conclusion",
)

SCENARIO_STEPS: Sequence[CaseStep] = (
    CaseStep(
        name="Focused history scaffolding",
        prompt=(
            "I'd like to take a focused history. Walk me through onset, tempo, provocative factors, "
            "and associated neurological symptoms to structure my questioning."
        ),
        required_groups=(
            ("onset", "time course", "tempo"),
            ("progress", "progression", "course"),
            ("risk", "hypertension", "diabetes", "lipid"),
            ("weakness", "motor"),
            ("sensory", "numb", "paresthesia"),
            ("speech", "aphasia", "dysarthria"),
            ("vision", "visual"),
        ),
        min_hits=3,
        min_words=60,
    ),
    CaseStep(
        name="Motor and sensory specifics",
        prompt=(
            "Can you specify the distribution of weakness, any sensory components, and whether cranial "
            "nerves are involved?"
        ),
        required_groups=(
            ("distribution", "pattern", "topography"),
            ("weakness", "motor"),
            ("sensory", "numb", "paresthesia"),
            ("cranial", "facial", "dysarthria"),
        ),
        min_hits=3,
        min_words=50,
    ),
    CaseStep(
        name="Localization analysis",
        prompt=(
            "Help me localize the lesion and specify the most likely vascular territory or neuroanatomical structure."
        ),
        required_groups=(
            ("localization", "localise", "localizing"),
            ("territory", "circulation", "vascular"),
            ("internal capsule", "cortex", "brainstem", "thal", "pons", "mca", "pca", "aca", "basilar"),
        ),
        min_hits=2,
        min_words=40,
    ),
    CaseStep(
        name="Investigations summary",
        prompt=(
            "Summarize the investigations that have already been completed, including imaging and key laboratory data, "
            "plus what they showed."
        ),
        required_groups=(
            ("ct", "computed tomography", "mri", "imaging", "angiogram", "angiography"),
            ("lab", "laboratory", "cbc", "glucose", "chemistry"),
            ("showed", "revealed", "demonstrated", "results"),
        ),
        min_hits=2,
        forbidden_terms=(
            "would you like",
            "should we order",
            "what imaging",
            "which test",
            "order any",
            "do you want to order",
            "request any tests",
        ),
        min_words=45,
    ),
    CaseStep(
        name="Differential and red flags",
        prompt=(
            "Provide a prioritized differential diagnosis, highlight any red flags, and explain the evidence behind your reasoning."
        ),
        required_groups=(
            ("differential", "considerations", "possibilities"),
            ("red flag", "red-flag", "worrisome", "danger"),
            ("evidence", "guideline", "evidence-based", "studies"),
        ),
        min_hits=2,
        min_words=55,
    ),
    CaseStep(
        name="Diagnosis and management",
        prompt="State the leading diagnosis explicitly and outline key acute management steps.",
        required_groups=(
            ("diagnosis", "most consistent", "likely diagnosis"),
            ("management", "treatment", "therapy", "plan"),
            ("acute", "immediate", "urgent"),
        ),
        min_hits=2,
        min_words=50,
    ),
    CaseStep(
        name="Teaching pearls and follow-up",
        prompt="Share teaching pearls, follow-up plans, and how a neurology resident should reflect on this case.",
        required_groups=(
            ("teaching", "pearls", "learning"),
            ("follow-up", "follow up", "outpatient", "next steps"),
            ("reflection", "resident", "practice"),
        ),
        min_hits=2,
        min_words=40,
    ),
)


def _contains_any(text: str, options: Iterable[str]) -> bool:
    return any(opt in text for opt in options)


class CaseSmokeTester:
    def __init__(
        self,
        *,
        base_url: str,
        username: str,
        password: str,
        specialty: str,
        difficulty: str,
        timeout: int,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.username = username
        self.password = password
        self.specialty = specialty
        self.difficulty = difficulty
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "CaseSmokeTester/1.0"})
        self.session_id: str | None = None
        self.violations: List[str] = []
        self.transcript: List[Dict[str, Any]] = []

    def execute(self) -> Dict[str, Any]:
        start_ts = time.time()
        error_message = None
        try:
            self.login()
            intro = self.start_case()
            self._validate_intro(intro)
            for step in SCENARIO_STEPS:
                self.ask(step)
            self.skip_case()
        except CaseSmokeError as exc:
            error_message = str(exc)
        duration = time.time() - start_ts
        success = not self.violations and error_message is None
        return {
            "success": success,
            "violations": self.violations,
            "transcript": self.transcript,
            "duration_seconds": round(duration, 2),
            "error": error_message,
        }

    def login(self) -> None:
        login_url = self._url("/login/")
        try:
            response = self.session.get(login_url, timeout=self.timeout)
        except requests.RequestException as exc:
            raise CaseSmokeError(f"Failed to load login page: {exc}") from exc
        if response.status_code != 200:
            raise CaseSmokeError(f"Login page returned {response.status_code}")
        csrf_token = self._extract_csrf(response.text) or self.session.cookies.get("csrftoken")
        if not csrf_token:
            raise CaseSmokeError("Unable to locate CSRF token on login page.")
        payload = {
            "username": self.username,
            "password": self.password,
            "csrfmiddlewaretoken": csrf_token,
        }
        try:
            post_response = self.session.post(
                login_url,
                data=payload,
                headers={"Referer": login_url},
                timeout=self.timeout,
            )
        except requests.RequestException as exc:
            raise CaseSmokeError(f"Login submission failed: {exc}") from exc
        if post_response.status_code not in (200, 302):
            raise CaseSmokeError(f"Login submission failed with {post_response.status_code}")
        if "Invalid username or password" in post_response.text:
            raise CaseSmokeError("Login rejected: invalid credentials.")
        try:
            dashboard_response = self.session.get(self._url("/dashboard/"), timeout=self.timeout)
        except requests.RequestException as exc:
            raise CaseSmokeError(f"Dashboard check failed: {exc}") from exc
        if dashboard_response.status_code != 200:
            raise CaseSmokeError("Authenticated dashboard check failed.")
        dashboard_text = dashboard_response.text.lower()
        if not any(
            marker in dashboard_text
            for marker in ("case-based learning", "case based learning", "case-based-learning")
        ):
            self.violations.append("Dashboard did not render case-based learning entry.")

    def start_case(self) -> Dict[str, Any]:
        payload = {
            "specialty": self.specialty,
            "difficulty": self.difficulty,
        }
        data = self._post_case_api(payload, step_name="Start case")
        if not data.get("session_id"):
            raise CaseSmokeError("No session_id returned when starting case.")
        self.session_id = data["session_id"]
        self._record_turn(
            step="Start case",
            prompt="system",
            response=data["message"],
            violations=[],
        )
        return data

    def ask(self, step: CaseStep) -> Dict[str, Any]:
        if not self.session_id:
            raise CaseSmokeError("Session not initialised before asking questions.")
        payload = {
            "session_id": self.session_id,
            "message": step.prompt,
        }
        data = self._post_case_api(payload, step_name=step.name)
        message = data["message"]
        lower = message.lower()
        violations = self._validate_message(step, lower, message)
        if data.get("session_id") != self.session_id:
            violations.append("Response returned different session_id.")
        self._record_turn(step=step.name, prompt=step.prompt, response=message, violations=violations)
        return data

    def skip_case(self) -> Dict[str, Any]:
        if not self.session_id:
            raise CaseSmokeError("Cannot skip case without active session.")
        payload = {
            "action": "skip_case",
            "session_id": self.session_id,
        }
        data = self._post_case_api(payload, step_name="Skip case")
        message = data["message"]
        lower = message.lower()
        violations = []
        if not _contains_any(lower, INTRO_GROUPS[0]):
            violations.append("Skipped case did not provide a new chief complaint.")
        self._record_turn(step="Skip case", prompt="skip_case", response=message, violations=violations)
        return data

    def _validate_intro(self, data: Dict[str, Any]) -> None:
        message = data.get("message", "")
        lower = message.lower()
        if not _contains_any(lower, INTRO_GROUPS[0]):
            self.violations.append("Initial response did not include a chief complaint.")
        if not _contains_any(lower, INTRO_GROUPS[1]):
            self.violations.append("Initial response did not prompt the resident to begin history-taking.")
        for term in INTRO_FORBIDDEN:
            if term in lower:
                self.violations.append(f"Initial response revealed forbidden detail: '{term}'.")

    def _validate_message(self, step: CaseStep, lower: str, raw: str) -> List[str]:
        violations: List[str] = []
        words = raw.split()
        if step.min_words and len(words) < step.min_words:
            violations.append(
                f"{step.name}: Expected at least {step.min_words} words, received {len(words)}."
            )
        if step.min_chars and len(raw) < step.min_chars:
            violations.append(
                f"{step.name}: Expected at least {step.min_chars} characters, received {len(raw)}."
            )
        hits = 0
        missing_groups: List[str] = []
        for group in step.required_groups:
            if _contains_any(lower, group):
                hits += 1
            else:
                missing_groups.append("/".join(group[:2]))
        if step.required_groups and hits < step.min_hits:
            remaining = step.min_hits - hits
            sample_missing = ", ".join(missing_groups[:3]) if missing_groups else "unspecified elements"
            violations.append(
                f"{step.name}: Needed {step.min_hits} clinical elements, found {hits}. Missing examples: {sample_missing}."
            )
        for term in step.forbidden_terms:
            if term in lower:
                violations.append(f"{step.name}: Response contained forbidden phrase '{term}'.")
        if violations:
            self.violations.extend(violations)
        return violations

    def _post_case_api(self, payload: Dict[str, Any], *, step_name: str) -> Dict[str, Any]:
        try:
            response = self.session.post(
                self._url("/api/neurology-bot-enhanced/"),
                json=payload,
                timeout=self.timeout,
            )
        except requests.RequestException as exc:
            raise CaseSmokeError(f"{step_name} request failed: {exc}") from exc
        if response.status_code != 200:
            raise CaseSmokeError(f"{step_name} failed with status {response.status_code}")
        try:
            data = response.json()
        except json.JSONDecodeError as exc:
            raise CaseSmokeError(f"{step_name} returned non-JSON response.") from exc
        if not data.get("success"):
            raise CaseSmokeError(f"{step_name} response indicated failure: {data}")
        if not data.get("message"):
            raise CaseSmokeError(f"{step_name} response lacked assistant message.")
        return data

    def _record_turn(self, *, step: str, prompt: str, response: str, violations: Sequence[str]) -> None:
        self.transcript.append(
            {
                "step": step,
                "prompt": prompt,
                "response_excerpt": self._truncate(response),
                "full_response": response,
                "violations": list(violations),
            }
        )

    def _url(self, path: str) -> str:
        return urljoin(self.base_url + "/", path.lstrip("/"))

    @staticmethod
    def _truncate(text: str, length: int = 320) -> str:
        return text if len(text) <= length else text[: length - 3] + "..."

    @staticmethod
    def _extract_csrf(html: str) -> str | None:
        match = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', html)
        return match.group(1) if match else None


class Command(BaseCommand):
    help = "Run a Heroku-first smoke test of the case-based learning flow."

    def add_arguments(self, parser) -> None:
        parser.add_argument("--host", default=os.environ.get("CASE_SMOKE_HOST"))
        parser.add_argument("--username", default=os.environ.get("CASE_SMOKE_USER"))
        parser.add_argument("--password", default=os.environ.get("CASE_SMOKE_PASS"))
        parser.add_argument("--specialty", default="vascular neurology")
        parser.add_argument("--difficulty", default="moderate")
        parser.add_argument("--timeout", type=int, default=int(os.environ.get("CASE_SMOKE_TIMEOUT", "30")))
        parser.add_argument("--retries", type=int, default=int(os.environ.get("CASE_SMOKE_RETRIES", "1")))
        parser.add_argument("--retry-delay", type=int, default=int(os.environ.get("CASE_SMOKE_RETRY_DELAY", "5")))

    def handle(self, *args, **options) -> None:
        host = options["host"]
        username = options["username"]
        password = options["password"]
        specialty = options["specialty"]
        difficulty = options["difficulty"]
        timeout = options["timeout"]
        retries = max(1, options["retries"])
        retry_delay = max(0, options["retry_delay"])

        if not host or not username or not password:
            raise CommandError("Provide host, username, and password via arguments or environment variables.")

        attempts: List[Dict[str, Any]] = []
        for attempt in range(1, retries + 1):
            tester = CaseSmokeTester(
                base_url=host,
                username=username,
                password=password,
                specialty=specialty,
                difficulty=difficulty,
                timeout=timeout,
            )
            self.stdout.write(f"Attempt {attempt} against {host}")
            summary = tester.execute()
            summary["attempt"] = attempt
            attempts.append(summary)
            if summary["success"]:
                break
            if attempt < retries:
                self.stdout.write(self.style.WARNING("Smoke test failed; retrying after delay."))
                time.sleep(retry_delay)

        final = attempts[-1]
        result = {
            "host": host,
            "specialty": specialty,
            "difficulty": difficulty,
            "attempts": attempts,
        }
        self.stdout.write(json.dumps(result, indent=2))
        if not final["success"]:
            raise CommandError("Case-based learning smoke test failed.")
        self.stdout.write(self.style.SUCCESS("Case-based learning smoke test passed."))
