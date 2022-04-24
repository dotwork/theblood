import math
from decimal import Decimal

from composer import midi
from composer.midi import MAX_VELOCITY
from composer.translators._translator import Translator
from the_blood.data import PITCHES
from the_blood.models import Note, PianoRange

ACC_MIN = -32768
ACC_MAX = 32767

VELOCITY_UNIT = int(ACC_MAX / MAX_VELOCITY)  # 258. The Velocity value increments 1 with every change of 258.
PITCH_UNIT = int(ACC_MAX / (len(PianoRange)/2))  #


class AccelerometerTranslator(Translator):

    def __init__(self):
        self.x = None
        self.y = None
        self.z = None
        middle_e = Decimal('329.63')
        self.pitches_lower_than_middle_f = [p for p in PianoRange if p <= middle_e]
        self.middle_f_and_higher = [p for p in PianoRange if p > middle_e]

    def receive(self):
        raise NotImplemented()

    def get_note(self, x):
        assert ACC_MIN <= x <= ACC_MAX
        index = x % len(PianoRange)
        note = PianoRange.notes[index]
        return note

    def get_pitch(self, x):
        if x > PITCH_UNIT * 43:
            return self.middle_f_and_higher[-1]
        elif x <= PITCH_UNIT * 43 * -1:
            return self.pitches_lower_than_middle_f[0]

        index = int(x/PITCH_UNIT)
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
        raw = y/VELOCITY_UNIT
        int_y = int(raw)
        abs_y = abs(int_y)
        reverse_y = abs_y - 127
        velocity = abs(reverse_y)
        return velocity

    def get_note_value(self, z):
        assert ACC_MIN <= z <= ACC_MAX
        return 4


class MockAccelerometer(AccelerometerTranslator):
    _x = []
    _y = []
    _z = []
    _range = [i for i in reversed(range(ACC_MAX))]

    def receive(self):
        if len(self._x) == 0:
            self._x = list(self._range)
        if len(self._y) == 0:
            self._y = list(self._range)
        if len(self._z) == 0:
            self._z = list(self._range)

        return self._x.pop(), self._y.pop(), self._z.pop()
