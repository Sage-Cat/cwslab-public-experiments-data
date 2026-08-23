# Validation

`validate_repository.py` checks exact manifest/file agreement, JSON and gzip
readability, file-size limits, local links, checksums, row accounting, and the
absence of common private identifiers or credentials.

## Repository Validation

Run the same bounded checks used by GitHub Actions:

```text
python3 scripts/validate_repository.py
```
