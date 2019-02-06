from unittest import TestCase

from errors import InvalidModeError
from models import Key, MajorScale, C, Mode, D, E, F, G, A, B, IonianScale, E_flat, B_flat, DorianScale, C_sharp, \
    F_sharp, D_sharp, E_sharp, G_sharp, A_sharp, B_sharp, C_flat, D_flat, F_flat, G_flat, A_flat, PhrygianScale, \
    LydianScale, MixolydianScale, AeolianScale, LocrianScale


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

    ####################################################################
    def test_phrygian__natural_tonics(self):
        self.assertEqual(('C', 'Db', 'Eb', 'F', 'G', 'Ab', 'Bb'), Mode(C, PhrygianScale).notes)
        self.assertEqual(('D', 'Eb', 'F', 'G', 'A', 'Bb', 'C'), Mode(D, PhrygianScale).notes)
        self.assertEqual(('E', 'F', 'G', 'A', 'B', 'C', 'D'), Mode(E, PhrygianScale).notes)
        self.assertEqual(('F', 'Gb', 'Ab', 'Bb', 'C', 'Db', 'Eb'), Mode(F, PhrygianScale).notes)
        self.assertEqual(('G', 'Ab', 'Bb', 'C', 'D', 'Eb', 'F'), Mode(G, PhrygianScale).notes)
        self.assertEqual(('A', 'Bb', 'C', 'D', 'E', 'F', 'G'), Mode(A, PhrygianScale).notes)
        self.assertEqual(('B', 'C', 'D', 'E', 'F#', 'G', 'A'), Mode(B, PhrygianScale).notes)

    ####################################################################
    def test_phrygian__sharp_tonics(self):
        self.assertEqual(('C#', 'D', 'E', 'F#', 'G#', 'A', 'B'), Mode(C_sharp, PhrygianScale).notes)
        self.assertEqual(('D#', 'E', 'F#', 'G#', 'A#', 'B', 'C#'), Mode(D_sharp, PhrygianScale).notes)
        self.assertEqual(('E#', 'F#', 'G#', 'A#', 'B#', 'C#', 'D#'), Mode(E_sharp, PhrygianScale).notes)
        self.assertEqual(('F#', 'G', 'A', 'B', 'C#', 'D', 'E'), Mode(F_sharp, PhrygianScale).notes)
        self.assertEqual(('G#', 'A', 'B', 'C#', 'D#', 'E', 'F#'), Mode(G_sharp, PhrygianScale).notes)
        self.assertEqual(('A#', 'B', 'C#', 'D#', 'E#', 'F#', 'G#'), Mode(A_sharp, PhrygianScale).notes)
        self.assertEqual(('B#', 'C#', 'D#', 'E#', 'F##', 'G#', 'A#'), Mode(B_sharp, PhrygianScale).notes)

    ####################################################################
    def test_phrygian__flat_tonics(self):
        self.assertEqual(('Cb', 'Dbb', 'Ebb', 'Fb', 'Gb', 'Abb', 'Bbb'), Mode(C_flat, PhrygianScale).notes)
        self.assertEqual(('Db', 'Ebb', 'Fb', 'Gb', 'Ab', 'Bbb', 'Cb'), Mode(D_flat, PhrygianScale).notes)
        self.assertEqual(('Eb', 'Fb', 'Gb', 'Ab', 'Bb', 'Cb', 'Db'), Mode(E_flat, PhrygianScale).notes)
        self.assertEqual(('Fb', 'Gbb', 'Abb', 'Bbb', 'Cb', 'Dbb', 'Ebb'), Mode(F_flat, PhrygianScale).notes)
        self.assertEqual(('Gb', 'Abb', 'Bbb', 'Cb', 'Db', 'Ebb', 'Fb'), Mode(G_flat, PhrygianScale).notes)
        self.assertEqual(('Ab', 'Bbb', 'Cb', 'Db', 'Eb', 'Fb', 'Gb'), Mode(A_flat, PhrygianScale).notes)
        self.assertEqual(('Bb', 'Cb', 'Db', 'Eb', 'F', 'Gb', 'Ab'), Mode(B_flat, PhrygianScale).notes)

    ####################################################################
    def test_lydian__natural_tonics(self):
        self.assertEqual(('C', 'D', 'E', 'F#', 'G', 'A', 'B'), Mode(C, LydianScale).notes)
        self.assertEqual(('D', 'E', 'F#', 'G#', 'A', 'B', 'C#'), Mode(D, LydianScale).notes)
        self.assertEqual(('E', 'F#', 'G#', 'A#', 'B', 'C#', 'D#'), Mode(E, LydianScale).notes)
        self.assertEqual(('F', 'G', 'A', 'B', 'C', 'D', 'E'), Mode(F, LydianScale).notes)
        self.assertEqual(('G', 'A', 'B', 'C#', 'D', 'E', 'F#'), Mode(G, LydianScale).notes)
        self.assertEqual(('A', 'B', 'C#', 'D#', 'E', 'F#', 'G#'), Mode(A, LydianScale).notes)
        self.assertEqual(('B', 'C#', 'D#', 'E#', 'F#', 'G#', 'A#'), Mode(B, LydianScale).notes)

    ####################################################################
    def test_lydian__sharp_tonics(self):
        self.assertEqual(('C#', 'D#', 'E#', 'F##', 'G#', 'A#', 'B#'), Mode(C_sharp, LydianScale).notes)
        self.assertEqual(('D#', 'E#', 'F##', 'G##', 'A#', 'B#', 'C##'), Mode(D_sharp, LydianScale).notes)
        self.assertEqual(('E#', 'F##', 'G##', 'A##', 'B#', 'C##', 'D##'), Mode(E_sharp, LydianScale).notes)
        self.assertEqual(('F#', 'G#', 'A#', 'B#', 'C#', 'D#', 'E#'), Mode(F_sharp, LydianScale).notes)
        self.assertEqual(('G#', 'A#', 'B#', 'C##', 'D#', 'E#', 'F##'), Mode(G_sharp, LydianScale).notes)
        self.assertEqual(('A#', 'B#', 'C##', 'D##', 'E#', 'F##', 'G##'), Mode(A_sharp, LydianScale).notes)
        self.assertEqual(('B#', 'C##', 'D##', 'E##', 'F##', 'G##', 'A##'), Mode(B_sharp, LydianScale).notes)

    ####################################################################
    def test_lydian__flat_tonics(self):
        self.assertEqual(('Cb', 'Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb'), Mode(C_flat, LydianScale).notes)
        self.assertEqual(('Db', 'Eb', 'F', 'G', 'Ab', 'Bb', 'C'), Mode(D_flat, LydianScale).notes)
        self.assertEqual(('Eb', 'F', 'G', 'A', 'Bb', 'C', 'D'), Mode(E_flat, LydianScale).notes)
        self.assertEqual(('Fb', 'Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb'), Mode(F_flat, LydianScale).notes)
        self.assertEqual(('Gb', 'Ab', 'Bb', 'C', 'Db', 'Eb', 'F'), Mode(G_flat, LydianScale).notes)
        self.assertEqual(('Ab', 'Bb', 'C', 'D', 'Eb', 'F', 'G'), Mode(A_flat, LydianScale).notes)
        self.assertEqual(('Bb', 'C', 'D', 'E', 'F', 'G', 'A'), Mode(B_flat, LydianScale).notes)

    ####################################################################
    def test_mixolydian__natural_tonics(self):
        self.assertEqual(('C', 'D', 'E', 'F', 'G', 'A', 'Bb'), Mode(C, MixolydianScale).notes)
        self.assertEqual(('D', 'E', 'F#', 'G', 'A', 'B', 'C'), Mode(D, MixolydianScale).notes)
        self.assertEqual(('E', 'F#', 'G#', 'A', 'B', 'C#', 'D'), Mode(E, MixolydianScale).notes)
        self.assertEqual(('F', 'G', 'A', 'Bb', 'C', 'D', 'Eb'), Mode(F, MixolydianScale).notes)
        self.assertEqual(('G', 'A', 'B', 'C', 'D', 'E', 'F'), Mode(G, MixolydianScale).notes)
        self.assertEqual(('A', 'B', 'C#', 'D', 'E', 'F#', 'G'), Mode(A, MixolydianScale).notes)
        self.assertEqual(('B', 'C#', 'D#', 'E', 'F#', 'G#', 'A'), Mode(B, MixolydianScale).notes)

    ####################################################################
    def test_mixolydian__sharp_tonics(self):
        self.assertEqual(('C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B'), Mode(C_sharp, MixolydianScale).notes)
        self.assertEqual(('D#', 'E#', 'F##', 'G#', 'A#', 'B#', 'C#'), Mode(D_sharp, MixolydianScale).notes)
        self.assertEqual(('E#', 'F##', 'G##', 'A#', 'B#', 'C##', 'D#'), Mode(E_sharp, MixolydianScale).notes)
        self.assertEqual(('F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E'), Mode(F_sharp, MixolydianScale).notes)
        self.assertEqual(('G#', 'A#', 'B#', 'C#', 'D#', 'E#', 'F#'), Mode(G_sharp, MixolydianScale).notes)
        self.assertEqual(('A#', 'B#', 'C##', 'D#', 'E#', 'F##', 'G#'), Mode(A_sharp, MixolydianScale).notes)
        self.assertEqual(('B#', 'C##', 'D##', 'E#', 'F##', 'G##', 'A#'), Mode(B_sharp, MixolydianScale).notes)

    ####################################################################
    def test_mixolydian__flat_tonics(self):
        self.assertEqual(('Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bbb'), Mode(C_flat, MixolydianScale).notes)
        self.assertEqual(('Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'Cb'), Mode(D_flat, MixolydianScale).notes)
        self.assertEqual(('Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'Db'), Mode(E_flat, MixolydianScale).notes)
        self.assertEqual(('Fb', 'Gb', 'Ab', 'Bbb', 'Cb', 'Db', 'Ebb'), Mode(F_flat, MixolydianScale).notes)
        self.assertEqual(('Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Fb'), Mode(G_flat, MixolydianScale).notes)
        self.assertEqual(('Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'Gb'), Mode(A_flat, MixolydianScale).notes)
        self.assertEqual(('Bb', 'C', 'D', 'Eb', 'F', 'G', 'Ab'), Mode(B_flat, MixolydianScale).notes)

    ####################################################################
    def test_aeolian__natural_tonics(self):
        self.assertEqual(('C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'), Mode(C, AeolianScale).notes)
        self.assertEqual(('D', 'E', 'F', 'G', 'A', 'Bb', 'C'), Mode(D, AeolianScale).notes)
        self.assertEqual(('E', 'F#', 'G', 'A', 'B', 'C', 'D'), Mode(E, AeolianScale).notes)
        self.assertEqual(('F', 'G', 'Ab', 'Bb', 'C', 'Db', 'Eb'), Mode(F, AeolianScale).notes)
        self.assertEqual(('G', 'A', 'Bb', 'C', 'D', 'Eb', 'F'), Mode(G, AeolianScale).notes)
        self.assertEqual(('A', 'B', 'C', 'D', 'E', 'F', 'G'), Mode(A, AeolianScale).notes)
        self.assertEqual(('B', 'C#', 'D', 'E', 'F#', 'G', 'A'), Mode(B, AeolianScale).notes)

    ####################################################################
    def test_aeolian__sharp_tonics(self):
        self.assertEqual(('C#', 'D#', 'E', 'F#', 'G#', 'A', 'B'), Mode(C_sharp, AeolianScale).notes)
        self.assertEqual(('D#', 'E#', 'F#', 'G#', 'A#', 'B', 'C#'), Mode(D_sharp, AeolianScale).notes)
        self.assertEqual(('E#', 'F##', 'G#', 'A#', 'B#', 'C#', 'D#'), Mode(E_sharp, AeolianScale).notes)
        self.assertEqual(('F#', 'G#', 'A', 'B', 'C#', 'D', 'E'), Mode(F_sharp, AeolianScale).notes)
        self.assertEqual(('G#', 'A#', 'B', 'C#', 'D#', 'E', 'F#'), Mode(G_sharp, AeolianScale).notes)
        self.assertEqual(('A#', 'B#', 'C#', 'D#', 'E#', 'F#', 'G#'), Mode(A_sharp, AeolianScale).notes)
        self.assertEqual(('B#', 'C##', 'D#', 'E#', 'F##', 'G#', 'A#'), Mode(B_sharp, AeolianScale).notes)

    ####################################################################
    def test_aeolian__flat_tonics(self):
        self.assertEqual(('Cb', 'Db', 'Ebb', 'Fb', 'Gb', 'Abb', 'Bbb'), Mode(C_flat, AeolianScale).notes)
        self.assertEqual(('Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bbb', 'Cb'), Mode(D_flat, AeolianScale).notes)
        self.assertEqual(('Eb', 'F', 'Gb', 'Ab', 'Bb', 'Cb', 'Db'), Mode(E_flat, AeolianScale).notes)
        self.assertEqual(('Fb', 'Gb', 'Abb', 'Bbb', 'Cb', 'Dbb', 'Ebb'), Mode(F_flat, AeolianScale).notes)
        self.assertEqual(('Gb', 'Ab', 'Bbb', 'Cb', 'Db', 'Ebb', 'Fb'), Mode(G_flat, AeolianScale).notes)
        self.assertEqual(('Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Fb', 'Gb'), Mode(A_flat, AeolianScale).notes)
        self.assertEqual(('Bb', 'C', 'Db', 'Eb', 'F', 'Gb', 'Ab'), Mode(B_flat, AeolianScale).notes)

    ####################################################################
    def test_locrian__natural_tonics(self):
        self.assertEqual(('C', 'Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb'), Mode(C, LocrianScale).notes)
        self.assertEqual(('D', 'Eb', 'F', 'G', 'Ab', 'Bb', 'C'), Mode(D, LocrianScale).notes)
        self.assertEqual(('E', 'F', 'G', 'A', 'Bb', 'C', 'D'), Mode(E, LocrianScale).notes)
        self.assertEqual(('F', 'Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb'), Mode(F, LocrianScale).notes)
        self.assertEqual(('G', 'Ab', 'Bb', 'C', 'Db', 'Eb', 'F'), Mode(G, LocrianScale).notes)
        self.assertEqual(('A', 'Bb', 'C', 'D', 'Eb', 'F', 'G'), Mode(A, LocrianScale).notes)
        self.assertEqual(('B', 'C', 'D', 'E', 'F', 'G', 'A'), Mode(B, LocrianScale).notes)

    ####################################################################
    def test_locrian__sharp_tonics(self):
        self.assertEqual(('C#', 'D', 'E', 'F#', 'G', 'A', 'B'), Mode(C_sharp, LocrianScale).notes)
        self.assertEqual(('D#', 'E', 'F#', 'G#', 'A', 'B', 'C#'), Mode(D_sharp, LocrianScale).notes)
        self.assertEqual(('E#', 'F#', 'G#', 'A#', 'B', 'C#', 'D#'), Mode(E_sharp, LocrianScale).notes)
        self.assertEqual(('F#', 'G', 'A', 'B', 'C', 'D', 'E'), Mode(F_sharp, LocrianScale).notes)
        self.assertEqual(('G#', 'A', 'B', 'C#', 'D', 'E', 'F#'), Mode(G_sharp, LocrianScale).notes)
        self.assertEqual(('A#', 'B', 'C#', 'D#', 'E', 'F#', 'G#'), Mode(A_sharp, LocrianScale).notes)
        self.assertEqual(('B#', 'C#', 'D#', 'E#', 'F#', 'G#', 'A#'), Mode(B_sharp, LocrianScale).notes)

    ####################################################################
    def test_locrian__flat_tonics(self):
        self.assertEqual(('Cb', 'Dbb', 'Ebb', 'Fb', 'Gbb', 'Abb', 'Bbb'), Mode(C_flat, LocrianScale).notes)
        self.assertEqual(('Db', 'Ebb', 'Fb', 'Gb', 'Abb', 'Bbb', 'Cb'), Mode(D_flat, LocrianScale).notes)
        self.assertEqual(('Eb', 'Fb', 'Gb', 'Ab', 'Bbb', 'Cb', 'Db'), Mode(E_flat, LocrianScale).notes)
        self.assertEqual(('Fb', 'Gbb', 'Abb', 'Bbb', 'Cbb', 'Dbb', 'Ebb'), Mode(F_flat, LocrianScale).notes)
        self.assertEqual(('Gb', 'Abb', 'Bbb', 'Cb', 'Dbb', 'Ebb', 'Fb'), Mode(G_flat, LocrianScale).notes)
        self.assertEqual(('Ab', 'Bbb', 'Cb', 'Db', 'Ebb', 'Fb', 'Gb'), Mode(A_flat, LocrianScale).notes)
        self.assertEqual(('Bb', 'Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab'), Mode(B_flat, LocrianScale).notes)
