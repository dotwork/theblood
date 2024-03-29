import unittest
from unittest import TestCase

from the_blood.models import *


########################################################################
class TestMajorKey(TestCase):

    ####################################################################
    def test_init(self):
        a_major = Key('A')
        self.assertEqual(A, a_major.tonic)

        a_major = Key('A major')
        self.assertEqual(A, a_major.tonic)

        a_major = Key('A maj')
        self.assertEqual(A, a_major.tonic)

        a_major = Key('Amaj')
        self.assertEqual(A, a_major.tonic)

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
        expected_notes = (C_sharp, D_sharp, E_sharp, F_sharp, G_sharp, A_sharp, Note('B#'))
        self.assertEqual(expected_notes, key_notes)

    ####################################################################
    def test_note_names__natural(self):
        names = Key('A').note_names
        expected = ('A', 'B', 'C#', 'D', 'E', 'F#', 'G#')
        self.assertEqual(expected, names)

        names = Key('B').note_names
        expected = ('B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#')
        self.assertEqual(expected, names)

        names = Key('C').note_names
        expected = ('C', 'D', 'E', 'F', 'G', 'A', 'B')
        self.assertEqual(expected, names)

        names = Key('D').note_names
        expected = ('D', 'E', 'F#', 'G', 'A', 'B', 'C#')
        self.assertEqual(expected, names)

        names = Key('E').note_names
        expected = ('E', 'F#', 'G#', 'A', 'B', 'C#', 'D#')
        self.assertEqual(expected, names)

        names = Key('F').note_names
        expected = ('F', 'G', 'A', 'Bb', 'C', 'D', 'E')
        self.assertEqual(expected, names)

        names = Key('G').note_names
        expected = ('G', 'A', 'B', 'C', 'D', 'E', 'F#')
        self.assertEqual(expected, names)

    ####################################################################
    def test_note_names__sharps(self):
        names = Key('C#').note_names
        expected = ('C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#')
        self.assertEqual(expected, names)

        names = Key('F#').note_names
        expected = ('F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E#')
        self.assertEqual(expected, names)

    ####################################################################
    def test_note_names__non_standard_sharps(self):
        names = Key('A#').note_names
        expected = ('A#', 'B#', 'C##', 'D#', 'E#', 'F##', 'G##')
        self.assertEqual(expected, names)

        names = Key('B#').note_names
        expected = ('B#', 'C##', 'D##', 'E#', 'F##', 'G##', 'A##')
        self.assertEqual(expected, names)

        names = Key('D#').note_names
        expected = ('D#', 'E#', 'F##', 'G#', 'A#', 'B#', 'C##')
        self.assertEqual(expected, names)

        names = Key('E#').note_names
        expected = ('E#', 'F##', 'G##', 'A#', 'B#', 'C##', 'D##')
        self.assertEqual(expected, names)

        names = Key('G#').note_names
        expected = ('G#', 'A#', 'B#', 'C#', 'D#', 'E#', 'F##')
        self.assertEqual(expected, names)

    ####################################################################
    def test_note_names__flats(self):
        names = Key('Ab').note_names
        expected = ('Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G')
        self.assertEqual(expected, names)

        names = Key('Bb').note_names
        expected = ('Bb', 'C', 'D', 'Eb', 'F', 'G', 'A')
        self.assertEqual(expected, names)

        names = Key('Cb').note_names
        expected = ('Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bb')
        self.assertEqual(expected, names)

        names = Key('Db').note_names
        expected = ('Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C')
        self.assertEqual(expected, names)

        names = Key('Eb').note_names
        expected = ('Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D')
        self.assertEqual(expected, names)

        names = Key('Gb').note_names
        expected = ('Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'F')
        self.assertEqual(expected, names)

    ####################################################################
    def test_note_names__non_standard_flats(self):
        names = Key('Fb').note_names
        expected = ('Fb', 'Gb', 'Ab', 'Bbb', 'Cb', 'Db', 'Eb')
        self.assertEqual(expected, names)


########################################################################
class TestMinorKey(TestCase):

    ####################################################################
    def test_init(self):
        a_minor = Key('A minor')
        self.assertEqual(A, a_minor.tonic)

        a_minor = Key('Am')
        self.assertEqual(A, a_minor.tonic)

        a_minor = Key('A min')
        self.assertEqual(A, a_minor.tonic)

        a_minor = Key('Amin')
        self.assertEqual(A, a_minor.tonic)

    ####################################################################
    def test_generate_notes(self):
        key_notes = Key('C# minor').scale.notes
        expected = (C_sharp, D_sharp, E, F_sharp, G_sharp, A, B)
        self.assertEqual(expected, key_notes)

        key_notes = Key('C#').scale.notes
        expected = (C_sharp, D_sharp, E_sharp, F_sharp, G_sharp, A_sharp, Note('B#'))
        self.assertEqual(expected, key_notes)

    ####################################################################
    def test_notes__natural_majors(self):
        expected = (A, B, C_sharp, D, E, F_sharp, G_sharp)
        self.assertEqual(expected, Key('A').scale.notes)

        expected = (B, C_sharp, D_sharp, E, F_sharp, G_sharp, A_sharp)
        self.assertEqual(expected, Key('B').scale.notes)

        expected = (C, D, E, F, G, A, B)
        self.assertEqual(expected, Key('C').scale.notes)

        expected = (D, E, F_sharp, G, A, B, C_sharp)
        self.assertEqual(expected, Key('D').scale.notes)

        expected = (E, F_sharp, G_sharp, A, B, C_sharp, D_sharp)
        self.assertEqual(expected, Key('E').scale.notes)

        expected = (F, G, A, B_flat, C, D, E)
        self.assertEqual(expected, Key('F').scale.notes)

        expected = (G, A, B, C, D, E, F_sharp)
        self.assertEqual(expected, Key('G').scale.notes)

    ####################################################################
    def test_notes__natural__minors(self):
        notes = Key('A minor').scale.notes
        expected = (A, B, C, D, E, F, G)
        self.assertEqual(expected, notes)

        names = Key('B minor').scale.notes
        expected = (B, C_sharp, D, E, F_sharp, G, A)
        self.assertEqual(expected, names)

        names = Key('C minor').scale.notes
        expected = (C, D, E_flat, F, G, A_flat, B_flat)
        self.assertEqual(expected, names)

        names = Key('D minor').scale.notes
        expected = (D, E, F, G, A, B_flat, C)
        self.assertEqual(expected, names)

        names = Key('E minor').scale.notes
        expected = (E, F_sharp, G, A, B, C, D)
        self.assertEqual(expected, names)

        names = Key('F minor').scale.notes
        expected = (F, G, A_flat, B_flat, C, D_flat, E_flat)
        self.assertEqual(expected, names)

        names = Key('G minor').scale.notes
        expected = (G, A, B_flat, C, D, E_flat, F)
        self.assertEqual(expected, names)

    ####################################################################
    def test_note_names__sharps(self):
        names = Key('A# minor').note_names
        expected = ('A#', 'B#', 'C#', 'D#', 'E#', 'F#', 'G#')
        self.assertEqual(expected, names)

        names = Key('C# minor').note_names
        expected = ('C#', 'D#', 'E', 'F#', 'G#', 'A', 'B')
        self.assertEqual(expected, names)

        names = Key('D# minor').note_names
        expected = ('D#', 'E#', 'F#', 'G#', 'A#', 'B', 'C#')
        self.assertEqual(expected, names)

        names = Key('F# minor').note_names
        expected = ('F#', 'G#', 'A', 'B', 'C#', 'D', 'E')
        self.assertEqual(expected, names)

        names = Key('G# minor').note_names
        expected = ('G#', 'A#', 'B', 'C#', 'D#', 'E', 'F#')
        self.assertEqual(expected, names)

    ####################################################################
    def test_note_names__non_standard_sharps(self):
        names = Key('B# minor').note_names
        expected = ('B#', 'C##', 'D#', 'E#', 'F##', 'G#', 'A#')
        self.assertEqual(expected, names)

        names = Key('E# minor').note_names
        expected = ('E#', 'F##', 'G#', 'A#', 'B#', 'C#', 'D#')
        self.assertEqual(expected, names)

    ####################################################################
    def test_note_names__flat(self):
        names = Key('Ab minor').note_names
        expected = ('Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Fb', 'Gb')
        self.assertEqual(expected, names)

        names = Key('Bb minor').note_names
        expected = ('Bb', 'C', 'Db', 'Eb', 'F', 'Gb', 'Ab')
        self.assertEqual(expected, names)

        names = Key('Db minor').note_names
        expected = ('Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bbb', 'Cb')
        self.assertEqual(expected, names)

        names = Key('Eb minor').note_names
        expected = ('Eb', 'F', 'Gb', 'Ab', 'Bb', 'Cb', 'Db')
        self.assertEqual(expected, names)

        names = Key('Gb minor').note_names
        expected = ('Gb', 'Ab', 'Bbb', 'Cb', 'Db', 'Ebb', 'Fb')
        self.assertEqual(expected, names)

    ####################################################################
    def test_note_names__non_standard_flats(self):
        names = Key('Cb minor').note_names
        expected = ('Cb', 'Db', 'Ebb', 'Fb', 'Gb', 'Abb', 'Bbb')
        self.assertEqual(expected, names)

        names = Key('Fb minor').note_names
        expected = ('Fb', 'Gb', 'Abb', 'Bbb', 'Cb', 'Dbb', 'Ebb')
        self.assertEqual(expected, names)


#######################################################################
class BaseModalScalesInKeyTest(TestCase):

    ####################################################################
    def assert_key_modes_are_correct(self, key):
        expected = key.scale.notes
        error_msg = '"{mode}" scale did not match. {expected} != {actual}'
        scales = []
        print(f'\n{"*" * 50}')
        print(f'Running test on modal scales for {key}.')
        for mode in key.modes:
            print(f'{mode}: {mode.notes}')
            scales.append(mode.notes)
            msg = error_msg.format(mode=mode.name, expected=expected, actual=mode.notes)
            self.assertEqual(expected, mode.notes, msg=msg)
            expected = expected[1:] + (expected[0], )
        return scales


#######################################################################
@unittest.skip('NEED TO RE-IMPLEMENT MODES.')
class TestModesInMajorKeys(BaseModalScalesInKeyTest):

    ####################################################################
    def test_helper_assertion_function(self):
        """
        The helper function iterates through each mode, shifting the expected
        set of notes over 1 degree. For example, from Ionian to Dorian, the
        expected notes for C Major shift from:
            ('C', 'D', 'E', 'F', 'G', 'A', 'B')
        to:
            ('D', 'E', 'F', 'G', 'A', 'B', 'C')

        This test asserts that we are doing so correctly in the helper function.
        """
        modal_scales = self.assert_key_modes_are_correct(Key('C'))
        expected = [
            ('C', 'D', 'E', 'F', 'G', 'A', 'B'),
            ('D', 'E', 'F', 'G', 'A', 'B', 'C'),
            ('E', 'F', 'G', 'A', 'B', 'C', 'D'),
            ('F', 'G', 'A', 'B', 'C', 'D', 'E'),
            ('G', 'A', 'B', 'C', 'D', 'E', 'F'),
            ('A', 'B', 'C', 'D', 'E', 'F', 'G'),
            ('B', 'C', 'D', 'E', 'F', 'G', 'A'),
        ]
        self.assertEqual(expected, modal_scales)

    ####################################################################
    def test_keys_with_natural_tonic(self):
        self.assert_key_modes_are_correct(Key('C'))
        self.assert_key_modes_are_correct(Key('D'))
        self.assert_key_modes_are_correct(Key('E'))
        self.assert_key_modes_are_correct(Key('F'))
        self.assert_key_modes_are_correct(Key('G'))
        self.assert_key_modes_are_correct(Key('A'))
        self.assert_key_modes_are_correct(Key('B'))

    ####################################################################
    def test_keys_with_sharp_tonic(self):
        self.assert_key_modes_are_correct(Key('C#'))
        self.assert_key_modes_are_correct(Key('D#'))
        self.assert_key_modes_are_correct(Key('E#'))
        self.assert_key_modes_are_correct(Key('F#'))
        self.assert_key_modes_are_correct(Key('G#'))
        self.assert_key_modes_are_correct(Key('A#'))
        self.assert_key_modes_are_correct(Key('B#'))

    ####################################################################
    def test_keys_with_flat_tonic(self):
        self.assert_key_modes_are_correct(Key('Cb'))
        self.assert_key_modes_are_correct(Key('Db'))
        self.assert_key_modes_are_correct(Key('Eb'))
        self.assert_key_modes_are_correct(Key('Fb'))
        self.assert_key_modes_are_correct(Key('Gb'))
        self.assert_key_modes_are_correct(Key('Ab'))
        self.assert_key_modes_are_correct(Key('Bb'))


#######################################################################
@unittest.skip('NEED TO RE-IMPLEMENT MODES.')
class TestModesInMinorKeys(BaseModalScalesInKeyTest):

    ####################################################################
    def test_helper_assertion_function(self):
        """
        The helper function iterates through each mode, shifting the expected
        set of notes over 1 degree. For example, from Ionian to Dorian, the
        expected notes for C Minor shift from:
            ('C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb')
        to:
            ('D', 'Eb', 'F', 'G', 'Ab', 'Bb'. 'C')

        This test asserts that we are doing so correctly in the helper function.
        """
        modal_scales = self.assert_key_modes_are_correct(Key('Cm'))
        expected = [
            ('C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'),
            ('D', 'Eb', 'F', 'G', 'Ab', 'Bb', 'C'),
            ('Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D'),
            ('F', 'G', 'Ab', 'Bb', 'C', 'D', 'Eb'),
            ('G', 'Ab', 'Bb', 'C', 'D', 'Eb', 'F'),
            ('Ab', 'Bb', 'C', 'D', 'Eb', 'F', 'G'),
            ('Bb', 'C', 'D', 'Eb', 'F', 'G', 'Ab'),
        ]
        self.assertEqual(expected, modal_scales)

    ####################################################################
    def test_keys_with_natural_tonic(self):
        self.assert_key_modes_are_correct(Key('Cm'))
        self.assert_key_modes_are_correct(Key('Dm'))
        self.assert_key_modes_are_correct(Key('Em'))
        self.assert_key_modes_are_correct(Key('Fm'))
        self.assert_key_modes_are_correct(Key('Gm'))
        self.assert_key_modes_are_correct(Key('Am'))
        self.assert_key_modes_are_correct(Key('Bm'))

    ####################################################################
    def test_keys_with_sharp_tonic(self):
        self.assert_key_modes_are_correct(Key('C#m'))
        self.assert_key_modes_are_correct(Key('D#m'))
        self.assert_key_modes_are_correct(Key('E#m'))
        self.assert_key_modes_are_correct(Key('F#m'))
        self.assert_key_modes_are_correct(Key('G#m'))
        self.assert_key_modes_are_correct(Key('A#m'))
        self.assert_key_modes_are_correct(Key('B#m'))

    ####################################################################
    def test_keys_with_flat_tonic(self):
        self.assert_key_modes_are_correct(Key('Cbm'))
        self.assert_key_modes_are_correct(Key('Dbm'))
        self.assert_key_modes_are_correct(Key('Ebm'))
        self.assert_key_modes_are_correct(Key('Fbm'))
        self.assert_key_modes_are_correct(Key('Gbm'))
        self.assert_key_modes_are_correct(Key('Abm'))
        self.assert_key_modes_are_correct(Key('Bbm'))
