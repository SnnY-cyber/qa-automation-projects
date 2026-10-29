# Selenium login validation

This folder contains a focused negative-login check for the public SauceDemo store. It enters invalid credentials and verifies the error shown to the user. The checkout happy path lives in the Playwright suite, where the cart and order flow is already covered.

## Run

Requires Python 3.11+ and Google Chrome. Selenium Manager resolves a compatible driver. From the repository root:

```bash
python -m pip install -r python-selenium/requirements.txt
pytest -q python-selenium/tests
```

The test uses `data-test` selectors and an explicit wait for the validation message; it has no fixed sleep and uses no real account.

## CI and evidence

GitHub Actions runs the Selenium check on changes under `python-selenium/`. If it fails, the workflow uploads a screenshot to the run artifacts. It does not require a personal browser session or secret. The demo site is external, so availability and markup changes can affect results.
