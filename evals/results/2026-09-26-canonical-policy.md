# Canonical policy and validation-gap evaluation — 2026-09-26

This run evaluates the canonical catalog and accounting migration. The [previous report](2026-09-26-policy-preservation.md) remains unchanged and does not claim to have tested stable IDs. Inputs were the existing [tiny](../cases/tiny-project.md), [service](../cases/service-project.md), [monorepo](../cases/monorepo.md), [desktop](../cases/policy-preservation.md), and new [accounting](../cases/canonical-accounting.md) and [validation-gap](../cases/validation-gaps.md) cases.

## Method

One independent Codex subagent received the installed skill and raw requests/inventories, withholding expected behavior, failure signals, and implementation conversation. It materialized 17 isolated Git repositories/runs, initial commits, dirty user edits, external parent fixtures, and temporary per-ID ledgers. The parent reviewed actual instructions, evidence locators, hashes, status/diff snapshots, questions, and command logs against the rubric. Bounded follow-up corrections are disclosed below; they were not independent first-pass successes. These results cover one client/session and synthetic client-discovery evidence, not cross-client reliability.

## Results after review and bounded corrections

| Fixture / mode | Expected | Actual and reviewer verdict |
| --- | --- | --- |
| Tiny / bootstrap | Existing test owner, no invented capabilities, complete selected policy | Pass: one root file, README-owned unittest, 95-ID accounting; no setup or lint tooling introduced |
| Service / audit, maintain, repeat | Read-only audit, minimal workflow repair, dirty README preserved, repeat no-op | Pass after correction: check/CI pointers fixed, “before finishing” preserved, unrelated wording retained; broader policy observation separated from repair ledger |
| Monorepo / audit | Scope and policy conflicts reported, generated owner preserved | Pass: no file changes; pnpm question remains pending; private path excluded and discovery uncertainty reported |
| Desktop supplied / bootstrap | Supplied policy replaces defaults | Pass: 242-word output preserves supplied obligations; Kubernetes condition excluded with inspection evidence |
| Desktop bundled / bootstrap | All applicable catalog meaning accounted for | Pass: 95 unique IDs accounted for; 88 retained/merged and 7 conditional exclusions supported; output preserves workflow/boundary owners |
| Desktop supplied inheritance / bootstrap | Verify parent coverage and discovery; unloaded prose cannot supply coverage | Pass: equivalent loaded integrity policy inherited; optional active-voice file not relied upon; parent unchanged |
| Desktop dependency conflict / bootstrap | Preserve established restriction after supplied answer | Pass: question/answer recorded, restriction retained, no inferred migration or installation |
| Canonical valid inheritance / bootstrap | Equivalent rule and target/consumer scope required | Pass: TEST-002 verified-inherited with quote, discovery evidence, scope and SHA-256 |
| Canonical false inheritance / bootstrap | Parent existence alone insufficient | Pass: full TEST-002 prohibition retained locally |
| Canonical scope mismatch / bootstrap | Sibling-only scope insufficient | Pass: full TEST-002 prohibition retained locally |
| Canonical weakened inheritance / bootstrap | “Run tests” cannot supply integrity policy | Pass: full TEST-002 prohibition retained locally |
| DETECTED / bootstrap | Use exact public canonical check | Pass: `make lint` from Makefile/CI; synthetic AST-parser scope described accurately; check passed |
| AMBIGUOUS material / bootstrap | No invented invocation; targeted question and incomplete claim | Pass: asks which existing lint command owns README requirement; no command or installation; strict completion validation rejects pending question |
| AMBIGUOUS nonmaterial / audit | Assessment without needless interview or mutation | Pass: no question, no edits, tooling evidence and unresolved invocation reported |
| ABSENT / bootstrap | No command, installation recommendation, or routine tool-selection question | Pass: no lint command/tooling question; universal validation and integrity rules retained |
| Inaccessible parent / bootstrap | Inspection limit, not assumed absence or inheritance | Pass: limit recorded; ordinary structure passes, strict completion validation rejects incomplete evidence |
| Desktop / audit, focused migration, repeat | Unrelated integrity gap reported; only stale invocation repaired | Pass: dirty boundaries preserved; separate gap remains visible; only instruction pointer changed; repeat no-op |

All executed fixture checks passed: Python unittests, service/desktop npm check tasks, migrated npm verify task, and the project-owned synthetic lint script. Audit-only checks and unchanged application checks were not repeatedly executed. Source inspection was kept distinct from successful execution. All audited before/after content snapshots and parent hashes matched. Both maintenance sequences preserved dirty documentation and repeated as no-ops.

## Initial defects and corrections

1. **Service accounting scope:** The initial evaluator selected EVID-005 because the agent performed a focused correction, then correctly marked its absence from target instructions as uncovered. That ID was outside the requested repair. The clarified procedure distinguishes agent behavior from target policy coverage; the final focused ledger covers the affected TEST-001 obligation while preserving the broader observation separately. No extra policy was injected.
2. **Service temporal qualifier:** Initial generated wording lost the original “before finishing” requirement. Semantic review restored that qualifier and repeated the maintenance check without changing the application. This demonstrates why a locator or structural pass alone cannot prove preservation.
3. **Desktop invocation evidence:** Initial ledgers used the expanded package-script body as the DETECTED command, although generated instructions pointed to the workflow owner and actual executions used npm. The evidence procedure now explicitly preserves public named-task invocations. Corrected ledgers use `npm run check` or `npm run verify`, supported by task definition and runner ownership. No unchanged application tests were rerun.
4. **Completion guard:** The helper now rejects pending material check questions under `--require-covered`, in addition to uncovered obligations, unresolved conflicts, and inspection limits. Ordinary accounting remains valid for an honest partial assessment.

Original evaluation artifacts and subsequent corrections were preserved in the isolated run, rather than rewriting initial failures as successes. The final reviewed results above reflect corrections, not an assertion of flawless first-pass generation.

## Semantic negative controls

Two copies of actual generated output were deliberately degraded. Removing TEST-002's prohibition and substituting “Run checks” was rejected by manual review. Appending automatic linter installation to an ABSENT bootstrap was also rejected. Their evidence locations remained structurally valid, so the structural helper passed them; that is intentional and is not semantic approval. Structured attempts to attach invented commands to AMBIGUOUS/ABSENT states or request installation are separately rejected by unit tests.

The complete bundled output was manually compared with the catalog: testing integrity, independent execution reporting, future-action conditions, writing preferences and strict-compliance distinction, documentation/comment ownership, generator/lockfile exceptions, security, Git, tools, scope, and completion meaning survive. Conditional exclusions concern inspected capabilities or conventions, not failure to find an incident demonstrating a universal rule.

## Structural checks and migration review

- Repository validator and all 36 standard-library policy tests passed, including omission/duplication/invalid IDs, missing evidence, hash drift, output locators, conditional exclusions, conflicts, audit gaps, capability-state payloads and control-marker leakage.
- Skill-creator validation passed using the existing isolated PyYAML environment.
- A copied standalone installed skill validated its catalog from an unrelated working directory; no checkout-relative dependency was required.
- The catalog has 95 IDs across 13 families; reordering preserves identity. The former independent baseline is removed and its consumers now reference the catalog.
- Historical results remain unchanged. The migration map in the accounting reference records old sections by ID family without maintaining another policy catalog.
- Final diff, whitespace, local reference targets, scope, and clean-source provenance were reviewed separately from behavioral scoring.

The external check was narrow: [Agent Skills progressive disclosure](https://agentskills.io/specification), [AGENTS.md guidance](https://agents.md/), and [GitHub instruction scope](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) support keeping reference loading and client discovery explicit. [OSCAL control identifiers](https://pages.nist.gov/OSCAL-Reference/models/v1.2.3/catalog/json-reference/) provide prior art for referencable catalog identities; no OSCAL framework or dependency was adopted.

## Limits

Bundled output was approximately 964–1010 words versus 242 for the supplied desktop policy. This run establishes preservation and recorded decision behavior, not optimal prose compression or reliability across models. Ledger selection, semantic equivalence, true applicability, authority, and exact command ownership remain review responsibilities. SHA-256 detects changed source bytes, not semantic or discovery correctness. Synthetic security and architecture constraints were preserved as policy, not runtime-tested. No real Seigyo application, Electron runtime, Anki service, production data, or external client adapter was exercised.
