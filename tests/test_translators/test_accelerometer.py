import datetime
from unittest import TestCase, mock

from composer.compose import ComposedNote
from composer import midi
from composer.translators import accelerometer
from composer.translators.accelerometer import NOTE_VALUE_UNIT, NOTE_VALUE_REMAINDER, MockAccelerometer, \
    AccelerometerStrategy
from the_blood.models import *


class TestAccelerometer(TestCase):

    def setUp(self):
        bpm = 120
        key = Key('C')
        self.acc = accelerometer.MockAccelerometer(AccelerometerStrategy, key, bpm)

    def test_get_pitch(self):
        # Middle F Pitch
        for x in range(accelerometer.PITCH_UNIT):
            pitch = self.acc.strategy.get_pitch(x)
            self.assertEqual(Decimal('349.23'), pitch, msg=f'x: {x}')
        for x in range(accelerometer.PITCH_UNIT):
            pitch = self.acc.strategy.get_pitch(x * -1)
            self.assertEqual(Decimal('349.23'), pitch)

        # 1 Note above Middle F
        fsharp4 = Pitch('369.99')
        for x in range(accelerometer.PITCH_UNIT, accelerometer.PITCH_UNIT * 2):
            pitch = self.acc.strategy.get_pitch(x)
            self.assertEqual(fsharp4, pitch, msg=f'x: {x}')

        # 1 Note below Middle E
        e4 = Pitch('329.63')
        for x in range(accelerometer.PITCH_UNIT, accelerometer.PITCH_UNIT * 2):
            pitch = self.acc.strategy.get_pitch(x * -1)
            self.assertEqual(e4, pitch, msg=f'x: {x}')

        # Highest Pitch
        c_8_pitch = Pitch('4186.01')
        self.assertEqual(44, len(self.acc.strategy.middle_f_and_higher))
        for x in range(accelerometer.PITCH_UNIT * 43, accelerometer.PITCH_UNIT * 44):
            pitch = self.acc.strategy.get_pitch(x)
            self.assertEqual(c_8_pitch, pitch, msg=f'x: {x}')

        # Lowest Pitch
        a0_pitch = Pitch('27.50')
        self.assertEqual(44, len(self.acc.strategy.pitches_lower_than_middle_f))
        for x in range(accelerometer.PITCH_UNIT * 43, accelerometer.PITCH_UNIT * 44):
            pitch = self.acc.strategy.get_pitch(x * -1)
            self.assertEqual(a0_pitch, pitch, msg=f'x: {x}')

    def test_get_velocity(self):
        zero_to_258 = accelerometer.VELOCITY_UNIT
        for y in range(zero_to_258):
            velocity = self.acc.strategy.get_velocity(y)
            self.assertEqual(127, velocity)

        for y in range(accelerometer.VELOCITY_UNIT):
            velocity = self.acc.strategy.get_velocity(y * -1)
            self.assertEqual(127, velocity)

        for y in range(accelerometer.VELOCITY_UNIT, accelerometer.VELOCITY_UNIT * 2):
            velocity = self.acc.strategy.get_velocity(y)
            self.assertEqual(126, velocity)
        for y in range(accelerometer.VELOCITY_UNIT, accelerometer.VELOCITY_UNIT * 2):
            velocity = self.acc.strategy.get_velocity(y * -1)
            self.assertEqual(126, velocity)

        for y in range(accelerometer.VELOCITY_UNIT * 2, accelerometer.VELOCITY_UNIT * 3):
            velocity = self.acc.strategy.get_velocity(y)
            self.assertEqual(125, velocity)
        for y in range(accelerometer.VELOCITY_UNIT * 2, accelerometer.VELOCITY_UNIT * 3):
            velocity = self.acc.strategy.get_velocity(y * -1)
            self.assertEqual(125, velocity)

        for y in range(accelerometer.VELOCITY_UNIT * 126, accelerometer.VELOCITY_UNIT * 127):
            velocity = self.acc.strategy.get_velocity(y)
            self.assertEqual(0, velocity, msg=f'y value: {y}, velocity: {velocity}')
        for y in range(accelerometer.VELOCITY_UNIT * 126, accelerometer.VELOCITY_UNIT * 127):
            velocity = self.acc.strategy.get_velocity(y * -1)
            self.assertEqual(0, velocity, msg=f'y value: {y}, velocity: {velocity}')

        max_accelerometer_value = (accelerometer.VELOCITY_UNIT * 127 + 1)
        self.assertEqual(max_accelerometer_value, accelerometer.ACC_MAX)
        self.assertEqual(0, self.acc.strategy.get_velocity(max_accelerometer_value))

        min_accelerometer_value = (accelerometer.VELOCITY_UNIT * 127 + 2) * -1
        self.assertEqual(min_accelerometer_value, accelerometer.ACC_MIN)
        self.assertEqual(0, self.acc.strategy.get_velocity(min_accelerometer_value))

        one_over_max = (accelerometer.VELOCITY_UNIT * 127 + 2)
        self.assertEqual(accelerometer.ACC_MAX + 1, one_over_max)
        with self.assertRaises(AssertionError):
            self.acc.strategy.get_velocity(one_over_max)

        one_less_than_max = (accelerometer.VELOCITY_UNIT * 127 + 3) * -1
        self.assertEqual(accelerometer.ACC_MIN - 1, one_less_than_max)
        with self.assertRaises(AssertionError):
            self.acc.strategy.get_velocity(one_less_than_max)

    def test_get_note_value(self):
        for z in range(NOTE_VALUE_UNIT):
            self.assertEqual(ThirtySecondNote, self.acc.strategy.get_note_value(z))

        for z in range(NOTE_VALUE_UNIT, NOTE_VALUE_UNIT*2):
            self.assertEqual(SixteenthNote, self.acc.strategy.get_note_value(z))

        for z in range(NOTE_VALUE_UNIT*2, NOTE_VALUE_UNIT*3):
            self.assertEqual(EighthNote, self.acc.strategy.get_note_value(z))

        for z in range(NOTE_VALUE_UNIT*3, NOTE_VALUE_UNIT*4):
            self.assertEqual(QuarterNote, self.acc.strategy.get_note_value(z))

        for z in range(NOTE_VALUE_UNIT*4, NOTE_VALUE_UNIT*5):
            self.assertEqual(HalfNote, self.acc.strategy.get_note_value(z))

        for z in range(NOTE_VALUE_UNIT*5, NOTE_VALUE_UNIT*6 + NOTE_VALUE_REMAINDER):
            self.assertEqual(WholeNote, self.acc.strategy.get_note_value(z))

    def test_translate(self):
        expected_midi_number = 65  # F4
        expected_velocity = midi.MAX_VELOCITY
        F4 = ComposedNote('F', octave=4)

        x, y, z = self.acc.receive()
        self.assertEqual(True, x == y == z == 0)

        midi_note = self.acc.translate()
        self.assertEqual(F4, midi_note.note)
        self.assertEqual(expected_midi_number, midi_note.number)
        self.assertEqual(0.0625, midi_note.duration)

        # Start Midi Signal
        start_command = midi_note.get_start_command()
        expected_start_command = [midi.NOTE_CHANNEL_1_ON, expected_midi_number, expected_velocity]
        self.assertEqual(expected_start_command, start_command)

        # End Midi Signal
        expected_end_command = [midi.NOTE_CHANNEL_1_OFF, expected_midi_number, expected_velocity]
        with mock.patch('composer.midi.MidiNote.now') as now:
            now.return_value = midi_note.start
            end_command = midi_note.get_end_command()
            self.assertEqual(None, end_command)

            now.return_value = midi_note.start + datetime.timedelta(seconds=midi_note.duration)
            end_command = midi_note.get_end_command()
            self.assertEqual(expected_end_command, end_command)

    def test_run(self):
        start = datetime.datetime.now()
        ten_seconds = start + datetime.timedelta(seconds=60)

        midi_note = None
        while datetime.datetime.now() < ten_seconds:
            self.acc.receive()
            if not midi_note:
                midi_note = self.acc.translate()
                start_command = midi_note.get_start_command()
                print(start_command)
            else:
                end_command = midi_note.get_end_command()
                if end_command:
                    print(end_command)
                    midi_note = None
