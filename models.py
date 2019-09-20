import collections
import string
from decimal import Decimal

from data import SHARP, FLAT, IN_TUNE, NATURAL_NOTES, SHARPS_AND_FLATS, PITCHES, MINOR, \
    QUALITIES, MAJOR_SCALE_NAME, MINOR_SCALE_NAME, IONIAN_SCALE_NAME, DORIAN_SCALE_NAME, PHRYGIAN_SCALE_NAME, \
    LYDIAN_SCALE_NAME, MIXOLYDIAN_SCALE_NAME, AEOLIAN_SCALE_NAME, LOCRIAN_SCALE_NAME, MAJOR, MODE_NAMES, SEVENTH, \
    MAJOR_ABBREVIATION
from errors import InvalidNoteError, InvalidKeyError, InvalidQualityError, InvalidScaleError, InvalidModeError


#######################################################################
def divisible_by(word, i):
    return (len(word) % i) == 0


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

    ####################################################################
    def decrease(self, semitones):
        decreased = 0

        for hz in reversed(PitchMap):
            if hz < self:
                decreased += 1
            if decreased == semitones:
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
    def get_note_with_letter(cls, letter, notes):
        for note in notes:
            if note.natural_name.startswith(letter):
                return note
        else:
            raise InvalidKeyError(f'Did not find a {letter} note in {notes}.')


#######################################################################
class Interval(int):
    pass


G_double_sharp = Note('G♯♯')
A = Note('A')
B_double_flat = Note('B♭♭')

A_sharp = Note('A♯')
B_flat = Note('B♭')

B = Note('B')
C_flat = Note('C♭')

B_sharp = Note('B♯')
C = Note('C')
D_double_flat = Note('D♭♭')

C_sharp = Note('C♯')
D_flat = Note('D♭')

C_double_sharp = Note('C♯♯')
D = Note('D')
E_double_flat = Note('E♭♭')

D_sharp = Note('D♯')
E_flat = Note('E♭')

E = Note('E')
F_flat = Note('F♭')

E_sharp = Note('E♯')
F = Note('F')
G_double_flat = Note('G♭♭')

F_sharp = Note('F♯')
G_flat = Note('G♭')

F_double_sharp = Note('F♯♯')
G = Note('G')
A_double_flat = Note('A♭♭')

G_sharp = Note('G♯')
A_flat = Note('A♭')


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
        pitch = self.tonic.fundamental

        # A key has a set of whole and half steps that determine what notes
        # fall into the key, starting from the root note. Iterate through
        # each of these intervals to add each successive note to the key.
        for interval in self.intervals[:-1]:  # iterating up to the last one with [:-1]
            # because we're just generating notes. We don't need the last step because
            # it will lead us back to the tonic, which we already have.

            # Increase it to the pitch we want for the next note.
            pitch = pitch.increase(interval)

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
class Key:

    ####################################################################
    def __init__(self, name):
        tonic, quality = get_note_and_quality_from_music_element(name.strip())

        self.tonic = tonic
        self.quality = quality
        self.name = f'{self.tonic.name}{self.quality}'
        self.base_scale = MinorScale if quality == MINOR else MajorScale
        self.scale = Scale(self.tonic, self.base_scale)
        self.note_names = tuple(n.name for n in self.scale.notes)

        self.aeolian_mode = None
        self.locrian_mode = None
        self.ionian_mode = None
        self.dorian_mode = None
        self.phrygian_mode = None
        self.lydian_mode = None
        self.mixolydian_mode = None
        self.modes = None

        self.set_modes()

    ####################################################################
    def set_modes(self):
        if self.is_major():
            self.ionian_mode = Mode(tonic=self.scale.first, modal_scale=IonianScale)
            self.dorian_mode = Mode(tonic=self.scale.second, modal_scale=DorianScale)
            self.phrygian_mode = Mode(tonic=self.scale.third, modal_scale=PhrygianScale)
            self.lydian_mode = Mode(tonic=self.scale.fourth, modal_scale=LydianScale)
            self.mixolydian_mode = Mode(tonic=self.scale.fifth, modal_scale=MixolydianScale)
            self.aeolian_mode = Mode(tonic=self.scale.sixth, modal_scale=AeolianScale)
            self.locrian_mode = Mode(tonic=self.scale.seventh, modal_scale=LocrianScale)

            self.modes = (
                self.ionian_mode,
                self.dorian_mode,
                self.phrygian_mode,
                self.lydian_mode,
                self.mixolydian_mode,
                self.aeolian_mode,
                self.locrian_mode,
            )
        else:
            self.aeolian_mode = Mode(tonic=self.scale.first, modal_scale=AeolianScale)
            self.locrian_mode = Mode(tonic=self.scale.second, modal_scale=LocrianScale)
            self.ionian_mode = Mode(tonic=self.scale.third, modal_scale=IonianScale)
            self.dorian_mode = Mode(tonic=self.scale.fourth, modal_scale=DorianScale)
            self.phrygian_mode = Mode(tonic=self.scale.fifth, modal_scale=PhrygianScale)
            self.lydian_mode = Mode(tonic=self.scale.sixth, modal_scale=LydianScale)
            self.mixolydian_mode = Mode(tonic=self.scale.seventh, modal_scale=MixolydianScale)

            self.modes = (
                self.aeolian_mode,
                self.locrian_mode,
                self.ionian_mode,
                self.dorian_mode,
                self.phrygian_mode,
                self.lydian_mode,
                self.mixolydian_mode,
            )

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
        root, quality = get_note_and_quality_from_music_element(name.strip())
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


#######################################################################
class Game:

    ####################################################################
    def __init__(self, text):
        self.text = text
        self.words = self.text.split(' ')
        self.key = self._calculate_key()
        self.chords = self._calculate_chords()
        self.time_signature = self._calculate_time_signature()

    ####################################################################
    def _calculate_key(self):
        first_word = self.words[0]
        if divisible_by(first_word, 4):
            return Key('C')
        elif divisible_by(first_word, 2):
            return Key('Am')
        elif divisible_by(first_word, 3):
            # Update this with logic for number of sharps/flats
            return Key('A')
        else:
            raise NotImplementedError()

    ####################################################################
    def _calculate_time_signature(self):
        first_word = self.words[0]
        if divisible_by(first_word, 2):
            return '4/4'
        elif divisible_by(first_word, 3):
            return '3/4'
        else:
            raise NotImplementedError()

    ####################################################################
    def _calculate_chords(self):
        chords = [Chord(self.key.name).triad]
        for word in self.words[1:]:
            chord = []
            for char in word:
                if char.lower() in string.ascii_lowercase:
                    i = string.ascii_lowercase.index(char)
                    while i > 6:
                        i -= 7
                    note = self.key.scale[i]
                    chord.append(note)
            chords.append(tuple(chord))
        return chords
