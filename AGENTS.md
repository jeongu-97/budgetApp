# Project Agent Instructions

## Project

This repository is a Python CLI budget application that uses CSV files as its
primary data source. The app should support reading, validating, summarizing,
and updating household finance transaction data from CSV files.

## Coding Rules

- Use Python type hints for all public functions, internal functions, and class
  methods.
- Keep each function at 50 lines or fewer.
- Prefer small, pure functions for parsing, validation, filtering, aggregation,
  and formatting.
- Keep file I/O, CLI argument parsing, and domain logic separated.

## TDD Rules

- Write the failing test before implementing behavior.
- Do not add production code for a feature until the intended behavior is
  covered by tests.
- Update or add tests first when changing existing behavior.
- Keep tests focused on observable CLI behavior and CSV/domain logic.

## Quality Rules

- Keep cyclomatic complexity at 10 or lower for every function and method.
- Refactor branching logic into smaller typed helpers when complexity rises.
- Avoid broad exception handling unless the CLI converts a specific expected
  error into a user-facing message.

## Quality Review Rules

- Before every commit, run a quality review with the `qa_engineer` subagent.
- The `qa_engineer` review must check tests, type-hint coverage, function size,
  cyclomatic complexity, CSV edge cases, and CLI behavior regressions.
- Do not commit if the `qa_engineer` reports unresolved high-impact issues.

## Test And Quality Commands

Run these before committing:

```bash
pytest
radon cc .
```

## Commit Rules

- Commit after one complete feature is developed and verified.
- Push the feature commit after local tests and the `qa_engineer` review pass.
- Keep commits focused on a single feature or tightly related fix.
