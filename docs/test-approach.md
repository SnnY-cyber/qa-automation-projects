# Test approach

These examples answer a narrow question: can a reviewer see the critical behavior, reproduce a failure, and understand the limits of the result?

## Coverage choices

| Risk / behavior | Check | Why this level |
|---|---|---|
| A valid user can complete a purchase | Playwright and Selenium checkout flow | It exercises the main user path across multiple pages.
| Invalid credentials are rejected | Browser negative test | The error should be visible to the user without reaching inventory.
| A known API response has the expected fields | Postman/Newman and Playwright API checks | Contract failures are faster to isolate outside the UI.
| A submitted demo resource returns a create response | Newman POST check | Confirms response shape/status; the demo service does not persist writes.
| An unknown resource returns not found | API negative-path check | Covers a useful boundary without adding test data setup.

## Implementation decisions

- Prefer the demo app's `data-test` attributes for controls, then wait for the next meaningful UI state before continuing.
- Keep customer details synthetic and avoid credentials or internal URLs in the repository. The public demo login is documented by the demo site.
- Assert outcomes such as a visible confirmation or expected response fields, not implementation details like CSS classes.
- Keep visual comparison separate from the normal CI run because screenshot baselines vary by browser and operating system. Review baseline changes before accepting them.

## Limits and next steps

The demo store and JSONPlaceholder are external dependencies; their availability and behavior can change. JSONPlaceholder simulates writes, so a `201` response does not prove persistence. The Appium folder is only a starter until a licensed demo APK and device/emulator are supplied. The Jenkinsfile is an example pipeline and has not been run on a Jenkins server.

The sample bug report in `web-api-automation/manual-qa-samples.md` is illustrative, not a filed defect. These projects are portfolio samples, not tests or code copied from Ericsson systems.
