from unittest import TestCase

from models import A, A_sharp, B, F, E, G, F_flat, B_flat, G_sharp, A_flat, E_sharp, B_sharp, C_flat, C_sharp, D_flat, \
    D_sharp, E_flat, F_sharp, G_flat, C, D


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
    def test_next_whole_note(self):
        self.assertEqual(B, A.next_whole_note)
        self.assertEqual(C, B.next_whole_note)
        self.assertEqual(D, C.next_whole_note)
        self.assertEqual(E, D.next_whole_note)
        self.assertEqual(F, E.next_whole_note)
        self.assertEqual(G, F.next_whole_note)
        self.assertEqual(A, G.next_whole_note)

    ####################################################################
    def test_(self):
        self.assertEqual(B_sharp, C_sharp)

    ####################################################################
    def test_previous_whole_note(self):
        self.assertEqual(A, B.previous_whole_note)
        self.assertEqual(E, F.previous_whole_note)
        self.assertEqual(G, A.previous_whole_note)

    ####################################################################
    def test_next(self):
        # self.assertEqual(A, A_flat.next())
        #
        # self.assertEqual(A_sharp, A.next())
        # self.assertEqual(B_flat, A.next())
        #
        # self.assertEqual(B, A_sharp.next())
        # self.assertEqual(B, B_flat.next())
        # self.assertEqual(C_flat, B_flat.next())
        #
        # self.assertEqual(B_sharp, B.next())
        # self.assertEqual(C, B.next())
        # self.assertEqual(C, C_flat.next())
        #
        # self.assertEqual(C_sharp, C.next())
        # self.assertEqual(D_flat, C.next())
        # self.assertEqual(C_sharp, B_sharp.next())
        #
        self.assertEqual(D, C_sharp.next())
        # self.assertEqual(D, D_flat.next())

        # self.assertEqual(B, A_sharp.next())
        # self.assertEqual(C, B.next())
        # self.assertEqual(C_sharp, C.next())
        # self.assertEqual(D, C_sharp.next())
        # self.assertEqual(D_sharp, D.next())
        # self.assertEqual(E, D_sharp.next())
        # self.assertEqual(F, E.next())
        # self.assertEqual(F_sharp, F.next())
        # self.assertEqual(G, F_sharp.next())
        # self.assertEqual(G_sharp, G.next())

