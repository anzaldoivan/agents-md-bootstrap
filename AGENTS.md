# Repository guidance

- [skills/agents-md-bootstrap/SKILL.md](skills/agents-md-bootstrap/SKILL.md) is the Skill entry point and owns mode routing.
- [production-agents-template.md](skills/agents-md-bootstrap/references/production-agents-template.md) owns canonical policy obligations and stable IDs; these are not repository facts.
- [references/](skills/agents-md-bootstrap/references/) owns detailed procedures. Change the relevant reference rather than duplicating it here.
- [evals/](evals/README.md) contains behavioral examples and the evaluation rubric.
- Run `python3 scripts/validate.py` after changes. [The validator](scripts/validate.py) and [CI](.github/workflows/validate.yml) own executable checks; behavioral claims require separate evaluation.
- Keep the skill portable: no dependency on a specific agent client, private baseline, or local machine path.
