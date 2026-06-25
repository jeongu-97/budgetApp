---
name: budget-cli-tdd
description: Use when modifying, extending, testing, reviewing, or committing this repository's Python CSV-based budget CLI application. Enforces test-first development, typed small functions, cyclomatic complexity limits, pytest/radon validation, and qa_engineer review before commit.
---

# Budget CLI TDD

## Workflow

1. Read `AGENTS.md` before making changes.
2. Identify the smallest observable behavior to implement.
3. Write or update tests first. The first test run should fail for the expected
   reason.
4. Implement the minimal production code needed to pass the tests.
5. Refactor while preserving behavior.
6. Run:

```bash
pytest
radon cc .
```

7. Ask the `qa_engineer` subagent to review before committing.
8. Commit and push after one complete verified feature.

## Design Rules

- Use type hints on all functions and methods.
- Keep each function at 50 lines or fewer.
- Keep cyclomatic complexity at 10 or lower.
- Separate CLI parsing, CSV I/O, domain logic, and output formatting.
- Prefer deterministic pure functions for calculations and validation.

## Testing Guidance

- Cover CSV parsing with valid rows, malformed rows, empty files, and missing
  columns when relevant.
- Cover domain behavior such as income/expense totals, category summaries,
  date filtering, and invalid amounts when relevant.
- Cover CLI behavior through command invocation tests when changing user-facing
  commands, output, or exit codes.

## Commit Gate

Before committing, collect the latest `pytest` and `radon cc .` results and
request `qa_engineer` review. Treat unresolved high-impact review findings as
blockers.
