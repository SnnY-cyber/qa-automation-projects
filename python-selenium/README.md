# Selenium + Python UI Regression

A small Selenium 4 + pytest suite for SauceDemo. It demonstrates explicit waits, stable `data-test` selectors, a checkout happy path, invalid-login validation, and failure screenshots.

## Requirements and run
- Python 3.11+
- Google Chrome

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
pytest
```

Selenium Manager resolves a compatible browser driver. The tests use the public demo login (`standard_user` / `secret_sauce`) and synthetic checkout data.

## CI
The parent repository runs this suite in GitHub Actions with headless Chrome and uploads screenshots on failure. A Jenkins pipeline example is available at `../Jenkinsfile`.
