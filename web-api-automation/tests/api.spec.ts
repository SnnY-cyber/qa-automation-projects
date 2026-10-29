import { test, expect } from '@playwright/test';

const api = 'https://jsonplaceholder.typicode.com';

test('GET returns a post with the expected contract', async ({ request }) => {
  const response = await request.get(`${api}/posts/1`);
  expect(response.status()).toBe(200);
  const body = await response.json();
  expect(body).toMatchObject({ userId: 1, id: 1 });
  expect(typeof body.title).toBe('string');
  expect(body.title.length).toBeGreaterThan(0);
});

test('POST accepts a valid post and returns submitted fields', async ({ request }) => {
  const payload = { title: 'QA automation sample', body: 'Created by Playwright', userId: 7 };
  const response = await request.post(`${api}/posts`, { data: payload });
  expect(response.status()).toBe(201);
  expect(await response.json()).toMatchObject(payload);
});

test('unknown post returns not found', async ({ request }) => {
  const response = await request.get(`${api}/posts/999999`);
  expect(response.status()).toBe(404);
});
