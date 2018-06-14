from unittest import TestCase

from models import A, A_sharp, B, F, E, G, F_flat, B_flat, G_sharp, A_flat, E_sharp, B_sharp, C_flat


########################################################################
class TestNote(TestCase):

    ####################################################################
    def test_equal_to_string(self):
        self.assertEqual('A', A)

    ####################################################################
    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            self.assertEqual(1, A)
        with self.assertRaises(TypeError):
            self.assertEqual(None, A)

    ####################################################################
    def test_equals__sharps_and_flats__going_down(self):
        self.assertEqual(A_sharp, B_flat)
        self.assertEqual(G_sharp, A_flat)
        self.assertEqual(E_sharp, F_flat)
        self.assertEqual(B_sharp, C_flat)

    ####################################################################
    def test_equals__sharps_and_flats__going_up(self):
        self.assertEqual(B_flat, A_sharp)
        self.assertEqual(A_flat, G_sharp)
        self.assertEqual(F_flat, E_sharp)
        self.assertEqual(C_flat, B_sharp)

    ####################################################################
    def test_next_whole_note(self):
        self.assertEqual(B, A.next_whole_note)
        self.assertEqual(F, E.next_whole_note)
        self.assertEqual(A, G.next_whole_note)

    ####################################################################
    def test_previous_whole_note(self):
        self.assertEqual(A, B.previous_whole_note)
        self.assertEqual(E, F.previous_whole_note)
        self.assertEqual(G, A.previous_whole_note)
