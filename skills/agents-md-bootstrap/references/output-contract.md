# Output contract

Deliver the requested artifact and a compact evidence-backed report. Keep analysis and the working evidence ledger out of permanent instructions unless the user explicitly requests them.

## Bootstrap

Create or improve only justified instruction files. Report changed paths, the decisions the rules support, canonical sources inspected, the baseline used and its policy dispositions (retained, merged, covered elsewhere, inapplicable, or conflicting), and any material assumption. Explain any new scoped file's concrete purpose and discovery basis. Preserve useful existing content. Group routine retained policies concisely, but identify consequential omissions and their reasons individually; cite inspected equivalent coverage and its applicability when relying on another instruction surface.

## Audit

Return prioritized findings with file/section or line locations, supporting source locations, scope, impact, confidence, and minimal recommendations. Include sound rules to retain, the evaluated policy source and coverage gaps with dispositions, uncovered surfaces, and questions that actually block resolution. Make no file edits unless separately authorized. A clean audit should identify coverage and limitations, not fabricate findings.

## Maintain / update

Provide a minimal patch tied to verified repository evolution. State what became stale, which owner now governs it, and why retained instructions remain valid. Account for affected policy obligations and report any discovered out-of-scope gaps without applying new defaults. If no patch is needed, report a no-op and the sources checked. Do not imply a historical comparison was performed when only current state was available.

## Verification for edits

- Inspect the complete relevant diff and preserve unrelated work.
- Check local reference targets, actual command definitions, instruction scope, and client discovery assumptions.
- Run existing relevant checks when safe and available; distinguish success, failure, and unrun checks. Documentation-only work need not run unrelated application suites.
- Check that facts and selected policies remain distinct, no secrets or private paths leaked, and no duplicated source of truth or unnecessary file appeared.
- Compare affected baseline and existing-policy obligations with the final wording and verified inherited coverage; explain consequential omissions and unresolved conflicts. Do not count generic wording as equivalent to specific safeguards.
- Confirm instructions are lean enough for their demonstrated needs; there is no minimum length or mandatory section count.

Report remaining blockers precisely. Do not label behavior tested when only structural validation ran. Do not install new tools, modify unrelated project configuration, or commit/publish without task authorization.
