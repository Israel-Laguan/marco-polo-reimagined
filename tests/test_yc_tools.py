import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import cite_convert as cc  # noqa: E402
import yc_name_keys as nk  # noqa: E402
import yc_note_locate as nl  # noqa: E402


class NoteLocateTests(unittest.TestCase):
    def test_locator_forms(self):
        self.assertEqual(nl.locator(0, 17), '[@yc, Prol. 17]')
        self.assertEqual(nl.locator(2, 18), '[@yc, 2.18]')

    def test_yule_passage_is_clear_only_in_range(self):
        b, c, text, _ = next(ch for ch in cc.chapters() if (ch[0], ch[1]) == (2, 18))
        para = ' '.join(text.split()[:120])
        self.assertEqual(nl.classify(para, {(2, 18)})[:2], ('clear', (2, 18)))
        self.assertEqual(nl.classify(para, {(2, 19)})[0], 'out of range')
        self.assertEqual(nl.classify('a few words of our own', {(2, 18)})[0], 'no match')


class NameKeyTests(unittest.TestCase):
    def test_modern_translation_is_refused(self):
        self.assertIsNone(nk.decide('Ibn Baṭṭūṭa', '2.20')[0])

    def test_edition_yule_used_and_unknown_name(self):
        self.assertEqual(nk.decide('Gaubil', '2.8')[0], 'gaubil1739histoire')
        self.assertEqual(nk.decide('Nobody', '2.8'), (None, 'no candidate key'))

    def test_convert_keys_only_the_decided_name(self):
        log = []
        line = nk.convert('As cited in Yule: Ibn Baṭṭūṭa, Gaubil [@yc, 2.8].', log, 'x')
        self.assertIn('Gaubil [-@gaubil1739histoire] [@yc, 2.8]', line)
        self.assertIn('Ibn Baṭṭūṭa,', line)


if __name__ == '__main__':
    unittest.main()
