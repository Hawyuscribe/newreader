import { test, expect, Page } from '@playwright/test';

const adminUsername = process.env.PLAYWRIGHT_ADMIN_USERNAME;
const adminPassword = process.env.PLAYWRIGHT_ADMIN_PASSWORD;
const explicitMcqId = process.env.PLAYWRIGHT_MCQ_ID
  ? Number.parseInt(process.env.PLAYWRIGHT_MCQ_ID, 10)
  : undefined;

const aiJobTimeoutMs =
  Number.parseInt(process.env.PLAYWRIGHT_AI_TIMEOUT_MS ?? '', 10) || 600_000;
const aiJobPollIntervalMs =
  Number.parseInt(process.env.PLAYWRIGHT_AI_POLL_MS ?? '', 10) || 5_000;

test.describe('Admin AI editing flows', () => {
  test.describe.configure({
    timeout: aiJobTimeoutMs + 60_000,
  });

  test.skip(
    ({ browserName }) => browserName !== 'chromium',
    'AI editing integration tests run on Chromium only to keep run duration manageable.'
  );

  test.skip(
    !adminUsername || !adminPassword,
    'Set PLAYWRIGHT_ADMIN_USERNAME and PLAYWRIGHT_ADMIN_PASSWORD to run admin AI tests.'
  );

  test('question edit endpoint queues job or reports missing AI config', async ({ page }) => {
    await loginAsAdmin(page, adminUsername!, adminPassword!);
    const mcqId = await resolveTargetMcqId(page);

    const response = await page.request.post(`/mcq/${mcqId}/ai/edit/question/`, {
      headers: {
        'Content-Type': 'application/json',
      },
      data: {
        custom_instructions: 'Trim verbosity and highlight the key clinical clue.',
      },
    });

    expect([200, 202, 503]).toContain(response.status());
    const payload = await response.json();

    if (response.status() === 503) {
      expect(payload.success ?? false).toBeFalsy();
      expect(String(payload.error)).toMatch(/OpenAI|Celery|Redis/i);
    } else if (response.status() === 202) {
      expect(payload.success).toBeTruthy();
      expect(payload.job_id).toBeTruthy();
      const job = await verifyJobStatus(page, payload.job_id);
      expect(job.result?.success).toBeTruthy();
      const improved = String(job.result?.improved_text ?? '').trim();
      expect(improved.length).toBeGreaterThan(100);
    } else {
      expect(payload.success).toBeTruthy();
      const improved = String(payload.improved_text ?? '').trim();
      expect(improved.length).toBeGreaterThan(100);
    }
  });

  test('options edit endpoint accepts payload', async ({ page }) => {
    await loginAsAdmin(page, adminUsername!, adminPassword!);
    const mcqId = await resolveTargetMcqId(page);

    const response = await page.request.post(`/mcq/${mcqId}/ai/edit/options/`, {
      headers: {
        'Content-Type': 'application/json',
      },
      data: {
        mode: 'fill_missing',
        custom_instructions: 'Ensure distractors target common neurology misconceptions.',
        question_text:
          'A 45-year-old patient presents with progressive neurological symptoms consistent with demyelinating disease.',
        auto_regenerate_explanations: false,
        auto_apply: false,
      },
    });

    expect([200, 202, 503]).toContain(response.status());
    const payload = await response.json();

    if (response.status() === 503) {
      expect(payload.success ?? false).toBeFalsy();
      expect(String(payload.error)).toMatch(/OpenAI|Celery|Redis/i);
    } else if (response.status() === 202) {
      expect(payload.success).toBeTruthy();
      expect(payload.job_id).toBeTruthy();
      const job = await verifyJobStatus(page, payload.job_id);
      expect(job.result?.success).toBeTruthy();
      expect(job.result?.options).toBeTruthy();
    } else {
      expect(payload.success).toBeTruthy();
      expect(payload.options).toBeTruthy();
    }
  });

  test('explanation edit endpoint queues job with section metadata', async ({ page }) => {
    await loginAsAdmin(page, adminUsername!, adminPassword!);
    const mcqId = await resolveTargetMcqId(page);

    const sectionName = 'key_points';
    const response = await page.request.post(`/mcq/${mcqId}/ai/edit/explanation/`, {
      headers: {
        'Content-Type': 'application/json',
      },
      data: {
        section_name: sectionName,
        current_content: 'Existing explanation fragment used for smoke testing.',
        custom_instructions: 'Focus on diagnostic pearls and red flags.',
        mode: 'enhance',
      },
    });

    expect([200, 202, 500, 503]).toContain(response.status());
    const payload = await response.json();

    if (response.status() === 503) {
      expect(payload.success ?? false).toBeFalsy();
      expect(String(payload.error)).toMatch(/OpenAI|Celery|Redis/i);
    } else if (response.status() === 500) {
      expect(payload.success ?? false).toBeFalsy();
      expect(String(payload.error)).toMatch(/AI|agent|retry|redis|connection/i);
    } else if (response.status() === 202) {
      expect(payload.success).toBeTruthy();
      expect(payload.job_id).toBeTruthy();
      expect(payload.section_name).toBe(sectionName);
      const job = await verifyJobStatus(page, payload.job_id);
      expect(job.result?.success).toBeTruthy();
      const enhanced = String(job.result?.enhanced_content ?? '').trim();
      expect(enhanced.length).toBeGreaterThan(200);
      expect(job.result?.section_name).toBe(sectionName);
    } else {
      expect(payload.success).toBeTruthy();
      expect(payload.section_name).toBe(sectionName);
      const enhanced = String(payload.enhanced_content ?? '').trim();
      expect(enhanced.length).toBeGreaterThan(200);
    }
  });
});

async function loginAsAdmin(page: Page, username: string, password: string) {
  await page.goto('/dashboard/', { waitUntil: 'domcontentloaded' });

  if (page.url().includes('/dashboard/')) {
    return;
  }

  await page.goto('/login/', { waitUntil: 'domcontentloaded' });
  await expect(page.getByRole('heading', { name: 'Login' })).toBeVisible();
  await page.getByLabel('Username').fill(username);
  await page.getByLabel('Password').fill(password);
  await page.getByRole('button', { name: 'Login' }).click();
  await page.waitForURL('**/dashboard/**', {
    timeout: 30_000,
    waitUntil: 'domcontentloaded',
  });
  await expect(page.locator('#mockExamModalLabel')).toContainText(
    'Mock Examination'
  );
}

async function resolveTargetMcqId(page: Page): Promise<number> {
  if (explicitMcqId && Number.isFinite(explicitMcqId)) {
    return explicitMcqId;
  }

  const response = await page.request.get('/debug/mcq-ids/');

  expect(response.ok()).toBeTruthy();
  const payload = await response.json();

  const candidates: Array<{ id: number; question?: string }> = [];

  const samples = payload?.neuro_infectious_samples;
  if (Array.isArray(samples)) {
    for (const item of samples) {
      if (!item || typeof item.id !== 'number') continue;
      const text = typeof item.question_text === 'string' ? item.question_text : '';
      candidates.push({ id: item.id, question: text });
    }
  }

  const fromStats = payload?.id_range;
  if (fromStats?.max_id) {
    candidates.push({ id: Number(fromStats.max_id) });
  }
  if (fromStats?.min_id) {
    candidates.push({ id: Number(fromStats.min_id) });
  }

  let picked =
    candidates.find(
      (item) => (item.question ?? '').split(/\s+/).filter(Boolean).length >= 40
    ) ?? null;

  if (!picked && candidates.length > 0) {
    picked = candidates.reduce((best, current) => {
      const score = (current.question ?? '').split(/\s+/).filter(Boolean).length;
      const bestScore = (best.question ?? '').split(/\s+/).filter(Boolean).length;
      return score > bestScore ? current : best;
    });
  }

  if (!picked) {
    throw new Error('Unable to determine an MCQ ID for AI editing tests.');
  }

  return Number(picked.id);
}

async function verifyJobStatus(page: Page, jobId: string) {
  const deadline = Date.now() + aiJobTimeoutMs;
  let payload: any | undefined;

  while (Date.now() < deadline) {
    const response = await page.request.get(`/mcq/ai/jobs/${jobId}/`);
    expect(response.status()).toBe(200);
    payload = await response.json();
    expect(payload.job_id).toBe(jobId);

    if (!['pending', 'running'].includes(String(payload.status))) {
      break;
    }

    await page.waitForTimeout(aiJobPollIntervalMs);
  }

  if (!payload || ['pending', 'running'].includes(String(payload.status))) {
    throw new Error(
      `AI job ${jobId} did not finish within ${aiJobTimeoutMs / 1000}s (last status: ${
        payload?.status ?? 'unknown'
      })`
    );
  }

  expect(payload.status).not.toBe('failed');
  return payload;
}
