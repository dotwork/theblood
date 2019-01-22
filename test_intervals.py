from unittest import TestCase

from models import E, MajorThird, C, D, F, G, A, B, C_sharp, D_sharp, F_sharp, G_sharp


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
