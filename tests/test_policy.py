"""Objective invariants only; behavioral meaning is evaluated separately."""
import copy
import hashlib
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / 'skills/agents-md-bootstrap/scripts/validate_policy.py'
spec = importlib.util.spec_from_file_location('policy', HELPER)
policy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(policy)


class PolicyTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'AGENTS.md').write_text('Run owned checks. Preserve valid checks.\n')
        (self.root / 'parent.md').write_text('Preserve valid checks.\n')
        (self.root / 'client.json').write_text('Parent applies to this target.\n')
        (self.root / 'Makefile').write_text('lint:\n\tpython3 scripts/lint.py\n# canonical: make lint\n')
        self.catalog = {'TEST-001': 'universal', 'TEST-002': 'universal', 'GEN-002': 'conditional: generated artifacts exist'}
        self.data = {'version': 1, 'policy': 'bundled', 'mode': 'bootstrap', 'scope': '.', 'coverage': 'full', 'expected_ids': list(self.catalog), 'entries': [
            {'id': 'TEST-001', 'disposition': 'retained', 'output': self.loc('AGENTS.md', 'Run owned checks.')},
            {'id': 'TEST-002', 'disposition': 'merged', 'output': self.loc('AGENTS.md', 'Preserve valid checks.')},
            {'id': 'GEN-002', 'disposition': 'inapplicable', 'reason': 'No generation workflow after inventory inspection', 'evidence': self.inspection()},
        ]}

    def loc(self, path, quote):
        return {'path': path, 'quote': quote}

    def inspection(self):
        return [{'inspection': 'Reviewed full relevant inventory and task definitions.', 'paths': ['.']}]

    def errors(self, require=False):
        return policy.validate_ledger(self.data, self.catalog, self.root, require)

    def assert_error(self, substring, require=False):
        self.assertTrue(any(substring in e for e in self.errors(require)), self.errors(require))

    def inherited(self):
        entry = self.data['entries'][1]
        entry.clear()
        entry.update(id='TEST-002', disposition='verified-inherited', source=self.loc('parent.md', 'Preserve valid checks.'), scope='.', discovery=self.loc('client.json', 'Parent applies to this target.'))
        entry['source']['sha256'] = hashlib.sha256((self.root / 'parent.md').read_bytes()).hexdigest()
        return entry

    def check(self, state):
        value = {'kind': 'lint', 'scope': '.', 'state': state, 'evidence': self.inspection()}
        if state == 'DETECTED':
            value.update(command='make lint', cwd='.', invocation=self.loc('Makefile', 'make lint'))
        else:
            value['assessment'] = 'Inspected sources do not establish a canonical invocation.'
        self.data['checks'] = [value]
        return value

    def test_valid_accounting(self):
        self.assertEqual([], self.errors(True))

    def test_invalid_id(self):
        self.data['expected_ids'][0] = 'FAKE-001'
        self.assert_error('unknown obligation')

    def test_omission(self):
        self.data['entries'].pop(0)
        self.assert_error('missing disposition')

    def test_cannot_shrink_full_expected_set(self):
        self.data['expected_ids'].pop(0)
        self.data['entries'].pop(0)
        self.assert_error('every catalog ID')

    def test_duplicate_disposition(self):
        self.data['entries'].append(copy.deepcopy(self.data['entries'][0]))
        self.assert_error('duplicate disposition')

    def test_duplicate_expected(self):
        self.data['expected_ids'].append('TEST-001')
        self.assert_error('duplicate expected')

    def test_missing_output(self):
        del self.data['entries'][0]['output']
        self.assert_error('requires path')

    def test_bad_merged_locator(self):
        self.data['entries'][1]['output']['quote'] = 'Not in file'
        self.assert_error('not found')

    def test_inapplicable_evidence(self):
        self.data['entries'][2]['evidence'] = []
        self.assert_error('inspection evidence')

    def test_universal_not_inapplicable(self):
        self.data['entries'][0] = dict(self.data['entries'][2], id='TEST-001')
        self.assert_error('universal semantic')

    def test_inheritance(self):
        self.inherited()
        self.assertEqual([], self.errors(True))

    def test_inheritance_missing_scope(self):
        self.inherited().pop('scope')
        self.assert_error('applicable scope')

    def test_inheritance_missing_discovery(self):
        self.inherited().pop('discovery')
        self.assert_error('discovery basis')

    def test_inheritance_missing_content(self):
        self.inherited()['source']['quote'] = 'Run all checks'
        self.assert_error('not found')

    def test_inheritance_hash_drift(self):
        self.inherited()
        (self.root / 'parent.md').write_text('Preserve valid checks. Changed context.\n')
        self.assert_error('changed source SHA-256')

    def test_conflicting_requires_authority(self):
        self.data['entries'][1] = {'id': 'TEST-002', 'disposition': 'conflicting', 'source': self.loc('parent.md', 'Preserve valid checks.'), 'scope': '.', 'human_resolution_required': True}
        self.assert_error('authority')

    def test_conflict_source_and_resolution(self):
        self.data['entries'][1] = {'id': 'TEST-002', 'disposition': 'conflicting', 'authority': 'explicit user policy', 'scope': '.', 'human_resolution_required': False}
        self.assert_error('conflict source')
        self.assert_error('resolution')

    def test_unresolved_conflict_not_covered(self):
        self.data['entries'][1] = {'id': 'TEST-002', 'disposition': 'conflicting', 'source': self.loc('parent.md', 'Preserve valid checks.'), 'scope': '.', 'authority': 'user', 'human_resolution_required': True}
        self.assertEqual([], self.errors())
        self.assert_error('unresolved conflict', True)

    def test_audit_gap_is_not_bootstrap_completion(self):
        self.data['entries'][1] = {'id': 'TEST-002', 'disposition': 'uncovered', 'reason': 'Inspected root lacks integrity policy', 'evidence': self.inspection()}
        self.assert_error('uncovered obligation')
        self.data['mode'] = 'audit'
        self.assertEqual([], self.errors())
        self.assert_error('uncovered obligation', True)

    def test_focused_requires_reason(self):
        self.data.update(mode='maintain', coverage='focused', expected_ids=['TEST-001'])
        self.data['entries'] = self.data['entries'][:1]
        self.assert_error('selection_reason')
        self.data['selection_reason'] = 'Only check invocation changed'
        self.assertEqual([], self.errors(True))

    def test_supplied_policy(self):
        self.data.update(policy='supplied', selection_reason='Replaces bundled policy', expected_ids=['USER-001'], supplied=[{'id': 'USER-001', 'source': self.loc('parent.md', 'Preserve valid checks.')}])
        self.data['entries'] = [dict(self.data['entries'][1], id='USER-001')]
        self.assertEqual([], self.errors(True))
        self.data['supplied'] = []
        self.assert_error('declarations must match')

    def test_detected_command(self):
        self.check('DETECTED')
        self.assertEqual([], self.errors(True))
        del self.data['checks'][0]['invocation']
        self.assert_error('invocation')

    def test_ambiguous_no_command(self):
        self.check('AMBIGUOUS')['command'] = 'npx eslint .'
        self.assert_error('cannot carry')

    def test_absent_no_command(self):
        self.check('ABSENT')['command'] = 'ruff check .'
        self.assert_error('cannot carry')

    def test_unauthorized_tooling(self):
        self.check('ABSENT')['install_tooling'] = 'eslint'
        self.assert_error('installation is outside')

    def test_question_threshold(self):
        value = self.check('AMBIGUOUS')
        value.update(question='Which existing command is canonical?', material_reason='User requested required check list')
        self.assertEqual([], self.errors())
        self.assert_error('pending material question', True)
        value['state'] = 'ABSENT'
        self.assert_error('questions require ambiguity')

    def test_question_materiality(self):
        self.check('AMBIGUOUS')['question'] = 'Which command?'
        self.assert_error('materiality')

    def test_duplicate_capability_scope(self):
        check = self.check('ABSENT')
        self.data['checks'].append(copy.deepcopy(check))
        self.assert_error('duplicate capability')

    def test_inspection_limits(self):
        self.data['inspection_limits'] = ['Parent cannot be inspected']
        self.assertEqual([], self.errors())
        self.assert_error('inspection limits', True)

    def test_output_control_leak(self):
        with (self.root / 'AGENTS.md').open('a') as f:
            f.write('TEST-002\n')
        self.assert_error('leaked')

    def test_template_slot_leak(self):
        with (self.root / 'AGENTS.md').open('a') as f:
            f.write('<LINT_COMMAND>\n')
        self.assert_error('leaked')

    def test_malformed_data_is_error(self):
        for key in ('mode', 'policy', 'coverage'):
            with self.subTest(key=key):
                original = self.data[key]
                self.data[key] = []
                self.assertTrue(self.errors())
                self.data[key] = original
        self.data['entries'][0]['disposition'] = []
        self.assert_error('invalid disposition')
        self.check([])
        self.assert_error('invalid validation state')

    def test_semantics_not_faked_by_validator(self):
        # Structurally located text can still be semantically inadequate.
        self.data['entries'][1]['output']['quote'] = 'Run owned checks.'
        self.assertEqual([], self.errors())

    def test_catalog_unique_reorder_and_empty(self):
        path = self.root / 'catalog.md'
        first = '### TEST-001\n\nApplicability: universal\n\nRun owned checks.\n\n'
        second = '### TEST-002\n\nApplicability: universal\n\nPreserve valid checks.\n\n'
        path.write_text(first + second)
        before, errors = policy.read_catalog(path)
        self.assertEqual([], errors)
        path.write_text(second + first)
        self.assertEqual((before, []), policy.read_catalog(path))
        path.write_text(first + first)
        self.assertTrue(any('duplicate' in e for e in policy.read_catalog(path)[1]))
        path.write_text('### TEST-001\n\nApplicability: universal\n\n## Next family\n\n' + second)
        self.assertTrue(policy.read_catalog(path)[1])

    def test_real_catalog_and_pinned_integrity_id(self):
        catalog, errors = policy.read_catalog()
        self.assertEqual([], errors)
        self.assertEqual('universal', catalog['TEST-002'])

    def test_cli_invalid_json_is_nonzero(self):
        path = self.root / 'ledger.json'
        path.write_text('{')
        result = subprocess.run([sys.executable, '-B', str(HELPER), '--ledger', str(path)], capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
        self.assertIn('FAIL: ledger', result.stderr)


if __name__ == '__main__':
    unittest.main()
