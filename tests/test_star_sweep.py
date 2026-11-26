import importlib.util
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location('star_sweep', Path(__file__).resolve().parents[1] / 'tools/star_sweep.py')
sweep = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sweep)


class StarSweepTests(unittest.TestCase):
    def test_suggestions_cover_count_existing_marker_and_exceptions(self):
        self.assertEqual(sweep.proposals('★★★ Attested.')[0]['proposal'], '✓')
        self.assertEqual(sweep.proposals('★★ Plausible.')[0]['proposal'], '~')
        self.assertEqual(sweep.proposals('★ Unsettled.')[0]['proposal'], '?')
        self.assertEqual(sweep.proposals('✓★★★ Attested.')[0]['proposal'], 'delete')
        self.assertEqual(sweep.proposals('★ Dispute: figures exaggerated.')[0]['proposal'], '✗')
        self.assertEqual(sweep.proposals('★ Dispute: a legend.')[0]['proposal'], '◇')
        self.assertTrue(sweep.proposals('★ Dispute: a legend.')[0]['dispute_label'])

    def test_inventory_only_reads_notes_and_lists_each_group(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'vol-1').mkdir()
            (root / 'vol-1' / 'chapter.md').write_text(
                'Body ★\n\n## Notes\n\n[1] ★ A claim; ★★ another.\n', encoding='utf-8')
            rows = sweep.inventory(root)
        self.assertEqual([r['stars'] for r in rows], ['★', '★★'])
        self.assertEqual([r['note'] for r in rows], [1, 1])
        self.assertEqual([r['line'] for r in rows], [5, 5])


if __name__ == '__main__':
    unittest.main()
