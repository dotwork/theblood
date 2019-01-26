from unittest import TestCase

from errors import InvalidQualityError
from models import Key, A, A_sharp, B, B_sharp, C, C_sharp, D, D_sharp, E, E_sharp, F, F_sharp, G, G_sharp, E_flat, \
    B_flat


########################################################################
class TestMajorKey(TestCase):

    ####################################################################
    def test_init(self):
        a_major = Key('A')
        self.assertEqual(A, a_major.root_note)

        a_major = Key('A major')
        self.assertEqual(A, a_major.root_note)

        a_major = Key('A maj')
        self.assertEqual(A, a_major.root_note)

        a_major = Key('Amaj')
        self.assertEqual(A, a_major.root_note)

    ####################################################################
    def test_init__invalid(self):
        with self.assertRaises(InvalidQualityError):
            Key('A foo')

        with self.assertRaises(InvalidQualityError):
            Key('A major quack a doodle')

        with self.assertRaises(InvalidQualityError):
            Key('A 4000')

    ####################################################################
    def test_notes__natural(self):
        key_notes = Key('C').scale.notes
        expected = (C, D, E, F, G, A, B)
        self.assertEqual(expected, key_notes)

    ####################################################################
    def test_notes__sharp(self):
        key_notes = Key('C#').scale.notes
        expected_notes = (C_sharp, D_sharp, E_sharp, F_sharp, G_sharp, A_sharp, B_sharp)
        self.assertEqual(expected_notes, key_notes)

    ####################################################################
    def test_note_names__natural(self):
        names = Key('A').note_names
        expected = ('A', 'B', 'C♯', 'D', 'E', 'F♯', 'G♯')
        self.assertEqual(expected, names)

        names = Key('B').note_names
        expected = ('B', 'C♯', 'D♯', 'E', 'F♯', 'G♯', 'A♯')
        self.assertEqual(expected, names)

        names = Key('C').note_names
        expected = ('C', 'D', 'E', 'F', 'G', 'A', 'B')
        self.assertEqual(expected, names)

        names = Key('D').note_names
        expected = ('D', 'E', 'F♯', 'G', 'A', 'B', 'C♯')
        self.assertEqual(expected, names)

        names = Key('E').note_names
        expected = ('E', 'F♯', 'G♯', 'A', 'B', 'C♯', 'D♯')
        self.assertEqual(expected, names)

        names = Key('F').note_names
        expected = ('F', 'G', 'A', 'B♭', 'C', 'D', 'E')
        self.assertEqual(expected, names)

        names = Key('G').note_names
        expected = ('G', 'A', 'B', 'C', 'D', 'E', 'F♯')
        self.assertEqual(expected, names)

    ####################################################################
    def test_note_names__sharps(self):
        names = Key('C♯').note_names
        expected = ('C♯', 'D♯', 'E♯', 'F♯', 'G♯', 'A♯', 'B♯')
        self.assertEqual(expected, names)

        names = Key('F♯').note_names
        expected = ('F♯', 'G♯', 'A♯', 'B', 'C♯', 'D♯', 'E♯')
        self.assertEqual(expected, names)

    ####################################################################
    def test_note_names__non_standard_sharps(self):
        names = Key('A♯').note_names
        expected = ('A♯', 'B♯', 'C♯♯', 'D♯', 'E♯', 'F♯♯', 'G♯♯')
        self.assertEqual(expected, names)

        names = Key('B♯').note_names
        expected = ('B♯', 'C♯♯', 'D♯♯', 'E♯', 'F♯♯', 'G♯♯', 'A♯♯')
        self.assertEqual(expected, names)

        names = Key('D♯').note_names
        expected = ('D♯', 'E♯', 'F♯♯', 'G♯', 'A♯', 'B♯', 'C♯♯')
        self.assertEqual(expected, names)

        names = Key('E♯').note_names
        expected = ('E♯', 'F♯♯', 'G♯♯', 'A♯', 'B♯', 'C♯♯', 'D♯♯')
        self.assertEqual(expected, names)

        names = Key('G♯').note_names
        expected = ('G♯', 'A♯', 'B♯', 'C♯', 'D♯', 'E♯', 'F♯♯')
        self.assertEqual(expected, names)

    ####################################################################
    def test_note_names__flats(self):
        names = Key('A♭').note_names
        expected = ('A♭', 'B♭', 'C', 'D♭', 'E♭', 'F', 'G')
        self.assertEqual(expected, names)

        names = Key('B♭').note_names
        expected = ('B♭', 'C', 'D', 'E♭', 'F', 'G', 'A')
        self.assertEqual(expected, names)

        names = Key('C♭').note_names
        expected = ('C♭', 'D♭', 'E♭', 'F♭', 'G♭', 'A♭', 'B♭')
        self.assertEqual(expected, names)

        names = Key('D♭').note_names
        expected = ('D♭', 'E♭', 'F', 'G♭', 'A♭', 'B♭', 'C')
        self.assertEqual(expected, names)

        names = Key('E♭').note_names
        expected = ('E♭', 'F', 'G', 'A♭', 'B♭', 'C', 'D')
        self.assertEqual(expected, names)

        names = Key('G♭').note_names
        expected = ('G♭', 'A♭', 'B♭', 'C♭', 'D♭', 'E♭', 'F')
        self.assertEqual(expected, names)

    ####################################################################
    def test_note_names__non_standard_flats(self):
        names = Key('F♭').note_names
        expected = ('F♭', 'G♭', 'A♭', 'B♭♭', 'C♭', 'D♭', 'E♭')
        self.assertEqual(expected, names)


########################################################################
class TestMinorKey(TestCase):

    ####################################################################
    def test_init(self):
        a_minor = Key('A minor')
        self.assertEqual(A, a_minor.root_note)

        a_minor = Key('Am')
        self.assertEqual(A, a_minor.root_note)

        a_minor = Key('A min')
        self.assertEqual(A, a_minor.root_note)

        a_minor = Key('Amin')
        self.assertEqual(A, a_minor.root_note)

    ####################################################################
    def test_generate_notes(self):
        key_notes = Key('C# minor').scale.notes
        expected = (C_sharp, D_sharp, E, F_sharp, G_sharp, A, B)
        self.assertEqual(expected, key_notes)

        key_notes = Key('C#').scale.notes
        expected = (C_sharp, D_sharp, E_sharp, F_sharp, G_sharp, A_sharp, B_sharp)
        self.assertEqual(expected, key_notes)

    ####################################################################
    def test_notes__natural_majors(self):
        expected = ('A', 'B', 'C♯', 'D', 'E', 'F♯', 'G♯')
        self.assertEqual(expected, Key('A').scale.notes)

        expected = ('B', 'C♯', 'D♯', 'E', 'F♯', 'G♯', 'A♯')
        self.assertEqual(expected, Key('B').scale.notes)

        expected = ('C', 'D', 'E', 'F', 'G', 'A', 'B')
        self.assertEqual(expected, Key('C').scale.notes)

        expected = ('D', 'E', 'F♯', 'G', 'A', 'B', 'C♯')
        self.assertEqual(expected, Key('D').scale.notes)

        expected = ('E', 'F♯', 'G♯', 'A', 'B', 'C♯', 'D♯')
        self.assertEqual(expected, Key('E').scale.notes)

        expected = ('F', 'G', 'A', 'B♭', 'C', 'D', 'E')
        self.assertEqual(expected, Key('F').scale.notes)

        expected = ('G', 'A', 'B', 'C', 'D', 'E', 'F♯')
        self.assertEqual(expected, Key('G').scale.notes)

    ####################################################################
    def test_notes__natural__minors(self):
        names = Key('A minor').note_names
        expected = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
        self.assertEqual(expected, names)

        names = Key('B minor').note_names
        expected = ('B', 'C♯', 'D', 'E', 'F♯', 'G', 'A')
        self.assertEqual(expected, names)

        names = Key('C minor').note_names
        expected = ('C', 'D', 'E♭', 'F', 'G', 'A♭', 'B♭')
        self.assertEqual(expected, names)

        names = Key('D minor').note_names
        expected = ('D', 'E', 'F', 'G', 'A', 'B♭', 'C')
        self.assertEqual(expected, names)

        names = Key('E minor').note_names
        expected = ('E', 'F♯', 'G', 'A', 'B', 'C', 'D')
        self.assertEqual(expected, names)

        names = Key('F minor').note_names
        expected = ('F', 'G', 'A♭', 'B♭', 'C', 'D♭', 'E♭')
        self.assertEqual(expected, names)

        names = Key('G minor').note_names
        expected = ('G', 'A', 'B♭', 'C', 'D', 'E♭', 'F')
        self.assertEqual(expected, names)

    ####################################################################
    def test_note_names__sharps(self):
        names = Key('A♯ minor').note_names
        expected = ('A♯', 'B♯', 'C♯', 'D♯', 'E♯', 'F♯', 'G♯')
        self.assertEqual(expected, names)

        names = Key('C♯ minor').note_names
        expected = ('C♯', 'D♯', 'E', 'F♯', 'G♯', 'A', 'B')
        self.assertEqual(expected, names)

        names = Key('D♯ minor').note_names
        expected = ('D♯', 'E♯', 'F♯', 'G♯', 'A♯', 'B', 'C♯')
        self.assertEqual(expected, names)

        names = Key('F♯ minor').note_names
        expected = ('F♯', 'G♯', 'A', 'B', 'C♯', 'D', 'E')
        self.assertEqual(expected, names)

        names = Key('G♯ minor').note_names
        expected = ('G♯', 'A♯', 'B', 'C♯', 'D♯', 'E', 'F♯')
        self.assertEqual(expected, names)

    ####################################################################
    def test_note_names__non_standard_sharps(self):
        names = Key('B♯ minor').note_names
        expected = ('B♯', 'C♯♯', 'D♯', 'E♯', 'F♯♯', 'G♯', 'A♯')
        self.assertEqual(expected, names)

        names = Key('E♯ minor').note_names
        expected = ('E♯', 'F♯♯', 'G♯', 'A♯', 'B♯', 'C♯', 'D♯')
        self.assertEqual(expected, names)

    ####################################################################
    def test_note_names__flat(self):
        names = Key('A♭ minor').note_names
        expected = ('A♭', 'B♭', 'C♭', 'D♭', 'E♭', 'F♭', 'G♭')
        self.assertEqual(expected, names)

        names = Key('B♭ minor').note_names
        expected = ('B♭', 'C', 'D♭', 'E♭', 'F', 'G♭', 'A♭')
        self.assertEqual(expected, names)

        names = Key('D♭ minor').note_names
        expected = ('D♭', 'E♭', 'F♭', 'G♭', 'A♭', 'B♭♭', 'C♭')
        self.assertEqual(expected, names)

        names = Key('E♭ minor').note_names
        expected = ('E♭', 'F', 'G♭', 'A♭', 'B♭', 'C♭', 'D♭')
        self.assertEqual(expected, names)

        names = Key('G♭ minor').note_names
        expected = ('G♭', 'A♭', 'B♭♭', 'C♭', 'D♭', 'E♭♭', 'F♭')
        self.assertEqual(expected, names)

    ####################################################################
    def test_note_names__non_standard_flats(self):
        names = Key('C♭ minor').note_names
        expected = ('C♭', 'D♭', 'E♭♭', 'F♭', 'G♭', 'A♭♭', 'B♭♭')
        self.assertEqual(expected, names)

        names = Key('F♭ minor').note_names
        expected = ('F♭', 'G♭', 'A♭♭', 'B♭♭', 'C♭', 'D♭♭', 'E♭♭')
        self.assertEqual(expected, names)


#######################################################################
class TestModes(TestCase):

    ####################################################################
    def test_ionian(self):
        c = Key('C')
        expected = (C, D, E, F, G, A, B)
        self.assertEqual(expected, c.ionian_in_key())
        self.assertEqual(expected, c.ionian())

    ####################################################################
    def test_dorian(self):
        c = Key('C')

        # Starting on D, playing dorian scale to stay in key of C
        expected = (D, E, F, G, A, B, C)
        self.assertEqual(expected, c.dorian_in_key())

        # The dorian scale starting on C, puts us in key of B flat
        expected = (C, D, E_flat, F, G, A, B_flat)
        self.assertEqual(expected, c.dorian)
