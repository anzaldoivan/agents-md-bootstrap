# Audit checklist

Use the evidence ledger and topology map described in the evidence policy. Apply this checklist to actual rules, not as mandatory headings in generated instructions.

| Check | Evidence to inspect | Minimal response |
| --- | --- | --- |
| Stale information | Current paths, task definitions, configuration, and changed behavior | Correct or remove invalid claim |
| Duplicated facts | Canonical owner and repeated copies | Replace copies with a useful pointer |
| Conflicting instructions | Overlapping scopes, active client precedence, policy versus fact | Resolve from authority or report the specific ambiguity |
| Dead rules | Removed component or workflow and any remaining consumers | Remove only after confirming obsolescence |
| Excessive scope | Local constraint applied globally | Narrow scope; add a scoped file only if justified |
| Generic low-value guidance | Policy provenance, applicable obligations, and verified equivalent coverage | Compress platitudes; preserve meaningful selected policy even when not repository-specific |
| Policy loss | Baseline obligations, final wording, dispositions, and inspected inherited coverage | Report omitted or weakened meaning; recommend restoration within authorized scope |
| Validation-gap classification | Task owners, config, dependencies, CI and inspection limits | Distinguish DETECTED, AMBIGUOUS and ABSENT; do not invent commands or install tools |
| Missing high-value constraints | Repeated failure evidence, generation boundaries, unusual checks | Add a concise evidenced constraint |
| Topology drift | Nested/tool-specific files, links, generators, client discovery | Fix at owner; preserve necessary consumers |
| Over-scaffolding | Empty sections, directory mirrors, speculative policy catalogs | Consolidate or remove needless structure |
| Baseline leakage | Private paths, secrets, personal preferences stated as discovered facts | Remove private details and label policy provenance in report |

Prioritize by consequence: high for instructions likely to cause unsafe or incorrect changes, medium for repeated workflow failures or substantive ambiguity, low for clarity and avoidable context cost. Explain impact rather than assigning severity mechanically.

For every finding record instruction location, evidence location, affected scope, confidence, and smallest corrective action. Distinguish confirmed defects from unverified concerns. Note retained high-value rules and inspection limits. A no-findings result is valid; do not manufacture edits to satisfy the checklist.

For maintenance, trace the repository change to affected rules and their shared dependencies. Avoid expanding a focused update into a full rewrite. Verify removed rules have no remaining applicable scope and that replacements point to existing owners.

For policy coverage, use the evidence policy’s obligation-level dispositions. Audit reports gaps without editing. Focused maintenance preserves unrelated policy and dirty work, records out-of-scope gaps, and checks that affected obligations survive the patch. A repeated update against the resulting state should be a no-op absent new evidence.

Use stable canonical IDs in findings and distinguish `uncovered` from `inapplicable`. The accounting helper checks objective evidence structure; reviewers must still reject false, weakened, or scope-mismatched inheritance.
