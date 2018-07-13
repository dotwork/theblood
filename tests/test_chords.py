from unittest import TestCase

from models import Chord, Key, A, B, C, D, E, F, G, C_sharp, D_sharp, E_sharp, F_sharp, G_sharp, A_sharp, B_sharp


########################################################################
class TestChord(TestCase):

    ####################################################################
    def test_init(self):
        self.fail()

    ####################################################################
    def test_name(self):
        a_major = Chord('A')
        self.assertEqual('A', a_major.name)

        a_major = Chord('A maj')
        self.assertEqual('A', a_major.name)
