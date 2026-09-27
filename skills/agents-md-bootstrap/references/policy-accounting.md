# Canonical obligation accounting

[The production catalog](production-agents-template.md) alone owns bundled policy prose. This reference owns the temporary ledger contract, not a second policy manifest. Use a working ledger outside the target repository; only keep it as an evaluation artifact or when requested. IDs and controls must not leak into generated instructions.

## Selection and scope

For bundled bootstrap, evaluate all catalog IDs, recording evidenced inapplicability for conditional obligations that do not activate. A full audit against bundled policy uses the same set but may report uncovered obligations. Maintenance uses only the affected IDs with an explicit selection reason; report other discovered gaps separately and do not call focused coverage a full audit. Applicability concerns the repository scope served by the generated instructions, not just the instruction-editing task. Preserve future-action conditions (for example, regression tests for bug fixes or regeneration after generator changes) when that workflow can apply; do not exclude them merely because bootstrap itself changes no application behavior. Capability exclusions require proportionate evidence that the relevant capability does not exist in that scope. One ledger evaluates one target scope. Use separate ledgers when subtrees have different applicable rules. IDs describe obligations expressed by the target instructions, not the skill agent’s own actions: making a focused correction does not prove the target already expresses EVID-005. Keep that broader gap in the audit/report unless its restoration is within scope.

A supplied personal baseline replaces bundled defaults. Reuse a canonical ID only for equivalent meaning. Assign other supplied obligations `USER-001`, `USER-002`, etc., stable within that source, and reference the original text without copying a second policy catalog. Declare every selected supplied obligation, including canonical equivalents, with its source locator. Preserve useful existing repository instructions separately; these are evidence/policy inputs, not permission to invent bundled defaults. Human decisions must retain their explicit provenance.

## Version 1 ledger

Use JSON with these fields:

| Field | Meaning |
| --- | --- |
| `version` | `1` |
| `policy` | `bundled` or `supplied` |
| `mode` | `bootstrap`, `audit`, or `maintain` |
| `scope` | Target paths/scope in human-readable form |
| `coverage` | `full`, or `focused` for maintenance only |
| `expected_ids` | All selected obligation IDs, without duplicates; full bundled selection must equal the catalog |
| `selection_reason` | Required for focused maintenance or supplied policy |
| `supplied` | For supplied policy only: list of `{id, source}` locators matching `expected_ids` |
| `entries` | One disposition record per expected ID |
| `checks` | Optional capability assessments described below |
| `inspection_limits` | Optional list of nonempty explanations of inaccessible or incomplete inspection |
| `generated` | Optional output paths to check for internal control-marker leakage; claimed output locations are checked automatically |

A source/output **locator** is `{ "path": "AGENTS.md", "quote": "exact supporting text" }`. Paths resolve from the explicitly selected target root (`--root`), including readable ancestor paths when relevant. Quotes locate actual evidence; they are not semantic proofs. Never include secrets in evidence. Private paths may remain in temporary local ledgers, not shared output. Record user-provided instructions or discovery facts in an external temporary evidence file when they have no file location; distinguish that supplied evidence from observed client configuration.

| Disposition | Required fields beyond `id` and `disposition` |
| --- | --- |
| `retained` | `output`: supporting output locator |
| `merged` | `output`: supporting output locator for this obligation's full meaning |
| `verified-inherited` | `source`: locator plus `sha256` of complete source bytes; `scope`; `discovery`: locator supporting actual consumer discovery |
| `inapplicable` | `reason`; `evidence`: nonempty inspection list demonstrating the unmet condition |
| `conflicting` | `source`: conflict locator; `scope`; `authority`; boolean `human_resolution_required`; `resolution` when no human decision remains |
| `uncovered` | `reason`; `evidence` of inspected coverage gap |

Evidence lists contain locators or inspection records such as `{ "inspection": "Checked tracked/untracked inventory, generation scripts, CI and generated markers; none found", "paths": ["."] }`. Inspection assertions need semantic review; a directory's existence alone does not prove a capability absent.

`uncovered` is necessary for honest read-only audits, demonstrated by the existing missing-testing-integrity fixture. It is not coverage and cannot satisfy bootstrap or a completed repair. For focused maintenance, keep unrelated uncovered gaps in the report or a separate audit ledger. `conflicting` accounts for an obligation but is not a claim that the baseline was adopted: unresolved human decisions block full-coverage claims. A resolved conflict must identify the authoritative resolution; do not silently weaken policy.

## Validation capability records

Each `checks` item has `kind` (`format`, `lint`, `type`, `static`, `tests`, `build`, or `security`), `scope`, `state`, and a nonempty `evidence` list. There is at most one record per capability/scope. Follow the [decision procedure](evidence-policy.md) to classify meaning.

- `DETECTED`: require `command`, `cwd`, and an `invocation` locator supporting the canonical task/runner invocation. A task definition plus inspected runner evidence can support a named invocation without that whole command appearing verbatim; do not substitute the task implementation body to satisfy a quote locator. Inspection is not successful execution. Record execution outcomes in the report.
- `AMBIGUOUS` or `ABSENT`: require `assessment`; do not include `command`, `cwd`, or `invocation` payloads.
- A `question` is allowed only for `AMBIGUOUS`, accompanied by `material_reason`. All three interview conditions still require review.
- Normal instruction maintenance never installs quality tooling; an `install_tooling` request is rejected. Explicitly authorized toolchain engineering is a separate task, not a state transition that creates authorization.
- If inspection is blocked, report `inspection_limits` rather than pretending a capability is absent. Do not fabricate a fourth state or force a classification.

## Running the helper

From the installed skill, run `python3 scripts/validate_policy.py` to check the catalog. For a ledger, add `--ledger /path/to/temporary-ledger.json --root /path/to/target`. Add `--require-covered` when checking a proposed complete result. The helper only reads files; it never executes evidence commands, installs tooling, or edits targets.

The helper rejects unknown/duplicate/missing IDs, invalid dispositions, missing evidence, nonexistent output/source quotes, changed inherited hashes, invalid state payloads, and leaked catalog controls. `--require-covered` also rejects uncovered obligations, unresolved conflicts, and inspection limits or pending material questions. Full bundled ledgers cannot quietly shrink their expected set. Supplied selections and maintenance scope still require manual completeness review.

A successful run means **structural accounting is valid**, not that prose is equivalent, a scope truly applies, the selected set is sufficient, or a source is trustworthy. Manually review merged/inherited meaning, authority, applicability, state classification, and exact command ownership. Hash changes invalidate the old evidence and trigger reinspection; a hash alone proves neither semantics nor discovery. Recheck discovery evidence too.

## Migration

The previous baseline asset is removed, not generated or maintained alongside the catalog. Old evaluations retain their original non-ID evidence; do not relabel historical results as ID-validated. For new runs, the old template's Core Principles map to CORE/EVID/TEST; Sources of Truth and Repository Map to EVID; Architecture and Development Workflow to ARCH/CORE/TEST; Commands and Testing to TEST/TOOL; Technical Writing to WRITE; Documentation/Comments to DOC; Generated Artifacts to GEN; Dependencies to DEP; Security to SEC; Git Hygiene to GIT; Agent Instructions/Skills and Tool Use to TOOL; Nested Instructions to SCOPE; Definition of Done to DONE. Review exact catalog entries rather than treating this family map as policy prose.
