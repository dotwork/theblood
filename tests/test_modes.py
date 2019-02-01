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
    def test_ionian(self):
        c_ionian_mode = Mode(C, IonianScale)
        key_c = Key('C')
        self.assertEqual((C, D, E, F, G, A, B), c_ionian_mode.notes)
        self.assertEqual(c_ionian_mode, key_c.ionian_mode)
        self.assertEqual(c_ionian_mode, key_c.scale)

    ####################################################################
    def test_ionian__c_sharp(self):
        c_sharp_ionian_mode = Mode(C_sharp, IonianScale)
        key_c_sharp = Key('C#')
        expected_notes = (C_sharp, D_sharp, E_sharp, F_sharp, G_sharp, A_sharp, B_sharp)
        self.assertEqual(expected_notes, c_sharp_ionian_mode.notes)
        self.assertEqual(c_sharp_ionian_mode, key_c_sharp.ionian_mode)
        self.assertEqual(c_sharp_ionian_mode, key_c_sharp.scale)

    ####################################################################
    def test_ionian__c_flat(self):
        c_flat_ionian_mode = Mode(C_flat, IonianScale)
        key_c_flat = Key('Cb')
        expected_notes = (C_flat, D_flat, E_flat, F_flat, G_flat, A_flat, B_flat)
        self.assertEqual(expected_notes, c_flat_ionian_mode.notes)
        self.assertEqual(c_flat_ionian_mode, key_c_flat.ionian_mode)
        self.assertEqual(c_flat_ionian_mode, key_c_flat.scale)

    ####################################################################
    def test_ionian__d(self):
        d_ionian_mode = Mode(D, IonianScale)
        key_d = Key('D')
        self.assertEqual((D, E, F_sharp, G, A, B, C_sharp), d_ionian_mode.notes)
        self.assertEqual(d_ionian_mode, key_d.ionian_mode)
        self.assertEqual(d_ionian_mode, key_d.scale)

    ####################################################################
    def test_ionian__d_sharp(self):
        d_sharp_ionian_mode = Mode(D_sharp, IonianScale)
        key_d_sharp = Key('D#')
        expected_notes = (D_sharp, E_sharp, F_double_sharp, G_sharp, A_sharp, B_sharp, C_double_sharp)
        self.assertEqual(expected_notes, d_sharp_ionian_mode.notes)
        self.assertEqual(d_sharp_ionian_mode, key_d_sharp.ionian_mode)
        self.assertEqual(d_sharp_ionian_mode, key_d_sharp.scale)

    ####################################################################
    def test_ionian__d_flat(self):
        d_flat_ionian_mode = Mode(D_flat, IonianScale)
        key_d_flat = Key('Db')
        expected_notes = (D_flat, E_flat, F, G_flat, A_flat, B_flat, C)
        self.assertEqual(expected_notes, d_flat_ionian_mode.notes)
        self.assertEqual(d_flat_ionian_mode, key_d_flat.ionian_mode)
        self.assertEqual(d_flat_ionian_mode, key_d_flat.scale)

    ####################################################################
    def test_modes_in_key_of_c(self):
        key_c = Key('C')

        # Starting on C, playing ionian scale to stay in key of C
        self.assertEqual((C, D, E, F, G, A, B), key_c.ionian_mode.notes)
        self.assertEqual((D, E, F, G, A, B, C), key_c.dorian_mode.notes)
        self.assertEqual((E, F, G, A, B, C, D), key_c.phrygian_mode.notes)
        self.assertEqual((F, G, A, B, C, D, E), key_c.lydian_mode.notes)
        self.assertEqual((G, A, B, C, D, E, F), key_c.mixolydian_mode.notes)
        self.assertEqual((A, B, C, D, E, F, G), key_c.aeolian_mode.notes)
        self.assertEqual((B, C, D, E, F, G, A), key_c.locrian_mode.notes)

    ####################################################################
    def test_dorian(self):
        # Starting on D, playing dorian scale to stay in key of C
        key_c = Key('C')
        self.assertEqual((D, E, F, G, A, B, C), key_c.dorian_mode.notes)

        # The dorian scale starting on C, puts us in key of B flat
        c_dorian_mode = Mode(C, DorianScale)
        self.assertEqual((C, D, E_flat, F, G, A, B_flat), c_dorian_mode.notes)
        key_b_flat = Key('Bb')
        c_dorian_note_names = tuple(n.name for n in c_dorian_mode.notes)
        self.assertEqual(set(key_b_flat.note_names), set(c_dorian_note_names))
