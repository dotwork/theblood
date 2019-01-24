from decimal import Decimal
from unittest import TestCase

from data import PITCHES
from models import Pitch, IN_TUNE, FLAT, SHARP, PitchMap, G_double_sharp, A, B_double_flat, B_sharp, C, D_double_flat


#######################################################################
class TestPitchMap(TestCase):

    ###################################################################
    def test_pitch_map__pitch_to_notes(self):
        self.assertEqual(['B#0', 'C0', 'Dbb0'], PitchMap[Decimal('16.35')])

    ###################################################################
    def test_pitch_map__note_to_pitch(self):
        self.assertEqual(Decimal('16.35'), PitchMap['C0'])
        self.assertEqual(Decimal('16.35'), PitchMap['B#0'])

    ###################################################################
    def test_pitch_map__length(self):
        """
        Iterating through it should iterate through the distinct
        pitch values, rather than the notes which have duplicates
        (harmonically equivalent notes such as A# and B#)
        """
        self.assertEqual(len(PITCHES), len(PitchMap))


#######################################################################
class TestPitch(TestCase):

    ###################################################################
    def setUp(self):
        self.a4 = Pitch('440')

    ###################################################################
    def test_multiply(self):
        self.assertEqual(Pitch('880'), Pitch('440') * 2)

    ###################################################################
    def test_divide(self):
        self.assertEqual(Pitch('440'), Pitch('880') / 2)
        self.assertEqual(Pitch('2'), Decimal('880') / Pitch('440'))

    ###################################################################
    def test_add(self):
        self.assertEqual(Pitch('440'), Pitch('220') + Decimal('220'))

    ###################################################################
    def test_subtract(self):
        self.assertEqual(Pitch('220'), Pitch('440') - Decimal('220'))
        self.assertEqual(Pitch('220'), Decimal('440') - Pitch('220'))

    ###################################################################
    def test_greater_than(self):
        self.assertTrue(Pitch('440') > Pitch('220'))

    ###################################################################
    def test_less_than(self):
        self.assertTrue(Pitch('220') < Pitch('440'))

    ###################################################################
    def test_notes(self):
        self.assertEqual([B_sharp, C, D_double_flat], Pitch('16.35').notes)
        self.assertEqual([G_double_sharp, A, B_double_flat], Pitch('440').notes)

    ####################################################################
    def test_in_tune(self):
        pitch_2 = Pitch('440')
        self.assertTrue(IN_TUNE, self.a4.in_tune(pitch_2))

    ####################################################################
    def test_sharp(self):
        pitch_2 = self.a4 * Decimal('1.051')
        self.assertEqual(SHARP, self.a4.in_tune(pitch_2))

        pitch_2 = self.a4 * Decimal('1.05')
        self.assertEqual('In Tune', self.a4.in_tune(pitch_2))

    ####################################################################
    def test_flat(self):
        pitch_2 = self.a4 * Decimal('0.949')
        self.assertEqual(FLAT, self.a4.in_tune(pitch_2))

        pitch_2 = self.a4 * Decimal('0.95')
        self.assertEqual(IN_TUNE, self.a4.in_tune(pitch_2))
