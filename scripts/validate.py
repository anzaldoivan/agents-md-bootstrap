#!/usr/bin/env python3
"""Offline repository checks; deliberately not a general Agent Skills validator."""

from pathlib import Path
import importlib.util
import os
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL = Path('skills/agents-md-bootstrap')
REQUIRED = (
    'README.md', 'LICENSE', 'AGENTS.md', '.github/workflows/validate.yml',
    'scripts/validate.py', 'evals/README.md',
    'evals/cases/tiny-project.md', 'evals/cases/service-project.md',
    'evals/cases/monorepo.md', 'evals/cases/policy-preservation.md',
    'evals/cases/canonical-accounting.md', 'evals/cases/validation-gaps.md',
    'tests/test_policy.py',
    str(SKILL / 'SKILL.md'), str(SKILL / 'scripts/validate_policy.py'),
    *(str(SKILL / 'references' / name) for name in (
        'evidence-policy.md', 'conflict-resolution.md', 'interview-policy.md',
        'audit-checklist.md', 'output-contract.md',
        'production-agents-template.md', 'policy-accounting.md',
    )),
)


def validate(root: Path) -> list[str]:
    errors = []
    for name in REQUIRED:
        path = root / name
        if not path.is_file() or not path.read_text(encoding='utf-8').strip():
            errors.append(f'{name}: required nonempty file missing')
    sys.dont_write_bytecode = True
    catalog = {}
    helper = root / SKILL / 'scripts/validate_policy.py'
    if helper.is_file():
        spec = importlib.util.spec_from_file_location('policy_validation', helper)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        catalog, catalog_errors = module.read_catalog(root / SKILL / 'references/production-agents-template.md')
        errors.extend(catalog_errors)
    if (root / SKILL / 'assets/baseline-agents.md').exists():
        errors.append('obsolete independent baseline asset must not coexist with canonical catalog')
    entry = root / SKILL / 'SKILL.md'
    if entry.is_file():
        content = entry.read_text(encoding='utf-8')
        match = re.fullmatch(r'---\n(.*?)\n---\n(.+)', content, re.S)
        if not match:
            errors.append(f'{SKILL}/SKILL.md: missing frontmatter or body')
        else:
            fields = {}
            for line in match[1].splitlines():
                # Project convention: one-line unquoted plain string fields only.
                item = re.fullmatch(r'([a-z-]+): ([A-Za-z0-9][^\n]*)', line)
                if not item or ': ' in item[2] or ' #' in item[2]:
                    errors.append(f'SKILL.md: unsupported frontmatter line: {line!r}')
                    continue
                key, value = item.groups()
                if key in fields:
                    errors.append(f'SKILL.md: duplicate field {key}')
                fields[key] = value
            if set(fields) != {'name', 'description', 'license'}:
                errors.append('SKILL.md: expected name, description, license fields')
            name = fields.get('name', '')
            if (name != SKILL.name or len(name) > 64
                    or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name)):
                errors.append('SKILL.md: invalid or inconsistent name')
            if not 1 <= len(fields.get('description', '')) <= 1024:
                errors.append('SKILL.md: description must contain 1–1024 characters')
            if fields.get('license') != 'MIT':
                errors.append('SKILL.md: expected MIT license')

    docs = sorted(root.glob('*.md'))
    docs += sorted((root / 'skills').rglob('*.md'))
    docs += sorted((root / 'evals').rglob('*.md'))
    for path in docs:
        content = path.read_text(encoding='utf-8')
        label = path.relative_to(root)
        if 'agents-md-' + 'maintainer' in content:
            errors.append(f'{label}: inconsistent project name')
        if re.search(r'\b(?:TODO|TBD|FIXME)\b|\[INSERT\b|<placeholder>', content):
            errors.append(f'{label}: unfinished marker')
        # Inline file links in authored prose; fenced examples are not links.
        prose = re.sub(r'^```.*?^```[^\n]*$', '', content, flags=re.M | re.S)
        if 'results' not in path.relative_to(root).parts:
            for key in re.findall(r'\b[A-Z]{2,10}-[0-9]{3}\b', prose):
                if key not in catalog and not key.startswith('USER-'):
                    errors.append(f'{label}: unknown canonical obligation reference: {key}')
        for target in re.findall(r'\[[^\]\n]+\]\(([^)\s]+)\)', prose):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve()
            if not destination.is_relative_to(root.resolve()):
                errors.append(f'{label}: link escapes repository: {target}')
            elif not destination.exists():
                errors.append(f'{label}: broken local link: {target}')
    license_path = root / 'LICENSE'
    if license_path.is_file() and not license_path.read_text().startswith('MIT License\n'):
        errors.append('LICENSE: expected MIT license')
    return errors


if __name__ == '__main__':
    failures = validate(ROOT)
    if failures:
        print('\n'.join(f'FAIL: {failure}' for failure in failures), file=sys.stderr)
        sys.exit(1)
    for path, count, limit in ((ROOT / SKILL / 'SKILL.md', 'lines', 500), (ROOT / 'AGENTS.md', 'words', 250)):
        content = path.read_text(encoding='utf-8')
        size = len(content.splitlines() if count == 'lines' else content.split())
        if size >= limit:
            print(f'NOTE: {path.name} has {size} {count}; review concision without dropping obligations')
    result = subprocess.run([sys.executable, '-B', '-m', 'unittest', 'discover', '-s', 'tests'], cwd=ROOT, env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'})
    if result.returncode:
        sys.exit(result.returncode)
    print('PASS: metadata, resources, naming, links, markers, canonical IDs, and policy regression tests; semantics require review')
