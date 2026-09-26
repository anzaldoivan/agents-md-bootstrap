---
name: agents-md-bootstrap
description: Bootstrap, audit, and maintain lean AGENTS.md files using repository evidence, canonical sources of truth, and a reusable policy baseline. Use when creating repository agent instructions, reviewing instruction quality or conflicts, or updating instructions after repository changes.
license: MIT
---

# agents-md-bootstrap

Produce the smallest useful set of repository instructions supported by evidence and selected policy. Bootstrap is the entry point; audit and maintenance keep the result healthy afterward.

## Shared workflow

1. Determine the requested mode and scope. Inspect repository status, tracked and relevant untracked files, existing instructions, and any supplied personal baseline before editing. Preserve existing work. An audit is read-only unless edits are explicitly requested.
2. Read [evidence-policy.md](references/evidence-policy.md). Build a compact working evidence ledger and instruction-topology map. Inspect actual sources; do not infer project commands, architecture, or client precedence from filenames alone.
3. Separate repository facts from personal policy. For bootstrap, inspect [baseline-agents.md](assets/baseline-agents.md) as an adaptable output template, not active instructions for the current session. A supplied personal baseline replaces the bundled defaults. For audit/update, consult a baseline only when evaluating policy; do not inject defaults into healthy existing instructions.
4. If instructions or sources disagree, read [conflict-resolution.md](references/conflict-resolution.md). If a consequential decision remains unknown, read [interview-policy.md](references/interview-policy.md). Continue independent work while waiting; do not invent an answer.
5. Use the selected mode below. Do not create instructions per directory, duplicate tool-specific files, architecture documentation, or policy catalogs without demonstrated need. New scoped files must prevent a concrete mistake that root instructions cannot address concisely.
6. Read [output-contract.md](references/output-contract.md) before delivery. Verify changed links, claims, scope, and relevant checks; inspect the diff. Report uncertainty and unrun checks honestly. Do not commit, push, or publish merely because this skill was invoked; follow the user's authorized scope.

## Bootstrap

Start with useful existing instructions. Select applicable baseline rules, then add only high-value repository constraints and pointers justified by the evidence ledger. Prefer a single lean root `AGENTS.md`; add scoped instructions only when topology analysis establishes distinct local needs and client applicability. If canonical documentation is missing, include the smallest verified actionable instruction rather than inventing a source or creating a new document hierarchy. Omit empty sections and unsupported rules.

## Audit

Read [audit-checklist.md](references/audit-checklist.md). Review each discovered instruction against its evidence, scope, canonical owner, and expected discovery behavior. Produce prioritized findings with locations, supporting evidence, impact, and minimal recommendations. Include sound instructions worth retaining and coverage gaps. Do not rewrite files during a read-only audit; uncertainty is a finding, not proof of staleness.

## Maintain / update

Read [audit-checklist.md](references/audit-checklist.md), focusing first on the affected paths and their inherited instructions. Inspect the supplied diff, migration, or other change evidence and verify the current state; if no change range is supplied, compare current instructions with current sources without inventing history. Follow dependencies to shared rules as needed.

Patch only invalidated or newly necessary instructions. Remove obsolete rules and replace duplicated facts with canonical pointers where justified. Preserve sound policy, wording, and unrelated user changes. Do not apply the whole baseline or reformat everything. If nothing needs correction, return a no-op with the evidence checked.
