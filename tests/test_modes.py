from unittest import TestCase

from errors import InvalidModeError
from models import Key, MajorScale, C, Mode, D, E, F, G, A, B, IonianScale, E_flat, B_flat, DorianScale, C_sharp, \
    F_sharp, D_sharp, E_sharp, G_sharp, A_sharp, B_sharp, C_flat, D_flat, F_flat, G_flat, A_flat, C_double_sharp, \
    F_double_sharp


#######################################################################
class TestModes(TestCase):

    ####################################################################
    def test_invalid_mode(self):
        with self.assertRaises(InvalidModeError):
            Mode(C, MajorScale)

    ####################################################################
    def test_types(self):
        key_c = Key('C')
        self.assertEqual(IonianScale, key_c.ionian_mode.base_scale)
        self.assertTrue(isinstance(key_c.ionian_mode, Mode))

        c_ionian_mode = Mode(C, IonianScale)
        self.assertEqual(IonianScale, c_ionian_mode.base_scale)
        self.assertTrue(isinstance(c_ionian_mode, Mode))

    ####################################################################
    def test_ionian__natural_tonics(self):
        self.assertEqual(('C', 'D', 'E', 'F', 'G', 'A', 'B'), Mode(C, IonianScale).notes)
        self.assertEqual(('D', 'E', 'F#', 'G', 'A', 'B', 'C#'), Mode(D, IonianScale).notes)
        self.assertEqual(('E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'), Mode(E, IonianScale).notes)
        self.assertEqual(('F', 'G', 'A', 'Bb', 'C', 'D', 'E'), Mode(F, IonianScale).notes)
        self.assertEqual(('G', 'A', 'B', 'C', 'D', 'E', 'F#'), Mode(G, IonianScale).notes)
        self.assertEqual(('A', 'B', 'C#', 'D', 'E', 'F#', 'G#'), Mode(A, IonianScale).notes)
        self.assertEqual(('B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'), Mode(B, IonianScale).notes)

    ####################################################################
    def test_ionian__sharp_tonics(self):
        self.assertEqual(('C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#'), Mode(C_sharp, IonianScale).notes)
        self.assertEqual(('D#', 'E#', 'F##', 'G#', 'A#', 'B#', 'C##'), Mode(D_sharp, IonianScale).notes)
        self.assertEqual(('E#', 'F##', 'G##', 'A#', 'B#', 'C##', 'D##'), Mode(E_sharp, IonianScale).notes)
        self.assertEqual(('F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E#'), Mode(F_sharp, IonianScale).notes)
        self.assertEqual(('G#', 'A#', 'B#', 'C#', 'D#', 'E#', 'F##'), Mode(G_sharp, IonianScale).notes)
        self.assertEqual(('A#', 'B#', 'C##', 'D#', 'E#', 'F##', 'G##'), Mode(A_sharp, IonianScale).notes)
        self.assertEqual(('B#', 'C##', 'D##', 'E#', 'F##', 'G##', 'A##'), Mode(B_sharp, IonianScale).notes)

    ####################################################################
    def test_ionian__flat_tonics(self):
        self.assertEqual(('Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bb'), Mode(C_flat, IonianScale).notes)
        self.assertEqual(('Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C'), Mode(D_flat, IonianScale).notes)
        self.assertEqual(('Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D'), Mode(E_flat, IonianScale).notes)
        self.assertEqual(('Fb', 'Gb', 'Ab', 'Bbb', 'Cb', 'Db', 'Eb'), Mode(F_flat, IonianScale).notes)
        self.assertEqual(('Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'F'), Mode(G_flat, IonianScale).notes)
        self.assertEqual(('Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G'), Mode(A_flat, IonianScale).notes)
        self.assertEqual(('Bb', 'C', 'D', 'Eb', 'F', 'G', 'A'), Mode(B_flat, IonianScale).notes)

    ####################################################################
    def test_dorian__natural_tonics(self):
        self.assertEqual(('C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'), Mode(C, DorianScale).notes)
        self.assertEqual(('D', 'E', 'F', 'G', 'A', 'B', 'C'), Mode(D, DorianScale).notes)
        self.assertEqual(('E', 'F#', 'G', 'A', 'B', 'C#', 'D'), Mode(E, DorianScale).notes)
        self.assertEqual(('F', 'G', 'Ab', 'Bb', 'C', 'D', 'Eb'), Mode(F, DorianScale).notes)
        self.assertEqual(('G', 'A', 'Bb', 'C', 'D', 'E', 'F'), Mode(G, DorianScale).notes)
        self.assertEqual(('A', 'B', 'C', 'D', 'E', 'F#', 'G'), Mode(A, DorianScale).notes)
        self.assertEqual(('B', 'C#', 'D', 'E', 'F#', 'G#', 'A'), Mode(B, DorianScale).notes)

    ####################################################################
    def test_dorian__sharp_tonics(self):
        # DORIAN_INTERVALS = (W, H, W, W, W, H, W)
        self.assertEqual(('C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B'), Mode(C_sharp, DorianScale).notes)
        self.assertEqual(('D#', 'E#', 'F#', 'G#', 'A#', 'B#', 'C#'), Mode(D_sharp, DorianScale).notes)
        self.assertEqual(('E#', 'F##', 'G#', 'A#', 'B#', 'C##', 'D#'), Mode(E_sharp, DorianScale).notes)
        self.assertEqual(('F#', 'G#', 'A', 'B', 'C#', 'D#', 'E'), Mode(F_sharp, DorianScale).notes)
        self.assertEqual(('G#', 'A#', 'B', 'C#', 'D#', 'E#', 'F#'), Mode(G_sharp, DorianScale).notes)
        self.assertEqual(('A#', 'B#', 'C#', 'D#', 'E#', 'F##', 'G#'), Mode(A_sharp, DorianScale).notes)
        self.assertEqual(('B#', 'C##', 'D#', 'E#', 'F##', 'G##', 'A#'), Mode(B_sharp, DorianScale).notes)

    ####################################################################
    def test_dorian__flat_tonics(self):
        self.assertEqual(('Cb', 'Db', 'Ebb', 'Fb', 'Gb', 'Ab', 'Bbb'), Mode(C_flat, DorianScale).notes)
        self.assertEqual(('Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bb', 'Cb'), Mode(D_flat, DorianScale).notes)
        self.assertEqual(('Eb', 'F', 'Gb', 'Ab', 'Bb', 'C', 'Db'), Mode(E_flat, DorianScale).notes)
        self.assertEqual(('Fb', 'Gb', 'Abb', 'Bbb', 'Cb', 'Db', 'Ebb'), Mode(F_flat, DorianScale).notes)
        self.assertEqual(('Gb', 'Ab', 'Bbb', 'Cb', 'Db', 'Eb', 'Fb'), Mode(G_flat, DorianScale).notes)
        self.assertEqual(('Ab', 'Bb', 'Cb', 'Db', 'Eb', 'F', 'Gb'), Mode(A_flat, DorianScale).notes)
        self.assertEqual(('Bb', 'C', 'Db', 'Eb', 'F', 'G', 'Ab'), Mode(B_flat, DorianScale).notes)
