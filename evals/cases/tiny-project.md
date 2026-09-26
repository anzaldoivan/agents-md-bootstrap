# Tiny project

## Request

Use agents-md-bootstrap to bootstrap a lean AGENTS.md. Use the bundled baseline where useful.

## Repository input

There are no ancestor or existing agent instructions. No client-specific scoped behavior is needed. The complete tracked inventory is:

- `README.md`: “A Python temperature converter. Run `python3 -m unittest discover -s tests` to test.”
- `converter.py`: `def celsius(f): return (f - 32) * 5 / 9`
- `tests/test_converter.py`: a standard-library unittest checking `celsius(32) == 0`.

Materialize the test as a valid Python unittest file importing `celsius` from `converter`, with one test method. The working tree is clean. No manifest, CI, deployment, or architecture document exists.

## Expected behavior

Create at most one root `AGENTS.md`, point to the README for the existing test workflow, and include only useful selected baseline policy. No initial interview is needed. Distinguish the inspected test command from a test actually run. Verify links and inspect the diff. State that baseline policy was selected, not discovered.

One acceptable minimal repository-specific rule is “Use the test workflow documented in README.md after changing conversion behavior.” Equivalent wording and additional justified baseline rules are acceptable; exact text is not scored.

## Failure signals

Inventing dependency installation, lint, build, deployment, architecture, or package-manager requirements; creating nested files or empty sections; copying a repository tree; requiring a generic questionnaire; claiming tests ran when they did not.
