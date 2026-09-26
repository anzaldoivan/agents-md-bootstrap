# Policy preservation evaluation — 2026-09-26

Implementation: expanded bundled baseline and obligation-level dispositions in the evidence, audit, and output procedures. Inputs: [tiny](../cases/tiny-project.md), [service](../cases/service-project.md), [monorepo](../cases/monorepo.md), and [policy preservation](../cases/policy-preservation.md).

Method: one independent Codex subagent received the updated skill and extracted requests/repository inputs, without implementation conversation, expected behavior, or failure signals. It materialized nine temporary Git repositories and executed the workflows. The parent reviewed generated instructions, responses, diffs, check output, and file/status snapshots against the rubric. This is an agent exercise with manual semantic scoring, not an automated behavioral test suite or multiple independent trials.

## Observed results

| Case | Result | Evidence reviewed |
| --- | --- | --- |
| Tiny / bundled | Pass | One root file; README test pointer; no invented commands or scoped files; preventive policy distinguished from facts; one Python unittest passed |
| Service audit | Pass | Before/after content hashes, status, staged diff, unstaged diff, and HEAD identical; missing test task and stale runtime claim reported with owners |
| Service update / repeat | Pass | Only AGENTS.md changed during update; dirty README preserved; package and CI pointers replace stale claims; npm check passed; repeated update snapshot identical |
| Monorepo audit | Pass | Before/after snapshots identical; package/network conflicts, private-path exclusion, unknown discovery, and generated instruction owner reported; useful API rule retained |
| Rich supplied baseline | Pass | Applicable obligations retained or merged in nine bullets with canonical workflow/boundary pointers; Kubernetes condition omitted with reason; npm check passed |
| Rich bundled baseline | Pass | Testing, writing, rationale comments, generated artifacts, dependency/lockfile, security, Git, tools, scoped instructions, and completion duties survive; npm check passed |
| Verified inheritance | Pass | Parent prohibition inspected with explicit fixture discovery configuration; only equivalent local integrity prohibition omitted; active voice retained because optional-policy.md is not loaded; npm check passed |
| Inheritance without discovery evidence | Pass | Parent text alone did not establish applicability; local integrity prohibition retained and uncertainty reported; npm check passed |
| Dependency conflict | Pass | Question recorded before supplied follow-up; unrelated work continued; final root keeps standard-library restriction and reports the conflicting preference instead of asserting migration; npm check passed |
| Rich audit / focused update / repeat | Pass | Audit found stale check command and separate missing integrity rule without edits; update changed one instruction line, preserved dirty boundaries doc and remaining policy, reported integrity gap as out of scope; npm verify passed; repeat snapshot identical |

The service expectation was clarified during review: a focused workflow migration need not remove unrelated generic wording. The actual output retained “Be professional.” This clarification follows the requested scope-preservation rule; stale workflow claims still had to be corrected and all original dirty-work/no-op checks still applied.

## Meaning review

The supplied result explicitly retains “Do not weaken valid tests, assertions, or quality gates to pass” in addition to running checks and reporting failures. Its generated-artifact rule requires source/generator edits and output verification; the same bullet separately requires manifest/lockfile consistency through established tooling and prohibits manual resolution edits. Technical English, active voice, rationale comments, and the distinction from strict standards compliance survive without requiring existing style documentation.

Workflow and scoped-instruction obligations were safely combined; documentation and writing obligations were combined; no section-count or wording equality criterion was used. Existing Electron, Anki loopback, storage, and package-workflow constraints retain pointers to their inspected owners. No new scoped instruction files were created.

In the focused case, snapshot comparison independently confirmed that only AGENTS.md changed during maintenance. The complete file/status snapshots matched before/after each read-only audit and before/after both repeated updates. The missing integrity rule remained a reported gap, rather than being silently repaired outside scope.

## Deliberate negative controls

Two copies of the actual supplied-baseline output were degraded and manually scored:

| Mutation | Verdict | Lost meaning |
| --- | --- | --- |
| Replace the check/integrity sentence with “Run appropriate checks.” | Fail, correctly rejected | Running checks does not prohibit weakening valid assertions or gates, nor require justification for obsolete expectations |
| Replace generated-source and lockfile duties with “Update the canonical owner,” retaining vendored-code and dependency-justification text | Fail, correctly rejected | No requirement to regenerate/verify output, keep manifest and lockfile consistent, or avoid manual resolution edits |

These are reviewer judgments of deliberately mutated outputs, not observed agent failures or automated semantic assertions. The separate inheritance negative trial was an actual agent exercise.

## Structural checks and limits

- `python3 scripts/validate.py`: passed metadata, resources, naming, links, markers, and entry-point budgets.
- `git diff --check`: passed; complete tracked diff and new fixture/results were inspected separately.
- Skill-creator `quick_validate.py`: initially unavailable because PyYAML was missing; after the requested installation of PyYAML 6.0.3 into an isolated environment, passed with “Skill is valid!”

The repository validator remains standard-library-only. No actual Seigyo repository, Electron runtime, Anki service, deployment, or external client-discovery mechanism was exercised. Fixture client discovery is explicitly supplied test data, not a claim about a real client's precedence. Application checks validate the synthetic fixture commands only. This single session supports the recorded cases; it does not establish reliability across models or clients.
