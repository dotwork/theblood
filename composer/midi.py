import time

from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn

from composer import compose
from the_blood.models import *

NOTE_CHANNEL_1_OFF = 0x80  # 128 in hex
NOTE_CHANNEL_1_ON = 0x90  # 144 in hex
# https://computermusicresource.com/MIDI.Commands.html
controls = None  # midi channels 176-191

MAX_VELOCITY = 127
STANDARD_BEAT_VALUE = 4  # quarter note
A0_MIDI_NUMBER = 21  # LOWEST KEY ON A PIANO


def get_midi_number_from_note(composed_note):
    error = 'Expected a ComposedNote. Got {}.'.format(type(composed_note))
    assert isinstance(composed_note, compose.ComposedNote), error
    for midi_number, pitch in enumerate(PianoRange, start=A0_MIDI_NUMBER):
        if pitch == composed_note.pitch:
            return midi_number

    raise Exception('Could not find pitch for ComposedNote {}.'.format(composed_note))


class MidiNote:
    def __init__(self, composed_note, velocity, *, duration, start=None):
        self.note = composed_note
        self.velocity = int(velocity)
        self.duration = float(duration)
        self.start = start or self.now()
        self.end = self.start + self.duration
        self.number = get_midi_number_from_note(self.note)
        self.channel = 1

    def get_start_command(self):
        return NoteOn(self.number, self.velocity, channel=self.channel)

    @staticmethod
    def now():
        return time.time()

    def get_end_command(self, force=False):
        if force or self.now() >= self.end:
            return NoteOff(self.number, self.velocity, channel=self.channel)


def get_duration_seconds(note_value, bpm):
    # if note value is a quarter note, and bpm is 120
    # and a "beat" equals a quarter note
    # duration for each quarter note in seconds would be

    # rhythm_factor = 4 (quarter note as standard "beat" in bpm) / 4 (quarter note)
    # note_values_per_minute = 120 (bpm) / 120 quarter notes
    # duration = 60 seconds / 120 quarter notes
    # duration = 0.5 seconds per quarter note

    # for an eighth note, with a standard "beat" still being a quarter note
    # 120 (bpm) / (4 (quarter note as standard "beat" in bpm) / 8 (eighth note))
    # = 240 quarter notes per minute
    # so an eighth note is
    # 60 seconds / 240 eighth notes = 0.25 seconds per eighth note

    # for a thirty-second note, with a standard "beat" still being a quarter note
    # 120 (bpm) / (4 (quarter note as standard "beat" in bpm) / 32 (thirty-second note))
    # = 960 thirty-second notes per minute
    # so a thirty-second note is
    # 60 seconds / 960 eighth notes = 0.0625 seconds per eighth note

    rhythm_factor = STANDARD_BEAT_VALUE/note_value
    note_values_per_minute = bpm / rhythm_factor
    duration = 60 / note_values_per_minute
    return duration
