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
