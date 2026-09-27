#!/usr/bin/env python3
"""Validate catalog/ledger structure, never semantic equivalence or command safety."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

CATALOG = Path(__file__).resolve().parents[1] / 'references/production-agents-template.md'
ID = re.compile(r'(?:CORE|EVID|ARCH|TEST|WRITE|DOC|GEN|DEP|SEC|GIT|TOOL|SCOPE|DONE)-[0-9]{3}')
USER_ID = re.compile(r'USER-[0-9]{3}')
DISPOSITIONS = {'retained', 'merged', 'verified-inherited', 'inapplicable', 'conflicting', 'uncovered'}
KINDS = {'format', 'lint', 'type', 'static', 'tests', 'build', 'security'}


def read_catalog(path=CATALOG):
    """Return ID -> applicability; prose stays solely in the Markdown source."""
    catalog, errors = {}, []
    try:
        text = Path(path).read_text(encoding='utf-8')
    except (OSError, UnicodeError) as exc:
        return {}, [f'catalog: {exc}']
    blocks = re.findall(r'^### ([^\n]+)\n([\s\S]*?)(?=^#{1,3} |\Z)', text, flags=re.M)
    for key, body in blocks:
        if not ID.fullmatch(key):
            errors.append(f'catalog: invalid obligation heading {key!r}')
            continue
        if key in catalog:
            errors.append(f'catalog: duplicate ID {key}')
        match = re.fullmatch(r'\nApplicability: (universal|conditional: [^\n]+)\n\n(\S[\s\S]*?)\s*', body)
        if not match:
            errors.append(f'{key}: expected applicability and nonempty obligation prose')
            continue
        catalog[key] = match[1]
    if not catalog:
        errors.append('catalog: no obligations')
    return catalog, errors


def validate_ledger(data, catalog, root, require_covered=False):
    """Check evidence presence/locations; reviewer must verify meaning and scope."""
    errors = []
    root = Path(root)

    def fail(label, message):
        errors.append(f'{label}: {message}')

    def nonempty(value):
        return isinstance(value, str) and bool(value.strip())

    def locator(value, label, fingerprint=False):
        if not isinstance(value, dict) or not nonempty(value.get('path')) or not nonempty(value.get('quote')):
            fail(label, 'requires path and supporting quote')
            return
        try:
            raw = (root / value['path']).read_bytes()
            content = raw.decode('utf-8')
        except (OSError, UnicodeError) as exc:
            fail(label, f'cannot read evidence: {exc}')
            return
        if value['quote'] not in content:
            fail(label, 'supporting quote not found at source/output')
        if fingerprint:
            digest = hashlib.sha256(raw).hexdigest()
            if value.get('sha256') != digest:
                fail(label, 'missing or changed source SHA-256; reinspect inheritance')

    def evidence(value, label):
        if not isinstance(value, list) or not value:
            fail(label, 'requires nonempty inspection evidence')
            return
        for i, item in enumerate(value):
            loc = f'{label}[{i}]'
            if isinstance(item, dict) and 'path' in item:
                locator(item, loc)
            elif isinstance(item, dict) and nonempty(item.get('inspection')) and isinstance(item.get('paths'), list) and item['paths']:
                for path in item['paths']:
                    if not nonempty(path) or not (root / path).exists():
                        fail(loc, 'inspection paths must exist')
            else:
                fail(loc, 'requires a source locator or inspection with inspected paths')

    if not isinstance(data, dict):
        return ['ledger: expected object']
    if data.get('version') != 1 or isinstance(data.get('version'), bool):
        fail('ledger', 'version must be 1')
    mode, policy, coverage = (data.get(k) for k in ('mode', 'policy', 'coverage'))
    if not isinstance(mode, str) or mode not in {'bootstrap', 'audit', 'maintain'}:
        fail('ledger', 'invalid mode')
    if not isinstance(policy, str) or policy not in {'bundled', 'supplied'}:
        fail('ledger', 'invalid policy selection')
    if not isinstance(coverage, str) or coverage not in {'full', 'focused'}:
        fail('ledger', 'invalid coverage selection')
    if not nonempty(data.get('scope')):
        fail('ledger', 'target scope required')
    if coverage == 'focused' and mode != 'maintain':
        fail('ledger', 'focused coverage is only for maintenance')
    if coverage == 'focused' or policy == 'supplied':
        if not nonempty(data.get('selection_reason')):
            fail('ledger', 'selection_reason required')
    expected = data.get('expected_ids')
    if not isinstance(expected, list) or not expected or not all(nonempty(x) for x in expected):
        return errors + ['ledger: expected_ids must be a nonempty string list']
    if len(set(expected)) != len(expected):
        fail('ledger', 'duplicate expected ID')
    known = dict(catalog)
    supplied = data.get('supplied', [])
    if not isinstance(supplied, list):
        fail('ledger', 'supplied must be a list')
        supplied = []
    supplied_ids = set()
    for item in supplied:
        if not isinstance(item, dict) or not isinstance(item.get('id'), str):
            fail('supplied', 'invalid declaration')
            continue
        key = item['id']
        if key in supplied_ids or (key not in catalog and not USER_ID.fullmatch(key)):
            fail(key, 'duplicate or invalid supplied ID')
        supplied_ids.add(key)
        locator(item.get('source'), key + ' supplied source')
        known.setdefault(key, 'supplied')
    if policy == 'bundled' and supplied:
        fail('ledger', 'supplied declarations require supplied policy selection')
    if policy == 'supplied' and set(expected) != supplied_ids:
        fail('ledger', 'supplied declarations must match expected_ids')
    if policy == 'bundled' and coverage == 'full' and set(expected) != set(catalog):
        fail('ledger', 'full bundled accounting must include every catalog ID')
    for key in expected:
        if key not in known:
            fail(key, 'unknown obligation ID')
    entries = data.get('entries')
    if not isinstance(entries, list):
        return errors + ['ledger: entries must be a list']
    seen = set()
    for entry in entries:
        if not isinstance(entry, dict) or not nonempty(entry.get('id')):
            fail('entry', 'requires ID')
            continue
        key = entry['id']
        if key in seen:
            fail(key, 'duplicate disposition')
        seen.add(key)
        if key not in expected:
            fail(key, 'ID outside evaluated set')
        disposition = entry.get('disposition')
        if not isinstance(disposition, str) or disposition not in DISPOSITIONS:
            fail(key, 'invalid disposition')
        elif disposition in {'retained', 'merged'}:
            locator(entry.get('output'), key + ' output')
        elif disposition == 'verified-inherited':
            locator(entry.get('source'), key + ' inherited source', fingerprint=True)
            locator(entry.get('discovery'), key + ' discovery basis')
            if not nonempty(entry.get('scope')):
                fail(key, 'inherited applicable scope required')
        elif disposition == 'inapplicable':
            evidence(entry.get('evidence'), key)
            if not nonempty(entry.get('reason')):
                fail(key, 'inapplicability reason required')
            if known.get(key) == 'universal':
                fail(key, 'universal semantic obligation cannot be excluded for missing tooling')
        elif disposition == 'conflicting':
            locator(entry.get('source'), key + ' conflict source')
            if not nonempty(entry.get('authority')) or not nonempty(entry.get('scope')):
                fail(key, 'conflicting authority and scope required')
            human = entry.get('human_resolution_required')
            if not isinstance(human, bool):
                fail(key, 'human_resolution_required must be boolean')
            if human is False and not nonempty(entry.get('resolution')):
                fail(key, 'resolved conflict needs resolution')
            if require_covered and human is not False:
                fail(key, 'unresolved conflict prevents coverage claim')
        elif disposition == 'uncovered':
            evidence(entry.get('evidence'), key)
            if not nonempty(entry.get('reason')):
                fail(key, 'coverage gap reason required')
            if mode == 'bootstrap' or require_covered:
                fail(key, 'uncovered obligation prevents completion')
    for key in sorted(set(expected) - seen):
        fail(key, 'missing disposition')
    limits = data.get('inspection_limits', [])
    if not isinstance(limits, list) or not all(nonempty(x) for x in limits):
        fail('ledger', 'inspection_limits must be a list of nonempty strings')
    elif require_covered and limits:
        fail('ledger', 'inspection limits prevent full coverage claim')
    checks = data.get('checks', [])
    if not isinstance(checks, list):
        fail('ledger', 'checks must be a list')
        checks = []
    check_keys = set()
    for check in checks:
        if not isinstance(check, dict):
            fail('check', 'expected object')
            continue
        label = str(check.get('kind', 'check'))
        state = check.get('state')
        if not isinstance(check.get('kind'), str) or check.get('kind') not in KINDS or not nonempty(check.get('scope')):
            fail(label, 'known kind and scope required')
        else:
            key = (check['kind'], check['scope'])
            if key in check_keys:
                fail(label, 'duplicate capability/scope assessment')
            check_keys.add(key)
        evidence(check.get('evidence'), label)
        if state == 'DETECTED':
            if not nonempty(check.get('command')) or not nonempty(check.get('cwd')):
                fail(label, 'detected check requires canonical command and working directory')
            locator(check.get('invocation'), label + ' invocation')
            if nonempty(check.get('cwd')) and not (root / check['cwd']).is_dir():
                fail(label, 'working directory not found')
        elif isinstance(state, str) and state in {'AMBIGUOUS', 'ABSENT'}:
            if 'command' in check or 'invocation' in check or 'cwd' in check:
                fail(label, 'ambiguous/absent capability cannot carry a generated command')
            if not nonempty(check.get('assessment')):
                fail(label, 'assessment required')
        else:
            fail(label, 'invalid validation state')
        if 'question' in check:
            if state != 'AMBIGUOUS' or not nonempty(check['question']) or not nonempty(check.get('material_reason')):
                fail(label, 'questions require ambiguity and materiality evidence')
            if require_covered:
                fail(label, 'pending material question prevents completion claim')
        if check.get('install_tooling'):
            fail(label, 'tool installation is outside normal instruction maintenance')
    generated = data.get('generated', [])
    if not isinstance(generated, list):
        fail('ledger', 'generated must be a path list')
        generated = []
    # Inspect every claimed output as well, so omitting generated[] cannot hide leakage.
    outputs = {e['output']['path'] for e in entries if isinstance(e, dict) and isinstance(e.get('output'), dict) and nonempty(e['output'].get('path'))}
    for path in generated:
        if nonempty(path):
            outputs.add(path)
        else:
            fail('generated', 'invalid path')
    for path in sorted(outputs):
        try:
            text = (root / path).read_text(encoding='utf-8')
        except (OSError, UnicodeError) as exc:
            fail(path, str(exc))
            continue
        if re.search(r'\b(?:' + '|'.join(sorted({k.split('-')[0] for k in catalog})) + r'|USER)-[0-9]{3}\b|^Applicability:|<[A-Z][A-Z_]+>', text, re.M):
            fail(path, 'internal catalog ID, applicability field, or template slot leaked to output')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--catalog', type=Path, default=CATALOG)
    parser.add_argument('--ledger', type=Path)
    parser.add_argument('--root', type=Path, default=Path.cwd(), help='Base for evidence/output paths; only reads files')
    parser.add_argument('--require-covered', action='store_true')
    args = parser.parse_args()
    catalog, errors = read_catalog(args.catalog)
    if args.ledger:
        try:
            data = json.loads(args.ledger.read_text(encoding='utf-8'))
            errors += validate_ledger(data, catalog, args.root, args.require_covered)
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(f'ledger: {exc}')
    elif args.require_covered:
        errors.append('--require-covered requires --ledger')
    if errors:
        print('\n'.join('FAIL: ' + e for e in errors), file=sys.stderr)
        return 1
    print(f'PASS: {len(catalog)} canonical IDs; structural accounting only, semantic review still required')
    return 0


if __name__ == '__main__':
    sys.exit(main())
