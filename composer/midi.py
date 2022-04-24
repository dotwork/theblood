import collections

from the_blood.data import PITCHES

NOTE_CHANNEL_1_OFF = 0x80  # 128 in hex
NOTE_CHANNEL_1_ON = 0x90  # 144 in hex
# https://computermusicresource.com/MIDI.Commands.html
controls = None  # midi channels 176-191

MAX_VELOCITY = 127
STANDARD_BEAT_VALUE = 4  # quarter note


########################################################################
__MidiNote = collections.namedtuple('MidiNote', ['number', 'note'])


def MidiNote(note):
    name_with_octave = f'{note.name}{note.octave}'
    for midi_number, note_names in enumerate(PITCHES):
        if name_with_octave in note_names.split('/'):
            return __MidiNote(number=midi_number, note=note)
    raise Exception(f'Unrecognized note: {note}')


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

    rhythm_factor = STANDARD_BEAT_VALUE/note_value
    note_values_per_minute = bpm / rhythm_factor
    duration = 60 / note_values_per_minute
    return duration
