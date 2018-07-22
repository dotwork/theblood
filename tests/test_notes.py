from unittest import TestCase

from models import A, A_sharp, B, F, E, G, F_flat, B_flat, G_sharp, A_flat, E_sharp, B_sharp, C_flat, C_sharp, D_flat, \
    D_sharp, E_flat, F_sharp, G_flat, C, D, Note, InvalidNoteError


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
        self.assertTrue(B_flat.is_equal_pitch_to(A_sharp))
        self.assertTrue(D_flat.is_equal_pitch_to(C_sharp))
        self.assertTrue(E_flat.is_equal_pitch_to(D_sharp))
        self.assertTrue(G_flat.is_equal_pitch_to(F_sharp))
        self.assertTrue(A_flat.is_equal_pitch_to(G_sharp))

    ####################################################################
    def test_is_equal_pitch_to__standard_sharps(self):
        self.assertTrue(A_sharp.is_equal_pitch_to(B_flat))
        self.assertTrue(C_sharp.is_equal_pitch_to(D_flat))
        self.assertTrue(D_sharp.is_equal_pitch_to(E_flat))
        self.assertTrue(F_sharp.is_equal_pitch_to(G_flat))
        self.assertTrue(G_sharp.is_equal_pitch_to(A_flat))

    ####################################################################
    def test_is_equal_pitch_to__non_standard_flats(self):
        self.assertTrue(C_flat.is_equal_pitch_to(B))
        self.assertTrue(F_flat.is_equal_pitch_to(E))

        self.assertTrue(B.is_equal_pitch_to(C_flat))
        self.assertTrue(E.is_equal_pitch_to(F_flat))

    ####################################################################
    def test_is_equal_pitch_to__non_standard_sharps(self):
        self.assertTrue(C.is_equal_pitch_to(B_sharp))
        self.assertTrue(B_sharp.is_equal_pitch_to(C))

        self.assertTrue(F.is_equal_pitch_to(E_sharp))
        self.assertTrue(E_sharp.is_equal_pitch_to(F))

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

        self.assertNotEqual(C_sharp, C)
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

    ####################################################################
    def test_next__from_natural_to_sharp(self):
        self.assertEqual(A_sharp, A.next())
        self.assertEqual(C_sharp, C.next())
        self.assertEqual(D_sharp, D.next())
        self.assertEqual(F_sharp, F.next())
        self.assertEqual(G_sharp, G.next())

        self.assertNotEqual(B_sharp, B.next())
        self.assertNotEqual(E_sharp, E.next())

    ####################################################################
    def test_next__from_natural_to_flat(self):
        self.assertNotEqual(B_flat, A.next())
        self.assertEqual(B_flat, A.next(use_flats=True))

        self.assertNotEqual(D_flat, C.next())
        self.assertEqual(D_flat, C.next(use_flats=True))

        self.assertNotEqual(E_flat, D.next())
        self.assertEqual(E_flat, D.next(use_flats=True))

        self.assertNotEqual(G_flat, F.next())
        self.assertEqual(G_flat, F.next(use_flats=True))

        self.assertNotEqual(A_flat, G.next())
        self.assertEqual(A_flat, G.next(use_flats=True))

    ####################################################################
    def test_next__from_natural_to_natural(self):
        self.assertEqual(C, B.next())
        self.assertEqual(F, E.next())

    ####################################################################
    def test_next__from_sharp_to_natural(self):
        self.assertEqual(B, A_sharp.next())

        self.assertEqual(D, C_sharp.next())
        self.assertEqual(E, D_sharp.next())

        self.assertEqual(G, F_sharp.next())
        self.assertEqual(A, G_sharp.next())

    ####################################################################
    def test_next__from_sharp_to_sharp(self):
        self.assertEqual(C_sharp, B_sharp.next())
        self.assertEqual(F_sharp, E_sharp.next())

    ####################################################################
    def test_next__from_sharp_to_flat(self):
        self.assertNotEqual(C_flat, A_sharp.next())
        self.assertNotEqual(D_flat, B_sharp.next())
        self.assertNotEqual(F_flat, D_sharp.next())
        self.assertNotEqual(G_flat, E_sharp.next())

    ####################################################################
    def test_next__from_flat_to_natural(self):
        self.assertEqual(A, A_flat.next())
        self.assertEqual(B, B_flat.next())
        self.assertEqual(C, C_flat.next())
        self.assertEqual(D, D_flat.next())
        self.assertEqual(E, E_flat.next())
        self.assertEqual(F, F_flat.next())
        self.assertEqual(G, G_flat.next())

    ####################################################################
    def test_next__from_flat_to_sharp(self):
        self.assertNotEqual(B_sharp, C_flat.next())
        self.assertNotEqual(E_sharp, F_flat.next())

    ####################################################################
    def test_next__from_flat_to_flat(self):
        self.assertNotEqual(C_flat, B_flat.next())
        self.assertNotEqual(F_flat, E_flat.next())

    ####################################################################
    def test_previous__from_natural_to_sharp(self):
        self.assertEqual(G_sharp, A.previous(use_sharps=True))
        self.assertEqual(A_sharp, B.previous(use_sharps=True))
        self.assertEqual(C_sharp, D.previous(use_sharps=True))
        self.assertEqual(D_sharp, E.previous(use_sharps=True))
        self.assertEqual(F_sharp, G.previous(use_sharps=True))

    ####################################################################
    def test_previous__from_natural_to_flat(self):
        self.assertEqual(A_flat, A.previous())
        self.assertEqual(B_flat, B.previous())
        self.assertEqual(D_flat, D.previous())
        self.assertEqual(E_flat, E.previous())
        self.assertEqual(G_flat, G.previous())

    ####################################################################
    def test_previous__from_natural_to_natural(self):
        self.assertEqual(B, C.previous())
        self.assertEqual(E, F.previous())

    ####################################################################
    def test_previous__from_sharp_to_natural(self):
        self.assertEqual(A, A_sharp.previous())
        self.assertEqual(B, B_sharp.previous())
        self.assertEqual(C, C_sharp.previous())
        self.assertEqual(D, D_sharp.previous())
        self.assertEqual(E, E_sharp.previous())
        self.assertEqual(F, F_sharp.previous())
        self.assertEqual(G, G_sharp.previous())

    ####################################################################
    def test_previous__from_flat_to_natural(self):
        self.assertEqual(G, A_flat.previous())
        self.assertEqual(A, B_flat.previous())

        self.assertEqual(C, D_flat.previous())
        self.assertEqual(D, E_flat.previous())

        self.assertEqual(F, G_flat.previous())

    ####################################################################
    def test_previous__from_flat_to_sharp(self):
        self.assertEqual(A_sharp, C_flat.previous())
        self.assertEqual(D_sharp, F_flat.previous())

    ####################################################################
    def test_c_flat_b_sharp(self):
        self.assertNotEqual(C_flat, B_sharp)
        self.assertNotEqual(B_sharp, C_flat)
