import collections
from decimal import Decimal

from data import SHARP, FLAT, IN_TUNE, NATURAL_NOTES, SHARPS_AND_FLATS, PITCHES, MINOR, WHOLE_STEP, HALF_STEP, \
    QUALITIES, W, H, MAJOR_SCALE_NAME, MINOR_SCALE_NAME, IONIAN_SCALE_NAME, DORIAL_SCALE_NAME, PHRYGIAN_SCALE_NAME, \
    LYDIAN_SCALE_NAME, MIXOLYDIAN_SCALE_NAME, AEOLIAN_SCALE_NAME, LOCRIAN_SCALE_NAME
from errors import InvalidNoteError, InvalidKeyError, InvalidQualityError, InvalidScaleError


#######################################################################
class Quality(str):

    ###################################################################
    def __new__(cls, quality):
        cleaned_q = cls.clean(quality)
        return super().__new__(Quality, cleaned_q)

    ###################################################################
    @classmethod
    def clean(cls, quality):
        cleaned = quality.lower().strip().replace(' ', '')
        try:
            return QUALITIES[cleaned]
        except KeyError:
            raise InvalidQualityError(f'"{quality}" is not a valid quality.')


#######################################################################
class _PitchMap(collections.OrderedDict):
    """
    This dictionary maps hz frequency values (pitches)
    as Decimals to their corresponding notes and octaves.
    It also maps the other way as well. Each note/octave
    will correspond to the same Decimal hz value.

    Here are a couple entries each way:
        {
            Decimal('16.35'): ['B#0', 'C0'],
            Decimal('17.32'): ['C#0/Db0'],
            ...
            'B#0': Decimal('16.35'),
            'C0': Decimal('16.35'),
            'C#0': Decimal('17.32'),
            ...
        }
    """

    ####################################################################
    def __init__(self):
        data = collections.OrderedDict()
        note_to_hz_map = collections.OrderedDict()

        for _notes, _pitch in PITCHES.items():
            _notes = _notes.split('/')
            data[_pitch] = _notes

            for note in _notes:
                note_to_hz_map[self._make_key(note)] = _pitch

        super(_PitchMap, self).__init__(data)
        self.note_to_hz_map = note_to_hz_map

    ####################################################################
    @staticmethod
    def _make_key(note_with_octave):
        name = note_with_octave[0]  # first character
        octave = note_with_octave[-1]  # last character
        quality = Quality(note_with_octave[1:-1])  # any/every thing in the middle
        return f'{name}{quality}{octave}'

    ####################################################################
    def __getitem__(self, item):
        try:
            return super(_PitchMap, self).__getitem__(item)
        except KeyError:
            return self.note_to_hz_map[self._make_key(item)]


PitchMap = _PitchMap()


########################################################################
class Pitch(Decimal):

    __interval_increase = Decimal('1.0595')

    ####################################################################
    @property
    def notes(self):
        note_names = PitchMap[Decimal(self)]
        notes_list = []
        for name in note_names:
            note = name[:-1]
            octave = name[-1]
            notes_list.append(Note(note, octave=octave))
        return notes_list

    ####################################################################
    @property
    def next_pitch(self):
        next_hz = self * self.__interval_increase
        return Pitch(next_hz)

    ####################################################################
    def in_tune(self, pitch_2):
        diff = pitch_2 / self
        if diff > Decimal('1.05'):
            return SHARP
        elif diff < Decimal('0.95'):
            return FLAT
        return IN_TUNE

    ####################################################################
    def increase(self, semitones):
        increased = 0

        for hz in PitchMap:
            if hz > self:
                increased += 1
            if increased == semitones:
                break

        return Pitch(hz)


########################################################################
def get_note_and_quality_from_music_element(element_name):
    try:
        note = Note(element_name[0])
    except IndexError:
        raise InvalidNoteError(f'"{element_name}" does not contain a valid root note.')
    remainder = element_name[1:]

    if remainder:
        for char in remainder:
            try:
                note = Note(note.name + char)
            except InvalidNoteError:
                break

    quality = element_name[len(note.name):] or ''
    quality = Quality(quality)

    return note, quality


########################################################################
class Note:

    ####################################################################
    def __init__(self, note, octave=4):
        if isinstance(note, Note):
            self.name = note.name
            self.quality = note.quality
            self.octave = octave or note.octave
        else:
            name = note[:1].upper().strip()
            assert name in NATURAL_NOTES, f'"{name}" is not a valid note.'
            quality = note[1:].replace("-", "").replace("_", "").lower().strip()
            if quality:
                try:
                    quality = SHARPS_AND_FLATS[quality]
                except KeyError:
                    raise InvalidNoteError(f'"{note}" is not a valid note.')

            self.name = f'{name}{quality}'
            self.quality = quality
            self.octave = octave

        self.octave = int(octave)
        pitch_name = f'{self.name}{self.octave}'
        self.fundamental = Pitch(PitchMap[pitch_name])

    ####################################################################
    def __str__(self):
        """
        How the note object is formatted into a string. For example:
            a_sharp = Note('A#')
            print(f"This note object is printed as {a_sharp}."
        will print:
            This note object is printed as A#.
        """
        return self.name

    ####################################################################
    def __repr__(self):
        """
        How a note object is represented in Python, which should
        match how you create an instance of it. For example,
        in the python terminal, creating an instance will print
        the repr for it to the terminal screen:
            >>> Note('A')
            Note('A')
        """
        return f'Note("{self.name}")'

    ####################################################################
    def __eq__(self, other):
        """
        This is the function that gets called when one
        Note is compared to another, for example:
            >>> Note('A') == Note('A')
            True
            >>> Note('A') == Note('B')
            False
        """
        return self.name == Note(other).name

    ####################################################################
    @property
    def is_standard_flat(self):
        return self.is_flat and self.name not in (C_flat.name, F_flat.name)

    ####################################################################
    @property
    def is_standard_sharp(self):
        return self.is_sharp and self.name not in (B_sharp.name, E_sharp.name)

    ####################################################################
    @property
    def is_natural(self):
        has_no_quality = not bool(self.quality)
        return has_no_quality

    ####################################################################
    @property
    def is_sharp(self):
        return self.name.endswith('♯') and not self.is_double_sharp

    ####################################################################
    @property
    def is_double_sharp(self):
        return self.name.endswith('♯♯')

    ####################################################################
    @property
    def is_flat(self):
        return self.name.endswith('♭') and not self.is_double_flat

    ####################################################################
    @property
    def is_double_flat(self):
        return self.name.endswith('♭♭')

    ####################################################################
    @property
    def natural_name(self):
        return self.name[0]

    ####################################################################
    @property
    def next_natural_note(self):
        if self.natural_name == 'G':
            return Note('A')

        current_index = NATURAL_NOTES.index(self.natural_name)
        next_note_index = current_index + 1
        next_note_name = NATURAL_NOTES[next_note_index]
        return Note(next_note_name)

    ####################################################################
    @property
    def previous_natural_note(self):
        if self.natural_name == 'A':
            return Note('G')

        current_index = NATURAL_NOTES.index(self.natural_name)
        previous_note_index = current_index - 1
        previous_note_name = NATURAL_NOTES[previous_note_index]
        return Note(previous_note_name)

    ####################################################################
    def harmonically_equivalent_to(self, other):
        return self.fundamental == other.fundamental

    ####################################################################
    @classmethod
    def get_note_with_letter(cls, name, notes):
        for note in notes:
            if name.startswith(note.natural_name):
                return note
        else:
            raise InvalidKeyError(f'Did not find a {name} note in {notes}.')


A_flat = Note('A♭')
G_double_sharp = Note('G♯♯')
A = Note('A')
B_double_flat = Note('B♭♭')
A_sharp = Note('A♯')
B_flat = Note('B♭')
B = Note('B')
B_sharp = Note('B♯')
C_flat = Note('C♭')
C = Note('C')
C_sharp = Note('C♯')
D_double_flat = Note('D♭♭')
D_flat = Note('D♭')
D = Note('D')
D_sharp = Note('D♯')
E_flat = Note('E♭')
E = Note('E')
E_sharp = Note('E♯')
F_flat = Note('F♭')
F = Note('F')
F_sharp = Note('F♯')
G_flat = Note('G♭')
G = Note('G')
G_sharp = Note('G♯')


MAJOR_INTERVALS = (W, W, H, W, W, W, H)
MINOR_INTERVALS = (W, H, W, W, H, W, W)

# https://music.stackexchange.com/questions/73110/what-are-the-interval-patterns-for-the-modes
IONIAN_INTERVALS = (W, W, H, W, W, W, H)
DORIAL_INTERVALS = (W, H, W, W, W, H, W)
PHRYGIAN_INTERVALS = (H, W, W, W, H, W, W)
LYDIAN_INTERVALS = (W, W, W, H, W, W, H)
MIXOLYDIAN_INTERVALS = (W, W, H, W, W, H, W)
AEOLIAN_INTERVALS = (W, H, W, W, H, W, W)
LOCRIAN_INTERVALS = (H, W, W, H, W, W, W)

SCALE_TO_INTERVALS_MAP = {
    MAJOR_SCALE_NAME: MAJOR_INTERVALS,
    MINOR_SCALE_NAME: MINOR_INTERVALS,
    IONIAN_SCALE_NAME: IONIAN_INTERVALS,
    DORIAL_SCALE_NAME: DORIAL_INTERVALS,
    PHRYGIAN_SCALE_NAME: PHRYGIAN_INTERVALS,
    LYDIAN_SCALE_NAME: LYDIAN_INTERVALS,
    MIXOLYDIAN_SCALE_NAME: MIXOLYDIAN_INTERVALS,
    AEOLIAN_SCALE_NAME: AEOLIAN_INTERVALS,
    LOCRIAN_SCALE_NAME: LOCRIAN_INTERVALS,
}

KEY_INTERVALS_TO_NAME_MAP = {
    MAJOR_INTERVALS: MAJOR_SCALE_NAME,
    MINOR_INTERVALS: MINOR_SCALE_NAME,
}

MODAL_INTERVALS_TO_NAME_MAP = {
    IONIAN_INTERVALS: IONIAN_SCALE_NAME,
    DORIAL_INTERVALS: DORIAL_SCALE_NAME,
    PHRYGIAN_INTERVALS: PHRYGIAN_SCALE_NAME,
    LYDIAN_INTERVALS: LYDIAN_SCALE_NAME,
    MIXOLYDIAN_INTERVALS: MIXOLYDIAN_SCALE_NAME,
    AEOLIAN_INTERVALS: AEOLIAN_SCALE_NAME,
    LOCRIAN_INTERVALS: LOCRIAN_SCALE_NAME,
}


finger_positions = ('tonic', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
                    'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth', 'thirteenth',
                    'fourteenth', 'fifteenth', 'sixteenth')


#######################################################################
class BaseScale:

    ####################################################################
    def __init__(self, name='', intervals=None):
        name, intervals = self.clean_name_and_intervals(name, intervals)
        num_intervals = len(intervals)

        self.name = name
        self.intervals = tuple(intervals or [])
        self.tonic = intervals[0]

        self.second = intervals[1] if num_intervals > 1 else None
        self.third = intervals[2] if num_intervals > 2 else None
        self.fourth = intervals[3] if num_intervals > 3 else None
        self.fifth = intervals[4] if num_intervals > 4 else None
        self.sixth = intervals[5] if num_intervals > 5 else None
        self.seventh = intervals[6] if num_intervals > 6 else None
        self.eighth = intervals[7] if num_intervals > 7 else None
        self.ninth = intervals[8] if num_intervals > 8 else None
        self.tenth = intervals[9] if num_intervals > 9 else None
        self.eleventh = intervals[10] if num_intervals > 10 else None
        self.twelfth = intervals[11] if num_intervals > 11 else None
        self.thirteenth = intervals[12] if num_intervals > 12 else None
        self.fourteenth = intervals[13] if num_intervals > 13 else None
        self.fifteenth = intervals[14] if num_intervals > 14 else None
        self.sixteenth = intervals[15] if num_intervals > 15 else None

    ####################################################################
    @classmethod
    def clean_name_and_intervals(cls, name, intervals):
        assert name or intervals, 'A name or iterable of intervals must be provided.'

        name = name.strip().capitalize() if name else ''
        if intervals:
            intervals = tuple(intervals)

        adding_new_scale = bool(name and intervals)
        if adding_new_scale:
            err = "A scale with this {} already exists."
            assert name not in SCALE_TO_INTERVALS_MAP, err.format('name')
            assert intervals not in SCALE_TO_INTERVALS_MAP, err.format('set of intervals')
        else:
            # fetching a known scale by name or intervals
            try:
                intervals = SCALE_TO_INTERVALS_MAP[name]
            except KeyError:
                try:
                    name = KEY_INTERVALS_TO_NAME_MAP[intervals]
                except KeyError:
                    try:
                        name = MODAL_INTERVALS_TO_NAME_MAP[intervals]
                    except KeyError:
                        argument = name or intervals
                        raise InvalidScaleError(f'{argument} is not a recognized scale.')

        return name, intervals

    ####################################################################
    def __iter__(self):
        for interval in self.intervals:
            yield interval


#######################################################################
class Scale(BaseScale):

    ####################################################################
    def __init__(self, root_note, name='', intervals=None):
        super().__init__(name, intervals)
        self.root_note = Note(root_note)
        self.notes = tuple(self._generate_notes())

    ####################################################################
    def __eq__(self, other):
        return tuple(self) == tuple(other)

    ####################################################################
    def _generate_notes(self):
        # We already know the root note, so create a list starting with that
        notes = [self.root_note]

        # Get the base pitch to start with from our root note
        pitch = self.root_note.fundamental

        # A key has a set of whole and half steps that determine what notes
        # fall into the key, starting from the root note. Iterate through
        # each step to add each successive note to the key.
        for step in self.intervals[:-1]:  # iterating up to the last one with [:-1] because since we're
            # just generating notes, we don't need the last step because it will lead us to C,
            # which we already have.

            # Increase it to the pitch we want for the next note.
            semitones = step * 2
            pitch = pitch.increase(semitones)

            # Get the list of harmonically equivalent notes for the increased pitch
            equivalent_notes = pitch.notes

            # Find which of the equivalent notes is named with the next letter for our key
            # For example, if the last note was some kind of A (A, A#, or Ab)
            # the next note must be a B (B, B#, or Bb)
            next_note_natural_name = notes[-1].next_natural_note.name
            note = Note.get_note_with_letter(next_note_natural_name, equivalent_notes)

            # And add that note to the list
            notes.append(note)

        return notes

    ####################################################################
    def __getitem__(self, item):
        try:
            i = int(item)
            return self.notes[i]
        except IndexError:
            raise Exception(f'This scale does not have {i + 1} notes: {self.notes}')
        except ValueError:
            return getattr(self, item)

    ####################################################################
    def __iter__(self):
        for note in self.notes:
            yield note


########################################################################
class Key:

    ####################################################################
    def __init__(self, name):
        root, quality = get_note_and_quality_from_music_element(name.strip())

        self.root_note = root
        self.quality = quality
        self.name = f'{self.root_note.name}{self.quality}'
        self.intervals = MINOR_INTERVALS if quality == MINOR else MAJOR_INTERVALS
        self.scale = Scale(self.root_note, intervals=self.intervals)
        self.note_names = tuple(n.name for n in self.scale.notes)

    ####################################################################
    def __str__(self):
        return self.name

    ####################################################################
    def __iter__(self):
        for note in self.scale:
            yield note


########################################################################
class Chord:

    ####################################################################
    def __init__(self, name):
        root, quality = get_note_and_quality_from_music_element(name.strip())
        self.root_note = root
        self.quality = quality
        self.name = f"{root}{quality}"
        self.intervals = intervals
        self.notes = self._generate_notes()

    def _generate_notes(self):
        # We already know the root note, so create a list starting with that
        notes = [self.root_note]

        # Get the base pitch to start with from our root note
        pitch = self.root_note.fundamental

        # A key has a set of whole and half steps that determine what notes
        # fall into the key, starting from the root note. Iterate through
        # each step to add each successive note to the key.
        for intervals in self.intervals:
            # All 12 notes are 1 semitone, or half-step, apart from the note below and above.
            # Since there are 2 semitones in a step, multiply the current step in this loop by 2
            # to get the total amount of semitones we need to increase for out next note.
            semitones = step * 2

            # Increase it to the pitch we want for the next note.
            pitch = pitch.increase(semitones)

            # Get the list of harmonically equivalent notes for the increased pitch
            equivalent_notes = pitch.notes

            # Find which of the equivalent notes is named with the next letter for our key
            # For example, if the last note was some kind of A (A, A#, or Ab)
            # the next note must be a B (B, B#, or Bb)
            next_note_natural_name = notes[-1].next_natural_note.name
            note = Note.get_note_with_letter(next_note_natural_name, equivalent_notes)

            # And add that note to the list
            notes.append(note)

        return notes


########################################################################
class Transpose:

    ####################################################################
    def __init__(self, *notes):
        self.notes = tuple(Note(n) for n in notes)
        self.transpose_up = False
        self.transpose_down = False
        self._steps = 0

    ####################################################################
    def _semitones(self):
        semitones = self._steps * 2
        return int(semitones)

    ####################################################################
    def steps(self, *steps):
        self._steps = sum(steps)
        return self._transpose()

    ####################################################################
    @property
    def up(self):
        self.transpose_up = True
        self.transpose_down = False
        return self

    ####################################################################
    @property
    def down(self):
        self.transpose_down = True
        self.transpose_up = False
        return self

    ####################################################################
    @property
    def half_step(self):
        self._steps = HALF_STEP
        return self._transpose()

    ####################################################################
    @property
    def whole_step(self):
        self._steps = WHOLE_STEP
        return self._transpose()

    ####################################################################
    @property
    def third(self):
        self._steps = WHOLE_STEP + WHOLE_STEP
        return self._transpose()

    ####################################################################
    @property
    def minor_third(self):
        self._steps = WHOLE_STEP + HALF_STEP
        return self._transpose()

    ####################################################################
    @property
    def fifth(self):
        self._steps = sum((WHOLE_STEP, WHOLE_STEP, WHOLE_STEP, HALF_STEP))
        return self._transpose()

    ####################################################################
    def _transpose(self):
        raise NotImplementedError()
