# Postman API checks

`QA-API-Checks.postman_collection.json` contains three checks against JSONPlaceholder:

- `GET /posts/1`: status and required response fields
- `POST /posts`: status and echoed payload fields
- `GET /posts/999999`: not-found status for an unknown resource

## Run

Import the collection into Postman, or from the repository root run:

```bash
npm install --global newman@6
newman run postman/QA-API-Checks.postman_collection.json
```

The POST check only validates the demo response. JSONPlaceholder does not persist the created item, so this is not a persistence test. The assertions focus on response behavior rather than repeating the same checks through a browser.

GitHub Actions runs Newman on changes under `postman/` and uploads a JUnit report. See [`../docs/test-approach.md`](../docs/test-approach.md) for the suite assumptions.
