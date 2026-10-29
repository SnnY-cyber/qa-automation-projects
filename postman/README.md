# Postman + Newman API Checks

An importable Postman v2.1 collection covering a GET response contract, a POST create response, and an unknown-resource negative case against JSONPlaceholder.

## Run
Import `QA-API-Checks.postman_collection.json` into Postman, or run it with Newman:

```bash
npm install --global newman
newman run QA-API-Checks.postman_collection.json
```

The collection uses public demo endpoints and synthetic payloads. JSONPlaceholder simulates writes; created records are not persisted.

## CI
GitHub Actions runs the collection on pushes and pull requests and publishes the Newman report as a workflow artifact. A Jenkins example is in `../Jenkinsfile`.
