# Repository guidance

- [skills/agents-md-bootstrap/SKILL.md](skills/agents-md-bootstrap/SKILL.md) is the Skill entry point and owns mode routing.
- [assets/baseline-agents.md](skills/agents-md-bootstrap/assets/baseline-agents.md) owns reusable policy defaults; these are not repository facts.
- [references/](skills/agents-md-bootstrap/references/) owns detailed procedures. Change the relevant reference rather than duplicating it here.
- [evals/](evals/README.md) contains behavioral examples and the evaluation rubric.
- Run `python3 scripts/validate.py` after changes. [The validator](scripts/validate.py) and [CI](.github/workflows/validate.yml) own executable checks; behavioral claims require separate evaluation.
- Keep the skill portable: no dependency on a specific agent client, private baseline, or local machine path.
