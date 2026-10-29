# QA Web + API Automation

Portfolio project with browser E2E, REST API and visual regression examples. It uses public demo services; no production credentials or private data are needed.

## Stack
- Playwright Test + TypeScript
- UI demo: [SauceDemo](https://www.saucedemo.com/)
- API demo: [JSONPlaceholder](https://jsonplaceholder.typicode.com/)
- GitHub Actions CI, HTML report, failure screenshots and traces

## Run locally
Requires Node.js 20+.

```bash
npm install
npx playwright install chromium
npm test
```

Run a layer separately with `npm run test:ui`, `npm run test:api` or `npm run test:visual`. Open the report with `npm run report`.

The default `npm test` and CI run UI + API checks. To include visual regression, establish and commit a platform-specific baseline first:

```bash
npx playwright test tests/visual.spec.ts --update-snapshots
npm run test:all
```

Review snapshot diffs before accepting a baseline update. Browser, operating system, fonts and viewport affect screenshots.

## Coverage
- UI happy path: login → add product → checkout → confirmation
- UI negative path: invalid credentials show an error
- API contract: required fields and data types on GET
- API create flow: POST response contains submitted fields
- API negative path: missing resource returns 404
- Visual regression: inventory page screenshot comparison

## CI
Every push and pull request runs the suite on Chromium. The workflow uploads the HTML report and Playwright artifacts even when tests fail. External demo availability can affect runs; API and UI checks intentionally use public demo endpoints.

## Project layout
```
 tests/                  UI, API and visual checks
 .github/workflows/      CI pipeline
 playwright.config.ts    Browser, reporter and failure evidence settings
```



