from unittest import TestCase

from models import Chord, Key, A, B, C, D, E, F, G, C_sharp, D_sharp, E_sharp, F_sharp, G_sharp, A_sharp, B_sharp


########################################################################
class TestChord(TestCase):

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

    ####################################################################
    def test_note_names__major(self):
        self.assertEqual(('A', 'C♯', 'E'), Chord('A').note_names)
        self.assertEqual(('B', 'D♯', 'F♯'), Chord('B').note_names)
        self.assertEqual(('C', 'E', 'G'), Chord('C').note_names)
        self.assertEqual(('D', 'F♯', 'A'), Chord('D').note_names)
        self.assertEqual(('E', 'G♯', 'B'), Chord('E').note_names)
        self.assertEqual(('F', 'A', 'C'), Chord('F').note_names)
        self.assertEqual(('G', 'B', 'D'), Chord('G').note_names)

    ####################################################################
    def test_note_names__minor_sharps(self):
        self.assertEqual(('A', 'C', 'E'), Chord('Am').note_names)
        self.assertEqual(('B', 'D', 'F♯'), Chord('Bm').note_names)
        self.assertEqual(('D', 'F', 'A'), Chord('Dm').note_names)
        self.assertEqual(('E', 'G', 'B'), Chord('Em').note_names)

    ####################################################################
    def test_note_names__minor__flats(self):
        self.assertEqual(('C', 'E♭', 'G'), Chord('Cm').note_names)
        self.assertEqual(('F', 'A♭', 'C'), Chord('Fm').note_names)
        self.assertEqual(('G', 'B♭', 'D'), Chord('Gm').note_names)
