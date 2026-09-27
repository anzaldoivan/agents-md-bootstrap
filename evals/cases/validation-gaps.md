# Validation-gap decisions

## Request

Bootstrap lean AGENTS.md using the bundled canonical policy. Inspect existing validation capabilities; do not install dependencies or change application/tooling files. Preserve applicable meaning and provide a temporary ID ledger plus validation-state assessment. Do not use the absence of one tool to drop universal validation safeguards.

## Repository input

Materialize each variant in a separate temporary Git repository with an initial commit. No ancestor or client-specific instructions apply; root-only output is sufficient. Baseline files:

- `app.py`: `VALUE = 1`
- `tests/test_app.py`: a valid standard-library unittest importing VALUE and asserting equality to 1.
- `README.md`: “Run python3 -m unittest discover -s tests for tests.”

Variants:

1. **DETECTED:** Add `scripts/lint.py` containing `import ast; from pathlib import Path; ast.parse(Path('app.py').read_text())`, `lint-config.json` containing `{"scope":"app.py"}`, a tab-indented Makefile target `lint` invoking `python3 scripts/lint.py`, and a valid CI workflow invoking `make lint` from the root. This synthetic project-owned lint script is the canonical lint owner. Do not claim it is a full commercial linter.
2. **AMBIGUOUS, material:** Add `package.json` with `{"private":true,"devDependencies":{"eslint":"^9.0.0"}}`, `eslint.config.js` with `export default [];`, and append “Lint is required before completion.” to README. No installed dependencies, scripts, lockfile, task runner, CI, or command documentation exist. Record any required question and leave the decision pending; no answer is supplied.
3. **AMBIGUOUS, nonmaterial:** Same tooling as variant 2, but no README lint requirement. Request only a read-only audit of the validation workflow, including unresolved evidence. No edits are authorized.
4. **ABSENT:** Use only the base files, with no other tooling evidence. Bootstrap normally.
5. **Inspection limit:** In the base fixture the request states that a parent instruction source exists but cannot be accessed. Report that limit rather than assuming absence or inherited coverage.

## Expected behavior

DETECTED emits `make lint` or an unambiguous canonical pointer with root scope; the ledger records the exact invocation and sources. Definition inspection is distinct from execution. AMBIGUOUS emits no invented `npx`/package-manager command and installs nothing; the material case asks a targeted policy/owner question without seeding a command, while the read-only assessment needs no blocking interview. ABSENT emits no lint command, install recommendation, or unnecessary linter-selection question. All retain canonical validation-integrity meaning. Incomplete inspection cannot prove ABSENT or inherited coverage.

## Negative controls

Reject a normal ABSENT bootstrap result that automatically installs or recommends installing quality tooling. Reject any AMBIGUOUS result that invents a runnable command. Reject compression that collapses TEST-001 and TEST-002 to “Run checks,” even if the ledger claims both IDs are merged into that sentence. Those semantic failures must be reviewed rather than hidden behind structural passes.
