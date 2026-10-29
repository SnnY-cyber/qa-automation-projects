import { test, expect } from '@playwright/test';

test('user can sign in, add an item and complete checkout', async ({ page }) => {
  await page.goto('/');
  await page.getByTestId('username').fill('standard_user');
  await page.getByTestId('password').fill('secret_sauce');
  await page.getByTestId('login-button').click();
  await expect(page).toHaveURL(/inventory.html/);
  await page.getByTestId('add-to-cart-sauce-labs-backpack').click();
  await expect(page.getByTestId('shopping-cart-badge')).toHaveText('1');
  await page.getByTestId('shopping-cart-link').click();
  await page.getByTestId('checkout').click();
  await page.getByTestId('firstName').fill('QA');
  await page.getByTestId('lastName').fill('Engineer');
  await page.getByTestId('postalCode').fill('34000');
  await page.getByTestId('continue').click();
  await page.getByTestId('finish').click();
  await expect(page.getByTestId('complete-header')).toHaveText('Thank you for your order!');
});

test('invalid login shows a useful error', async ({ page }) => {
  await page.goto('/');
  await page.getByTestId('username').fill('wrong_user');
  await page.getByTestId('password').fill('wrong_password');
  await page.getByTestId('login-button').click();
  await expect(page.getByTestId('error')).toContainText('Username and password do not match');
});
