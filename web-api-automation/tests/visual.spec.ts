import { test, expect } from '@playwright/test';

test('inventory page visual baseline', async ({ page }) => {
  await page.goto('/');
  await page.getByTestId('username').fill('standard_user');
  await page.getByTestId('password').fill('secret_sauce');
  await page.getByTestId('login-button').click();
  await expect(page).toHaveURL(/inventory.html/);
  await expect(page).toHaveScreenshot('inventory-page.png', {
    fullPage: true,
    animations: 'disabled',
    mask: [page.locator('[data-test="shopping-cart-badge"]')],
  });
});
