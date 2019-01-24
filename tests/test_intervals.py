from unittest import TestCase

from models import MajorThird
from objects import A, B, C, C_sharp, D, D_sharp, E, F, F_sharp, G, G_sharp


########################################################################
class TestIntervals(TestCase):

    ####################################################################
    def test_from_note__major_third__natural_notes(self):
        self.assertEqual(C_sharp, MajorThird.up_from_note(A))
        self.assertEqual(D_sharp, MajorThird.up_from_note(B))
        self.assertEqual(E, MajorThird.up_from_note(C))
        self.assertEqual(F_sharp, MajorThird.up_from_note(D))
        self.assertEqual(G_sharp, MajorThird.up_from_note(E))
        self.assertEqual(A, MajorThird.up_from_note(F))
        self.assertEqual(B, MajorThird.up_from_note(G))
