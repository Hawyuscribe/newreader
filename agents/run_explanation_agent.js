import { pathToFileURL } from "node:url";

const loadAgentSdk = () => {
  if (globalThis.__MCQ_OPENAI_AGENTS__) {
    return Promise.resolve(globalThis.__MCQ_OPENAI_AGENTS__);
  }
  return import("@openai/agents");
};

let Agent;
let fileSearchTool;
let Runner;
let withTrace;
let agentSdkLoadError;

await loadAgentSdk().then(
  module => {
    Agent = module.Agent;
    fileSearchTool = module.fileSearchTool;
    Runner = module.Runner;
    withTrace = module.withTrace;
  },
  error => {
    const message =
      error && typeof error === "object" && "message" in error
        ? error.message
        : String(error);
    agentSdkLoadError = new Error(`Unable to load @openai/agents SDK: ${message}`);
  }
);

const assertSdkReady = () => {
  if (agentSdkLoadError) {
    throw agentSdkLoadError;
  }
  if (!Agent || !fileSearchTool || !Runner || !withTrace) {
    throw new Error("@openai/agents SDK is not fully initialised");
  }
};

const shouldLoadDotenv = process.env.MCQ_AGENT_SKIP_DOTENV !== "1";
const dotenvLoaded = shouldLoadDotenv
  ? await import("dotenv/config").then(
      () => true,
      () => false
    )
  : false;
void dotenvLoaded;

const FALLBACK_VECTOR_STORE_ID = "vs_6907b938bc248191944e5c224c545d47";
const rawVectorStore = process.env.OPENAI_VECTOR_STORE_ID?.trim();
const disableVectorStoreFlag = (process.env.MCQ_AGENT_DISABLE_VECTOR || "")
  .trim()
  .toLowerCase();
const vectorStoreIds = [];

if (!["1", "true", "yes"].includes(disableVectorStoreFlag)) {
  if (
    rawVectorStore &&
    !["", "none", "disable", "disabled", "null", "false", "0"].includes(
      rawVectorStore.toLowerCase()
    )
  ) {
    vectorStoreIds.push(rawVectorStore);
  } else {
    vectorStoreIds.push(FALLBACK_VECTOR_STORE_ID);
  }
}

assertSdkReady();

const tools = vectorStoreIds.length ? [fileSearchTool(vectorStoreIds)] : [];

const agentName = process.env.MCQ_AGENT_NAME?.trim() || "Dr. NeuroConsult";
const agentModel = process.env.MCQ_AGENT_MODEL?.trim() || "gpt-5-mini";

const knowledgeSourceIntro = vectorStoreIds.length
  ? `Primary sources live in the attached vector store${
      vectorStoreIds.length > 1 ? "s" : ""
    } (${vectorStoreIds.join(", ")}).`
  : "Vector store retrieval is currently disabled; rely on built-in corpus only.";

const agentInstructions = `ROLE
You are ${agentName}, a board-certified neurologist across all subspecialties and an educator preparing residents for board exams. Always deliver evidence-based, guideline-aligned answers.

SCOPE
Handle two input types:
1) Free-Ask neurology questions (diagnosis, management, anatomy, counseling, prognosis, localization).
2) MCQ questions with stem and options; the correct answer may or may not be supplied.

KNOWLEDGE SOURCES
${knowledgeSourceIntro}
- Continuum (by subspecialty and year)
- Bradley Neurology 8e
- Merritt’s Neurology
- Rowan’s Primer
- Blumenfeld (Neuroanatomy Through Clinical Cases)
- DeMyer’s The Neurologic Examination
- Grotta Stroke
- Merged stroke/vascular guidelines
- Neuroanesthesia and Neurocritical Care texts
- AAO BCSC Section 6
- Other subspecialty monographs present in the store
Prefer files whose title + subspecialty + YEAR best match the question. Prefer the most recent edition/volume available. Never invent citations. If retrieval yields nothing relevant, say: “No vector source found for this query.”

TOOLS
Always use the \`file_search\` tool before answering when it is available. Issue 2–4 targeted queries per topic. If initial retrieval lacks relevance, iterate. Synthesize only from retrieved passages. Cross-check for concordance. Flag conflicts or gaps.

RECENCY CHECK — ALWAYS VERIFY LATEST UPDATES
Before finalizing any answer, confirm that at least one retrieved source is the most recent available in the store for that subspecialty (e.g., Continuum 2024/2025 volumes, latest guideline revisions, newest RCTs/meta-analyses).
- If newer data update diagnostic criteria, lab tests/biomarkers, MRI/EDX patterns, or management principles, reflect these changes and cite the newest source.
- If no recent source is retrieved, run an additional targeted query using recency terms (e.g., “2024”, “2025”, “update”, “revision”, “criteria”, “guideline”, “trial”, “meta-analysis”).
- If you suspect newer guidance exists but it is not in the store, state: “Potential newer update beyond corpus—upload needed.”
- END-ONLY AUGMENTATION: You may add your own knowledge strictly for a final recency sanity check **at the very end only** under a separate section titled **“Outside-vector recency notes (verbatim log)”**. Do **not** intermix such content in the main body. Keep to 1–5 bullets. Each bullet must:
  • Be clearly labeled OV1, OV2, …
  • Be written verbatim as inserted (no paraphrase later).
  • Start with “Unverified—outside vector corpus:” and then the claim.
  • Avoid dosing/threshold specifics unless also supported by a retrieved source.
  • Include a one-line action prompt if relevant, e.g., “Upload 2025 guideline PDF to confirm.”

REGIONAL PREFERENCE
When guidelines conflict, prioritize the region if specified by the user. Otherwise prefer AAN, AHA/ASA, ESO/EAN, NICE, Health Canada, SFDA in that order.

DIAGNOSTIC MODE — MANDATORY WHEN THE TASK INVOLVES DIAGNOSIS (applies to both Free-Ask and MCQ)
When the user asks a diagnostic question or the stem requires identifying a disease, ALWAYS:
1) Name the official diagnostic criteria set(s) with issuing body and year.
2) Confirm the latest version. If multiple versions exist, state which is current and whether older versions are superseded.
3) Label type: Clinical guideline/endorsed vs Research/classification vs Consensus. Note region if applicable.
4) Present the criteria explicitly:
   - Elements: required, supportive, exclusions/red flags.
   - Threshold or scoring rules: points, counts, dissemination rules, or tiered certainty (definite/probable/possible).
   - Scenario pathways: distinct routes to diagnosis (clinical + imaging; biomarker; genetics; biopsy/EDX) and when each applies.
   - Test performance if available: sensitivity, specificity, LR+, LR−, 95% CI, key caveats.
5) Align reasoning to criteria: state which elements the case meets, which are unmet or uncertain, and what would confirm or refute.
6) State clearly whether the diagnosis is clinical practice criteria vs research/classification only, and which should be used for the patient context.

CONCISION AND EVIDENCE
Keep answers concise. Include effect sizes when available (RR/OR/HR, ARR, NNT/NNH, 95% CI). Use bracketed inline citations after claims, for example:
[Continuum: Cerebrovascular Disease, 2024, p.37], [AAN Guideline, 2023, sec 3.2].
Provide full AMA references at the end. Note regional differences when relevant.

OUTPUT FORMAT (Non-MCQ) — no initial summary
1) Direct answer: one or two sentences.
2) Clinical reasoning: one short paragraph.
   - If diagnostic: include a “Criteria check” line listing criteria name, year, type; elements met; threshold/score achieved; and pathway used. Note if this reflects the latest version.
3) Diagnostics — Algorithm: compact numbered flow (3–8 steps).
   - Include a “Criteria box” listing formal criteria elements and thresholds with issuing body and year; indicate if confirmed as latest.
   - Include synonyms/eponyms for imaging or signs when helpful.
   - Include “Alternative pathways” (genetics vs biopsy vs biomarker) and whether each yields a clinical vs research diagnosis.
4) Management — Evidence-first:
   - Evidence base: RCTs/meta-analyses and guideline strength/grade with effect sizes. Confirm inclusion of the latest trials/guideline revisions available in the store.
   - Consensus/practice: what experts do when evidence is limited.
   - Harms/contraindications: NNH, bleeding risk, drug–disease cautions, “do-nots.”
5) Key pearls: 3–5 board-style bullets.
6) Sources: full AMA references, with the most recent source in each category clearly identified.
7) Outside-vector recency notes (verbatim log): OPTIONAL. Include only if OV items exist. List OV1…OVn exactly as written.

OUTPUT FORMAT (MCQ)
Two sections only; no initial summary.
1) Option analysis
   - State the correct option with a one-sentence justification.
   - For each other option, give a one-line elimination with the key discriminant and a citation.
   - If diagnostic: add a “Criteria check” under the correct option showing criteria name, year, type, threshold/score, the scenario pathway used, and confirm it is the latest version; state why alternatives fail their criteria.
2) Brief overview (≤4 short paragraphs, tailored to the stem)
   - Paragraph 1: Foundations. Core pathophysiology, defining clinical features, prognosis, first principles of management. If diagnostic: name the criteria set(s), year, type; summarize threshold/score and main pathways; confirm latest version.
   - Paragraph 2: Diagnostic algorithm. 3–6 numbered steps inline. Include tests, thresholds, pathognomonic signs with synonyms/eponyms, and whether each pathway yields a clinical vs research diagnosis; indicate latest revisions if applicable.
   - Paragraphs 3–4: Management focus. Start with Evidence base (trial names, guideline sections, effect sizes), explicitly confirming the latest available updates; then Consensus/practice where evidence is limited. Include Harms/contraindications with NNH or key risks. Briefly note regional differences if applicable.
   - End with: Outside-vector recency notes (verbatim log) — OPTIONAL. Include only if OV items exist. List OV1…OVn exactly as written.

OUTPUT DELIVERY
Return a single-line JSON object of the form {"explanation": "..."}. The value must contain the fully formatted answer described above. Do not emit Markdown fences or extraneous keys. If unable to comply, state “No vector source found for this query.”

GUARDRAILS
- If \`file_search\` returns no relevant passages, output: “No vector source found for this query.” Stop or ask for a better query/upload.
- Outside-vector notes must be segregated at the end, cannot change core recommendations without corpus support, and must avoid dosing/threshold specifics unless corroborated by retrieved sources.
- No PHI. No Wikipedia.
- Adapt recommendations to patient factors and institutional policies.
- Do not speculate beyond retrieved evidence.
- Be concise, professional, and emotionless.
`;

const drNeuroconsult = new Agent({
  name: agentName,
  instructions: agentInstructions,
  model: agentModel,
  tools,
  modelSettings: {
    reasoning: {
      effort: "high",
      summary: "auto"
    },
    store: true
  }
});

const STDIN_SIZE_LIMIT = Number.parseInt(
  process.env.MCQ_AGENT_MAX_INPUT_BYTES || "1048576",
  10
);
const PROMPT_CHAR_LIMIT = Number.parseInt(
  process.env.MCQ_AGENT_MAX_PROMPT_CHARS || "65000",
  10
);
const EXPLANATION_CHAR_LIMIT = Number.parseInt(
  process.env.MCQ_AGENT_MAX_EXPLANATION_CHARS || "65000",
  10
);
const RAW_OUTPUT_LIMIT = Number.parseInt(
  process.env.MCQ_AGENT_MAX_RAW_OUTPUT_CHARS || "120000",
  10
);

const PRIORITY_KEYS = [
  "explanation",
  "content",
  "text",
  "output",
  "output_text",
  "value",
  "message",
  "answer",
  "response"
];

export const safeJsonParse = value => {
  if (typeof value !== "string") {
    return null;
  }
  try {
    return JSON.parse(value);
  } catch (error) {
    return null;
  }
};

export const readStdin = (stream = process.stdin, limit = STDIN_SIZE_LIMIT) =>
  new Promise((resolve, reject) => {
    let data = "";
    let settled = false;

    const closeWithError = error => {
      if (settled) {
        return;
      }
      settled = true;
      reject(error);
    };

    stream.setEncoding("utf8");
    stream.on("data", chunk => {
      if (settled) {
        return;
      }
      data += chunk;
      if (data.length > limit) {
        closeWithError(
          new Error(
            `Input payload exceeded maximum size of ${limit.toLocaleString()} characters`
          )
        );
        stream.pause();
      }
    });
    stream.once("end", () => {
      if (!settled) {
        settled = true;
        resolve(data);
      }
    });
    stream.once("error", closeWithError);
  });

const sanitizeText = value =>
  value
    .replace(/\u0000/g, " ")
    .replace(/\r\n/g, "\n")
    .trim();

const truncate = (value, maxLength) =>
  value.length > maxLength ? value.slice(0, maxLength) : value;

export const extractExplanation = (
  raw,
  { maxLength = EXPLANATION_CHAR_LIMIT } = {}
) => {
  if (raw == null) {
    return "";
  }

  const queue = [raw];
  const visited = new Set();

  while (queue.length) {
    const current = queue.shift();

    if (current == null) {
      continue;
    }

    if (typeof current === "string") {
      const trimmed = sanitizeText(current);
      if (!trimmed) {
        continue;
      }

      const parsed = safeJsonParse(trimmed);
      if (parsed && parsed !== current) {
        queue.unshift(parsed);
        continue;
      }

      return truncate(trimmed, maxLength);
    }

    if (typeof current === "number" || typeof current === "boolean") {
      const textValue = sanitizeText(String(current));
      if (textValue) {
        return truncate(textValue, maxLength);
      }
      continue;
    }

    if (typeof current === "object") {
      if (visited.has(current)) {
        continue;
      }
      visited.add(current);

      if (Array.isArray(current)) {
        queue.unshift(...current);
        continue;
      }

      for (const key of PRIORITY_KEYS) {
        if (key in current) {
          queue.unshift(current[key]);
        }
      }

      for (const value of Object.values(current)) {
        if (value == null) {
          continue;
        }
        if (
          typeof value === "string" ||
          typeof value === "number" ||
          typeof value === "boolean"
        ) {
          queue.push(value);
        } else if (typeof value === "object") {
          queue.push(value);
        }
      }
    }
  }

  return "";
};

export const ensureJsonExplanation = raw => {
  const explanation = extractExplanation(raw);
  return explanation || null;
};

const safeSerialize = value => {
  if (typeof value === "string") {
    return value;
  }
  if (value == null) {
    return "";
  }
  try {
    return JSON.stringify(value);
  } catch (error) {
    return String(value);
  }
};

const clampRawOutput = value => truncate(value, RAW_OUTPUT_LIMIT);

const buildConversationHistory = prompt => [
  {
    role: "user",
    content: [
      {
        type: "input_text",
        text: prompt
      }
    ]
  }
];

const parsePayload = input => {
  const payload = safeJsonParse(input);
  if (!payload || typeof payload !== "object" || Array.isArray(payload)) {
    throw new Error("Input payload must be a JSON object");
  }

  const prompt = typeof payload.prompt === "string" ? payload.prompt.trim() : "";
  if (!prompt) {
    throw new Error("Input payload missing 'prompt'");
  }

  if (prompt.length > PROMPT_CHAR_LIMIT) {
    throw new Error(
      `Prompt length ${prompt.length.toLocaleString()} exceeds limit of ${PROMPT_CHAR_LIMIT.toLocaleString()} characters`
    );
  }

  const workflowId =
    typeof payload.workflow_id === "string" && payload.workflow_id.trim()
      ? payload.workflow_id.trim()
      : "wf_explanation";

  const context =
    payload.context && typeof payload.context === "object" ? payload.context : undefined;

  return { prompt, workflowId, context };
};

const normaliseTraceMetadata = context => {
  if (!context || typeof context !== "object") {
    return {};
  }

  const metadata = {};
  for (const [key, value] of Object.entries(context)) {
    if (!key) {
      continue;
    }
    if (value == null) {
      continue;
    }
    if (typeof value === "string") {
      metadata[key] = value;
    } else if (typeof value === "number" || typeof value === "boolean") {
      metadata[key] = String(value);
    }
  }
  return metadata;
};

const runAgent = async (prompt, workflowId, context) => {
  assertSdkReady();
  const runnerOptions = {
    traceMetadata: {
      __trace_source__: "agent-runner",
      workflow_id: workflowId,
      ...normaliseTraceMetadata(context)
    }
  };

  const runner = new Runner(runnerOptions);
  const conversationHistory = buildConversationHistory(prompt);

  const response = await withTrace("Explanation edit", async () =>
    runner.run(drNeuroconsult, conversationHistory)
  );

  if (response && typeof response === "object") {
    if (
      "error" in response &&
      response.error &&
      typeof response.error === "object" &&
      typeof response.error.message === "string"
    ) {
      throw new Error(response.error.message);
    }
    if ("status" in response && response.status === "errored") {
      const detail =
        typeof response.error === "string"
          ? response.error
          : typeof response.error?.message === "string"
          ? response.error.message
          : "Agent run failed";
      throw new Error(detail);
    }
  }

  const finalOutput =
    response?.finalOutput ??
    response?.output ??
    (typeof response === "string" ? response : "");

  return finalOutput;
};

export const main = async () => {
  const stdin = await readStdin();
  if (!stdin) {
    throw new Error("No input provided to agent runner");
  }

  const { prompt, workflowId, context } = parsePayload(stdin);
  const finalOutput = await runAgent(prompt, workflowId, context);
  const explanation = ensureJsonExplanation(finalOutput);

  if (!explanation) {
    throw new Error("Agent returned empty explanation");
  }

  const raw = clampRawOutput(safeSerialize(finalOutput));
  process.stdout.write(JSON.stringify({ explanation, raw }) + "\n");
};

const emitError = error => {
  const message = error instanceof Error ? error.message : String(error);
  process.stderr.write(JSON.stringify({ error: message }) + "\n");
};

const isCliInvocation = () => {
  const entry = process.argv[1];
  if (!entry) {
    return false;
  }
  return import.meta.url === pathToFileURL(entry).href;
};

process.on("unhandledRejection", reason => {
  emitError(reason);
  process.exitCode = 1;
});

process.on("uncaughtException", error => {
  emitError(error);
  process.exitCode = 1;
});

if (isCliInvocation()) {
  try {
    await main();
  } catch (error) {
    emitError(error);
    process.exitCode = 1;
  }
}
