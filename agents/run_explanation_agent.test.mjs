import test from "node:test";
import assert from "node:assert/strict";
import { Readable } from "node:stream";

globalThis.__MCQ_OPENAI_AGENTS__ = {
  Agent: class Agent {
    constructor(config) {
      Object.assign(this, config);
    }
  },
  fileSearchTool: () => ({}),
  Runner: class Runner {
    constructor(options) {
      this.options = options;
    }

    async run() {
      return { finalOutput: '{"explanation":"stub"}' };
    }
  },
  withTrace: async (_label, fn) => fn()
};

const modulePromise = import("./run_explanation_agent.js");
const {
  extractExplanation,
  ensureJsonExplanation,
  readStdin,
  safeJsonParse
} = await modulePromise;

test("extractExplanation returns text from JSON string", () => {
  const raw = '{"explanation": "Final answer"}';
  const result = extractExplanation(raw);
  assert.equal(result, "Final answer");
});

test("extractExplanation returns text from nested object", () => {
  const raw = {
    output: [{
      content: "  Nested explanation  "
    }]
  };
  const result = extractExplanation(raw);
  assert.equal(result, "Nested explanation");
});

test("extractExplanation trims and truncates long values", () => {
  const raw = "   " + "a".repeat(10) + "  ";
  const result = extractExplanation(raw, { maxLength: 5 });
  assert.equal(result, "aaaaa");
});

test("extractExplanation handles boolean fallbacks", () => {
  const raw = { status: true };
  const result = extractExplanation(raw);
  assert.equal(result, "true");
});

test("ensureJsonExplanation falls back to null when empty", () => {
  const result = ensureJsonExplanation({});
  assert.equal(result, null);
});

test("safeJsonParse returns null on invalid payload", () => {
  const result = safeJsonParse("not-json");
  assert.equal(result, null);
});

test("readStdin resolves with collected text", async () => {
  const stream = Readable.from(["hello"]);
  const result = await readStdin(stream, 10);
  assert.equal(result, "hello");
});

test("readStdin rejects when payload exceeds limit", async () => {
  const stream = Readable.from(["excess"]);
  await assert.rejects(() => readStdin(stream, 3), {
    message: /exceeded maximum size/
  });
});

test("ensureJsonExplanation reads explanation key from object", () => {
  const raw = { explanation: "Structured" };
  const result = ensureJsonExplanation(raw);
  assert.equal(result, "Structured");
});

test("ensureJsonExplanation reads explanation from JSON string with content field", () => {
  const raw = '{"content": "Value"}';
  const result = ensureJsonExplanation(raw);
  assert.equal(result, "Value");
});
