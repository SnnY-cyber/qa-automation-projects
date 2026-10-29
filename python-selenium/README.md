# Selenium checkout checks

This folder has two browser checks against the public SauceDemo store: one standard-user checkout and one invalid-login error. The examples are intentionally small so a failed step is easy to locate in the pytest output.

## Run

Requires Python 3.11+ and Google Chrome. Selenium Manager resolves a compatible driver. From the repository root:

```bash
python -m pip install -r python-selenium/requirements.txt
pytest -q python-selenium/tests
```

The checkout uses the documented demo account and made-up customer details. The invalid-login case verifies the visible validation message. Waits target page state instead of using fixed sleeps.

## CI and evidence

GitHub Actions runs this suite on changes under `python-selenium/`. If a test fails, the workflow uploads a screenshot to the run artifacts. It does not require a personal browser session or secret.

This is a public-demo example. A demo-site outage or markup change can break it independently of the test code. See [`../docs/test-approach.md`](../docs/test-approach.md) for coverage choices and limits.
