import { test, expect } from '@playwright/test';

test('login page renders for anonymous users', async ({ page }) => {
  const response = await page.goto('/login/');
  expect(response?.status()).toBe(200);
  await expect(page.getByRole('heading', { name: 'Login' })).toBeVisible();
  await expect(page.getByRole('button', { name: 'Login' })).toBeEnabled();
});

test('dashboard redirects anonymous users to login', async ({ page }) => {
  await page.goto('/dashboard/');
  await page.waitForURL('**/login/**', { waitUntil: 'domcontentloaded' });
  expect(page.url()).toContain('/login/');
  await expect(page.getByRole('heading', { name: 'Login' })).toBeVisible();
});
