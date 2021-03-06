from unittest import TestCase

from models import Chord


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
class TestMajorChords(TestCase):

    ####################################################################
    def test_notes__natural(self):
        self.assertEqual(('A', 'C♯', 'E'), Chord('A').notes)
        self.assertEqual(('B', 'D♯', 'F♯'), Chord('B').notes)
        self.assertEqual(('C', 'E', 'G'), Chord('C').notes)
        self.assertEqual(('D', 'F♯', 'A'), Chord('D').notes)
        self.assertEqual(('E', 'G♯', 'B'), Chord('E').notes)
        self.assertEqual(('F', 'A', 'C'), Chord('F').notes)
        self.assertEqual(('G', 'B', 'D'), Chord('G').notes)

    ####################################################################
    def test_notes__sharp(self):
        self.assertEqual(('A♯', 'C♯♯', 'E♯'), Chord('A♯').notes)
        self.assertEqual(('B♯', 'D♯♯', 'F♯♯'), Chord('B♯').notes)
        self.assertEqual(('C♯', 'E♯', 'G♯'), Chord('C♯').notes)
        self.assertEqual(('D♯', 'F♯♯', 'A♯'), Chord('D♯').notes)
        self.assertEqual(('E♯', 'G♯♯', 'B♯'), Chord('E♯').notes)
        self.assertEqual(('F♯', 'A♯', 'C♯'), Chord('F♯').notes)
        self.assertEqual(('G♯', 'B♯', 'D♯'), Chord('G♯').notes)

    ####################################################################
    def test_notes__flat(self):
        self.assertEqual(('A♭', 'C', 'E♭'), Chord('A♭').notes)
        self.assertEqual(('B♭', 'D', 'F'), Chord('B♭').notes)
        self.assertEqual(('C♭', 'E♭', 'G♭'), Chord('C♭').notes)
        self.assertEqual(('D♭', 'F', 'A♭'), Chord('D♭').notes)
        self.assertEqual(('E♭', 'G', 'B♭'), Chord('E♭').notes)
        self.assertEqual(('F♭', 'A♭', 'C♭'), Chord('F♭').notes)
        self.assertEqual(('G♭', 'B♭', 'D♭'), Chord('G♭').notes)

    ####################################################################
    def test_notes__major_7th(self):
        self.assertEqual(('A', 'C♯', 'E', 'G♯'), Chord('Amaj7').notes)
        self.assertEqual(('B', 'D#', 'F#', 'A♯'), Chord('Bmaj7').notes)
        self.assertEqual(('C', 'E', 'G', 'B'), Chord('Cmaj7').notes)
        self.assertEqual(('D', 'F#', 'A', 'C♯'), Chord('Dmaj7').notes)
        self.assertEqual(('E', 'G#', 'B', 'D♯'), Chord('Emaj7').notes)
        self.assertEqual(('F', 'A', 'C', 'E'), Chord('Fmaj7').notes)
        self.assertEqual(('G', 'B', 'D', 'F♯'), Chord('Gmaj7').notes)


########################################################################
class TestMinorChords(TestCase):

    ####################################################################
    def test_notes__natural(self):
        self.assertEqual(('A', 'C', 'E'), Chord('Am').notes)
        self.assertEqual(('B', 'D', 'F♯'), Chord('Bm').notes)
        self.assertEqual(('C', 'E♭', 'G'), Chord('Cm').notes)
        self.assertEqual(('D', 'F', 'A'), Chord('Dm').notes)
        self.assertEqual(('E', 'G', 'B'), Chord('Em').notes)
        self.assertEqual(('F', 'A♭', 'C'), Chord('Fm').notes)
        self.assertEqual(('G', 'B♭', 'D'), Chord('Gm').notes)

    ####################################################################
    def test_notes__sharp(self):
        self.assertEqual(('A♯', 'C♯', 'E♯'), Chord('A♯m').notes)
        self.assertEqual(('B♯', 'D♯', 'F♯♯'), Chord('B♯m').notes)
        self.assertEqual(('C♯', 'E', 'G♯'), Chord('C♯m').notes)
        self.assertEqual(('D♯', 'F♯', 'A♯'), Chord('D♯m').notes)
        self.assertEqual(('E♯', 'G♯', 'B♯'), Chord('E♯m').notes)
        self.assertEqual(('F♯', 'A', 'C♯'), Chord('F♯m').notes)
        self.assertEqual(('G♯', 'B', 'D♯'), Chord('G♯m').notes)

    ####################################################################
    def test_notes__flat(self):
        self.assertEqual(('A♭', 'C♭', 'E♭'), Chord('A♭m').notes)
        self.assertEqual(('B♭', 'D♭', 'F'), Chord('B♭m').notes)
        self.assertEqual(('C♭', 'E♭♭', 'G♭'), Chord('C♭m').notes)
        self.assertEqual(('D♭', 'F♭', 'A♭'), Chord('D♭m').notes)
        self.assertEqual(('E♭', 'G♭', 'B♭'), Chord('E♭m').notes)
        self.assertEqual(('F♭', 'A♭♭', 'C♭'), Chord('F♭m').notes)
        self.assertEqual(('G♭', 'B♭♭', 'D♭'), Chord('G♭m').notes)

    ####################################################################
    def test_notes__minor_7th(self):
        self.assertEqual(('A', 'C', 'E', 'G'), Chord('Am7').notes)
        self.assertEqual(('B', 'D', 'F#', 'A'), Chord('Bm7').notes)
        self.assertEqual(('C', 'Eb', 'G', 'B♭'), Chord('Cm7').notes)
        self.assertEqual(('D', 'F', 'A', 'C'), Chord('Dm7').notes)
        self.assertEqual(('E', 'G', 'B', 'D'), Chord('Em7').notes)
        self.assertEqual(('F', 'Ab', 'C', 'E♭'), Chord('Fm7').notes)
        self.assertEqual(('G', 'Bb', 'D', 'F'), Chord('Gm7').notes)


#######################################################################
class TestDominantChords(TestCase):

    ####################################################################
    def test_notes__dominant_7th(self):
        self.assertEqual(('A', 'C♯', 'E', 'G'), Chord('A7').notes)
        self.assertEqual(('B', 'D#', 'F#', 'A'), Chord('B7').notes)
        self.assertEqual(('C', 'E', 'G', 'B♭'), Chord('C7').notes)
        self.assertEqual(('D', 'F#', 'A', 'C'), Chord('D7').notes)
        self.assertEqual(('E', 'G#', 'B', 'D'), Chord('E7').notes)
        self.assertEqual(('F', 'A', 'C', 'E♭'), Chord('F7').notes)
        self.assertEqual(('G', 'B', 'D', 'F'), Chord('G7').notes)
