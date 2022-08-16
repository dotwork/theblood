from unittest import TestCase

from the_blood.models import *


#######################################################################
class TestPitchMap(TestCase):

    ###################################################################
    def test_pitch_map__pitch_to_notes(self):
        expected = ((B_sharp, Octave(0)), (C, Octave(0)), (D_double_flat, Octave(0)))
        self.assertEqual(expected, PitchMap(Pitch(16.35)))

    ###################################################################
    def test_pitch_map__note_to_pitch(self):
        self.assertEqual(Pitch(16.35), PitchMap((C, Octave(0))))
        self.assertEqual(Pitch(16.35), PitchMap((B_sharp, Octave(0))))


#######################################################################
class TestPitch(TestCase):

    ###################################################################
    def setUp(self):
        self.a4 = Pitch(440)

    ###################################################################
    def test_multiply(self):
        self.assertEqual(Pitch(880), Pitch(440) * 2)

    ###################################################################
    # def test_divide(self):
    #     self.assertEqual(Pitch(440), Pitch(880) / 2)
    #     self.assertEqual(2, 880 / Pitch(440))

    ###################################################################
    def test_add(self):
        self.assertEqual(Pitch(440), Pitch(220) + 220)

    ###################################################################
    def test_subtract(self):
        self.assertEqual(Pitch(220), Pitch(440) - 220)
        self.assertEqual(Pitch(220), 440 - Pitch(220))

    ###################################################################
    def test_greater_than(self):
        self.assertTrue(Pitch(440) > Pitch(220))

    ###################################################################
    def test_less_than(self):
        self.assertTrue(Pitch(220) < Pitch(440))

    ####################################################################
    # def test_in_tune(self):
    #     pitch_2 = Pitch(440)
    #     self.assertTrue(IN_TUNE, self.a4.in_tune(pitch_2))
    #
    # ####################################################################
    # def test_sharp(self):
    #     pitch_2 = self.a4 * 1.051
    #     self.assertEqual(SHARP, self.a4.in_tune(pitch_2))
    #
    #     pitch_2 = self.a4 * 1.05
    #     self.assertEqual('In Tune', self.a4.in_tune(pitch_2))
    #
    # ####################################################################
    # def test_flat(self):
    #     pitch_2 = self.a4 * 0.949
    #     self.assertEqual(FLAT, self.a4.in_tune(pitch_2))
    #
    #     pitch_2 = self.a4 * 0.95
    #     self.assertEqual(IN_TUNE, self.a4.in_tune(pitch_2))
