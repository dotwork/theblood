from unittest import TestCase

from models import A, A_sharp


########################################################################
class TestNote(TestCase):

    ####################################################################
    def test_equal_to_string(self):
        self.assertEqual('A', A)
        self.assertEqual(A, A)
        self.assertEqual('A♯', A_sharp)
        self.assertEqual('B♭', A_sharp)

    ####################################################################
    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            self.assertEqual(1, A)
        with self.assertRaises(TypeError):
            self.assertEqual(None, A)
