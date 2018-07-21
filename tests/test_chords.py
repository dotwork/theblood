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
    def test_notes__major(self):
        self.assertEqual(['A', 'C♯', 'E'], Chord('A').notes)
        self.assertEqual(['B', 'D♯', 'F♯'], Chord('B').notes)
        self.assertEqual(['C', 'E', 'G'], Chord('C').notes)
        self.assertEqual(['D', 'F♯', 'A'], Chord('D').notes)
        self.assertEqual(['E', 'G♯', 'B'], Chord('E').notes)
        self.assertEqual(['F', 'A', 'C'], Chord('F').notes)
        self.assertEqual(['G', 'B', 'D'], Chord('G').notes)

    ####################################################################
    def test_notes__minor(self):
        self.assertEqual(['A', 'C', 'E'], Chord('Am').notes)
        self.assertEqual(['B', 'D', 'F♯'], Chord('Bm').notes)
        self.assertEqual(['C', 'E♭', 'G'], Chord('Cm').notes)
        self.assertEqual(['D', 'F', 'A'], Chord('Dm').notes)
        self.assertEqual(['E', 'G', 'B'], Chord('Em').notes)
        self.assertEqual(['F', 'A♭', 'C'], Chord('Fm').notes)
        self.assertEqual(['G', 'B♭', 'D'], Chord('Gm').notes)

    ####################################################################
    def test_notes__major_sharps(self):
        self.assertEqual(['A♯', 'C♯♯', 'E♯'], Chord('A♯').notes)
        self.assertEqual(['B♯', 'D♯♯', 'F♯♯'], Chord('B♯').notes)
        self.assertEqual(['C♯', 'E♯', 'G♯'], Chord('C♯').notes)
        self.assertEqual(['D♯', 'F♯♯', 'A♯'], Chord('D♯').notes)
        self.assertEqual(['E♯', 'G♯♯', 'B♯'], Chord('E♯').notes)
        self.assertEqual(['F♯', 'A♯', 'C♯'], Chord('F♯').notes)
        self.assertEqual(['G♯', 'B♯', 'D♯'], Chord('G♯').notes)
