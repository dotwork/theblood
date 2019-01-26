from unittest import TestCase

from errors import InvalidScaleError
from models import BaseScale, LOCRIAN_SCALE_NAME, MAJOR_SCALE_NAME, MINOR_SCALE_NAME, IONIAN_SCALE_NAME, \
    DORIAL_SCALE_NAME, PHRYGIAN_SCALE_NAME, LYDIAN_SCALE_NAME, MIXOLYDIAN_SCALE_NAME, AEOLIAN_SCALE_NAME, W, H, Scale, \
    C, D, E, F, G, A, B, MajorScale


#######################################################################
class TestBaseScale(TestCase):

    ####################################################################
    def test_name(self):
        self.assertEqual(MAJOR_SCALE_NAME, BaseScale('Major').name)
        self.assertEqual(MAJOR_SCALE_NAME, BaseScale('major').name)
        self.assertEqual(MAJOR_SCALE_NAME, BaseScale('MAJOR').name)

        self.assertEqual(LOCRIAN_SCALE_NAME, BaseScale('locrian').name)

    ####################################################################
    def test_intervals__standard_scales__by_name(self):
        self.assertEqual((W, W, H, W, W, W, H), BaseScale('Major').intervals)
        self.assertEqual((W, H, W, W, H, W, W), BaseScale('Minor').intervals)

        self.assertEqual((W, W, H, W, W, W, H), BaseScale('ionian').intervals)
        self.assertEqual((W, H, W, W, W, H, W), BaseScale('dorian').intervals)
        self.assertEqual((H, W, W, W, H, W, W), BaseScale('phrygian').intervals)
        self.assertEqual((W, W, W, H, W, W, H), BaseScale('lydian').intervals)
        self.assertEqual((W, W, H, W, W, H, W), BaseScale('mixolydian').intervals)
        self.assertEqual((W, H, W, W, H, W, W), BaseScale('aeolian').intervals)
        self.assertEqual((H, W, W, H, W, W, W), BaseScale('locrian').intervals)

    ####################################################################
    def test_intervals__standard_scales__by_intervals(self):
        self.assertEqual(MAJOR_SCALE_NAME, BaseScale(intervals=(W, W, H, W, W, W, H)).name)
        self.assertEqual(MINOR_SCALE_NAME, BaseScale(intervals=(W, H, W, W, H, W, W)).name)

        # self.assertEqual(IONIAN_SCALE_NAME, BaseScale(intervals=(W, W, H, W, W, W, H)).name)
        self.assertEqual(DORIAL_SCALE_NAME, BaseScale(intervals=(W, H, W, W, W, H, W)).name)
        self.assertEqual(PHRYGIAN_SCALE_NAME, BaseScale(intervals=(H, W, W, W, H, W, W)).name)
        self.assertEqual(LYDIAN_SCALE_NAME, BaseScale(intervals=(W, W, W, H, W, W, H)).name)
        self.assertEqual(MIXOLYDIAN_SCALE_NAME, BaseScale(intervals=(W, W, H, W, W, H, W)).name)
        # self.assertEqual(AEOLIAN_SCALE_NAME, BaseScale(intervals=(W, H, W, W, H, W, W)).name)
        self.assertEqual(LOCRIAN_SCALE_NAME, BaseScale(intervals=(H, W, W, H, W, W, W)).name)

    ####################################################################
    def test_intervals__custom_scale(self):
        intervals = (W, W, W, H, H, H)
        scale = BaseScale('Foo', intervals)
        self.assertEqual('Foo', scale.name)
        self.assertEqual(intervals, scale.intervals)

    ####################################################################
    def test_intervals__custom_scale__invalid(self):
        with self.assertRaises(InvalidScaleError) as err:
            BaseScale('foo', tuple())
        self.assertEqual('Foo is not a recognized scale.', str(err.exception))

        with self.assertRaises(InvalidScaleError) as err:
            unrecognized_scale = (W, W, H)
            BaseScale(intervals=unrecognized_scale)
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
        self.assertEqual('C Major slice[0:2]', c_slice.name)
        self.assertEqual((C, D), c_slice.notes)

    ####################################################################
    def test_slicing__copy(self):
        c_major = Scale(C, MajorScale)
        c_major_copy = c_major[:]
        self.assertEqual('C Major', c_major_copy.name)
