from unittest import TestCase

from the_blood.models import *


#######################################################################
class TestModes(TestCase):

    ####################################################################
    def test_invalid_mode(self):
        with self.assertRaises(InvalidModeError):
            Mode(C, MajorScale)

    ####################################################################
    def test_types(self):
        c_ionian_mode = Mode(C, IonianScale)
        self.assertEqual(IonianScale, c_ionian_mode.base_scale)
        self.assertTrue(isinstance(c_ionian_mode, Mode))

    ####################################################################
    def test_ionian__natural_tonics(self):
        self.assertEqual(('C', 'D', 'E', 'F', 'G', 'A', 'B'), Mode(C, IonianScale).note_names)
        self.assertEqual(('D', 'E', 'F#', 'G', 'A', 'B', 'C#'), Mode(D, IonianScale).note_names)
        self.assertEqual(('E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'), Mode(E, IonianScale).note_names)
        self.assertEqual(('F', 'G', 'A', 'Bb', 'C', 'D', 'E'), Mode(F, IonianScale).note_names)
        self.assertEqual(('G', 'A', 'B', 'C', 'D', 'E', 'F#'), Mode(G, IonianScale).note_names)
        self.assertEqual(('A', 'B', 'C#', 'D', 'E', 'F#', 'G#'), Mode(A, IonianScale).note_names)
        self.assertEqual(('B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'), Mode(B, IonianScale).note_names)

    ####################################################################
    def test_ionian__sharp_tonics(self):
        self.assertEqual(('C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#'), Mode(C_sharp, IonianScale).note_names)
        self.assertEqual(('D#', 'E#', 'F##', 'G#', 'A#', 'B#', 'C##'), Mode(D_sharp, IonianScale).note_names)
        self.assertEqual(('E#', 'F##', 'G##', 'A#', 'B#', 'C##', 'D##'), Mode(E_sharp, IonianScale).note_names)
        self.assertEqual(('F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E#'), Mode(F_sharp, IonianScale).note_names)
        self.assertEqual(('G#', 'A#', 'B#', 'C#', 'D#', 'E#', 'F##'), Mode(G_sharp, IonianScale).note_names)
        self.assertEqual(('A#', 'B#', 'C##', 'D#', 'E#', 'F##', 'G##'), Mode(A_sharp, IonianScale).note_names)
        self.assertEqual(('B#', 'C##', 'D##', 'E#', 'F##', 'G##', 'A##'), Mode(B_sharp, IonianScale).note_names)

    ####################################################################
    def test_ionian__flat_tonics(self):
        self.assertEqual(('Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bb'), Mode(C_flat, IonianScale).note_names)
        self.assertEqual(('Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C'), Mode(D_flat, IonianScale).note_names)
        self.assertEqual(('Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D'), Mode(E_flat, IonianScale).note_names)
        self.assertEqual(('Fb', 'Gb', 'Ab', 'Bbb', 'Cb', 'Db', 'Eb'), Mode(F_flat, IonianScale).note_names)
        self.assertEqual(('Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'F'), Mode(G_flat, IonianScale).note_names)
        self.assertEqual(('Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G'), Mode(A_flat, IonianScale).note_names)
        self.assertEqual(('Bb', 'C', 'D', 'Eb', 'F', 'G', 'A'), Mode(B_flat, IonianScale).note_names)

    ####################################################################
    def test_dorian__natural_tonics(self):
        self.assertEqual(('C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'), Mode(C, DorianScale).note_names)
        self.assertEqual(('D', 'E', 'F', 'G', 'A', 'B', 'C'), Mode(D, DorianScale).note_names)
        self.assertEqual(('E', 'F#', 'G', 'A', 'B', 'C#', 'D'), Mode(E, DorianScale).note_names)
        self.assertEqual(('F', 'G', 'Ab', 'Bb', 'C', 'D', 'Eb'), Mode(F, DorianScale).note_names)
        self.assertEqual(('G', 'A', 'Bb', 'C', 'D', 'E', 'F'), Mode(G, DorianScale).note_names)
        self.assertEqual(('A', 'B', 'C', 'D', 'E', 'F#', 'G'), Mode(A, DorianScale).note_names)
        self.assertEqual(('B', 'C#', 'D', 'E', 'F#', 'G#', 'A'), Mode(B, DorianScale).note_names)

    ####################################################################
    def test_dorian__sharp_tonics(self):
        self.assertEqual(('C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B'), Mode(C_sharp, DorianScale).note_names)
        self.assertEqual(('D#', 'E#', 'F#', 'G#', 'A#', 'B#', 'C#'), Mode(D_sharp, DorianScale).note_names)
        self.assertEqual(('E#', 'F##', 'G#', 'A#', 'B#', 'C##', 'D#'), Mode(E_sharp, DorianScale).note_names)
        self.assertEqual(('F#', 'G#', 'A', 'B', 'C#', 'D#', 'E'), Mode(F_sharp, DorianScale).note_names)
        self.assertEqual(('G#', 'A#', 'B', 'C#', 'D#', 'E#', 'F#'), Mode(G_sharp, DorianScale).note_names)
        self.assertEqual(('A#', 'B#', 'C#', 'D#', 'E#', 'F##', 'G#'), Mode(A_sharp, DorianScale).note_names)
        self.assertEqual(('B#', 'C##', 'D#', 'E#', 'F##', 'G##', 'A#'), Mode(B_sharp, DorianScale).note_names)

    ####################################################################
    def test_dorian__flat_tonics(self):
        self.assertEqual(('Cb', 'Db', 'Ebb', 'Fb', 'Gb', 'Ab', 'Bbb'), Mode(C_flat, DorianScale).note_names)
        self.assertEqual(('Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bb', 'Cb'), Mode(D_flat, DorianScale).note_names)
        self.assertEqual(('Eb', 'F', 'Gb', 'Ab', 'Bb', 'C', 'Db'), Mode(E_flat, DorianScale).note_names)
        self.assertEqual(('Fb', 'Gb', 'Abb', 'Bbb', 'Cb', 'Db', 'Ebb'), Mode(F_flat, DorianScale).note_names)
        self.assertEqual(('Gb', 'Ab', 'Bbb', 'Cb', 'Db', 'Eb', 'Fb'), Mode(G_flat, DorianScale).note_names)
        self.assertEqual(('Ab', 'Bb', 'Cb', 'Db', 'Eb', 'F', 'Gb'), Mode(A_flat, DorianScale).note_names)
        self.assertEqual(('Bb', 'C', 'Db', 'Eb', 'F', 'G', 'Ab'), Mode(B_flat, DorianScale).note_names)

    ####################################################################
    def test_phrygian__natural_tonics(self):
        self.assertEqual(('C', 'Db', 'Eb', 'F', 'G', 'Ab', 'Bb'), Mode(C, PhrygianScale).note_names)
        self.assertEqual(('D', 'Eb', 'F', 'G', 'A', 'Bb', 'C'), Mode(D, PhrygianScale).note_names)
        self.assertEqual(('E', 'F', 'G', 'A', 'B', 'C', 'D'), Mode(E, PhrygianScale).note_names)
        self.assertEqual(('F', 'Gb', 'Ab', 'Bb', 'C', 'Db', 'Eb'), Mode(F, PhrygianScale).note_names)
        self.assertEqual(('G', 'Ab', 'Bb', 'C', 'D', 'Eb', 'F'), Mode(G, PhrygianScale).note_names)
        self.assertEqual(('A', 'Bb', 'C', 'D', 'E', 'F', 'G'), Mode(A, PhrygianScale).note_names)
        self.assertEqual(('B', 'C', 'D', 'E', 'F#', 'G', 'A'), Mode(B, PhrygianScale).note_names)

    ####################################################################
    def test_phrygian__sharp_tonics(self):
        self.assertEqual(('C#', 'D', 'E', 'F#', 'G#', 'A', 'B'), Mode(C_sharp, PhrygianScale).note_names)
        self.assertEqual(('D#', 'E', 'F#', 'G#', 'A#', 'B', 'C#'), Mode(D_sharp, PhrygianScale).note_names)
        self.assertEqual(('E#', 'F#', 'G#', 'A#', 'B#', 'C#', 'D#'), Mode(E_sharp, PhrygianScale).note_names)
        self.assertEqual(('F#', 'G', 'A', 'B', 'C#', 'D', 'E'), Mode(F_sharp, PhrygianScale).note_names)
        self.assertEqual(('G#', 'A', 'B', 'C#', 'D#', 'E', 'F#'), Mode(G_sharp, PhrygianScale).note_names)
        self.assertEqual(('A#', 'B', 'C#', 'D#', 'E#', 'F#', 'G#'), Mode(A_sharp, PhrygianScale).note_names)
        self.assertEqual(('B#', 'C#', 'D#', 'E#', 'F##', 'G#', 'A#'), Mode(B_sharp, PhrygianScale).note_names)

    ####################################################################
    def test_phrygian__flat_tonics(self):
        self.assertEqual(('Cb', 'Dbb', 'Ebb', 'Fb', 'Gb', 'Abb', 'Bbb'), Mode(C_flat, PhrygianScale).note_names)
        self.assertEqual(('Db', 'Ebb', 'Fb', 'Gb', 'Ab', 'Bbb', 'Cb'), Mode(D_flat, PhrygianScale).note_names)
        self.assertEqual(('Eb', 'Fb', 'Gb', 'Ab', 'Bb', 'Cb', 'Db'), Mode(E_flat, PhrygianScale).note_names)
        self.assertEqual(('Fb', 'Gbb', 'Abb', 'Bbb', 'Cb', 'Dbb', 'Ebb'), Mode(F_flat, PhrygianScale).note_names)
        self.assertEqual(('Gb', 'Abb', 'Bbb', 'Cb', 'Db', 'Ebb', 'Fb'), Mode(G_flat, PhrygianScale).note_names)
        self.assertEqual(('Ab', 'Bbb', 'Cb', 'Db', 'Eb', 'Fb', 'Gb'), Mode(A_flat, PhrygianScale).note_names)
        self.assertEqual(('Bb', 'Cb', 'Db', 'Eb', 'F', 'Gb', 'Ab'), Mode(B_flat, PhrygianScale).note_names)

    ####################################################################
    def test_lydian__natural_tonics(self):
        self.assertEqual(('C', 'D', 'E', 'F#', 'G', 'A', 'B'), Mode(C, LydianScale).note_names)
        self.assertEqual(('D', 'E', 'F#', 'G#', 'A', 'B', 'C#'), Mode(D, LydianScale).note_names)
        self.assertEqual(('E', 'F#', 'G#', 'A#', 'B', 'C#', 'D#'), Mode(E, LydianScale).note_names)
        self.assertEqual(('F', 'G', 'A', 'B', 'C', 'D', 'E'), Mode(F, LydianScale).note_names)
        self.assertEqual(('G', 'A', 'B', 'C#', 'D', 'E', 'F#'), Mode(G, LydianScale).note_names)
        self.assertEqual(('A', 'B', 'C#', 'D#', 'E', 'F#', 'G#'), Mode(A, LydianScale).note_names)
        self.assertEqual(('B', 'C#', 'D#', 'E#', 'F#', 'G#', 'A#'), Mode(B, LydianScale).note_names)

    ####################################################################
    def test_lydian__sharp_tonics(self):
        self.assertEqual(('C#', 'D#', 'E#', 'F##', 'G#', 'A#', 'B#'), Mode(C_sharp, LydianScale).note_names)
        self.assertEqual(('D#', 'E#', 'F##', 'G##', 'A#', 'B#', 'C##'), Mode(D_sharp, LydianScale).note_names)
        self.assertEqual(('E#', 'F##', 'G##', 'A##', 'B#', 'C##', 'D##'), Mode(E_sharp, LydianScale).note_names)
        self.assertEqual(('F#', 'G#', 'A#', 'B#', 'C#', 'D#', 'E#'), Mode(F_sharp, LydianScale).note_names)
        self.assertEqual(('G#', 'A#', 'B#', 'C##', 'D#', 'E#', 'F##'), Mode(G_sharp, LydianScale).note_names)
        self.assertEqual(('A#', 'B#', 'C##', 'D##', 'E#', 'F##', 'G##'), Mode(A_sharp, LydianScale).note_names)
        self.assertEqual(('B#', 'C##', 'D##', 'E##', 'F##', 'G##', 'A##'), Mode(B_sharp, LydianScale).note_names)

    ####################################################################
    def test_lydian__flat_tonics(self):
        self.assertEqual(('Cb', 'Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb'), Mode(C_flat, LydianScale).note_names)
        self.assertEqual(('Db', 'Eb', 'F', 'G', 'Ab', 'Bb', 'C'), Mode(D_flat, LydianScale).note_names)
        self.assertEqual(('Eb', 'F', 'G', 'A', 'Bb', 'C', 'D'), Mode(E_flat, LydianScale).note_names)
        self.assertEqual(('Fb', 'Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb'), Mode(F_flat, LydianScale).note_names)
        self.assertEqual(('Gb', 'Ab', 'Bb', 'C', 'Db', 'Eb', 'F'), Mode(G_flat, LydianScale).note_names)
        self.assertEqual(('Ab', 'Bb', 'C', 'D', 'Eb', 'F', 'G'), Mode(A_flat, LydianScale).note_names)
        self.assertEqual(('Bb', 'C', 'D', 'E', 'F', 'G', 'A'), Mode(B_flat, LydianScale).note_names)

    ####################################################################
    def test_mixolydian__natural_tonics(self):
        self.assertEqual(('C', 'D', 'E', 'F', 'G', 'A', 'Bb'), Mode(C, MixolydianScale).note_names)
        self.assertEqual(('D', 'E', 'F#', 'G', 'A', 'B', 'C'), Mode(D, MixolydianScale).note_names)
        self.assertEqual(('E', 'F#', 'G#', 'A', 'B', 'C#', 'D'), Mode(E, MixolydianScale).note_names)
        self.assertEqual(('F', 'G', 'A', 'Bb', 'C', 'D', 'Eb'), Mode(F, MixolydianScale).note_names)
        self.assertEqual(('G', 'A', 'B', 'C', 'D', 'E', 'F'), Mode(G, MixolydianScale).note_names)
        self.assertEqual(('A', 'B', 'C#', 'D', 'E', 'F#', 'G'), Mode(A, MixolydianScale).note_names)
        self.assertEqual(('B', 'C#', 'D#', 'E', 'F#', 'G#', 'A'), Mode(B, MixolydianScale).note_names)

    ####################################################################
    def test_mixolydian__sharp_tonics(self):
        self.assertEqual(('C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B'), Mode(C_sharp, MixolydianScale).note_names)
        self.assertEqual(('D#', 'E#', 'F##', 'G#', 'A#', 'B#', 'C#'), Mode(D_sharp, MixolydianScale).note_names)
        self.assertEqual(('E#', 'F##', 'G##', 'A#', 'B#', 'C##', 'D#'), Mode(E_sharp, MixolydianScale).note_names)
        self.assertEqual(('F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E'), Mode(F_sharp, MixolydianScale).note_names)
        self.assertEqual(('G#', 'A#', 'B#', 'C#', 'D#', 'E#', 'F#'), Mode(G_sharp, MixolydianScale).note_names)
        self.assertEqual(('A#', 'B#', 'C##', 'D#', 'E#', 'F##', 'G#'), Mode(A_sharp, MixolydianScale).note_names)
        self.assertEqual(('B#', 'C##', 'D##', 'E#', 'F##', 'G##', 'A#'), Mode(B_sharp, MixolydianScale).note_names)

    ####################################################################
    def test_mixolydian__flat_tonics(self):
        self.assertEqual(('Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bbb'), Mode(C_flat, MixolydianScale).note_names)
        self.assertEqual(('Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'Cb'), Mode(D_flat, MixolydianScale).note_names)
        self.assertEqual(('Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'Db'), Mode(E_flat, MixolydianScale).note_names)
        self.assertEqual(('Fb', 'Gb', 'Ab', 'Bbb', 'Cb', 'Db', 'Ebb'), Mode(F_flat, MixolydianScale).note_names)
        self.assertEqual(('Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Fb'), Mode(G_flat, MixolydianScale).note_names)
        self.assertEqual(('Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'Gb'), Mode(A_flat, MixolydianScale).note_names)
        self.assertEqual(('Bb', 'C', 'D', 'Eb', 'F', 'G', 'Ab'), Mode(B_flat, MixolydianScale).note_names)

    ####################################################################
    def test_aeolian__natural_tonics(self):
        self.assertEqual(('C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'), Mode(C, AeolianScale).note_names)
        self.assertEqual(('D', 'E', 'F', 'G', 'A', 'Bb', 'C'), Mode(D, AeolianScale).note_names)
        self.assertEqual(('E', 'F#', 'G', 'A', 'B', 'C', 'D'), Mode(E, AeolianScale).note_names)
        self.assertEqual(('F', 'G', 'Ab', 'Bb', 'C', 'Db', 'Eb'), Mode(F, AeolianScale).note_names)
        self.assertEqual(('G', 'A', 'Bb', 'C', 'D', 'Eb', 'F'), Mode(G, AeolianScale).note_names)
        self.assertEqual(('A', 'B', 'C', 'D', 'E', 'F', 'G'), Mode(A, AeolianScale).note_names)
        self.assertEqual(('B', 'C#', 'D', 'E', 'F#', 'G', 'A'), Mode(B, AeolianScale).note_names)

    ####################################################################
    def test_aeolian__sharp_tonics(self):
        self.assertEqual(('C#', 'D#', 'E', 'F#', 'G#', 'A', 'B'), Mode(C_sharp, AeolianScale).note_names)
        self.assertEqual(('D#', 'E#', 'F#', 'G#', 'A#', 'B', 'C#'), Mode(D_sharp, AeolianScale).note_names)
        self.assertEqual(('E#', 'F##', 'G#', 'A#', 'B#', 'C#', 'D#'), Mode(E_sharp, AeolianScale).note_names)
        self.assertEqual(('F#', 'G#', 'A', 'B', 'C#', 'D', 'E'), Mode(F_sharp, AeolianScale).note_names)
        self.assertEqual(('G#', 'A#', 'B', 'C#', 'D#', 'E', 'F#'), Mode(G_sharp, AeolianScale).note_names)
        self.assertEqual(('A#', 'B#', 'C#', 'D#', 'E#', 'F#', 'G#'), Mode(A_sharp, AeolianScale).note_names)
        self.assertEqual(('B#', 'C##', 'D#', 'E#', 'F##', 'G#', 'A#'), Mode(B_sharp, AeolianScale).note_names)

    ####################################################################
    def test_aeolian__flat_tonics(self):
        self.assertEqual(('Cb', 'Db', 'Ebb', 'Fb', 'Gb', 'Abb', 'Bbb'), Mode(C_flat, AeolianScale).note_names)
        self.assertEqual(('Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bbb', 'Cb'), Mode(D_flat, AeolianScale).note_names)
        self.assertEqual(('Eb', 'F', 'Gb', 'Ab', 'Bb', 'Cb', 'Db'), Mode(E_flat, AeolianScale).note_names)
        self.assertEqual(('Fb', 'Gb', 'Abb', 'Bbb', 'Cb', 'Dbb', 'Ebb'), Mode(F_flat, AeolianScale).note_names)
        self.assertEqual(('Gb', 'Ab', 'Bbb', 'Cb', 'Db', 'Ebb', 'Fb'), Mode(G_flat, AeolianScale).note_names)
        self.assertEqual(('Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Fb', 'Gb'), Mode(A_flat, AeolianScale).note_names)
        self.assertEqual(('Bb', 'C', 'Db', 'Eb', 'F', 'Gb', 'Ab'), Mode(B_flat, AeolianScale).note_names)

    ####################################################################
    def test_locrian__natural_tonics(self):
        self.assertEqual(('C', 'Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb'), Mode(C, LocrianScale).note_names)
        self.assertEqual(('D', 'Eb', 'F', 'G', 'Ab', 'Bb', 'C'), Mode(D, LocrianScale).note_names)
        self.assertEqual(('E', 'F', 'G', 'A', 'Bb', 'C', 'D'), Mode(E, LocrianScale).note_names)
        self.assertEqual(('F', 'Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb'), Mode(F, LocrianScale).note_names)
        self.assertEqual(('G', 'Ab', 'Bb', 'C', 'Db', 'Eb', 'F'), Mode(G, LocrianScale).note_names)
        self.assertEqual(('A', 'Bb', 'C', 'D', 'Eb', 'F', 'G'), Mode(A, LocrianScale).note_names)
        self.assertEqual(('B', 'C', 'D', 'E', 'F', 'G', 'A'), Mode(B, LocrianScale).note_names)

    ####################################################################
    def test_locrian__sharp_tonics(self):
        self.assertEqual(('C#', 'D', 'E', 'F#', 'G', 'A', 'B'), Mode(C_sharp, LocrianScale).note_names)
        self.assertEqual(('D#', 'E', 'F#', 'G#', 'A', 'B', 'C#'), Mode(D_sharp, LocrianScale).note_names)
        self.assertEqual(('E#', 'F#', 'G#', 'A#', 'B', 'C#', 'D#'), Mode(E_sharp, LocrianScale).note_names)
        self.assertEqual(('F#', 'G', 'A', 'B', 'C', 'D', 'E'), Mode(F_sharp, LocrianScale).note_names)
        self.assertEqual(('G#', 'A', 'B', 'C#', 'D', 'E', 'F#'), Mode(G_sharp, LocrianScale).note_names)
        self.assertEqual(('A#', 'B', 'C#', 'D#', 'E', 'F#', 'G#'), Mode(A_sharp, LocrianScale).note_names)
        self.assertEqual(('B#', 'C#', 'D#', 'E#', 'F#', 'G#', 'A#'), Mode(B_sharp, LocrianScale).note_names)

    ####################################################################
    def test_locrian__flat_tonics(self):
        self.assertEqual(('Cb', 'Dbb', 'Ebb', 'Fb', 'Gbb', 'Abb', 'Bbb'), Mode(C_flat, LocrianScale).note_names)
        self.assertEqual(('Db', 'Ebb', 'Fb', 'Gb', 'Abb', 'Bbb', 'Cb'), Mode(D_flat, LocrianScale).note_names)
        self.assertEqual(('Eb', 'Fb', 'Gb', 'Ab', 'Bbb', 'Cb', 'Db'), Mode(E_flat, LocrianScale).note_names)
        self.assertEqual(('Fb', 'Gbb', 'Abb', 'Bbb', 'Cbb', 'Dbb', 'Ebb'), Mode(F_flat, LocrianScale).note_names)
        self.assertEqual(('Gb', 'Abb', 'Bbb', 'Cb', 'Dbb', 'Ebb', 'Fb'), Mode(G_flat, LocrianScale).note_names)
        self.assertEqual(('Ab', 'Bbb', 'Cb', 'Db', 'Ebb', 'Fb', 'Gb'), Mode(A_flat, LocrianScale).note_names)
        self.assertEqual(('Bb', 'Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab'), Mode(B_flat, LocrianScale).note_names)
