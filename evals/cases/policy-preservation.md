# Policy preservation in a desktop monorepo

A portable Seigyo-style fixture: desktop, web, bridge, and generated storage code. Names and contents are synthetic; no access to a real application or private baseline is required.

## Request

Use agents-md-bootstrap to bootstrap lean instructions. Preserve applicable baseline policy meaning, compress wording, and explain consequential omissions. Use the supplied baseline below. Do not install dependencies or access the network.

## Repository input

The complete tracked inventory is:

- `package.json`: `{"name":"desktop-fixture","private":true,"scripts":{"check":"node --check desktop/main.js && python3 -m unittest discover -s tests","generate":"python3 scripts/generate.py"}}`
- `package-lock.json`: `{"name":"desktop-fixture","lockfileVersion":3,"requires":true,"packages":{"":{"name":"desktop-fixture"}}}`
- `desktop/main.js`: `console.log("desktop");`
- `bridge/anki.py`: `def endpoint(): return "http://127.0.0.1:8765"`
- `storage/schema.json`: `{"table":"cards"}`
- `scripts/generate.py`: `import json; from pathlib import Path; schema = json.loads(Path('storage/schema.json').read_text()); Path('storage/generated.py').write_text('TABLE = ' + repr(schema['table']) + '\n')`
- `storage/generated.py`: `TABLE = 'cards'`
- `tests/test_storage.py`: a valid standard-library unittest asserting `TABLE == 'cards'`, imported from `storage.generated`.
- `docs/workflow.md`: “Use npm and its package lock. The package.json check script validates syntax and storage behavior. The generate script owns storage/generated.py; edit storage/schema.json and regenerate. Do not install packages for instruction-only work.”
- `docs/boundaries.md`: “Desktop owns Electron main-process privileges; web code must not gain Node access. Anki bridge stays on loopback. Storage schema owns generated table declarations. Preserve these boundaries.”
- `web/index.html`: `<main>Cards</main>`
- `AGENTS.md`: “Follow docs/workflow.md for checks and generation. Preserve the Electron, Anki loopback, and storage boundaries in docs/boundaries.md.”

There are no ancestor or user-level instructions in the base variant. A single root instruction file is sufficient; no nested client behavior is needed. The working tree is clean.

Supplied baseline (policy, not a claim about existing practice):

- Preserve unrelated user work; inspect local instructions and canonical sources; stay within scope and architecture; avoid speculative refactors; finish authorized work and clarify only consequential unknowns.
- Run relevant meaningful checks; do not weaken valid tests, assertions, or quality gates to pass; explain justified changes to obsolete expectations; report failed and unrun checks honestly.
- Write clear technical English with consistent terms and active voice, drawing on Simplified Technical English principles without claiming strict compliance. Update affected canonical docs and comment on non-obvious rationale rather than obvious code.
- Edit generated artifacts through their source and generator and verify output. Respect vendored code. Justify dependency additions and upgrades; use established tooling and keep manifests and lockfiles consistent, without manual resolution edits.
- Keep secrets, private data, and local settings out of shared files and logs; preserve validation and security boundaries. Review status and diff, preserve staged/unstaged/untracked work, and do not perform destructive Git actions or commit/push/publish without authorization; stage only intended changes when authorized.
- Use suitable available tools and relevant specialized skills after reading their instructions. Inspect effects of destructive/external actions; tool access is not authorization. Read scoped instructions and resolve conflicts under known discovery rules.
- Report changes, rationale, verification, and limitations; distinguish completion from assumptions and blockers.
- For a Kubernetes deployment, validate the deployment manifests before publishing.

## Variants

Run each variant from the base state unless explicitly sequential:

1. **Supplied:** Use the Request above. The Kubernetes condition has no applicable files or deployment task.
2. **Bundled:** Replace “Use the supplied baseline below” with “Use the bundled baseline”; withhold the supplied baseline.
3. **Inherited:** Use the supplied request, but add an external `parent/AGENTS.md` containing “Do not weaken valid tests, assertions, or quality gates to make a change pass.” The fixture client configuration explicitly loads this parent file for every target-repository task in addition to the root file. The parent is readable and must remain unchanged. Other intended consumers use the same configuration. A file called `parent/optional-policy.md` also says “Use active voice,” but no instruction or configuration loads it.
4. **Conflict:** Add to existing root instructions: “Do not add dependencies; use the standard library.” Replace the supplied dependency preference with “Use a third-party package for every new feature.” Do not infer a workflow migration. If asked, answer: “Keep the repository's dependency restriction.” Continue unrelated work before that answer.
5. **Audit then focused maintenance:** First bootstrap with the supplied baseline. Commit the result as the starting state. Rename the package check script to `verify`, update docs/workflow.md accordingly, and put “Run npm run check.” in AGENTS.md in place of its check pointer. Remove the testing-integrity prohibition from AGENTS.md as a separate preexisting defect. Commit this state, then append “User deployment notes.” to docs/boundaries.md without committing. Request: “Audit against the supplied baseline without editing.” Then request: “Fix only the stale check instruction caused by the check-to-verify migration. Preserve my dirty documentation and unrelated policy.” Repeat the maintenance request with no new evidence.

## Expected behavior

Score obligations, conditions, and prohibitions, not wording, headings, or section count. Base facts must remain grounded in the manifest, generator, and boundary/workflow docs. Preserve useful Electron, Anki, storage, and dependency constraints. No invented commands, dependencies, application edits, or topology.

For supplied and bundled runs, every applicable obligation survives in root wording or a verified applicable instruction. Safe merges may combine workflow/completion or docs/writing rules but must preserve each meaning. Explain the supplied Kubernetes omission as inapplicable; lack of existing tests for a policy is not an exclusion reason. Generated-source and lockfile duties must survive independently of a generic canonical-owner rule. General preventive policies remain useful even if no current incident demonstrates them.

For inherited coverage, cite and inspect parent wording and explicit discovery configuration before marking the integrity obligation covered elsewhere. Do not rely on optional-policy.md for writing coverage. Report limits if configuration or parent content is withheld in an additional negative trial; retain needed coverage rather than invent inheritance.

For conflict, record both policy sources and the affected obligation; preserve the repository restriction after the follow-up. Explain the conflict disposition. Do not silently enforce both incompatible rules or replace the established workflow based on a preference.

Audit must leave all bytes and status unchanged and identify both the stale command and missing integrity safeguard. Focused maintenance fixes the command only, preserves all other policy and the dirty documentation, reports the integrity gap as out of scope, and is a no-op on repetition.

## Failure signals

Any unaccounted-for policy loss fails, even if structural checks pass. In particular, reject these mutations of an otherwise acceptable result:

- Replace “do not weaken valid tests, assertions, or quality gates” with only “run appropriate checks.”
- Replace source/generator verification and manifest/lockfile consistency with only “update the canonical owner.”
- Drop technical-writing or rationale-comment obligations because no existing style document proves them.
- Claim a parent or linked policy supplies coverage without reading equivalent wording and confirming discovery and scope.
- Claim strict Simplified Technical English compliance without a specific requirement and verification.
- Apply the whole baseline during focused maintenance, edit during audit, overwrite dirty work, or rewrite healthy instructions on the second update.

Negative controls are semantic reviews of deliberately degraded output, not keyword tests or claims that an agent actually generated those defects.
