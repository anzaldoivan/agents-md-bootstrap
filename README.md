# agents-md-bootstrap

An Agent Skill that bootstraps, audits, and maintains lean `AGENTS.md` files using repository evidence, canonical sources of truth, and a reusable policy baseline.

Most `AGENTS.md` generators scaffold instructions once. `agents-md-bootstrap` treats repository instructions as a maintained engineering artifact. It combines a reusable policy baseline with live repository evidence, points agents to canonical sources instead of copying facts, and audits instructions for drift as the repository changes.

## Use it

Install the complete [skills/agents-md-bootstrap](skills/agents-md-bootstrap/SKILL.md) directory into your agent client's supported skill location, retaining `assets/` and `references/`. Keep the repository's [MIT license](LICENSE) with redistributed copies. Discovery paths and invocation syntax depend on the client; no particular client or network service is required by this skill.

Ask your skill-capable agent, for example:

```text
Use agents-md-bootstrap to bootstrap lean AGENTS.md instructions for this repository.
Use agents-md-bootstrap to audit our agent instructions; report findings without editing.
Use agents-md-bootstrap to update agent instructions after our package-manager migration.
```

Bootstrap initializes or substantially improves instructions. Audit reports stale facts, duplicates, conflicts, dead rules, excessive scope, generic advice, and missing constraints. Maintain/update makes the smallest evidence-backed change needed after repository evolution. A healthy repository can produce no changes. “Lean” means concise and nonduplicative while preserving applicable obligations, not removing policy meaning to reach a length or section target.

## How it works

The skill inspects repository structure, executable checks, canonical documentation, and the topology of existing agent instructions before proposing rules. It distinguishes observed facts from selected personal policy and unresolved assumptions. It links to maintained sources instead of copying versions, command catalogs, dependency lists, or directory inventories into `AGENTS.md`.

The [reusable baseline](skills/agents-md-bootstrap/assets/baseline-agents.md) is a portable starting policy, not evidence about your project. Supply a personal baseline with the request to replace it, or adapt the applicable defaults. Policy preferences do not need proof of existing repository practice. The temporary evidence ledger accounts for retained, merged, inherited, inapplicable, and conflicting obligations; the report explains consequential omissions and verifies any claimed coverage elsewhere. Do not copy secrets, machine-specific paths, or private policy references into a shared repository. The skill asks targeted questions only when an unresolved decision would materially change the result.

One small root file is usually enough. Scoped files require demonstrated local constraints and confirmed client discovery behavior. The skill does not create per-directory instructions, new architecture documents, or tool-specific copies just to fill a template.

## Repository map

| Path | Purpose |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Lean instructions for contributors' agents |
| [SKILL.md](skills/agents-md-bootstrap/SKILL.md) | Entry point and mode routing |
| [assets/baseline-agents.md](skills/agents-md-bootstrap/assets/baseline-agents.md) | Reusable policy template |
| [references/](skills/agents-md-bootstrap/references/) | Evidence, conflicts, interview, audit, and output procedures |
| [evals/](evals/README.md) | Behavioral fixtures and review rubric |
| [scripts/validate.py](scripts/validate.py) | Offline deterministic repository checks |
| [validate.yml](.github/workflows/validate.yml) | CI running the same checks |

## Validation and contributions

Run `python3 scripts/validate.py` with Python 3.10 or newer; no third-party packages are required. It checks this repository's deliberately restricted frontmatter format, required resources, local Markdown file links, naming, unfinished markers, and lean entry-point budgets. It is not a general YAML parser or a behavioral evaluator. Follow [evals/README.md](evals/README.md) to assess actual agent decisions separately.

For changes, keep procedures in their owning reference, keep the root instructions lean, and add or revise a behavioral case when decisions change. Describe which cases you exercised; do not call a fixture listing a passing agent evaluation.

The layout and metadata were checked against the [Agent Skills specification](https://agentskills.io/specification) on 2026-09-26. This project uses required `name` and `description` fields, an optional SPDX license identifier, and progressive disclosure through supporting resources. Client instruction discovery and precedence remain client-specific.

Repository: [anzaldoivan/agents-md-bootstrap](https://github.com/anzaldoivan/agents-md-bootstrap). Licensed under [MIT](LICENSE).
