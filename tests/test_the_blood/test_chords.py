import unittest
from unittest import TestCase

from the_blood.models import *


########################################################################
class TestChordName(TestCase):

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


########################################################################
@unittest.skip('NEED TO RE-IMPLEMENT CHORDS')
class TestMajorChords(TestCase):

    ####################################################################
    def test_notes__natural(self):
        self.assertEqual((A, C_sharp, E), Chord('A').notes)
        self.assertEqual((B, D_sharp, F_sharp), Chord('B').notes)
        self.assertEqual((C, E, G), Chord('C').notes)
        self.assertEqual((D, F_sharp, A), Chord('D').notes)
        self.assertEqual((E, G_sharp, B), Chord('E').notes)
        self.assertEqual((F, A, C), Chord('F').notes)
        self.assertEqual((G, B, D), Chord('G').notes)

    ####################################################################
    def test_notes__sharp(self):
        self.assertEqual((A_sharp, C_double_sharp, E_sharp), Chord('A♯').notes)
        self.assertEqual((B_sharp, D_double_sharp, F_double_sharp), Chord('B♯').notes)
        self.assertEqual((C_sharp, E_sharp, G_sharp), Chord('C♯').notes)
        self.assertEqual((D_sharp, F_double_sharp, A_sharp), Chord('D♯').notes)
        self.assertEqual((E_sharp, G_double_sharp, B_sharp), Chord('E♯').notes)
        self.assertEqual((F_sharp, A_sharp, C_sharp), Chord('F♯').notes)
        self.assertEqual((G_sharp, B_sharp, D_sharp), Chord('G♯').notes)

    ####################################################################
    def test_notes__flat(self):
        self.assertEqual((Ab, C, Eb), Chord('Ab').notes)
        self.assertEqual((Bb, D, F), Chord('Bb').notes)
        self.assertEqual((Cb, Eb, Gb), Chord('Cb').notes)
        self.assertEqual((Db, F, Ab), Chord('Db').notes)
        self.assertEqual((Eb, G, Bb), Chord('Eb').notes)
        self.assertEqual((Fb, Ab, Cb), Chord('Fb').notes)
        self.assertEqual((Gb, Bb, Db), Chord('Gb').notes)

    ####################################################################
    def test_notes__major_7th(self):
        self.assertEqual((A, C_sharp, E, G_sharp), Chord('Amaj7').notes)
        self.assertEqual((B, D_sharp, F_sharp, A_sharp), Chord('Bmaj7').notes)
        self.assertEqual((C, E, G, B), Chord('Cmaj7').notes)
        self.assertEqual((D, F_sharp, A, C_sharp), Chord('Dmaj7').notes)
        self.assertEqual((E, G_sharp, B, D_sharp), Chord('Emaj7').notes)
        self.assertEqual((F, A, C, E), Chord('Fmaj7').notes)
        self.assertEqual((G, B, D, F_sharp), Chord('Gmaj7').notes)


########################################################################
@unittest.skip('NEED TO RE-IMPLEMENT CHORDS')
class TestMinorChords(TestCase):

    ####################################################################
    def test_notes__natural(self):
        self.assertEqual((A, C, E), Chord('Am').notes)
        self.assertEqual((B, D, F_sharp), Chord('Bm').notes)
        self.assertEqual((C, Eb, G), Chord('Cm').notes)
        self.assertEqual((D, F, A), Chord('Dm').notes)
        self.assertEqual((E, G, B), Chord('Em').notes)
        self.assertEqual((F, Ab, C), Chord('Fm').notes)
        self.assertEqual((G, Bb, D), Chord('Gm').notes)

    ####################################################################
    def test_notes__sharp(self):
        self.assertEqual((A_sharp, C_sharp, E_sharp), Chord('A♯m').notes)
        self.assertEqual((B_sharp, D_sharp, F_double_sharp), Chord('B♯m').notes)
        self.assertEqual((C_sharp, E, G_sharp), Chord('C♯m').notes)
        self.assertEqual((D_sharp, F_sharp, A_sharp), Chord('D♯m').notes)
        self.assertEqual((E_sharp, G_sharp, B_sharp), Chord('E♯m').notes)
        self.assertEqual((F_sharp, A, C_sharp), Chord('F♯m').notes)
        self.assertEqual((G_sharp, B, D_sharp), Chord('G♯m').notes)

    ####################################################################
    def test_notes__flat(self):
        self.assertEqual((Ab, Cb, Eb), Chord('Abm').notes)
        self.assertEqual((Bb, Db, F), Chord('Bbm').notes)
        self.assertEqual((Cb, Ebb, Gb), Chord('Cbm').notes)
        self.assertEqual((Db, Fb, Ab), Chord('Dbm').notes)
        self.assertEqual((Eb, Gb, Bb), Chord('Ebm').notes)
        self.assertEqual((Fb, Abb, Cb), Chord('Fbm').notes)
        self.assertEqual((Gb, Bbb, Db), Chord('Gbm').notes)

    ####################################################################
    def test_notes__minor_7th(self):
        self.assertEqual((A, C, E, G), Chord('Am7').notes)
        self.assertEqual((B, D, F_sharp, A), Chord('Bm7').notes)
        self.assertEqual((C, Eb, G, Bb), Chord('Cm7').notes)
        self.assertEqual((D, F, A, C), Chord('Dm7').notes)
        self.assertEqual((E, G, B, D), Chord('Em7').notes)
        self.assertEqual((F, Ab, C, Eb), Chord('Fm7').notes)
        self.assertEqual((G, Bb, D, F), Chord('Gm7').notes)


#######################################################################
@unittest.skip('NEED TO RE-IMPLEMENT CHORDS')
class TestDominantChords(TestCase):

    ####################################################################
    def test_notes__dominant_7th(self):
        self.assertEqual((A, C_sharp, E, G), Chord('A7').notes)
        self.assertEqual((B, D_sharp, F_sharp, A), Chord('B7').notes)
        self.assertEqual((C, E, G, Bb), Chord('C7').notes)
        self.assertEqual((D, F_sharp, A, C), Chord('D7').notes)
        self.assertEqual((E, G_sharp, B, D), Chord('E7').notes)
        self.assertEqual((F, A, C, Eb), Chord('F7').notes)
        self.assertEqual((G, B, D, F), Chord('G7').notes)
