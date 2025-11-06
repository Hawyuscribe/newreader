import { defineConfig, devices } from '@playwright/test';

const baseURL =
  process.env.PLAYWRIGHT_BASE_URL?.replace(/\/$/, '') ?? 'http://127.0.0.1:8000';

const webServerCommand = process.env.PLAYWRIGHT_WEB_SERVER_COMMAND;
const webServerPort = Number.parseInt(
  process.env.PLAYWRIGHT_WEB_SERVER_PORT ?? '8000',
  10
);

export default defineConfig({
  testDir: 'playwright/tests',
  timeout: 60_000,
  expect: {
    timeout: 10_000,
  },
  fullyParallel: true,
  forbidOnly: Boolean(process.env.CI),
  retries: process.env.CI ? 1 : 0,
  workers: process.env.CI ? 2 : undefined,
  reporter: process.env.CI ? [['list'], ['html']] : [['list']],
  use: {
    baseURL,
    trace: 'on-first-retry',
    video: 'retain-on-failure',
    screenshot: 'only-on-failure',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
  ],
  webServer: webServerCommand
    ? {
        command: webServerCommand,
        port: webServerPort,
        reuseExistingServer: !process.env.CI,
        timeout: 180_000,
      }
    : undefined,
});
