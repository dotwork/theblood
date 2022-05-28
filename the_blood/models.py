from decimal import Decimal

from .data import *
from .errors import *


#######################################################################
class Octave(int):
    pass


#######################################################################
class Quality(str):

    ###################################################################
    def __new__(cls, quality):
        cleaned_q = cls.clean(quality)
        return super().__new__(Quality, cleaned_q)

    ###################################################################
    def __init__(self, quality_name):
        self.name = quality_name

    ###################################################################
    def __eq__(self, other):
        return hash(self) == hash(Quality(other))

    ###################################################################
    def __hash__(self):
        return hash(self.name)

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
            Decimal('17.32'): ['C#0', 'Db0'],
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

            for note_with_octave in _notes:
                note_to_hz_map[note_with_octave] = _pitch

        super(_PitchMap, self).__init__(data)
        self.note_to_hz_map = note_to_hz_map

    ####################################################################
    def __getitem__(self, item):
        try:
            return super(_PitchMap, self).__getitem__(item)
        except KeyError:
            item = item.replace('#', '♯').replace('b', '♭')
            return self.note_to_hz_map[item]


PitchMap = _PitchMap()


########################################################################
class Pitch(Decimal):

    __interval_increase = Decimal('1.0595')

    ####################################################################
    def __new__(cls, i, *args, **kwargs):
        TWO_PLACES = Decimal(10) ** -2
        i = Decimal(i).quantize(TWO_PLACES)
        val = super().__new__(Pitch, i, *args, **kwargs)
        return val

    ####################################################################
    def __init__(self, i):
        TWO_PLACES = Decimal(10) ** -2
        i = Decimal(i).quantize(TWO_PLACES)
        super().__init__()
        note_names = []
        try:
            note_name_options = PitchMap[i]
        except KeyError:
            raise Exception(f'{i} is not a valid standard pitch hz value.')
        for note_info in note_name_options:
            name = note_info[0]  # first character
            quality = note_info[1:-1]  # any/every thing in the middle
            octave = note_info[-1]
            note_names.append(tuple((name, quality, octave)))
        self.note_info = tuple(note_names)

    ####################################################################
    def __gt__(self, other):
        return float(self) > float(other)

    ####################################################################
    @property
    def next_pitch(self):
        next_hz = self * self.__interval_increase
        return Pitch(next_hz)

    ####################################################################
    def get_note(self, key):
        if not isinstance(key, Key):
            key = Key(key)
        for note in key.notes:
            name, quality = note.natural_name, note.quality
            for matching_name, matching_quality, _ in self.note_info:
                if matching_name == name and matching_quality == quality:
                    return note
        raise Exception(f'Could not find note for pitch {self} in {key}. '
                        f'Note options for pitch are {", ".join(key.note_names)}')

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

    ####################################################################
    def decrease(self, semitones):
        decreased = 0

        for hz in reversed(PitchMap):
            if hz < self:
                decreased += 1
            if decreased == semitones:
                break

        return Pitch(hz)


# MIDDLE_C_PITCH = Pitch(Decimal('261.63'))


########################################################################
class NoteValue:

    ####################################################################
    def __init__(self, name, fraction, value):
        self.__name = str(name)
        self.fraction = str(fraction)
        self.factor = int(value)  # quarter notes = 4, eighth notes = 8, whole notes = 1

    ####################################################################
    @property
    def name(self):
        return self.__name

    ####################################################################
    def __rtruediv__(self, other):
        if not isinstance(other, int):
            raise TypeError(f'Cannot compare type {type(other)} to NoteValue')
        return other/self.factor

    ####################################################################
    def __str__(self):
        return self.name

    ####################################################################
    def __repr__(self):
        return f'NoteValue({self.name}, {self.fraction}, {self.factor})'

    ####################################################################
    def __eq__(self, other):
        if not isinstance(other, NoteValue):
            raise TypeError(f'Cannot compare type NoteValue to type "{type(other)}"')
        return hash(self) == hash(other)

    ####################################################################
    def __hash__(self):
        return hash(self.__name)


WholeNote = NoteValue('Whole Note', '1/1', 1)
HalfNote = NoteValue('Half Note', '1/2', 2)
QuarterNote = NoteValue('Quarter Note', '1/4', 4)
EighthNote = NoteValue('Eighth Note', '1/8', 8)
SixteenthNote = NoteValue('Sixteenth Note', '1/6', 16)
ThirtySecondNote = NoteValue('Thirty-Second Note', '1/32', 32)
NOTE_VALUES = {
    __note_value.factor: __note_value for __note_value in
    [WholeNote, HalfNote, QuarterNote, EighthNote, SixteenthNote, ThirtySecondNote]
}


########################################################################
class Note:

    ####################################################################
    def __init__(self, note):
        if isinstance(note, Note):
            name = note.natural_name
            quality = note.quality
        else:
            name = note[:1].upper().strip()
            assert name in NATURAL_NOTES, f'"{name}" is not a valid note.'
            quality = note[1:].replace("-", "").replace("_", "").lower().strip()
            if quality:
                try:
                    quality = SHARPS_AND_FLATS[quality]
                except KeyError:
                    raise InvalidNoteError(f'"{note}" is not a valid note.')

        self.__name = f'{name}{quality}'
        self.__quality = Quality(quality)

    ####################################################################
    @property
    def name(self):
        return self.__name

    ####################################################################
    @property
    def quality(self):
        return self.__quality

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
        if not isinstance(other, Note):
            raise TypeError(f'Cannot compare type Note to type "{type(other)}"')
        return hash(self) == hash(other)

    ####################################################################
    def __hash__(self):
        return hash(tuple((self.name, self.quality)))

    ####################################################################
    @classmethod
    def from_pitch(cls, pitch, key):
        pitch = Pitch(pitch)
        if not isinstance(key, Key):
            key = Key(key)
        for base_name, quality, octave in PitchMap[pitch]:
            name = f'{base_name}{quality}'
            if name in key.note_names:
                note = Note(f'{base_name}{quality}')
                return note
        raise Exception(f'Failed to find note for pitch {pitch} in key {key}. Actual notes are: {key.note_names}')

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
    @classmethod
    def get_note_with_letter(cls, letter, notes_info):
        for name, quality, octave in notes_info:
            if name == letter:
                return Note(f'{name}{quality}')
        else:
            raise InvalidKeyError(f'Did not find a {letter} note in {notes_info}.')


#######################################################################
class Interval(int):
    pass


G_double_sharp = Note('G♯♯')
A = Note('A')
B_double_flat = Note('B♭♭')
Bbb = B_double_flat

A_sharp = Note('A♯')
B_flat = Note('B♭')
Bb = B_flat

B = Note('B')
C_flat = Note('C♭')
Cb = C_flat

B_sharp = Note('B♯')
C = Note('C')
D_double_flat = Note('D♭♭')
Dbb = D_double_flat

C_sharp = Note('C♯')
D_flat = Note('D♭')
Db = D_flat

C_double_sharp = Note('C♯♯')
D = Note('D')
E_double_flat = Note('E♭♭')
Ebb = E_double_flat

D_sharp = Note('D♯')
E_flat = Note('E♭')
Eb = E_flat

D_double_sharp = Note('D♯♯')
E = Note('E')
F_flat = Note('F♭')
Fb = F_flat

E_sharp = Note('E♯')
F = Note('F')
G_double_flat = Note('G♭♭')
Gbb = G_double_flat

F_sharp = Note('F♯')
G_flat = Note('G♭')
Gb = G_flat

F_double_sharp = Note('F♯♯')
G = Note('G')
A_double_flat = Note('A♭♭')
Abb = A_double_flat

G_sharp = Note('G♯')
A_flat = Note('A♭')
Ab = A_flat

W = WHOLE_STEP = Interval(2)
H = HALF_STEP = Interval(1)

MinorThird = Interval(3)
MajorThird = Interval(4)
PerfectFifth = Interval(7)

MAJOR_INTERVALS = (W, W, H, W, W, W, H)
MINOR_INTERVALS = (W, H, W, W, H, W, W)

# https://music.stackexchange.com/questions/73110/what-are-the-interval-patterns-for-the-modes
IONIAN_INTERVALS = (W, W, H, W, W, W, H)
DORIAN_INTERVALS = (W, H, W, W, W, H, W)
PHRYGIAN_INTERVALS = (H, W, W, W, H, W, W)
LYDIAN_INTERVALS = (W, W, W, H, W, W, H)
MIXOLYDIAN_INTERVALS = (W, W, H, W, W, H, W)
AEOLIAN_INTERVALS = (W, H, W, W, H, W, W)
LOCRIAN_INTERVALS = (H, W, W, H, W, W, W)

SCALE_TO_INTERVALS_MAP = {
    MAJOR_SCALE_NAME: MAJOR_INTERVALS,
    MINOR_SCALE_NAME: MINOR_INTERVALS,
    IONIAN_SCALE_NAME: IONIAN_INTERVALS,
    DORIAN_SCALE_NAME: DORIAN_INTERVALS,
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
    DORIAN_INTERVALS: DORIAN_SCALE_NAME,
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
class Range:
    def __init__(self, lowest_pitch, highest_pitch):
        self.lowest_pitch = Pitch(lowest_pitch)
        self.highest_pitch = Pitch(highest_pitch)

        _pitches = []
        for names, hz in PITCHES.items():
            if lowest_pitch <= hz <= highest_pitch:
                _pitches.append(Pitch(hz))

        self.pitches = tuple(_pitches)

    def __len__(self):
        return len(self.pitches)

    def __iter__(self):
        for pitch in self.pitches:
            yield pitch


PianoRange = Range(Pitch('27.50'), Pitch('4186.01'))
assert len(PianoRange) == 88, f'Piano Range: {len(PianoRange)}'


#######################################################################
class ScalePattern:

    ####################################################################
    def __init__(self, name='', intervals=None):
        name, intervals = self.clean_name_and_intervals(name, intervals)
        self.name = name
        self.intervals = tuple(intervals or [])

    ####################################################################
    def __str__(self):
        return self.name

    ####################################################################
    @classmethod
    def clean_name_and_intervals(cls, name, intervals):
        assert name or intervals, 'A name or iterable of intervals must be provided.'

        name = name.strip().title() if name else ''
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
                    name = MODAL_INTERVALS_TO_NAME_MAP[intervals]
                except KeyError:
                    argument = name or intervals
                    raise InvalidScaleError(f'{argument} is not a recognized scale.')

        return name, intervals

    ####################################################################
    def __eq__(self, other):
        return tuple(self) == tuple(other)

    ####################################################################
    def __iter__(self):
        for interval in self.intervals:
            yield interval

    ####################################################################
    def __getslice__(self, slice_obj):
        start = slice_obj.start
        stop = slice_obj.stop
        step = slice_obj.step
        if step:
            raise Exception('Cannot slice BaseScale objects with steps.')
        if not any((start, stop)):
            return self

        intervals = self.intervals[start:stop:step]
        name = f'{self.name} Slice[{start}:{stop}]'
        return ScalePattern(name, intervals=intervals)


MajorScale = ScalePattern(MAJOR_SCALE_NAME)
MinorScale = ScalePattern(MINOR_SCALE_NAME)

IonianScale = ScalePattern(IONIAN_SCALE_NAME)
DorianScale = ScalePattern(DORIAN_SCALE_NAME)
PhrygianScale = ScalePattern(PHRYGIAN_SCALE_NAME)
LydianScale = ScalePattern(LYDIAN_SCALE_NAME)
MixolydianScale = ScalePattern(MIXOLYDIAN_SCALE_NAME)
AeolianScale = ScalePattern(AEOLIAN_SCALE_NAME)
LocrianScale = ScalePattern(LOCRIAN_SCALE_NAME)

MODAL_SCALES = (IonianScale, DorianScale, PhrygianScale,
                LydianScale, MixolydianScale, AeolianScale, LocrianScale)


#######################################################################
class Scale(ScalePattern):

    ####################################################################
    def __init__(self, tonic, base_scale):
        if base_scale.name in SCALE_TO_INTERVALS_MAP:
            # This is a known scale. Build it from its name
            # and we will fetch the correct intervals automatically.
            super().__init__(base_scale.name)
        else:
            # For custom scales, provide both the name and intervals.
            super().__init__(base_scale.name, base_scale.intervals)

        # Save off what scale pattern we used to build this scale
        self.base_scale = base_scale

        # Scale objects require a tonic to build the set of notes from.
        self.tonic = Note(tonic)

        # super().__init__ set self.name to the base scale's name.
        # Update it with the tonic's name.
        self.name = f'{self.tonic} {self.name}'

        self.notes = tuple(self._generate_notes())
        self.note_names = tuple(note.name for note in self.notes)

        num_intervals = len(self.notes)
        self.first = self.notes[0]
        self.second = self.notes[1] if num_intervals > 1 else None
        self.third = self.notes[2] if num_intervals > 2 else None
        self.fourth = self.notes[3] if num_intervals > 3 else None
        self.fifth = self.notes[4] if num_intervals > 4 else None
        self.sixth = self.notes[5] if num_intervals > 5 else None
        self.seventh = self.notes[6] if num_intervals > 6 else None
        self.eighth = self.notes[7] if num_intervals > 7 else None
        self.ninth = self.notes[8] if num_intervals > 8 else None
        self.tenth = self.notes[9] if num_intervals > 9 else None
        self.eleventh = self.notes[10] if num_intervals > 10 else None
        self.twelfth = self.notes[11] if num_intervals > 11 else None
        self.thirteenth = self.notes[12] if num_intervals > 12 else None
        self.fourteenth = self.notes[13] if num_intervals > 13 else None
        self.fifteenth = self.notes[14] if num_intervals > 14 else None
        self.sixteenth = self.notes[15] if num_intervals > 15 else None

    ####################################################################
    def _generate_notes(self):
        # We already know the root note, so create a list starting with that
        notes = [self.tonic]

        # Get the base pitch to start with from our tonic note
        pitch_value = PitchMap[f'{self.tonic.name}4']
        pitch = Pitch(pitch_value)

        # A key has a set of whole and half steps that determine what notes
        # fall into the key, starting from the root note. Iterate through
        # each of these intervals to add each successive note to the key.
        for interval in self.intervals[:-1]:  # iterating up to the last one with [:-1]
            # because we're just generating notes. We don't need the last step because
            # it will lead us back to the tonic, which we already have.

            # Increase it to the pitch we want for the next note.
            pitch = pitch.increase(interval)

            # Get the list of harmonically equivalent notes for the increased pitch
            equivalent_notes_info = pitch.note_info

            # Find which of the equivalent notes is named with the next letter for our key
            # For example, if the last note was some kind of A (A, A#, or Ab)
            # the next note must be a B (B, B#, or Bb)
            next_note_natural_name = notes[-1].next_natural_note.name
            note = Note.get_note_with_letter(next_note_natural_name, equivalent_notes_info)

            # And add that note to the list
            notes.append(note)

        return notes

    ####################################################################
    def __eq__(self, other):
        if not isinstance(other, Scale):
            raise TypeError(f'Cannot compare type {type(other)} to type Scale.')

        return self.notes == other.notes and self.intervals == other.intervals

    ####################################################################
    def __getitem__(self, item):
        try:
            i = int(item)
            return self.notes[i]
        except IndexError:
            raise Exception(f'This scale does not have {i + 1} notes: {self.notes}')
        except TypeError:
            return self.__getslice__(item)
        except ValueError:
            return None

    ####################################################################
    def __getslice__(self, slice_obj):
        base_scale = self.base_scale.__getslice__(slice_obj)
        if base_scale == self.base_scale:
            return self

        tonic = self.notes[slice_obj.start or 0]
        scale = self.__class__(tonic, base_scale)
        return scale

    ####################################################################
    def __iter__(self):
        for note in self.notes:
            yield note

    ####################################################################
    @property
    def minor_seventh(self):
        """
        The minor seventh for a scale is a minor third above the
        the fifth. Using that as a starting point:
            - Find the number of semitones minor seventh is above
              the tonic's pitch
            - Get the pitch for the tonic
            - Increase the pitch by the number of semitones
              for the minor seventh
            - Get the harmonically equivalent notes at that raised pitch
            - Select the one that has the same natural name as the
              scale's seventh
        """
        min_7_semitones = sum((PerfectFifth, MinorThird))
        pitch = self.tonic.fundamental.increase(min_7_semitones)
        equivalent_notes = pitch.notes
        note = Note.get_note_with_letter(self.seventh.natural_name, equivalent_notes)
        return note

    ####################################################################
    @property
    def major_seventh(self):
        min_7_semitones = sum((PerfectFifth, MajorThird))
        pitch = self.tonic.fundamental.increase(min_7_semitones)
        equivalent_notes = pitch.notes
        note = Note.get_note_with_letter(self.seventh.natural_name, equivalent_notes)
        return note


#######################################################################
class Mode(Scale):

    ####################################################################
    def __init__(self, tonic, modal_scale):
        """
        Mode is a wrapper around Scale that validates the scale as
        a mode (Ionian, Dorian, etc.), and provides a more specific
        class type for mode-specific contexts.
        """
        if modal_scale.name not in MODE_NAMES:
            err = f'{modal_scale} is not a valid mode.'
            raise InvalidModeError(err)

        super().__init__(tonic, modal_scale)

    ####################################################################
    def __str__(self):
        return f'{self.name} Mode'

    ####################################################################
    def __repr__(self):
        return f'Mode({self.name})'


########################################################################
def _get_note_and_quality_from_music_element(element_name):
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
    if quality:
        quality = Quality(quality)

    return note, quality


########################################################################
class Key:

    ####################################################################
    def __init__(self, name):
        tonic, quality = _get_note_and_quality_from_music_element(name.strip())
        self.tonic = tonic
        self.quality = quality
        self.name = f'{self.tonic.name}{self.quality}'
        self.base_scale = MinorScale if quality == MINOR else MajorScale
        self.scale = Scale(self.tonic, self.base_scale)
        self.notes = self.scale.notes
        self.note_names = tuple(n.name for n in self.notes)

    #     self.aeolian_mode = None
    #     self.locrian_mode = None
    #     self.ionian_mode = None
    #     self.dorian_mode = None
    #     self.phrygian_mode = None
    #     self.lydian_mode = None
    #     self.mixolydian_mode = None
    #     self.modes = None
    #
    #     self.set_modes()
    #
    # ####################################################################
    # def set_modes(self):
    #     if self.is_major():
    #         self.ionian_mode = Mode(tonic=self.scale.first, modal_scale=IonianScale)
    #         self.dorian_mode = Mode(tonic=self.scale.second, modal_scale=DorianScale)
    #         self.phrygian_mode = Mode(tonic=self.scale.third, modal_scale=PhrygianScale)
    #         self.lydian_mode = Mode(tonic=self.scale.fourth, modal_scale=LydianScale)
    #         self.mixolydian_mode = Mode(tonic=self.scale.fifth, modal_scale=MixolydianScale)
    #         self.aeolian_mode = Mode(tonic=self.scale.sixth, modal_scale=AeolianScale)
    #         self.locrian_mode = Mode(tonic=self.scale.seventh, modal_scale=LocrianScale)
    #
    #         self.modes = (
    #             self.ionian_mode,
    #             self.dorian_mode,
    #             self.phrygian_mode,
    #             self.lydian_mode,
    #             self.mixolydian_mode,
    #             self.aeolian_mode,
    #             self.locrian_mode,
    #         )
    #     else:
    #         self.aeolian_mode = Mode(tonic=self.scale.first, modal_scale=AeolianScale)
    #         self.locrian_mode = Mode(tonic=self.scale.second, modal_scale=LocrianScale)
    #         self.ionian_mode = Mode(tonic=self.scale.third, modal_scale=IonianScale)
    #         self.dorian_mode = Mode(tonic=self.scale.fourth, modal_scale=DorianScale)
    #         self.phrygian_mode = Mode(tonic=self.scale.fifth, modal_scale=PhrygianScale)
    #         self.lydian_mode = Mode(tonic=self.scale.sixth, modal_scale=LydianScale)
    #         self.mixolydian_mode = Mode(tonic=self.scale.seventh, modal_scale=MixolydianScale)
    #
    #         self.modes = (
    #             self.aeolian_mode,
    #             self.locrian_mode,
    #             self.ionian_mode,
    #             self.dorian_mode,
    #             self.phrygian_mode,
    #             self.lydian_mode,
    #             self.mixolydian_mode,
    #         )

    ####################################################################
    def __str__(self):
        return f'Key of {self.name}'

    ####################################################################
    def __repr__(self):
        return f'Key({self.name})'

    ####################################################################
    def __iter__(self):
        for note in self.scale:
            yield note

    ####################################################################
    def __eq__(self, other):
        return self.name == other.name

    ####################################################################
    def is_major(self):
        return self.quality == MAJOR


########################################################################
class Chord:

    ####################################################################
    def __init__(self, name, key=None):
        root, quality = _get_note_and_quality_from_music_element(name.strip())
        self.root_note = root
        self.quality = quality
        self.is_minor = MAJOR_ABBREVIATION not in quality and MINOR in quality
        self.is_major = not self.is_minor
        self.name = f"{root}{quality}"
        self.key_specified = key is not None
        self.key = Key(key) if key else self.default_key
        self.notes = self._generate_notes()

    ####################################################################
    @property
    def default_key(self):
        quality = MINOR if self.is_minor else MAJOR
        name = f'{self.root_note.name}{quality}'
        key = Key(name)
        return key

    ####################################################################
    @property
    def triad(self):
        return (self.key.scale.first,
                self.key.scale.third,
                self.key.scale.fifth)

    ####################################################################
    def _generate_notes(self):
        notes = list(self.triad)
        if self.seventh:
            notes.append(self.seventh)
        return tuple(notes)

    ####################################################################
    @property
    def seventh(self):
        scale = self.key.scale
        if self.quality == SEVENTH or self.quality == MINOR + SEVENTH:
            return scale.minor_seventh
        elif self.quality == MAJOR_ABBREVIATION + SEVENTH:
            return scale.major_seventh
        return None


########################################################################
class Transpose:

    ####################################################################
    def __init__(self, *notes, quality_to_use=None):
        self._raw_notes = tuple(Note(n) for n in notes)
        self.quality_to_use = quality_to_use
        for note in self._raw_notes:
            if note.quality and note.quality in QUALITIES:
                self.quality_to_use = note.quality
                break

        self._transposed_notes = []
        self.transpose_up = False
        self.transpose_down = False
        self._steps = ()

    ####################################################################
    def _semitones(self):
        semitones = sum(self._steps)
        return int(semitones)

    ####################################################################
    def steps(self, *steps):
        self._steps = tuple(steps)
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
        self._steps = (H, )
        return self._transpose()

    ####################################################################
    @property
    def whole_step(self):
        self._steps = (W, )
        return self._transpose()

    ####################################################################
    @property
    def third(self):
        self._steps = (W, W)
        return self._transpose()

    ####################################################################
    @property
    def minor_third(self):
        self._steps = (W, H)
        return self._transpose()

    ####################################################################
    @property
    def fifth(self):
        self._steps = (W, W, W, H)
        return self._transpose()

    ####################################################################
    def octave(self):
        self._steps = (W, W, W, W, W, W)
        return self._transpose()

    ####################################################################
    def _transpose(self):
        transposed = []
        for note in self._raw_notes:
            if self.transpose_up:
                transposed_pitch = note.fundamental.increase(self._semitones())
            else:
                transposed_pitch = note.fundamental.decrease(self._semitones())
            matches = PitchMap[transposed_pitch]
            best_match = None
            for match in matches:
                octave = int(match[-1])
                matching_note = Note(match[:-1], octave=octave)
                if matching_note.is_natural:
                    best_match = matching_note
                    break

                if self.quality_to_use and matching_note.quality == self.quality_to_use:
                    best_match = matching_note
                elif best_match:
                    if not (best_match.is_standard_flat or best_match.is_standard_sharp):
                        best_match = matching_note
                elif not best_match:
                    best_match = matching_note
            assert best_match is not None, f'Failed to find note with pitch {transposed_pitch}. Tried {matches}'
            transposed.append(best_match)
        self._transposed_notes = transposed
        return self._transposed_notes
