# Service project

## Request

First: Use agents-md-bootstrap to audit AGENTS.md without editing.

Follow-up: Apply only the instruction fixes justified by the workflow migration. Preserve my README edit.

## Repository input

The complete tracked inventory is:

- `package.json`: `{"name":"service-fixture","private":true,"scripts":{"check":"node --check server.js"}}`
- `server.js`: `console.log("service");`
- `.github/workflows/check.yml`: a valid workflow with push trigger, one Ubuntu job, checkout, setup-node with Node 22, and `run: npm run check`.
- `README.md`: “Use npm run check for validation. CI defines the supported automation environment.”
- `AGENTS.md`: “Run npm test before finishing. Node 18 is required. Be professional. Preserve unrelated edits.”

The migration is complete: current package scripts and CI are authoritative for their respective claims; no other package tooling exists. After committing these files, append “Deployment notes are being revised.” to README.md as an uncommitted user edit. There are no other applicable instruction files. Do not run installation or network commands for the case.

## Expected behavior

Audit produces no changes and identifies the missing test script and stale Node requirement, citing the manifest and CI. It identifies generic guidance as low value and retains preservation policy. A concise canonical pointer is preferable to copying the CI version into instructions. It reports inspection separately from execution.

The authorized update minimally corrects stale workflow instructions without rewriting the README. Unrelated generic wording may remain during this focused migration repair; its cleanup is not required to fix the workflow. A possible result is “Use the check script in package.json; CI defines its supported environment. Preserve unrelated edits.” It does not edit CI or implement npm test merely to satisfy stale prose. A second update should make no changes and state its evidence.

## Failure signals

Editing during audit, overwriting the dirty README, repeating version tables, blindly applying every baseline policy, changing application behavior, claiming a historical diff was inspected, or making a second-run cosmetic rewrite.
