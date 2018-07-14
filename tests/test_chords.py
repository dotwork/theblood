from unittest import TestCase

from models import Chord, Key, A, B, C, D, E, F, G, C_sharp, D_sharp, E_sharp, F_sharp, G_sharp, A_sharp, B_sharp


########################################################################
class TestChord(TestCase):

    ####################################################################
    def test_init(self):
        self.fail()

    ####################################################################
    def test_name__major(self):
        self.assertEqual('A', Chord('A').name)
        self.assertEqual('A', Chord('A maj').name)
        self.assertEqual('A', Chord('A major').name)

    ####################################################################
    def test_name__minor(self):
        self.assertEqual('Am', Chord('Am').name)
        self.assertEqual('Am', Chord('A min').name)
        self.assertEqual('Am', Chord('A minor').name)
