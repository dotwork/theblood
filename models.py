import collections
from decimal import Decimal

from data import SHARP, FLAT, IN_TUNE, QUALITIES, NATURAL_NOTES, SHARPS_AND_FLATS, NATURAL, DOUBLE_SHARP, \
    DOUBLE_FLAT, PITCHES
from errors import InvalidNoteError, InvalidKeyError, InvalidQualityError


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
                if len(note) == 2:
                    name, octave = note
                    quality = ''
                else:
                    name = note[0]
                    octave = note[-1]
                    quality = note[1:-1]

                if quality:
                    quality = QUALITIES[quality]
                note_to_hz_map[f'{name}{quality}{octave}'] = _pitch

        super(_PitchMap, self).__init__(data)
        self.note_to_hz_map = note_to_hz_map

    ####################################################################
    def __getitem__(self, item):
        try:
            return super(_PitchMap, self).__getitem__(item)
        except KeyError:
            note = item[0].upper()
            octave = item[-1]
            quality = QUALITIES[item[1:-1]]
            item = f'{note}{quality}{octave}'
            return self.note_to_hz_map[item]


PitchMap = _PitchMap()


########################################################################
class Pitch:

    __interval_increase = Decimal('1.0595')

    ####################################################################
    def __init__(self, hz):
        if isinstance(hz, Pitch):
            hz = hz.hz
        self.hz = Decimal(hz)

    ####################################################################
    def __eq__(self, other):
        return self.hz == Pitch(other).hz

    ####################################################################
    def __add__(self, other):
        hz = self.hz + Pitch(other).hz
        return Pitch(hz)

    ####################################################################
    def __sub__(self, other):
        hz = self.hz - Pitch(other).hz
        return Pitch(hz)

    ####################################################################
    def __rsub__(self, other):
        hz = Pitch(other).hz - self.hz
        return Pitch(hz)

    ####################################################################
    def __mul__(self, other):
        hz = self.hz * Pitch(other).hz
        return Pitch(hz)
    __rmul__ = __mul__

    ####################################################################
    def __truediv__(self, other):
        hz = self.hz / Pitch(other).hz
        return Pitch(hz)

    ####################################################################
    def __rtruediv__(self, other):
        hz = Pitch(other).hz / self.hz
        return Pitch(hz)

    ####################################################################
    def __gt__(self, other):
        return self.hz > Pitch(other).hz

    ####################################################################
    def __lt__(self, other):
        return self.hz < Pitch(other).hz

    ####################################################################
    @property
    def notes(self):
        note_names = PitchMap[self.hz]
        notes_list = []
        for name in note_names:
            note = name[:-1]
            octave = name[-1]
            notes_list.append(Note(note, octave=octave))
        return notes_list

    ####################################################################
    @property
    def next_pitch(self):
        next_hz = self.hz * self.__interval_increase
        return Pitch(next_hz)

    ####################################################################
    def in_tune(self, pitch_2):
        diff = pitch_2 / self.hz
        if diff > Decimal('1.05'):
            return SHARP
        elif diff < Decimal('0.95'):
            return FLAT
        return IN_TUNE

    ####################################################################
    def increase(self, semitones):
        increased = 0

        for hz in PitchMap:
            if hz > self.hz:
                increased += 1
            if increased == semitones:
                break

        return Pitch(hz)


########################################################################
def validate_and_clean_quality(quality):
    cleaned = quality.lower().strip().replace(' ', '')
    try:
        return QUALITIES[cleaned]
    except KeyError:
        raise InvalidQualityError(f'"{quality}" is not a valid quality.')


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
    quality = validate_and_clean_quality(quality)

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


########################################################################
A_flat = Note('A♭')
A = Note('A')
A_sharp = Note('A♯')

B_flat = Note('B♭')
B = Note('B')
B_sharp = Note('B♯')

C_flat = Note('C♭')
C = Note('C')
C_sharp = Note('C♯')

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


########################################################################
class Interval:

    ####################################################################
    def __init__(self, number, is_minor=False):
        self.degree = self.clean_degree(number)
        self.is_minor = is_minor
        self.is_major = not is_minor
        self.quality = ''

    ####################################################################
    @property
    def semitones(self):
        raise NotImplementedError()

    ####################################################################
    def clean_degree(self, number):
        try:
            degree = int(number)
        except Exception:
            print('Provide a number for the interval, ie. for a Third, provide "3".')
            raise

        return degree

    ####################################################################
    @classmethod
    def from_notes_difference(cls, note1, note2):
        raise NotImplementedError()

    ####################################################################
    def up_from_note(self, note):
        current_index = NATURAL_NOTES.index(note.natural_name)

        interval_note_index = current_index + self.degree - 1
        interval_note_name = (NATURAL_NOTES + NATURAL_NOTES)[interval_note_index]

        for quality in (NATURAL, SHARP, FLAT, DOUBLE_SHARP, DOUBLE_FLAT):
            interval_note = Note(interval_note_name + quality)
            semitone_difference = interval_note.semitones_up_from(note)
            if semitone_difference == self.semitones:
                return interval_note
        else:
            raise Exception('This should be unreachable code.')


MajorThird = Interval(3)
MinorThird = Interval(3, is_minor=True)
PerfectFifth = Interval(5)

MAJOR_CHORD_INTERVALS = [MajorThird, MinorThird]
MINOR_CHORD_INTERVALS = [MinorThird, MajorThird]

HALF_STEP = .5
H = HALF_STEP
WHOLE_STEP = 1
W = WHOLE_STEP


MAJOR_KEY_STEPS = (WHOLE_STEP, WHOLE_STEP, HALF_STEP, WHOLE_STEP, WHOLE_STEP, WHOLE_STEP)
MINOR_KEY_STEPS = (WHOLE_STEP, HALF_STEP, WHOLE_STEP, WHOLE_STEP, HALF_STEP, WHOLE_STEP)


####################################################################
class Scale:

    ################################################################
    def __init__(self):
        self.notes = None
        self.intervals = None

    ####################################################################
    @classmethod
    def from_notes(cls, notes):
        raise NotImplementedError()

    ####################################################################
    def from_root(self, root_note, intervals):
        raise NotImplementedError()

    ####################################################################
    def is_major(self):
        raise NotImplementedError()

    ####################################################################
    def is_minor(self):
        raise NotImplementedError()


########################################################################
class Chord:

    ####################################################################
    def __init__(self, name):
        root_note, quality = get_note_and_quality_from_music_element(name)

        self.root_note = root_note
        self.quality = quality
        self.name = f'{self.root_note.name}{self.quality}'
        self._notes = []
        self._intervals = []

    ####################################################################
    def __len__(self):
        return len(self._notes)

    ####################################################################
    @classmethod
    def get_chord_name(cls, notes):
        """
        Figure out the chord's name based on the notes.
        """
        raise NotImplementedError()

    ####################################################################
    @classmethod
    def from_notes(cls, notes):
        notes = [Note(n) for n in notes]
        chord_name = cls.get_chord_name(notes)
        chord = Chord(chord_name)
        chord._notes = notes

        intervals = []
        last_note = notes[0]
        for note in notes[:-1]:
            interval = Interval.from_notes_difference(last_note, note)
            intervals.append(interval)
        chord._intervals = intervals

        return chord

    ####################################################################
    @classmethod
    def from_root_note(cls, root_note, intervals):
        raise NotImplementedError()

    ####################################################################
    @classmethod
    def from_scale_interval(cls, scale, interval):
        raise NotImplementedError()

    ####################################################################
    @classmethod
    def from_chord_interval(cls, chord, interval):
        raise NotImplementedError()

    ####################################################################
    def notes(self):
        if self._notes:
            return self._notes
        else:
            self._notes = [self.root_note]
            for interval in self.intervals:
                last_note = self._notes[-1]
                next_note = interval.up_from_note(last_note)
                self._notes.append(next_note)
            return self._notes

    ####################################################################
    @property
    def intervals(self):
        if self._intervals:
            return self._intervals
        else:
            raise NotImplementedError()


########################################################################
class Key:
    STEPS_MAP = {
        '': MAJOR_KEY_STEPS,
        'm': MINOR_KEY_STEPS,
    }

    ####################################################################
    def __init__(self, name):
        root, quality = get_note_and_quality_from_music_element(name.strip())
        self.root_note = root
        self.quality = quality
        self.name = f'{self.root_note.name}{self.quality}'
        self.steps = self.STEPS_MAP[self.quality]
        self.notes = self._generate_notes()
        self.note_names = tuple(n.name for n in self.notes)

    ####################################################################
    @classmethod
    def get_root_note_and_quality(cls, key_name):
        note, quality = get_note_and_quality_from_music_element(key_name)
        return note, quality

    ####################################################################
    def __str__(self):
        return self.name

    ####################################################################
    def _generate_notes(self):
        notes = [self.root_note]
        pitch = self.root_note.fundamental

        for step in self.steps:

            # Take the current pitch, and increase it by 2 semitones
            semitones = step * 2
            pitch = pitch.increase(semitones)

            # Now get the list of harmonically equivalent notes for the increased pitch
            equivalent_notes = pitch.notes

            # Find which of the equivalent notes is named with the next letter for our key
            next_note_natural_name = notes[-1].next_natural_note.name
            for note in equivalent_notes:
                if next_note_natural_name.startswith(note.natural_name):
                    # And add that note to the list
                    notes.append(note)
                    break  # out of this inner forloop, and back to the outer forloop
            else:
                msg = f'Did not find a {next_note_natural_name} note in {equivalent_notes}.'
                raise InvalidKeyError(msg)

        return notes


########################################################################
class Transposer:

    ####################################################################
    def __init__(self, notes):
        self.notes = [Note(n) for n in notes]
        self.transpose_up = False
        self.transpose_down = False
        self._steps = 0

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
        self._steps = .5
        return self._transpose()

    ####################################################################
    @property
    def whole_step(self):
        self._steps = 1
        return self._transpose()

    ####################################################################
    @property
    def third(self):
        self._steps = 2
        return self._transpose()

    ####################################################################
    @property
    def fifth(self):
        self._steps = 3.5
        return self._transpose()

    ####################################################################
    def steps(self, *steps):
        self._steps = sum(steps)
        return self._transpose()

    ####################################################################
    def _get_number_of_semitones(self):
        semitones = self._steps * 2
        return int(semitones)

    ####################################################################
    def _transpose(self):
        transposed = []
        semitones = self._get_number_of_semitones()
        for note in self.notes:
            transposed_note = note
            for i in range(semitones):
                if self.transpose_up:
                    transposed_note = transposed_note.next()
                else:
                    transposed_note = transposed_note.previous(use_sharps=note.is_sharp)

            transposed.append(transposed_note)
        return transposed


########################################################################
def transpose(*notes):
    _notes = []
    for n in notes:
        if isinstance(n, (str, Note)):
            _notes.append(n)
        else:
            _notes.extend(n)
    return Transposer(_notes)
