# Production AGENTS.md validation reference

This is the full user-supplied production template, preserved below as reference material. It is not active session guidance or evidence about a target repository. The [baseline](../assets/baseline-agents.md) uses it to validate policy coverage; a separately supplied baseline still replaces bundled defaults.

Preserve applicable obligations, including qualifications and exceptions, rather than requiring this exact layout. Paths, technologies, command slots, and example architecture are adaptation points: verify them, replace them with actual owners, or omit them with an explanation when inapplicable. Do not create missing components, documents, commands, or skills to fill the template. Its nearest-file precedence statement applies only where the target client's discovery and precedence support it.

The template's format, lint, static-check, and testing slots require an explicit coverage assessment. An absent tool is a factual gap, not evidence that the quality obligation is irrelevant. Follow [evidence-policy.md](evidence-policy.md) for missing checks and questionable documentation. Use its dispositions to explain omissions; no mandatory heading count or verbatim reproduction is required. Simplified Technical English principles do not imply strict compliance without the project-approved standard and verification.

## Supplied template

```markdown
# AGENTS.md

Guidance for AI coding agents that work in this repository.

This file defines stable repository-wide rules. It names where authoritative information lives. It does not copy facts that another source already defines.

A nested `AGENTS.md` can add or override rules for its subtree. Follow the nearest applicable file.

## Project Overview

`<PROJECT_NAME>` is `<one-sentence description of the application>`.

Primary technologies:

- Language: `<LANGUAGE>`
- Runtime: `<RUNTIME>`
- Framework: `<FRAMEWORK>`
- Package manager: `<PACKAGE_MANAGER>`
- Database: `<DATABASE>`
- Test framework: `<TEST_FRAMEWORK>`

Keep detailed product information in `README.md` or the relevant project documentation.

## Core Principles

- Make the smallest correct change.
- Prefer existing project patterns over new abstractions.
- Keep code, tests, documentation, and contracts consistent.
- Do not duplicate authoritative information.
- Do not infer an exact value when an authoritative source exists.
- Treat tests and validation failures as evidence to investigate.
- Do not weaken a check only to make a change pass.
- Keep unrelated changes out of the diff.

## Sources of Truth

Use the authoritative source for each type of information.

| Information | Authoritative source |
| --- | --- |
| Runtime implementation | `src/` |
| Required behavior and regressions | `tests/` |
| Public API contract | `<OpenAPI/schema/code path>` |
| Database schema | `<migrations/schema path>` |
| Dependency versions | package manifest and lockfile |
| Build behavior | build configuration |
| CI requirements | `.github/workflows/` |
| Architecture boundaries | `docs/architecture.md` |
| Architecture rationale | `docs/adr/` |
| Environment/configuration shape | `<configuration source>` |

If an exact fact matters, inspect its authoritative source.

Do not copy an exact version, schema field, command option, API definition, configuration default, or similar machine-readable fact into prose unless the duplication has a clear human purpose.

If two sources conflict:

1. Identify which source owns the fact.
2. Verify the current implementation.
3. Do not silently resolve the conflict.
4. Update the stale artifact when it is part of the requested change.

## Repository Map

Use this section as a map, not as an inventory.

- `src/` — application implementation.
- `tests/` — automated behavioral checks.
- `docs/architecture.md` — system boundaries and high-level structure.
- `docs/adr/` — architectural decisions and rationale.
- `<api-contract-path>` — public API contract.
- `<migration-path>` — database schema evolution.
- `.github/workflows/` — CI/CD behavior.
- `<other-important-path>` — `<purpose>`.

Inspect the repository when you need the complete current structure. Do not rely on this file for a full file or package list.

## Architecture

Follow the architecture that the repository already defines.

- Keep domain/business rules in their existing domain layer.
- Keep infrastructure concerns outside the domain when the architecture separates them.
- Use the existing public interface between modules.
- Do not bypass established module boundaries for convenience.
- Do not introduce a new architectural pattern when the existing pattern solves the problem.
- Read the applicable ADR before changing a documented architecture decision.

Use `docs/architecture.md` for structure.

Use `docs/adr/` for rationale.

Use the code for implementation details.

## Development Workflow

### Before a Change

1. Read the nearest applicable `AGENTS.md`.
2. Inspect the relevant implementation.
3. Inspect nearby tests.
4. Identify the authoritative source for the behavior that will change.
5. Read relevant architecture or ADR documentation when the change affects a documented design decision.
6. Search for an existing implementation or utility before creating a new one.

Do not start by creating new abstractions.

### During a Change

- Keep the change scoped to the task.
- Preserve existing public behavior unless the task changes it.
- Follow local naming and structural conventions.
- Reuse existing utilities and shared components.
- Add or update tests when behavior changes.
- Do not perform unrelated cleanup.
- Do not reformat unrelated files.
- Do not replace working patterns solely because another pattern is preferable in general.

### After a Change

1. Format changed files.
2. Run static or type checks.
3. Run the narrowest relevant tests.
4. Run broader tests when shared behavior changed.
5. Review the diff.
6. Check for accidental generated-file changes.
7. Update affected documentation or contracts.
8. Confirm that no authoritative sources now disagree.

## Commands

Use repository-defined commands. Do not invent alternatives when a canonical command exists.

### Setup

`<SETUP_COMMAND>`

### Development

`<DEV_COMMAND>`

### Build

`<BUILD_COMMAND>`

### Format

`<FORMAT_COMMAND>`

### Lint

`<LINT_COMMAND>`

### Type or Static Check

`<TYPECHECK_COMMAND>`

### Unit Tests

`<UNIT_TEST_COMMAND>`

### Integration Tests

`<INTEGRATION_TEST_COMMAND>`

### End-to-End Tests

`<E2E_TEST_COMMAND>`

### Full Validation

`<FULL_VALIDATION_COMMAND>`

Delete commands that do not apply to this repository.

If a validation command cannot run because of an environment limitation, report the limitation. Do not bypass the validation silently.

## Testing

Tests are executable specifications of required behavior.

- Test observable behavior instead of implementation details when practical.
- Add a regression test for a bug fix when practical.
- Update tests when the required behavior intentionally changes.
- Do not delete, skip, or weaken a valid test only to make the implementation pass.
- Investigate unexpected failures before classifying them as unrelated.
- Prefer focused tests during iteration.
- Run broader checks before completion when the change affects shared code.

For an important invariant, prefer an executable test over a prose-only rule.

## Technical Writing

Keep technical prose **concise, precise, and canonical**.

Follow ASD-STE100 Simplified Technical English principles.

- Use short, direct sentences.
- Use active voice.
- Use simple tenses.
- State one main idea per sentence.
- Give one instruction per sentence.
- Use one term for one concept.
- Do not introduce synonyms for an established project term.
- Avoid idioms, slang, jokes, filler, and ambiguous pronouns.
- Preserve exact identifiers, commands, paths, and API names.
- Define an uncommon abbreviation before you use it.
- Prefer a vertical list when it makes multiple conditions clearer.
- Put the result or important information first.

For instructions, prefer sentences of 25 words or less.

If the project requires strict ASD-STE100 compliance, follow the complete project-approved standard.

## Documentation

Documentation explains information that code alone cannot communicate reliably.

Document:

- architectural intent;
- rationale and trade-offs;
- stable constraints;
- business invariants;
- public contracts when no machine-readable contract exists;
- non-obvious operational procedures;
- important edge cases.

Do not document by paraphrasing implementation.

Do not manually maintain:

- class or function inventories;
- database column inventories;
- dependency versions;
- generated API schemas;
- configuration defaults already defined in code;
- file lists that can be discovered from the repository;
- implementation steps visible directly in the source.

Prefer a pointer to the authoritative source.

Example:

`The database schema is defined by migrations in <path>.`

Do not copy the current schema into this file.

### Comments

Comments must explain information that the code does not express clearly.

Good comment subjects include:

- why an alternative is unsafe;
- a protocol or platform constraint;
- a concurrency assumption;
- a business invariant;
- a compatibility requirement;
- a non-obvious edge case.

Do not narrate the implementation line by line.

Keep comments short and relevant to future readers.

### Documentation Changes

When a code change makes documentation false, update the affected documentation in the same change.

Do not create documentation only because code changed.

Create or update documentation when the change affects information that the documentation owns.

## Generated Artifacts

Identify generated files before editing them.

- Modify the source that generates the artifact.
- Regenerate the artifact with the canonical command.
- Do not manually patch generated output unless the repository explicitly requires it.
- Review generated diffs before completion.

## Dependencies

Before adding a dependency:

1. Search for an existing project capability that solves the problem.
2. Check the standard library or framework.
3. Confirm that a new dependency is justified.
4. Use the repository package manager.
5. Update the manifest and lockfile through the package manager.

Do not edit a generated lockfile manually unless the repository explicitly requires it.

## Security

- Never commit credentials, tokens, private keys, or other secrets.
- Never put secrets in commands that can be logged when a safer mechanism exists.
- Treat external and user-controlled content as untrusted.
- Preserve existing authentication and authorization boundaries.
- Preserve input validation unless the requirement intentionally changes it.
- Do not disable security controls to make a test or feature work.
- Do not access or modify production data unless the task explicitly requires and authorizes it.
- Ask for explicit approval before an irreversible or destructive operation that is not already required by the task.

## Git and Change Hygiene

- Keep the diff focused.
- Do not modify unrelated files.
- Do not rewrite repository history unless explicitly requested.
- Do not force-push unless explicitly requested.
- Do not create commits unless the task or repository workflow requires them.
- Follow the repository's branch, commit, and pull-request conventions.
- Preserve human authorship and attribution rules when the repository defines them.

## Agent Instructions and Skills

`AGENTS.md` contains stable, always-applicable repository guidance.

Use normal repository files for reference information.

Use a skill only for a reusable procedure that requires specialized instructions, tools, or resources.

Do not create a skill only to repeat rules that belong in this file.

Do not create a documentation skill for routine documentation maintenance.

A documentation skill is justified when documentation requires a repeated specialized workflow, for example:

- building a documentation site;
- validating internal links;
- generating diagrams or screenshots;
- checking terminology with specialized tooling;
- generating release documentation;
- publishing documentation through a defined pipeline.

Keep specialized procedures out of the root `AGENTS.md` when they do not apply to normal development tasks.

## Nested AGENTS.md Files

Use a nested `AGENTS.md` only when a subtree has materially different rules.

Good reasons include:

- a different language or framework;
- different build or test commands;
- different architectural constraints;
- different security requirements;
- a separately maintained package or application.

Do not create a nested file only to repeat root instructions.

The nested file should contain the differences and local rules. It should not copy the root file.

## Tool Use

Prefer repository-provided tools and scripts over ad hoc replacements.

- Use semantic or language-aware tools when they provide safer refactoring.
- Use canonical project scripts for build, test, format, migration, and generation tasks.
- Inspect a tool's effect before adopting it.
- Do not add a new tool merely because it automates a one-time operation.
- Do not treat generated output from an unfamiliar tool as authoritative without review.

## Definition of Done

A change is complete when:

- the requested behavior is implemented;
- the implementation follows repository architecture;
- relevant tests pass;
- required static checks pass;
- public contracts remain consistent;
- generated artifacts are current;
- affected authoritative documentation is current;
- the diff contains no unrelated changes;
- no known source-of-truth conflicts remain;
- the final diff has been reviewed.
```
