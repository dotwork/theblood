from unittest import TestCase

from models import Note, InvalidNoteError
from objects import A_flat, A, A_sharp, B_flat, B, B_sharp, C_flat, C, C_sharp, D_flat, D, D_sharp, E_flat, E, E_sharp, \
    F_flat, F, F_sharp, G_flat, G, G_sharp


########################################################################
class TestNote(TestCase):

    ####################################################################
    def test_equal_to_string(self):
        self.assertEqual('A', A)

    ####################################################################
    def test_invalid_name(self):
        with self.assertRaises(InvalidNoteError):
            Note('A#foo')

    ####################################################################
    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            self.assertEqual(1, A)
        with self.assertRaises(TypeError):
            self.assertEqual(None, A)

    ####################################################################
    def test_equals__natural_notes(self):
        self.assertEqual(A, A)
        self.assertEqual(B, B)
        self.assertEqual(C, C)
        self.assertEqual(D, D)
        self.assertEqual(E, E)
        self.assertEqual(F, F)
        self.assertEqual(G, G)

    ####################################################################
    def test_is_equal_pitch_to__standard_flats(self):
        self.assertTrue(B_flat.harmonically_equivalent_to(A_sharp))
        self.assertTrue(D_flat.harmonically_equivalent_to(C_sharp))
        self.assertTrue(E_flat.harmonically_equivalent_to(D_sharp))
        self.assertTrue(G_flat.harmonically_equivalent_to(F_sharp))
        self.assertTrue(A_flat.harmonically_equivalent_to(G_sharp))

    ####################################################################
    def test_is_equal_pitch_to__standard_sharps(self):
        self.assertTrue(A_sharp.harmonically_equivalent_to(B_flat))
        self.assertTrue(C_sharp.harmonically_equivalent_to(D_flat))
        self.assertTrue(D_sharp.harmonically_equivalent_to(E_flat))
        self.assertTrue(F_sharp.harmonically_equivalent_to(G_flat))
        self.assertTrue(G_sharp.harmonically_equivalent_to(A_flat))

    ####################################################################
    def test_is_equal_pitch_to__non_standard_flats(self):
        self.assertTrue(C_flat.harmonically_equivalent_to(B))
        self.assertTrue(F_flat.harmonically_equivalent_to(E))

        self.assertTrue(B.harmonically_equivalent_to(C_flat))
        self.assertTrue(E.harmonically_equivalent_to(F_flat))

    ####################################################################
    def test_is_equal_pitch_to__non_standard_sharps(self):
        self.assertTrue(C.harmonically_equivalent_to(B_sharp))
        self.assertTrue(B_sharp.harmonically_equivalent_to(C))

        self.assertTrue(F.harmonically_equivalent_to(E_sharp))
        self.assertTrue(E_sharp.harmonically_equivalent_to(F))

    ####################################################################
    def test_next_natural_note__from_natural_note(self):
        self.assertEqual(B, A.next_natural_note)
        self.assertEqual(C, B.next_natural_note)
        self.assertEqual(D, C.next_natural_note)
        self.assertEqual(E, D.next_natural_note)
        self.assertEqual(F, E.next_natural_note)
        self.assertEqual(G, F.next_natural_note)
        self.assertEqual(A, G.next_natural_note)

    ####################################################################
    def test_next_natural_note__from_sharp(self):
        self.assertEqual(B, A_sharp.next_natural_note)
        self.assertEqual(D, C_sharp.next_natural_note)
        self.assertEqual(E, D_sharp.next_natural_note)
        self.assertEqual(G, F_sharp.next_natural_note)
        self.assertEqual(A, G_sharp.next_natural_note)

        self.assertEqual(C, B_sharp.next_natural_note)
        self.assertEqual(F, E_sharp.next_natural_note)

    ####################################################################
    def test_next_natural_note__from_flat(self):
        self.assertEqual(B, A_flat.next_natural_note)
        self.assertEqual(D, C_flat.next_natural_note)
        self.assertEqual(E, D_flat.next_natural_note)
        self.assertEqual(G, F_flat.next_natural_note)
        self.assertEqual(A, G_flat.next_natural_note)
        self.assertEqual(C, B_flat.next_natural_note)
        self.assertEqual(F, E_flat.next_natural_note)

    ####################################################################
    def test_previous_natural_note__from_natural_note(self):
        self.assertEqual(A, B.previous_natural_note)
        self.assertEqual(B, C.previous_natural_note)
        self.assertEqual(C, D.previous_natural_note)
        self.assertEqual(D, E.previous_natural_note)
        self.assertEqual(E, F.previous_natural_note)
        self.assertEqual(F, G.previous_natural_note)
        self.assertEqual(G, A.previous_natural_note)

    ####################################################################
    def test_previous_natural_note__from_sharp(self):
        self.assertEqual(B, C_sharp.previous_natural_note)
        self.assertEqual(C, D_sharp.previous_natural_note)
        self.assertEqual(E, F_sharp.previous_natural_note)
        self.assertEqual(F, G_sharp.previous_natural_note)
        self.assertEqual(G, A_sharp.previous_natural_note)

        self.assertEqual(A, B_sharp.previous_natural_note)
        self.assertEqual(D, E_sharp.previous_natural_note)

    ####################################################################
    def test_not_equal(self):
        self.assertNotEqual(B, C_flat)
        self.assertNotEqual(B, B_sharp)
        self.assertNotEqual(B, C)
        self.assertNotEqual(B, C_sharp)
        self.assertNotEqual(B, D_flat)
        self.assertNotEqual(B, D)
        self.assertNotEqual(B, D_sharp)
        self.assertNotEqual(B, E_flat)
        self.assertNotEqual(B, E)
        self.assertNotEqual(B, E_sharp)
        self.assertNotEqual(B, F_flat)
        self.assertNotEqual(B, F)
        self.assertNotEqual(B, F_sharp)
        self.assertNotEqual(B, G_flat)
        self.assertNotEqual(B, G)
        self.assertNotEqual(B, G_sharp)
        self.assertNotEqual(B, A_flat)
        self.assertNotEqual(B, A)
        self.assertNotEqual(B, A_sharp)
        self.assertNotEqual(B, B_flat)

        self.assertNotEqual(C_sharp, D_flat)
        self.assertNotEqual(C_sharp, D)
        self.assertNotEqual(C_sharp, D_sharp)
        self.assertNotEqual(C_sharp, E_flat)
        self.assertNotEqual(C_sharp, E)
        self.assertNotEqual(C_sharp, E_sharp)
        self.assertNotEqual(C_sharp, F_flat)
        self.assertNotEqual(C_sharp, F)
        self.assertNotEqual(C_sharp, F_sharp)
        self.assertNotEqual(C_sharp, G_flat)
        self.assertNotEqual(C_sharp, G)
        self.assertNotEqual(C_sharp, G_sharp)
        self.assertNotEqual(C_sharp, A_flat)
        self.assertNotEqual(C_sharp, A)
        self.assertNotEqual(C_sharp, A_sharp)
        self.assertNotEqual(C_sharp, B_flat)
        self.assertNotEqual(C_sharp, B)
        self.assertNotEqual(C_sharp, B_sharp)
        self.assertNotEqual(C_sharp, C)
