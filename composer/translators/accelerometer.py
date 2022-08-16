import math

from composer import midi
from composer.compose import ComposedNote
from composer.midi import MAX_VELOCITY
from composer.translators._translator import Translator, Strategy
from the_blood.models import *

ACC_MIN = -32768
ACC_MAX = 32767

VELOCITY_UNIT = int(ACC_MAX / MAX_VELOCITY)  # 258. The Velocity value increments 1 with every change of 258.
PITCH_UNIT = int(ACC_MAX / (len(PianoRange) / 2))
NOTE_VALUE_UNIT = int(ACC_MAX / len(NOTE_VALUES))
NOTE_VALUE_REMAINDER = int(ACC_MAX % len(NOTE_VALUES))


class _AccelerometerStrategy(Strategy):
    def __init__(self):
        middle_e = 329.63
        self.pitches_lower_than_middle_f = [p for p in PianoRange if p <= middle_e]
        self.middle_f_and_higher = [p for p in PianoRange if p > middle_e]

    def get_pitch(self, x):
        if x > PITCH_UNIT * 43:
            return self.middle_f_and_higher[-1]
        elif x <= PITCH_UNIT * 43 * -1:
            return self.pitches_lower_than_middle_f[0]

        index = int(x / PITCH_UNIT)
        if index < 0:
            return self.pitches_lower_than_middle_f[index]
        else:
            return self.middle_f_and_higher[index]

    def get_velocity(self, y):
        """
        Strategy:
            At a "y" value of zero, velocity is at max (127)
            At negative minimum (-32768) and positive maximum (32767)
            velocity is at min (0)

        """
        assert ACC_MIN <= y <= ACC_MAX
        if y == 0:
            return midi.MAX_VELOCITY
        elif abs(y) >= ACC_MAX - VELOCITY_UNIT - 1:
            return 0

        # range unit = max acceleration number / max velocity
        # 258 = 32768/127
        raw = y / VELOCITY_UNIT
        int_y = int(raw)
        abs_y = abs(int_y)
        reverse_y = abs_y - 127
        velocity = abs(reverse_y)
        return velocity

    def get_note_value(self, z):
        assert ACC_MIN <= z <= ACC_MAX
        if z >= ACC_MAX - NOTE_VALUE_REMAINDER:
            return WholeNote

        # NOTE_VALUE_UNIT = 5461
        index = math.floor(abs(z/NOTE_VALUE_UNIT))
        sorted_by_factor = sorted(NOTE_VALUES.values(), key=lambda nv: nv.factor, reverse=True)

        note_value = sorted_by_factor[index]
        return note_value


AccelerometerStrategy = _AccelerometerStrategy()


class AccelerometerTranslator(Translator):

    def __init__(self, strategy, key, bpm):
        self.strategy = strategy
        self.key = key
        self.bpm = bpm
        self.x = None
        self.y = None
        self.z = None

    def receive(self, accelerometer):
        self.x, self.y, self.z = accelerometer.acceleration

    def translate(self):
        pitch = self.strategy.get_pitch(self.x)
        composed_note = None

        while pitch in PITCHES.values():
            try:
                composed_note = ComposedNote.from_pitch(pitch, self.key.notes)
                print('COMPOSED NOTE FROM {x}: {composed_note}'.format(x=self.x, composed_note=composed_note))
                break
            except UnavailableNoteError:
                pitch = pitch.increase(semitones=1)

        if composed_note is None:
            raise Exception('Failed to translate x value to a ComposedNote: x={x}'.format(x=self.x))

        velocity = self.strategy.get_velocity(self.y)
        note_value = self.strategy.get_note_value(self.z)
        duration = midi.get_duration_seconds(note_value, self.bpm)
        midi_note = midi.MidiNote(composed_note, velocity, duration=duration)
        return midi_note


class MockAccelerometer(AccelerometerTranslator):
    _x = []
    _y = []
    _z = []
    _range = [i for i in reversed(range(ACC_MAX))]

    def receive(self, accelerometer):
        if len(self._x) == 0:
            self._x = list(self._range)
        if len(self._y) == 0:
            self._y = list(self._range)
        if len(self._z) == 0:
            self._z = list(self._range)

        self.x, self.y, self.z = self._x.pop(), self._y.pop(), self._z.pop()
        return self.x, self.y, self.z
