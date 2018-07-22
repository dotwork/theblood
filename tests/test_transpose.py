from unittest import TestCase

from models import transpose, A, A_sharp, B, C, C_sharp, D, D_sharp, F, E, F_sharp, G, G_sharp, WHOLE_STEP, B_flat, \
    D_flat, E_flat, A_flat


########################################################################
class TestTranspose(TestCase):

    ####################################################################
    def test_transpose_with_str(self):
        self.assertEqual([B], transpose('D♯').down.third)

    ####################################################################
    def test_transpose_up_a_third(self):
        self.assertEqual([C_sharp], transpose(A).up.third)
        self.assertEqual([C], transpose(G_sharp).up.third)
        self.assertEqual([A], transpose(F).up.third)
        self.assertEqual([A_sharp], transpose(F_sharp).up.third)
        self.assertEqual([B], transpose(G).up.third)
        self.assertEqual([D], transpose(A_sharp).up.third)
        self.assertEqual([D_sharp], transpose(B).up.third)
        self.assertEqual([E], transpose(C).up.third)
        self.assertEqual([F], transpose(C_sharp).up.third)
        self.assertEqual([F_sharp], transpose(D).up.third)
        self.assertEqual([G], transpose(D_sharp).up.third)
        self.assertEqual([G_sharp], transpose(E).up.third)

    ####################################################################
    def test_transpose_down_a_third(self):
        self.assertEqual([D_flat], transpose(F).down.third)
        self.assertEqual([D], transpose(F_sharp).down.third)
        self.assertEqual([E_flat], transpose(G).down.third)
        self.assertEqual([E], transpose(G_sharp).down.third)
        self.assertEqual([F], transpose(A).down.third)
        self.assertEqual([F_sharp], transpose(A_sharp).down.third)
        self.assertEqual([G], transpose(B).down.third)
        self.assertEqual([A_flat], transpose(C).down.third)
        self.assertEqual([A], transpose(C_sharp).down.third)
        self.assertEqual([B_flat], transpose(D).down.third)
        self.assertEqual([B], transpose(D_sharp).down.third)
        self.assertEqual([C], transpose(E).down.third)

    ####################################################################
    def test_transpose_up_a_fifth(self):
        self.assertEqual([C], transpose(F).up.fifth)
        self.assertEqual([C_sharp], transpose(F_sharp).up.fifth)
        self.assertEqual([D], transpose(G).up.fifth)
        self.assertEqual([D_sharp], transpose(G_sharp).up.fifth)
        self.assertEqual([E], transpose(A).up.fifth)
        self.assertEqual([F], transpose(A_sharp).up.fifth)
        self.assertEqual([F_sharp], transpose(B).up.fifth)
        self.assertEqual([G], transpose(C).up.fifth)
        self.assertEqual([G_sharp], transpose(C_sharp).up.fifth)
        self.assertEqual([A], transpose(D).up.fifth)
        self.assertEqual([A_sharp], transpose(D_sharp).up.fifth)
        self.assertEqual([B], transpose(E).up.fifth)

    ####################################################################
    def test_transpose_down_a_fifth(self):
        self.assertEqual([B_flat], transpose(F).down.fifth)
        self.assertEqual([B], transpose(F_sharp).down.fifth)
        self.assertEqual([C], transpose(G).down.fifth)
        self.assertEqual([C_sharp], transpose(G_sharp).down.fifth)
        self.assertEqual([D], transpose(A).down.fifth)
        self.assertEqual([D_sharp], transpose(A_sharp).down.fifth)
        self.assertEqual([E], transpose(B).down.fifth)
        self.assertEqual([F], transpose(C).down.fifth)
        self.assertEqual([F_sharp], transpose(C_sharp).down.fifth)
        self.assertEqual([G], transpose(D).down.fifth)
        self.assertEqual([G_sharp], transpose(D_sharp).down.fifth)
        self.assertEqual([A], transpose(E).down.fifth)


########################################################################
class TestTransposeMultiple(TestCase):

    ####################################################################
    def test_transpose_multiple_notes_up_a_third(self):
        transposed = transpose(B, G, A).up.third
        self.assertEqual([D_sharp, B, C_sharp], transposed)

    ####################################################################
    def test_transpose_multiple_notes_down_a_third(self):
        self.assertEqual([G, E_flat, F], transpose(B, G, A).down.third)

    ####################################################################
    def test_transpose_multiple_notes_up_a_fifth(self):
        transposed = transpose(B, G, A).up.fifth
        expected = [F_sharp, D, E]
        self.assertEqual(expected, transposed)

    ####################################################################
    def test_steps(self):
        self.assertEqual([B], transpose(A).up.steps(WHOLE_STEP))
        self.assertEqual([B], transpose(A).up.steps(1))
        self.assertEqual([B], transpose(A).up.steps(.5, .5))

        up_a_third = transpose(A).up.third
        up_two_whole_steps = transpose(A).up.steps(WHOLE_STEP, WHOLE_STEP)
        self.assertEqual(up_a_third, up_two_whole_steps)
        self.assertEqual([C_sharp], up_two_whole_steps)

        self.assertEqual([B], transpose(A).up.steps(*[.5, .5]))
