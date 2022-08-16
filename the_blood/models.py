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
        self.name = self.clean(quality_name)

    ###################################################################
    def __eq__(self, other):
        return self.name == Quality(other).name

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
            raise InvalidQualityError('"{}" is not a valid quality.'.format(quality))


########################################################################
class Pitch:

    __interval_increase = 1.0595

    ####################################################################
    def __init__(self, _float):
        self._value = _float
        if isinstance(_float, Pitch):
            _float = _float._value
        self.value = float(_float)

    ####################################################################
    def __str__(self):
        return 'Pitch({})'.format(self._value)

    ####################################################################
    def __repr__(self):
        return 'Pitch({})'.format(self._value)

    ####################################################################
    def __hash__(self):
        return hash(self._value)

    ####################################################################
    def __eq__(self, other):
        if isinstance(other, (float, int)):
            return self._value == other
        elif isinstance(other, Pitch):
            return self._value == other._value
        else:
            raise TypeError('Cannot compare Pitch to type {}'.format(type(other)))

    ####################################################################
    def __add__(self, other):
        if isinstance(other, (float, int)):
            return self._value + other
        elif isinstance(other, Pitch):
            return self._value + other._value
        else:
            raise TypeError('Cannot compare Pitch to type {}'.format(type(other)))

    ####################################################################
    def __sub__(self, other):
        if isinstance(other, (float, int)):
            return self._value - other
        elif isinstance(other, Pitch):
            return self._value - other._value
        else:
            raise TypeError('Cannot compare Pitch to type {}'.format(type(other)))

    ####################################################################
    def __rsub__(self, other):
        if isinstance(other, (float, int)):
            return other - self._value
        elif isinstance(other, Pitch):
            return other._value - self._value
        else:
            raise TypeError('Cannot compare Pitch to type {}'.format(type(other)))

    ####################################################################
    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return self._value * other
        elif isinstance(other, Pitch):
            return self._value * other._value
        else:
            raise TypeError('Cannot compare Pitch to type {}'.format(type(other)))

    ####################################################################
    def __gt__(self, other):
        if isinstance(other, (float, int)):
            return self._value > other
        elif isinstance(other, Pitch):
            return self._value > other._value
        else:
            raise TypeError('Cannot compare Pitch to type {}'.format(type(other)))

    ####################################################################
    def __ge__(self, other):
        if isinstance(other, (float, int)):
            return self._value >= other
        elif isinstance(other, Pitch):
            return self._value >= other._value
        else:
            raise TypeError('Cannot compare Pitch to type {}'.format(type(other)))

    ####################################################################
    def __lt__(self, other):
        if isinstance(other, (float, int)):
            return self._value < other
        elif isinstance(other, Pitch):
            return self._value < other._value
        else:
            raise TypeError('Cannot compare Pitch to type {}'.format(type(other)))

    ####################################################################
    def __le__(self, other):
        if isinstance(other, (float, int)):
            return self._value <= other
        elif isinstance(other, Pitch):
            return self._value <= other._value
        else:
            raise TypeError('Cannot compare Pitch to type {}'.format(type(other)))

    ####################################################################
    @property
    def next_pitch(self):
        next_hz = self._value * self.__interval_increase
        return Pitch(next_hz)

    ####################################################################
    # def in_tune(self, pitch_2):
    #     diff = pitch_2 / self._value
    #     if diff > 1.05:
    #         return SHARP
    #     elif diff < 0.95:
    #         return FLAT
    #     return IN_TUNE

    ####################################################################
    def increase(self, semitones):
        increased = 0

        for hz in PITCHES.values():
            if hz > self._value:
                increased += 1
            if increased == semitones:
                break

        return Pitch(hz)

    ####################################################################
    def decrease(self, semitones):
        decreased = 0

        for hz in reversed(PitchMap):
            if hz < self._value:
                decreased += 1
            if decreased == semitones:
                break

        return Pitch(hz)


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
            raise TypeError('Cannot compare type {} to NoteValue'.format(type(other)))
        return other/self.factor

    ####################################################################
    def __str__(self):
        return self.name

    ####################################################################
    def __repr__(self):
        r = 'NoteValue({name}, {fraction}, {factor})'
        return r.format(name=self.name, fraction=self.fraction, factor=self.factor)

    ####################################################################
    def __eq__(self, other):
        if not isinstance(other, NoteValue):
            raise TypeError('Cannot compare type NoteValue to type "{}"'.format(type(other)))
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


class UnavailableNoteError(Exception): pass


########################################################################
class Note:

    ####################################################################
    def __init__(self, note):
        if isinstance(note, Note):
            name = note.natural_name
            quality = note.quality
        else:
            name = note[:1].upper().strip()
            assert name in NATURAL_NOTES, '"{}" is not a valid note.'.format(name)
            quality = note[1:].replace("-", "").replace("_", "").lower().strip()
            if quality:
                try:
                    quality = SHARPS_AND_FLATS[quality]
                except KeyError:
                    raise InvalidNoteError('"{}" is not a valid note.'.format(note))

        self.__name = '{}{}'.format(name, quality)
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
        return self.name

    ####################################################################
    def __repr__(self):
        return 'Note("{}")'.format(self.name)

    ####################################################################
    def __eq__(self, other):
        if not isinstance(other, Note):
            raise TypeError('Cannot compare type Note to type "{}"'.format(type(other)))
        return hash(self) == hash(other)

    ####################################################################
    def __hash__(self):
        return hash(tuple((self.name, self.quality)))

    ####################################################################
    @classmethod
    def from_pitch(cls, pitch, available_notes):
        for note, octave in PitchMap(pitch):
            if note in available_notes:
                return note
        error = ('Failed to find note for pitch {pitch} with available notes {available_notes}. '
                 'Actual notes are: {available_notes}')
        raise UnavailableNoteError(error.format(pitch=pitch, available_notes=available_notes))

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
        return self.name.endswith('#') and not self.is_double_sharp

    ####################################################################
    @property
    def is_double_sharp(self):
        return self.name.endswith('##')

    ####################################################################
    @property
    def is_flat(self):
        return self.name.endswith('b') and not self.is_double_flat

    ####################################################################
    @property
    def is_double_flat(self):
        return self.name.endswith('bb')

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


#######################################################################
def PitchMap(item):
    """
    This dictionary maps pitches to their corresponding notes and octaves.
    The value is a tuple of tuples. Each inner tuple containing a (Note, Octave).
    It also maps the other way as well.
    Each tuple of (Note, Octave) will correspond to the same Pitch.

    Here are a couple entries each way:
        {
            Pitch('16.35'): ((Note('B#') Octave(0)), (Note('C'), Octave(0))),
            Pitch('17.32'): ((Note('C#') Octave(0)), (Note('Db'), Octave(0))),
            ...
            (Note('B#') Octave(0)): Pitch('16.35'),
            (Note('C'), Octave(0)): Pitch('16.35'),
            (Note('C#') Octave(0)): Pitch('17.32'),
            ...
        }
    """
    need_pitch = isinstance(item, tuple) and isinstance(item[0], Note) and isinstance(item[1], Octave)
    need_note = isinstance(item, Pitch)

    for notes_with_octaves, _pitch in PITCHES.items():
        if need_note:
            if _pitch == item:
                notes_with_octaves = notes_with_octaves.split('/')
                notes = []
                for note_with_octave in notes_with_octaves:
                    name = note_with_octave[0]  # first character
                    quality = note_with_octave[1:-1]  # any/every thing in the middle
                    octave = Octave(note_with_octave[-1])  # last character, integer for octave
                    note = Note(name + quality)
                    notes.append((note, octave))
                return tuple(notes)
        elif need_pitch:
            target_note, target_octave = item
            notes_with_octaves = notes_with_octaves.split('/')
            for note_with_octave in notes_with_octaves:
                name = note_with_octave[0]  # first character
                quality = note_with_octave[1:-1]  # any/every thing in the middle
                octave = Octave(note_with_octave[-1])  # last character, integer for octave
                note = Note(name + quality)
                if target_note == note and target_octave == octave:
                    return Pitch(_pitch)


#######################################################################
class Interval(int):
    pass


G_double_sharp = Note('G##')
A = Note('A')
B_double_flat = Note('Bbb')
Bbb = B_double_flat

A_sharp = Note('A#')
B_flat = Note('Bb')
Bb = B_flat

B = Note('B')
C_flat = Note('Cb')
Cb = C_flat

B_sharp = Note('B#')
C = Note('C')
D_double_flat = Note('Dbb')
Dbb = D_double_flat

C_sharp = Note('C#')
D_flat = Note('Db')
Db = D_flat

C_double_sharp = Note('C##')
D = Note('D')
E_double_flat = Note('Ebb')
Ebb = E_double_flat

D_sharp = Note('D#')
E_flat = Note('Eb')
Eb = E_flat

D_double_sharp = Note('D##')
E = Note('E')
F_flat = Note('Fb')
Fb = F_flat

E_sharp = Note('E#')
F = Note('F')
G_double_flat = Note('Gbb')
Gbb = G_double_flat

F_sharp = Note('F#')
G_flat = Note('Gb')
Gb = G_flat

F_double_sharp = Note('F##')
G = Note('G')
A_double_flat = Note('Abb')
Abb = A_double_flat

G_sharp = Note('G#')
A_flat = Note('Ab')
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
            pitch = Pitch(hz)
            if lowest_pitch <= pitch <= highest_pitch:
                _pitches.append(pitch)

        self.pitches = tuple(_pitches)

    def __len__(self):
        return len(self.pitches)

    def __iter__(self):
        for pitch in self.pitches:
            yield pitch


PianoRange = Range(Pitch(27.50), Pitch(4186.01))
assert len(PianoRange) == 88, 'Piano Range: {}'.format(len(PianoRange))


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

        name = (name.strip() if name else '')
        name = ' '.join(word.capitalize() for word in name.split(' '))
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
                    raise InvalidScaleError('{} is not a recognized scale.'.format(argument))

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
        name = '{name} Slice[{start}:{stop}]'.format(name=self.name, start=start, stop=stop)
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
        self.name = '{tonic} {name}'.format(tonic=self.tonic, name=self.name)

        self.notes = tuple(self._generate_notes())
        self.note_names = tuple(note.name for note in self.notes)

        # num_intervals = len(self.notes)
        # self.first = self.notes[0]
        # self.second = self.notes[1] if num_intervals > 1 else None
        # self.third = self.notes[2] if num_intervals > 2 else None
        # self.fourth = self.notes[3] if num_intervals > 3 else None
        # self.fifth = self.notes[4] if num_intervals > 4 else None
        # self.sixth = self.notes[5] if num_intervals > 5 else None
        # self.seventh = self.notes[6] if num_intervals > 6 else None
        # self.eighth = self.notes[7] if num_intervals > 7 else None
        # self.ninth = self.notes[8] if num_intervals > 8 else None
        # self.tenth = self.notes[9] if num_intervals > 9 else None
        # self.eleventh = self.notes[10] if num_intervals > 10 else None
        # self.twelfth = self.notes[11] if num_intervals > 11 else None
        # self.thirteenth = self.notes[12] if num_intervals > 12 else None
        # self.fourteenth = self.notes[13] if num_intervals > 13 else None
        # self.fifteenth = self.notes[14] if num_intervals > 14 else None
        # self.sixteenth = self.notes[15] if num_intervals > 15 else None

    ####################################################################
    def _generate_notes(self):
        # We already know the root note, so create a list starting with that
        notes = [self.tonic]

        # Get the base pitch to start with from our tonic note
        pitch_value = PitchMap((self.tonic, Octave(4)))
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
            equivalent_notes = PitchMap(pitch)

            # Find which of the equivalent notes is named with the next letter for our key
            # For example, if the last note was some kind of A (A, A#, or Ab)
            # the next note must be a B (B, B#, or Bb)
            next_note_natural_name = notes[-1].next_natural_note.name
            for note, _ in equivalent_notes:
                if note.natural_name == next_note_natural_name:
                    # And add that note to the list
                    notes.append(note)
                    break
            else:
                error = 'Did not find a {next_name} note in {equivalent}.'
                raise InvalidKeyError(error.format(next_name=next_note_natural_name, equivalent=equivalent_notes))

        return notes

    ####################################################################
    def __eq__(self, other):
        if not isinstance(other, Scale):
            raise TypeError('Cannot compare type {} to type Scale.'.format(type(other)))

        return self.notes == other.notes and self.intervals == other.intervals

    ####################################################################
    def __getitem__(self, item):
        try:
            i = int(item)
            return self.notes[i]
        except IndexError:
            raise Exception('This scale does not have {qty} notes: {notes}'.format(qty=i + 1, notes=self.notes))
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
    # @property
    # def minor_seventh(self):
    #     """
    #     The minor seventh for a scale is a minor third above the
    #     the fifth. Using that as a starting point:
    #         - Find the number of semitones minor seventh is above
    #           the tonic's pitch
    #         - Get the pitch for the tonic
    #         - Increase the pitch by the number of semitones
    #           for the minor seventh
    #         - Get the harmonically equivalent notes at that raised pitch
    #         - Select the one that has the same natural name as the
    #           scale's seventh
    #     """
    #     min_7_semitones = sum((PerfectFifth, MinorThird))
    #     tonic_with_octave = '{}4'.format(self.tonic.name)
    #     pitch = Pitch(PitchMap[tonic_with_octave]).increase(min_7_semitones)
    #     return Note.from_pitch(pitch, self.notes)
    #
    # ####################################################################
    # @property
    # def major_seventh(self):
    #     maj_7_semitones = sum((PerfectFifth, MajorThird))
    #     tonic_with_octave = '{}4'.format(self.tonic.name)
    #     pitch = Pitch(PitchMap[tonic_with_octave]).increase(maj_7_semitones)
    #     return Note.from_pitch(pitch, self.notes)


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
        raise InvalidNoteError('"{}" does not contain a valid root note.'.format(element_name))
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
        self.name = '{name}{quality}'.format(name=self.tonic.name, quality=self.quality)
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
        return 'Key of {}'.format(self.name)

    ####################################################################
    def __repr__(self):
        return 'Key({})'.format(self.name)

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
