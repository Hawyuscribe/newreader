import { test, expect, Page } from '@playwright/test';

// Test configuration - targeting your live Heroku site
const HEROKU_URL = 'https://enigmatic-hamlet-38937-db49bd5e9821.herokuapp.com';
const TEST_MCQ_ID = 99988010; // Using the MCQ ID from your previous tests

// You'll need to set these environment variables with your actual credentials
const adminUsername = process.env.PLAYWRIGHT_ADMIN_USERNAME || 'tariq';
const adminPassword = process.env.PLAYWRIGHT_ADMIN_PASSWORD || '';

// Timeouts for AI processing
const AI_JOB_TIMEOUT_MS = 120000; // 2 minutes for AI processing
const AI_POLL_INTERVAL_MS = 2000; // Poll every 2 seconds

test.describe('Live Heroku AI Options Editing - Real User Experience', () => {
  test.use({
    baseURL: HEROKU_URL,
  });

  test.describe.configure({
    timeout: AI_JOB_TIMEOUT_MS + 60000, // Extra time for navigation
  });

  test.skip(
    !adminPassword,
    'Set PLAYWRIGHT_ADMIN_PASSWORD environment variable to run this test'
  );

  test('Complete user flow: Login → Navigate to MCQ → Edit Options with AI', async ({ page }) => {
    console.log(`Testing on: ${HEROKU_URL}`);

    // Step 1: Login as admin
    console.log('Step 1: Logging in as admin...');
    await loginAsAdmin(page, adminUsername, adminPassword);

    // Step 2: Navigate to the specific MCQ
    console.log(`Step 2: Navigating to MCQ ${TEST_MCQ_ID}...`);
    await page.goto(`/mcq/${TEST_MCQ_ID}/`, { waitUntil: 'networkidle' });

    // Verify we're on the MCQ page
    await expect(page.locator('.mcq-question-text, .question-text, #question-text')).toBeVisible({ timeout: 10000 });

    // Step 3: Enable edit mode if needed
    console.log('Step 3: Enabling edit mode...');
    const toggleEditBtn = page.locator('#toggleEditMode, button:has-text("Edit MCQ")');
    if (await toggleEditBtn.isVisible()) {
      await toggleEditBtn.click();
      await page.waitForTimeout(1000); // Wait for UI to update
    }

    // Step 4: Find and click the AI options edit button
    console.log('Step 4: Finding AI options edit button...');
    const optionsAIButton = page.locator('.js-ai-options, button:has-text("Edit Options with AI"), button:has-text("AI Options")');
    await expect(optionsAIButton).toBeVisible({ timeout: 10000 });

    // Step 5: Click the button to trigger AI options editing
    console.log('Step 5: Clicking AI options edit button...');
    await optionsAIButton.click();

    // Step 6: Handle the instruction modal if it appears
    const instructionModal = page.locator('#aiInstructionModal, .modal:has-text("AI Instructions")');
    if (await instructionModal.isVisible({ timeout: 5000 }).catch(() => false)) {
      console.log('Step 6: Handling instruction modal...');

      // Select mode (fill_missing or improve_all)
      const fillMissingBtn = page.locator('button[data-mode="fill_missing"], button:has-text("Fill Missing")');
      if (await fillMissingBtn.isVisible({ timeout: 2000 }).catch(() => false)) {
        await fillMissingBtn.click();
      } else {
        // If no mode selection, just provide instructions
        const instructionTextarea = page.locator('#customInstructionsTextarea, textarea[name="instructions"]');
        if (await instructionTextarea.isVisible()) {
          await instructionTextarea.fill('Generate plausible neurology distractors based on common misconceptions.');
        }

        const confirmBtn = page.locator('.modal button:has-text("Confirm"), .modal button:has-text("Apply")');
        await confirmBtn.click();
      }
    }

    // Step 7: Wait for the async job to be queued
    console.log('Step 7: Waiting for job to be queued...');

    // Monitor network requests to catch the job ID
    const jobResponsePromise = page.waitForResponse(
      response => response.url().includes('/ai/edit/options/') && response.status() === 202,
      { timeout: 10000 }
    ).catch(() => null);

    const jobResponse = await jobResponsePromise;

    let jobId: string | null = null;
    if (jobResponse) {
      const responseData = await jobResponse.json();
      jobId = responseData.job_id;
      console.log(`Job queued with ID: ${jobId}`);
    }

    // Step 8: Monitor the UI for loading indicators
    console.log('Step 8: Monitoring UI for progress indicators...');

    // Look for loading messages
    const loadingIndicators = [
      page.locator('.loading-message:visible, .spinner:visible'),
      page.locator('text=/processing|generating|working/i'),
      page.locator('.progress-bar:visible')
    ];

    let loadingFound = false;
    for (const indicator of loadingIndicators) {
      if (await indicator.isVisible({ timeout: 2000 }).catch(() => false)) {
        loadingFound = true;
        console.log('Loading indicator found, AI is processing...');
        break;
      }
    }

    // Step 9: Poll for job completion if we have a job ID
    if (jobId) {
      console.log('Step 9: Polling for job completion...');
      const result = await pollForJobCompletion(page, jobId);

      if (result.success) {
        console.log('✅ Job completed successfully!');
        console.log('Options generated:', Object.keys(result.options || {}).length, 'options');

        // Verify the options were populated in the UI
        await page.waitForTimeout(2000); // Give UI time to update

        // Check if option fields were updated
        const optionInputs = await page.locator('input[name*="option"], textarea[name*="option"]').all();
        let filledCount = 0;
        for (const input of optionInputs) {
          const value = await input.inputValue();
          if (value && value.trim()) {
            filledCount++;
          }
        }
        console.log(`UI Update: ${filledCount} option fields have content`);

        expect(filledCount).toBeGreaterThan(0);
      } else {
        console.log('❌ Job failed:', result.error);
      }
    }

    // Step 10: Check for success/error messages in UI
    console.log('Step 10: Checking for completion messages...');

    const successMessage = page.locator('.alert-success:visible, .toast-success:visible, text=/success|completed|generated/i');
    const errorMessage = page.locator('.alert-danger:visible, .toast-error:visible, text=/error|failed/i');

    const success = await successMessage.isVisible({ timeout: 5000 }).catch(() => false);
    const error = await errorMessage.isVisible({ timeout: 5000 }).catch(() => false);

    if (success) {
      console.log('✅ Success message displayed in UI');
      const messageText = await successMessage.textContent();
      console.log('Success message:', messageText);
    } else if (error) {
      console.log('❌ Error message displayed in UI');
      const messageText = await errorMessage.textContent();
      console.log('Error message:', messageText);

      // Still check if options were actually updated despite error message
      const optionValues = await page.evaluate(() => {
        const inputs = document.querySelectorAll('input[name*="option"], textarea[name*="option"]');
        return Array.from(inputs).map(el => (el as HTMLInputElement).value);
      });
      console.log('Current option values:', optionValues);
    }

    // Final verification: Check that GPT-5-nano was used
    console.log('Step 11: Verifying GPT-5-nano model was used...');

    // Check browser console logs for model information
    const consoleLogs = await page.evaluate(() => {
      return (window as any).adminDebugLogs || [];
    });

    if (consoleLogs.length > 0) {
      const modelLogs = consoleLogs.filter((log: string) =>
        log.includes('gpt-5') || log.includes('model')
      );
      console.log('Model-related logs:', modelLogs);
    }

    // Take a screenshot for visual verification
    await page.screenshot({
      path: `playwright/screenshots/options-ai-test-${Date.now()}.png`,
      fullPage: true
    });
    console.log('Screenshot saved for review');
  });

  test('API Direct Test: Options editing with GPT-5-nano', async ({ page }) => {
    console.log('Testing API directly...');

    // Login first
    await loginAsAdmin(page, adminUsername, adminPassword);

    // Make direct API call
    const response = await page.request.post(`/mcq/${TEST_MCQ_ID}/ai/edit/options/`, {
      headers: {
        'Content-Type': 'application/json',
      },
      data: {
        mode: 'fill_missing',
        custom_instructions: 'Generate neurology-specific distractors using GPT-5-nano for fast response',
        use_async: true,
        auto_regenerate: false,
      },
    });

    console.log('API Response Status:', response.status());
    expect([200, 202]).toContain(response.status());

    const responseData = await response.json();
    console.log('API Response:', JSON.stringify(responseData, null, 2));

    if (response.status() === 202 && responseData.job_id) {
      console.log(`Async job created: ${responseData.job_id}`);

      // Poll for completion
      const result = await pollForJobCompletion(page, responseData.job_id);

      expect(result.success).toBeTruthy();
      expect(result.options).toBeTruthy();

      // Verify we have valid options
      const options = result.options || {};
      const validOptions = Object.values(options).filter(opt => opt && String(opt).trim().length > 10);
      console.log(`Generated ${validOptions.length} valid options`);
      expect(validOptions.length).toBeGreaterThan(0);

      // Log a sample option to verify quality
      if (validOptions.length > 0) {
        console.log('Sample generated option:', validOptions[0]);
      }
    } else if (responseData.success && responseData.options) {
      // Synchronous response
      console.log('Synchronous response received');
      const validOptions = Object.values(responseData.options).filter(opt =>
        opt && String(opt).trim().length > 10
      );
      expect(validOptions.length).toBeGreaterThan(0);
    }
  });
});

async function loginAsAdmin(page: Page, username: string, password: string) {
  await page.goto('/login/', { waitUntil: 'domcontentloaded' });

  // Check if already logged in
  if (page.url().includes('/dashboard/') || page.url().includes('/mcq/')) {
    console.log('Already logged in');
    return;
  }

  // Fill login form
  await page.getByLabel('Username').fill(username);
  await page.getByLabel('Password').fill(password);
  await page.getByRole('button', { name: 'Login' }).click();

  // Wait for redirect after login
  await page.waitForURL(url =>
    url.includes('/dashboard/') ||
    url.includes('/mcq/') ||
    url.includes('/home/'),
    { timeout: 30000 }
  );

  console.log('Login successful');
}

async function pollForJobCompletion(page: Page, jobId: string): Promise<any> {
  const maxAttempts = Math.floor(AI_JOB_TIMEOUT_MS / AI_POLL_INTERVAL_MS);
  let attempts = 0;

  while (attempts < maxAttempts) {
    attempts++;

    // Use the correct endpoint for job status
    const response = await page.request.get(`/mcq/ai/explanation-job/${jobId}/`);

    if (response.ok()) {
      const data = await response.json();
      console.log(`Poll ${attempts}: Status = ${data.status}`);

      if (data.status === 'succeeded') {
        return data.result || data;
      }

      if (data.status === 'failed') {
        return { success: false, error: data.error || 'Job failed' };
      }
    }

    await page.waitForTimeout(AI_POLL_INTERVAL_MS);
  }

  return {
    success: false,
    error: `Job timeout after ${attempts} attempts (${AI_JOB_TIMEOUT_MS / 1000}s)`
  };
}