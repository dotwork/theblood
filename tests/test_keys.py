from unittest import TestCase

from models import Key, A, B, C, D, E, F, G


########################################################################
class TestKey(TestCase):

    ####################################################################
    def test_generate_notes(self):
        c_major = Key('C')
        expected = [C, D, E, F, G, A, B]
        self.assertEqual(expected, c_major.notes)
