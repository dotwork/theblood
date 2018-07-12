from unittest import TestCase, skip

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
    def test_equals__whole_notes(self):
        self.assertEqual(A, A)
        self.assertEqual(B, B)
        self.assertEqual(C, C)
        self.assertEqual(D, D)
        self.assertEqual(E, E)
        self.assertEqual(F, F)
        self.assertEqual(G, G)

    ####################################################################
    def test_equals__sharps_and_flats__going_down(self):
        self.assertEqual(A_sharp, B_flat)
        self.assertEqual(B_sharp, C_flat)
        self.assertEqual(C_sharp, D_flat)
        self.assertEqual(D_sharp, E_flat)
        self.assertEqual(E_sharp, F_flat)
        self.assertEqual(F_sharp, G_flat)
        self.assertEqual(G_sharp, A_flat)

    ####################################################################
    def test_equals__sharps_and_flats__going_up(self):
        self.assertEqual(B_flat, A_sharp)
        self.assertEqual(C_flat, B_sharp)
        self.assertEqual(D_flat, C_sharp)
        self.assertEqual(E_flat, D_sharp)
        self.assertEqual(F_flat, E_sharp)
        self.assertEqual(G_flat, F_sharp)
        self.assertEqual(A_flat, G_sharp)

    ####################################################################
    def test_B_sharp_C_flat(self):
        self.assertEqual(B, C_flat)
        self.assertEqual(C_flat, B)

        self.assertEqual(B_sharp, C)
        self.assertEqual(C, B_sharp)

    ####################################################################
    def test_E_sharp_F_flat(self):
        self.assertEqual(E, F_flat)
        self.assertEqual(F_flat, E)

        self.assertEqual(E_sharp, F)
        self.assertEqual(F, E_sharp)

    ####################################################################
    def test_next_whole_note__from_whole_note(self):
        self.assertEqual(B, A.next_whole_note)
        self.assertEqual(C, B.next_whole_note)
        self.assertEqual(D, C.next_whole_note)
        self.assertEqual(E, D.next_whole_note)
        self.assertEqual(F, E.next_whole_note)
        self.assertEqual(G, F.next_whole_note)
        self.assertEqual(A, G.next_whole_note)

    ####################################################################
    def test_next_whole_note__from_sharp(self):
        self.assertEqual(B, A_sharp.next_whole_note)
        self.assertEqual(D, C_sharp.next_whole_note)
        self.assertEqual(E, D_sharp.next_whole_note)
        self.assertEqual(G, F_sharp.next_whole_note)
        self.assertEqual(A, G_sharp.next_whole_note)

        # TODO: Decide if this is how I actually want next_whole_note to work or not
        self.assertEqual(C, B_sharp.next_whole_note)
        self.assertEqual(F, E_sharp.next_whole_note)

    ####################################################################
    def test_next_whole_note__from_flat(self):
        self.assertEqual(B, A_flat.next_whole_note)
        self.assertEqual(D, C_flat.next_whole_note)
        self.assertEqual(E, D_flat.next_whole_note)
        self.assertEqual(G, F_flat.next_whole_note)
        self.assertEqual(A, G_flat.next_whole_note)
        self.assertEqual(C, B_flat.next_whole_note)
        self.assertEqual(F, E_flat.next_whole_note)

    ####################################################################
    def test_previous_whole_note__from_whole_note(self):
        self.assertEqual(A, B.previous_whole_note)
        self.assertEqual(B, C.previous_whole_note)
        self.assertEqual(C, D.previous_whole_note)
        self.assertEqual(D, E.previous_whole_note)
        self.assertEqual(E, F.previous_whole_note)
        self.assertEqual(F, G.previous_whole_note)
        self.assertEqual(G, A.previous_whole_note)

    ####################################################################
    def test_previous_whole_note__from_sharp(self):
        self.assertEqual(B, C_sharp.previous_whole_note)
        self.assertEqual(C, D_sharp.previous_whole_note)
        self.assertEqual(E, F_sharp.previous_whole_note)
        self.assertEqual(F, G_sharp.previous_whole_note)
        self.assertEqual(G, A_sharp.previous_whole_note)

        # TODO: Decide if this is how I actually want previous_whole_note to work or not
        self.assertEqual(A, B_sharp.previous_whole_note)
        self.assertEqual(D, E_sharp.previous_whole_note)

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
    def test_next__from_whole_to_sharp(self):
        self.assertEqual(A_sharp, A.next())
        self.assertEqual(B_sharp, B.next())
        self.assertEqual(C_sharp, C.next())
        self.assertEqual(D_sharp, D.next())
        self.assertEqual(E_sharp, E.next())
        self.assertEqual(F_sharp, F.next())
        self.assertEqual(G_sharp, G.next())

    ####################################################################
    def test_next__from_whole_to_flat(self):
        self.assertEqual(B_flat, A.next())

        self.assertEqual(D_flat, C.next())
        self.assertEqual(E_flat, D.next())

        self.assertEqual(G_flat, F.next())
        self.assertEqual(A_flat, G.next())

    ####################################################################
    def test_next__from_whole_to_whole(self):
        self.assertEqual(C, B.next())
        self.assertEqual(F, E.next())

    ####################################################################
    def test_next__from_sharp_to_whole(self):
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
        self.assertEqual(C_flat, A_sharp.next())
        self.assertEqual(D_flat, B_sharp.next())

        self.assertEqual(F_flat, D_sharp.next())
        self.assertEqual(G_flat, E_sharp.next())

    ####################################################################
    def test_next__from_flat_to_whole(self):
        self.assertEqual(A, A_flat.next())
        self.assertEqual(B, B_flat.next())
        self.assertEqual(C, C_flat.next())
        self.assertEqual(D, D_flat.next())
        self.assertEqual(E, E_flat.next())
        self.assertEqual(F, F_flat.next())
        self.assertEqual(G, G_flat.next())

    ####################################################################
    def test_next__from_flat_to_sharp(self):
        self.assertEqual(B_sharp, C_flat.next())
        self.assertEqual(E_sharp, F_flat.next())

    ####################################################################
    def test_next__from_flat_to_flat(self):
        self.assertEqual(C_flat, B_flat.next())
        self.assertEqual(F_flat, E_flat.next())

    ####################################################################
    def test_previous__from_whole_to_sharp(self):
        self.assertEqual(G_sharp, A.previous())
        self.assertEqual(A_sharp, B.previous())

        self.assertEqual(C_sharp, D.previous())
        self.assertEqual(D_sharp, E.previous())

        self.assertEqual(F_sharp, G.previous())

    ####################################################################
    def test_previous__from_whole_to_flat(self):
        self.assertEqual(A_flat, A.previous())
        self.assertEqual(B_flat, B.previous())

        self.assertEqual(D_flat, D.previous())
        self.assertEqual(E_flat, E.previous())

        self.assertEqual(G_flat, G.previous())

    ####################################################################
    def test_previous__from_whole_to_whole(self):
        self.assertEqual(B, C.previous())
        self.assertEqual(E, F.previous())

    ####################################################################
    def test_previous__from_sharp_to_whole(self):
        self.assertEqual(A, A_sharp.previous())
        self.assertEqual(B, B_sharp.previous())
        self.assertEqual(C, C_sharp.previous())
        self.assertEqual(D, D_sharp.previous())
        self.assertEqual(E, E_sharp.previous())
        self.assertEqual(F, F_sharp.previous())
        self.assertEqual(G, G_sharp.previous())

    ####################################################################
    def test_previous__from_flat_to_whole(self):
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
