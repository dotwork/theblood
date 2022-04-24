from decimal import Decimal
from unittest import TestCase

from composer.translators import accelerometer
from the_blood.models import Pitch


class TestAccelerometer(TestCase):

    def setUp(self):
        self.acc = accelerometer.MockAccelerometer()

    def test_get_pitch(self):
        # Middle F Pitch
        for x in range(accelerometer.PITCH_UNIT):
            pitch = self.acc.get_pitch(x)
            self.assertEqual(Decimal('349.23'), pitch, msg=f'x: {x}')
        for x in range(accelerometer.PITCH_UNIT):
            pitch = self.acc.get_pitch(x * -1)
            self.assertEqual(Decimal('349.23'), pitch)

        # 1 Note above Middle F
        fsharp4 = Pitch('369.99')
        for x in range(accelerometer.PITCH_UNIT, accelerometer.PITCH_UNIT * 2):
            pitch = self.acc.get_pitch(x)
            self.assertEqual(fsharp4, pitch, msg=f'x: {x}')

        # 1 Note below Middle E
        e4 = Pitch('329.63')
        for x in range(accelerometer.PITCH_UNIT, accelerometer.PITCH_UNIT * 2):
            pitch = self.acc.get_pitch(x * -1)
            self.assertEqual(e4, pitch, msg=f'x: {x}')

        # Highest Pitch
        c_8_pitch = Pitch('4186.01')
        self.assertEqual(44, len(self.acc.middle_f_and_higher))
        for x in range(accelerometer.PITCH_UNIT * 43, accelerometer.PITCH_UNIT * 44):
            pitch = self.acc.get_pitch(x)
            self.assertEqual(c_8_pitch, pitch, msg=f'x: {x}')

        # Lowest Pitch
        a0_pitch = Pitch('27.50')
        self.assertEqual(44, len(self.acc.pitches_lower_than_middle_f))
        for x in range(accelerometer.PITCH_UNIT * 43, accelerometer.PITCH_UNIT * 44):
            pitch = self.acc.get_pitch(x * -1)
            self.assertEqual(a0_pitch, pitch, msg=f'x: {x}')

    def test_get_velocity(self):
        zero_to_258 = accelerometer.VELOCITY_UNIT
        for y in range(zero_to_258):
            velocity = self.acc.get_velocity(y)
            self.assertEqual(127, velocity)

        for y in range(accelerometer.VELOCITY_UNIT):
            velocity = self.acc.get_velocity(y * -1)
            self.assertEqual(127, velocity)

        for y in range(accelerometer.VELOCITY_UNIT, accelerometer.VELOCITY_UNIT * 2):
            velocity = self.acc.get_velocity(y)
            self.assertEqual(126, velocity)
        for y in range(accelerometer.VELOCITY_UNIT, accelerometer.VELOCITY_UNIT * 2):
            velocity = self.acc.get_velocity(y * -1)
            self.assertEqual(126, velocity)

        for y in range(accelerometer.VELOCITY_UNIT * 2, accelerometer.VELOCITY_UNIT * 3):
            velocity = self.acc.get_velocity(y)
            self.assertEqual(125, velocity)
        for y in range(accelerometer.VELOCITY_UNIT * 2, accelerometer.VELOCITY_UNIT * 3):
            velocity = self.acc.get_velocity(y * -1)
            self.assertEqual(125, velocity)

        for y in range(accelerometer.VELOCITY_UNIT * 126, accelerometer.VELOCITY_UNIT * 127):
            velocity = self.acc.get_velocity(y)
            self.assertEqual(0, velocity, msg=f'y value: {y}, velocity: {velocity}')
        for y in range(accelerometer.VELOCITY_UNIT * 126, accelerometer.VELOCITY_UNIT * 127):
            velocity = self.acc.get_velocity(y * -1)
            self.assertEqual(0, velocity, msg=f'y value: {y}, velocity: {velocity}')

        max_accelerometer_value = (accelerometer.VELOCITY_UNIT * 127 + 1)
        self.assertEqual(max_accelerometer_value, accelerometer.ACC_MAX)
        self.assertEqual(0, self.acc.get_velocity(max_accelerometer_value))

        min_accelerometer_value = (accelerometer.VELOCITY_UNIT * 127 + 2) * -1
        self.assertEqual(min_accelerometer_value, accelerometer.ACC_MIN)
        self.assertEqual(0, self.acc.get_velocity(min_accelerometer_value))

        one_over_max = (accelerometer.VELOCITY_UNIT * 127 + 2)
        self.assertEqual(accelerometer.ACC_MAX + 1, one_over_max)
        with self.assertRaises(AssertionError):
            self.acc.get_velocity(one_over_max)

        one_less_than_max = (accelerometer.VELOCITY_UNIT * 127 + 3) * -1
        self.assertEqual(accelerometer.ACC_MIN - 1, one_less_than_max)
        with self.assertRaises(AssertionError):
            self.acc.get_velocity(one_less_than_max)

    def test_get_note_value(self):
        self.fail()
