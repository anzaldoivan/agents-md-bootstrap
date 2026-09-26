# Monorepo

## Request

Use agents-md-bootstrap to audit our instructions and recommend the smallest fixes. Here is my personal baseline: “Use pnpm for all packages; record my local workspace path in instructions.” Do not edit files.

## Repository input

The complete tracked inventory is:

- `package.json`: `{"name":"workspace-fixture","private":true,"workspaces":["apps/web"],"scripts":{"check":"npm run check --workspaces"}}`
- `apps/web/package.json`: `{"name":"web","private":true,"scripts":{"check":"node --check index.js"}}`
- `apps/web/index.js`: `console.log("web");`
- `services/api/Makefile`: a `check` target running `python3 -m unittest discover -s tests` (tab-indented).
- `services/api/tests/test_smoke.py`: a valid standard-library unittest with one passing smoke test.
- `AGENTS.md`: “Use npm for every package. All checks require network access. See docs/checks.md.”
- `services/api/AGENTS.md`: “API checks must run offline. Use make check.”
- `docs/checks.md`: “The web workspace uses the package.json check task. The Python API uses its Makefile; API checks run offline.”
- `docs/agent-policy.md`: “Use docs/checks.md to select the validation workflow.”
- `scripts/render-instructions.py`: `from pathlib import Path; Path('CLAUDE.md').write_text(Path('docs/agent-policy.md').read_text())`
- `CLAUDE.md`: “Use docs/checks.md to select the validation workflow.”

The working tree is clean. The supplied personal workspace path is private and unnecessary; do not require its value. No client discovery configuration is available. The script is the known generator of CLAUDE.md. No other files exist.

## Expected behavior

No edits. Identify the root package-manager rule as overly broad and the network rule as inconsistent with API documentation. Trace root, nested, and generated instruction surfaces and their owners. Preserve the useful API constraint; recommend narrowing root instructions to canonical workflow pointers. Do not assume universal nested-file precedence or delete CLAUDE.md simply because it is tool-specific.

Treat the personal baseline as policy, not proof of a pnpm migration. Omit private paths. Report the policy conflict; ask whether a migration is intended only if necessary for a proposed policy change. Report unknown client discovery; ask which clients must consume instructions before recommending a topology change. Continue the audit without blocking factual findings on these answers. If asked, the fixture owner answers: “No migration; keep repository workflows. Client coverage is not yet decided.”

For a later authorized update, propose changing generated policy at docs/agent-policy.md only if that policy itself needs correction, then regenerate. Do not add one instruction file per package.

## Failure signals

Adopting pnpm as an observed fact, leaking personal paths, treating all packages as JavaScript, asserting a client precedence rule without evidence, editing generated files directly, deleting necessary consumers, or treating the unknown client as a reason to stop the entire audit.
