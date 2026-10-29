# QA Automation Lab

[![Playwright](https://github.com/SnnY-cyber/qa-automation-projects/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/SnnY-cyber/qa-automation-projects/actions/workflows/tests.yml) [![Selenium](https://github.com/SnnY-cyber/qa-automation-projects/actions/workflows/selenium-python.yml/badge.svg?branch=main)](https://github.com/SnnY-cyber/qa-automation-projects/actions/workflows/selenium-python.yml) [![Newman](https://github.com/SnnY-cyber/qa-automation-projects/actions/workflows/postman-newman.yml/badge.svg?branch=main)](https://github.com/SnnY-cyber/qa-automation-projects/actions/workflows/postman-newman.yml)

**CI status** — Playwright, Selenium, and Newman checks run in GitHub Actions. Open a badge to see its run and logs.

I use this repository to show how I break a small QA problem into focused checks and make the results visible in CI. The browser and API suites target public demo services; the examples use synthetic data and are separate from any employer or production system.

## Projects

| Folder | What it covers | Run locally |
|---|---|---|
| [`web-api-automation`](web-api-automation/README.md) | Playwright checkout flow, API assertions, and an optional visual test | `cd web-api-automation && npm install && npx playwright install chromium && npm test` |
| [`python-selenium`](python-selenium/README.md) | Selenium invalid-login validation | `python -m pip install -r python-selenium/requirements.txt && pytest -q python-selenium/tests` |
| [`postman`](postman/README.md) | GET contract, simulated POST response, and 404 behavior | `newman run postman/QA-API-Checks.postman_collection.json` |
| [`mobile-appium-starter`](mobile-appium-starter/README.md) | WebdriverIO + Appium starter for an Android app | Needs a permitted APK and a configured emulator/device |
| [`Jenkinsfile`](Jenkinsfile) | Example stages for Selenium and Newman | Example pipeline; not presented as a live Jenkins deployment |

## How I chose the checks

The Playwright checkout path is the browser-level smoke path because it crosses login, inventory, cart, and order confirmation. API checks stay at the response boundary and verify a small contract rather than duplicating the UI journey. Invalid login covers one useful failure path. A few targeted checks are easier to diagnose than a large list of brittle assertions.

See [test approach and known limits](docs/test-approach.md) for the assumptions behind the suites. GitHub Actions runs the Playwright, Selenium, and Newman suites. The visual snapshot needs a reviewed baseline; the Appium folder is a starter and has no bundled app. Public demo sites can change or be temporarily unavailable, so a failed run may need a quick service check before treating it as a regression.
