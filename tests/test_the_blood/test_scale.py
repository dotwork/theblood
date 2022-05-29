from unittest import TestCase

from the_blood.models import *


#######################################################################
class TestBaseScale(TestCase):

    ####################################################################
    def test_name(self):
        self.assertEqual(MAJOR_SCALE_NAME, ScalePattern('Major').name)
        self.assertEqual(MAJOR_SCALE_NAME, ScalePattern('major').name)
        self.assertEqual(MAJOR_SCALE_NAME, ScalePattern('MAJOR').name)

        self.assertEqual(IONIAN_SCALE_NAME, ScalePattern('Ionian').name)
        self.assertEqual(DORIAN_SCALE_NAME, ScalePattern('DORIAN').name)
        self.assertEqual(PHRYGIAN_SCALE_NAME, ScalePattern('Phrygian').name)
        self.assertEqual(LYDIAN_SCALE_NAME, ScalePattern('LYDIAN').name)
        self.assertEqual(MIXOLYDIAN_SCALE_NAME, ScalePattern('MixoLydian').name)
        self.assertEqual(AEOLIAN_SCALE_NAME, ScalePattern('Aeolian').name)
        self.assertEqual(LOCRIAN_SCALE_NAME, ScalePattern('locrian').name)

    ####################################################################
    def test_intervals__standard_scales__by_name(self):
        self.assertEqual((W, W, H, W, W, W, H), ScalePattern('Major').intervals)
        self.assertEqual((W, H, W, W, H, W, W), ScalePattern('Minor').intervals)

        self.assertEqual((W, W, H, W, W, W, H), ScalePattern('ionian').intervals)
        self.assertEqual((W, H, W, W, W, H, W), ScalePattern('dorian').intervals)
        self.assertEqual((H, W, W, W, H, W, W), ScalePattern('phrygian').intervals)
        self.assertEqual((W, W, W, H, W, W, H), ScalePattern('lydian').intervals)
        self.assertEqual((W, W, H, W, W, H, W), ScalePattern('mixolydian').intervals)
        self.assertEqual((W, H, W, W, H, W, W), ScalePattern('aeolian').intervals)
        self.assertEqual((H, W, W, H, W, W, W), ScalePattern('locrian').intervals)

    ####################################################################
    def test_intervals__standard_scales__by_intervals(self):
        self.assertEqual(IONIAN_SCALE_NAME, ScalePattern(intervals=(W, W, H, W, W, W, H)).name)
        self.assertEqual(DORIAN_SCALE_NAME, ScalePattern(intervals=(W, H, W, W, W, H, W)).name)
        self.assertEqual(PHRYGIAN_SCALE_NAME, ScalePattern(intervals=(H, W, W, W, H, W, W)).name)
        self.assertEqual(LYDIAN_SCALE_NAME, ScalePattern(intervals=(W, W, W, H, W, W, H)).name)
        self.assertEqual(MIXOLYDIAN_SCALE_NAME, ScalePattern(intervals=(W, W, H, W, W, H, W)).name)
        self.assertEqual(AEOLIAN_SCALE_NAME, ScalePattern(intervals=(W, H, W, W, H, W, W)).name)
        self.assertEqual(LOCRIAN_SCALE_NAME, ScalePattern(intervals=(H, W, W, H, W, W, W)).name)

    ####################################################################
    def test_intervals__custom_scale(self):
        intervals = (W, W, W, H, H, H)
        scale = ScalePattern('Foo', intervals)
        self.assertEqual('Foo', scale.name)
        self.assertEqual(intervals, scale.intervals)

    ####################################################################
    def test_intervals__custom_scale__invalid(self):
        with self.assertRaises(InvalidScaleError) as err:
            ScalePattern('Custom Scale With No Intervals', tuple())
        self.assertEqual('Custom Scale With No Intervals is not a recognized scale.', str(err.exception))

        with self.assertRaises(InvalidScaleError) as err:
            scale_with_no_name = (W, W, H)
            ScalePattern(intervals=scale_with_no_name)
        self.assertEqual(f'({W}, {W}, {H}) is not a recognized scale.', str(err.exception))


#######################################################################
class TestScale(TestCase):

    ####################################################################
    def test_indexing(self):
        c_major = Scale(C, MajorScale)
        self.assertEqual(C, c_major[0])
        self.assertEqual(D, c_major[1])
        self.assertEqual(E, c_major[2])
        self.assertEqual(F, c_major[3])
        self.assertEqual(G, c_major[4])
        self.assertEqual(A, c_major[5])
        self.assertEqual(B, c_major[6])
        self.assertEqual(B, c_major[-1])

    ####################################################################
    def test_slicing(self):
        c_major = Scale(C, MajorScale)
        c_slice = c_major[0:2]
        self.assertEqual('C Major Slice[0:2]', c_slice.name)
        self.assertEqual((C, D), c_slice.notes)

    ####################################################################
    def test_slicing__copy(self):
        c_major = Scale(C, MajorScale)
        c_major_copy = c_major[:]
        self.assertEqual('C Major', c_major_copy.name)
