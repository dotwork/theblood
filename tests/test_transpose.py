from unittest import TestCase

from models import Transpose, WHOLE_STEP
from objects import A_flat, A, A_sharp, B_flat, B, C, C_sharp, D_flat, D, D_sharp, E_flat, E, F, F_sharp, G, G_sharp


########################################################################
class TestTranspose(TestCase):

    ####################################################################
    def test_transpose_with_str(self):
        self.assertEqual([B], Transpose('D♯').down.third)

    ####################################################################
    def test_transpose_up_a_third(self):
        self.assertEqual([C_sharp], Transpose(A).up.third)
        self.assertEqual([C], Transpose(G_sharp).up.third)
        self.assertEqual([A], Transpose(F).up.third)
        self.assertEqual([A_sharp], Transpose(F_sharp).up.third)
        self.assertEqual([B], Transpose(G).up.third)
        self.assertEqual([D], Transpose(A_sharp).up.third)
        self.assertEqual([D_sharp], Transpose(B).up.third)
        self.assertEqual([E], Transpose(C).up.third)
        self.assertEqual([F], Transpose(C_sharp).up.third)
        self.assertEqual([F_sharp], Transpose(D).up.third)
        self.assertEqual([G], Transpose(D_sharp).up.third)
        self.assertEqual([G_sharp], Transpose(E).up.third)

    ####################################################################
    def test_transpose_down_a_third(self):
        self.assertEqual([D_flat], Transpose(F).down.third)
        self.assertEqual([D], Transpose(F_sharp).down.third)
        self.assertEqual([E_flat], Transpose(G).down.third)
        self.assertEqual([E], Transpose(G_sharp).down.third)
        self.assertEqual([F], Transpose(A).down.third)
        self.assertEqual([F_sharp], Transpose(A_sharp).down.third)
        self.assertEqual([G], Transpose(B).down.third)
        self.assertEqual([A_flat], Transpose(C).down.third)
        self.assertEqual([A], Transpose(C_sharp).down.third)
        self.assertEqual([B_flat], Transpose(D).down.third)
        self.assertEqual([B], Transpose(D_sharp).down.third)
        self.assertEqual([C], Transpose(E).down.third)

    ####################################################################
    def test_transpose_up_a_fifth(self):
        self.assertEqual([C], Transpose(F).up.fifth)
        self.assertEqual([C_sharp], Transpose(F_sharp).up.fifth)
        self.assertEqual([D], Transpose(G).up.fifth)
        self.assertEqual([D_sharp], Transpose(G_sharp).up.fifth)
        self.assertEqual([E], Transpose(A).up.fifth)
        self.assertEqual([F], Transpose(A_sharp).up.fifth)
        self.assertEqual([F_sharp], Transpose(B).up.fifth)
        self.assertEqual([G], Transpose(C).up.fifth)
        self.assertEqual([G_sharp], Transpose(C_sharp).up.fifth)
        self.assertEqual([A], Transpose(D).up.fifth)
        self.assertEqual([A_sharp], Transpose(D_sharp).up.fifth)
        self.assertEqual([B], Transpose(E).up.fifth)

    ####################################################################
    def test_transpose_down_a_fifth(self):
        self.assertEqual([B_flat], Transpose(F).down.fifth)
        self.assertEqual([B], Transpose(F_sharp).down.fifth)
        self.assertEqual([C], Transpose(G).down.fifth)
        self.assertEqual([C_sharp], Transpose(G_sharp).down.fifth)
        self.assertEqual([D], Transpose(A).down.fifth)
        self.assertEqual([D_sharp], Transpose(A_sharp).down.fifth)
        self.assertEqual([E], Transpose(B).down.fifth)
        self.assertEqual([F], Transpose(C).down.fifth)
        self.assertEqual([F_sharp], Transpose(C_sharp).down.fifth)
        self.assertEqual([G], Transpose(D).down.fifth)
        self.assertEqual([G_sharp], Transpose(D_sharp).down.fifth)
        self.assertEqual([A], Transpose(E).down.fifth)


########################################################################
class TestTransposeMultiple(TestCase):

    ####################################################################
    def test_transpose_multiple_notes_up_a_third(self):
        Transposed = Transpose(B, G, A).up.third
        self.assertEqual([D_sharp, B, C_sharp], Transposed)

    ####################################################################
    def test_transpose_multiple_notes_down_a_third(self):
        self.assertEqual([G, E_flat, F], Transpose(B, G, A).down.third)

    ####################################################################
    def test_transpose_multiple_notes_up_a_fifth(self):
        Transposed = Transpose(B, G, A).up.fifth
        expected = [F_sharp, D, E]
        self.assertEqual(expected, Transposed)

    ####################################################################
    def test_steps(self):
        self.assertEqual([B], Transpose(A).up.steps(WHOLE_STEP))
        self.assertEqual([B], Transpose(A).up.steps(1))
        self.assertEqual([B], Transpose(A).up.steps(.5, .5))

        up_a_third = Transpose(A).up.third
        up_two_whole_steps = Transpose(A).up.steps(WHOLE_STEP, WHOLE_STEP)
        self.assertEqual(up_a_third, up_two_whole_steps)
        self.assertEqual([C_sharp], up_two_whole_steps)

        self.assertEqual([B], Transpose(A).up.steps(*[.5, .5]))
