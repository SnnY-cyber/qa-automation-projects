# QA Web + API Automation

Playwright Test examples for browser E2E, REST API and visual regression. The UI and API cases use public demo services and contain no production data or credentials.

## Stack
- Playwright Test + TypeScript
- UI demo: [SauceDemo](https://www.saucedemo.com/)
- API demo: [JSONPlaceholder](https://jsonplaceholder.typicode.com/)
- GitHub Actions, HTML report, failure screenshots and traces

## Run locally
Requires Node.js 20+.

```bash
npm install
npx playwright install chromium
npm test
```

`npm test` runs UI and API checks. Use `npm run test:ui` or `npm run test:api` for one layer; `npm run report` opens the HTML report.

## Visual regression
Visual comparison is an optional suite because screenshots depend on the browser and operating system. Create and review a baseline before running it:

```bash
npx playwright test tests/visual.spec.ts --update-snapshots
npm run test:visual
```

Review snapshot diffs before accepting baseline changes.

## Coverage
- UI happy path: login → add product → checkout → confirmation
- UI negative path: invalid credentials show an error
- API contract: response fields and data types
- API create flow: POST response contains submitted fields
- API negative path: missing resource returns 404
- Visual regression: inventory page screenshot comparison

## CI
The parent repository stores the workflow at `.github/workflows/tests.yml`. It runs the UI and API checks from this project folder on pushes and pull requests, then uploads the Playwright report and test artifacts. Public demo service availability can affect results.

## Manual QA examples
See [`manual-qa-samples.md`](manual-qa-samples.md) for a checkout scenario and sample bug report.

