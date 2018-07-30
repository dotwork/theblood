
from errors import InvalidNoteError, InvalidKeyError, InvalidQualityError

NATURAL = ''
FLAT = '♭'
SHARP = '♯'
DOUBLE_FLAT = '♭♭'
DOUBLE_SHARP = '♯♯'

HALF_STEP = .5
WHOLE_STEP = 1
NATURAL_NOTES = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'A')


MAJOR_KEY_STEPS = (WHOLE_STEP, WHOLE_STEP, HALF_STEP, WHOLE_STEP, WHOLE_STEP, WHOLE_STEP)
MINOR_KEY_STEPS = (WHOLE_STEP, HALF_STEP, WHOLE_STEP, WHOLE_STEP, HALF_STEP, WHOLE_STEP)


SHARPS_AND_FLATS = {
    '♯♯': '♯♯',
    '♭♭': '♭♭',

    '##': '♯♯',
    'bb': '♭♭',

    '♯': '♯',
    '♭': '♭',

    '#': '♯',
    'b': '♭',

    'sharp': '♯',
    'flat': '♭',

    'double sharp': '♯♯',
    'double flat': '♭♭',
}


QUALITIES = SHARPS_AND_FLATS.copy()
QUALITIES.update({
    'major': '',
    'maj': '',

    'minor': 'm',
    'min': 'm',
    'm': 'm',

    '7': '7',
    'minor7': 'm7',
    'min7': 'm7',
    'm7': 'm7',

    '9': '9',
    'minor9': 'm9',
    'min9': 'm9',
    'm9': 'm9',

    '11': '11',
    'minor11': 'm11',
    'min11': 'm11',
    'm11': 'm11',
})


########################################################################
def validate_and_clean_quality(quality):
    try:
        return QUALITIES[quality.lower().strip().replace(' ', '')]
    except KeyError:
        raise InvalidQualityError(f'"{quality}" is not a valid quality.')


########################################################################
def get_note_and_quality_from_music_element(element_name):
    note = Note(element_name[0])
    remainder = element_name[1:]

    if remainder:
        for char in remainder:
            try:
                note = Note(note.name + char)
            except InvalidNoteError:
                break

    quality = element_name[len(note.name):] or ''
    if quality:
        quality = validate_and_clean_quality(quality)

    return note, quality


########################################################################
class Note:

    ####################################################################
    def __init__(self, note):
        if isinstance(note, Note):
            self.name = note.name
            self.quality = note.quality
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

    ####################################################################
    @property
    def is_standard_flat(self):
        return self.is_flat and self.name not in (C_flat.name, F_flat.name)

    ####################################################################
    @property
    def is_standard_sharp(self):
        return self.is_sharp and self.name not in (B_sharp.name, E_sharp.name)

    ####################################################################
    def next(self, use_flats=False):
        if self.is_standard_flat:
            return Note(self.natural_note_name)
        elif self.is_standard_sharp or self == B or self == E:
            return self.next_natural_note
        elif self == B_sharp:
            return C_sharp
        elif self == C_flat:
            return C
        elif self == E_sharp:
            return F_sharp
        elif self == F_flat:
            return F
        elif self.is_double_sharp:
            return Note(self.next_natural_note.natural_note_name + '#')
        elif self.is_double_flat:
            return Note(self.natural_note_name + 'b')
        elif use_flats:
            return Note(self.next_natural_note.name + 'b')
        else:
            return Note(self.name + "#")

    ####################################################################
    def previous(self, use_sharps=False):
        if self.is_standard_flat:
            return self.previous_natural_note
        elif self.is_sharp:
            return Note(self.natural_note_name)
        elif self == C or self == F:
            return self.previous_natural_note
        elif self == C_flat:
            return A_sharp
        elif self == F_flat:
            return D_sharp
        elif use_sharps:
            return Note(self.previous_natural_note.name + '♯')
        else:
            assert self.name in NATURAL_NOTES
            return Note(self.name + '♭')

    ####################################################################
    @property
    def is_natural(self):
        return not bool(self.quality)

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
    def semitones_up_from(self, note):
        num_semitones = 0
        while note != self:
            num_semitones += 1
            note = note.next()
        return num_semitones

    ####################################################################
    def __str__(self):
        return self.name

    ####################################################################
    def __repr__(self):
        return f'Note("{self.name}")'

    ####################################################################
    @property
    def natural_note_name(self):
        return self.name[0]

    ####################################################################
    @property
    def next_natural_note(self):
        current_index = NATURAL_NOTES.index(self.natural_note_name)
        next_note_index = current_index + 1
        next_note_name = NATURAL_NOTES[next_note_index]
        return Note(next_note_name)

    ####################################################################
    @property
    def previous_natural_note(self):
        current_index = NATURAL_NOTES.index(self.natural_note_name)
        if current_index == 0:
            current_index = -1
        previous_note_index = current_index - 1
        previous_note_name = NATURAL_NOTES[previous_note_index]
        return Note(previous_note_name)

    ####################################################################
    def is_equal_pitch_to(self, other):
        if isinstance(other, str):
            other = Note(other)
        elif not isinstance(other, Note):
            raise TypeError(f'Cannot compare type {type(self)} to type {type(other)}')

        if self.name == other.name:
            return True
        else:
            if other.natural_note_name == self.next_natural_note.natural_note_name:
                if other.is_flat:
                    if self.is_standard_sharp:
                        return True
                    elif self.name == B.name and other.name == C_flat.name:
                        return True
                    elif self.name == E.name and other.name == F_flat.name:
                        return True
                elif self.is_sharp:
                    if self.name == B_sharp.name and other.name == C.name:
                        return True
                    elif self.name == E_sharp.name and other.name == F.name:
                        return True
                elif self.is_double_sharp and other.is_natural:
                    return True
            elif other.natural_note_name == self.previous_natural_note.natural_note_name:
                if self.is_flat:
                    if other.is_standard_sharp:
                        return True
                    elif self.name == C_flat.name and other.name == B.name:
                        return True
                    elif self.name == F_flat.name and other.name == E.name:
                        return True
                elif other.is_sharp:
                    if self.name == C.name and other.name == B_sharp.name:
                        return True
                    elif self.name == F.name and other.name == E_sharp.name:
                        return True
                elif self.is_double_flat and other.is_natural:
                    return True
            return False

    ####################################################################
    def __eq__(self, other):
        return self.name == Note(other).name


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
def generate_note_names():
    names = []

    for natural_note in NATURAL_NOTES:
        flat = Note(natural_note + "b")
        if flat.is_standard_flat:
            names.append(flat.name)

        names.append(natural_note)

        sharp = Note(natural_note + "#")
        if sharp.is_standard_sharp:
            names.append(sharp.name)

    return tuple(names)


NOTE_NAMES = generate_note_names()

NOTES = (
    A,
    A_sharp,
    B,
    C,
    C_sharp,
    D,
    D_sharp,
    E,
    F,
    F_sharp,
    G,
    G_sharp,
)


########################################################################
class Interval:

    ####################################################################
    def __init__(self, number, is_minor=False):
        self.degree = self.clean_degree(number)
        self.is_minor = is_minor
        self.is_major = not is_minor

    ####################################################################
    @property
    def semitones(self):
        if self.degree == 3:
            if self.is_major:
                return 4
            else:
                return 3
        elif self.degree == 5:
            return 7

    ####################################################################
    def clean_degree(self, number):
        try:
            degree = int(number)
        except Exception:
            print('Provide a number for the interval, ie. for a Third, provide "3".')
            raise

        return degree

    ####################################################################
    def from_note(self, note):
        NATURAL_NOTES = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
        current_index = NATURAL_NOTES.index(note.natural_note_name)

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


########################################################################
class Chord:

    ####################################################################
    def __init__(self, name):
        self.root_note, self.quality = get_note_and_quality_from_music_element(name)
        self.name = f'{self.root_note.name}{self.quality}'
        self.key = Key(self.name)
        self.is_minor = self.quality.startswith('m')
        self.is_major = not self.is_minor
        self.intervals = MAJOR_CHORD_INTERVALS if self.is_major else MINOR_CHORD_INTERVALS
        self.notes = self._generate_notes()
        self.note_names = tuple(n.name for n in self.notes)

    ####################################################################
    def _generate_notes(self):
        notes = self.triad
        if self.is_a_seventh_chord:
            if self.is_minor:
                notes.append(self.seventh)
            else:
                notes.append(self.diminished_seventh)
        return notes

    ####################################################################
    @property
    def triad(self):
        """
        Triad formula: 1 - 3 - 5
        """
        return self.key.get_scale_degrees(1, 3, 5)

    ####################################################################
    @property
    def is_a_seventh_chord(self):
        return '7' in self.name

    ####################################################################
    @property
    def seventh(self):
        """
        Minor 7th chord formula: 1 - 3 - 5 - 7
        The m7 chords add a minor seventh.
        """
        seventh = self.key.scale_degree(7)
        return seventh

    ####################################################################
    @property
    def diminished_seventh(self):
        """
        7 chord formula: 1 – 3 – 5 – ♭7
        The 7 chords add a diminished seventh, one semitone lower.
        """
        diminished = self.seventh.previous()
        return diminished


########################################################################
class Key:

    ####################################################################
    def __init__(self, name):
        self.root_note, quality = self.get_root_note_and_quality(name.strip())
        self.is_minor = quality.startswith('m')
        self.is_major = not self.is_minor
        self.steps = MINOR_KEY_STEPS if self.is_minor else MAJOR_KEY_STEPS
        self.notes = self._generate_notes()
        self.note_names = tuple(note.name for note in self.notes)

    ####################################################################
    @property
    def diatonic_scale(self):
        notes = [self.root_note]

        for step in self.steps:
            semitones = int(step * 2)
            for semitone in range(semitones):
                previous_note = notes[-1]
                if previous_note.is_standard_flat:
                    next_note = Note(previous_note.natural_note_name)
                elif previous_note.is_natural and not (previous_note == B or previous_note == E):
                    next_note = Note(previous_note.name + SHARP)
                else:
                    next_note = previous_note.next_natural_note

                notes.append(next_note)

        return notes

    ####################################################################
    def get_scale_degrees(self, *degrees):
        return [self.scale_degree(d) for d in degrees]

    ####################################################################
    def scale_degree(self, degree):
        degree = int(degree)
        return self.notes[degree - 1]

    ####################################################################
    @classmethod
    def get_root_note_and_quality(cls, key_name):
        note, quality = get_note_and_quality_from_music_element(key_name)
        try:
            if quality:
                is_minor = quality.startswith('m')
                if is_minor:
                    remainder = quality[1:]
                    assert remainder in ('', '7', '9', '11')
        except AssertionError:
            raise InvalidKeyError(f'{key_name} is not a valid key. quality={quality}')

        return note, quality

    ####################################################################
    def __str__(self):
        return f'Key of {self.root_note.name}'

    ####################################################################
    def _generate_notes(self):
        notes = [self.root_note]

        for step in self.steps:
            previous_note = notes[-1]
            transposed = transpose(previous_note).up.steps(step)[0]

            for quality in ('', '#', 'b', '##', 'bb'):
                note_name = previous_note.next_natural_note.name
                next_note = Note(note_name + quality)
                if next_note.is_equal_pitch_to(transposed):
                    notes.append(next_note)
                    break
            else:
                raise Exception('Should be unreachable code.')

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
