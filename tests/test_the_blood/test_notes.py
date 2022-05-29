from unittest import TestCase

from the_blood.models import *


########################################################################
class TestNote(TestCase):

    ####################################################################
    def test_equals_note(self):
        self.assertEqual(A, Note('A'))
        self.assertEqual(Note('A'), Note('A'))
        self.assertNotEqual(Note('A#'), Note('Bb'))

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
