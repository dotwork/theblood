from errors import InvalidNoteError, InvalidKeyError

HALF_STEP = .5
WHOLE_STEP = 1
WHOLE_NOTES = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'A')


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


########################################################################
def validate_and_clean_quality(quality):
    cleaned = quality.lower().strip()
    if cleaned in ('major', 'maj'):
        cleaned = ''
    elif cleaned in ('min', 'minor'):
        cleaned = 'm'

    return cleaned


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

    quality = element_name[len(note.name):]
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
            assert name in WHOLE_NOTES, f'"{name}" is not a valid whole note.'
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
    @property
    def is_B_or_E(self):
        return self.name in (B.name, E.name)

    ####################################################################
    @property
    def is_C_or_F(self):
        return self.name in (C.name, F.name)

    ####################################################################
    def next(self):
        if self.is_standard_flat:
            whole_note = Note(self.whole_note_name)
            return whole_note
        elif self.is_standard_sharp or self.is_B_or_E:
            return self.next_whole_note
        elif self.name == B_sharp.name:
            return C_sharp
        elif self.name == C_flat.name:
            return C
        elif self.name == E_sharp.name:
            return F_sharp
        elif self.name == F_flat.name:
            return F
        elif self.is_double_sharp:
            return Note(self.next_whole_note.whole_note_name + '#')
        elif self.is_double_flat:
            return Note(self.whole_note_name + 'b')
        else:
            return Note(self.name + "#")

    ####################################################################
    def previous(self):
        if self.is_standard_flat:
            return self.previous_whole_note
        elif self.is_sharp:
            whole_note = Note(self.whole_note_name)
            return whole_note
        elif self.is_C_or_F:
            return self.previous_whole_note
        elif self == C_flat:
            return A_sharp
        elif self == F_flat:
            return D_sharp
        else:
            assert self.name in WHOLE_NOTES
            return Note(self.name + "♭")

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
    def __str__(self):
        return self.name

    ####################################################################
    def __repr__(self):
        return f'Note("{self.name}")'

    ####################################################################
    @property
    def whole_note_name(self):
        return self.name[0]

    ####################################################################
    @property
    def next_whole_note(self):
        current_index = WHOLE_NOTES.index(self.whole_note_name)
        next_note_index = current_index + 1
        next_note_name = WHOLE_NOTES[next_note_index]
        return Note(next_note_name)

    ####################################################################
    @property
    def previous_whole_note(self):
        current_index = WHOLE_NOTES.index(self.whole_note_name)
        if current_index == 0:
            current_index = -1
        previous_note_index = current_index - 1
        previous_note_name = WHOLE_NOTES[previous_note_index]
        return Note(previous_note_name)

    ####################################################################
    def __eq__(self, other):
        if isinstance(other, str):
            other = Note(other)
        elif not isinstance(other, Note):
            raise TypeError(f'Cannot compare type {type(self)} to type {type(other)}')

        if self.name == other.name:
            return True
        else:
            if other.whole_note_name == self.next_whole_note.whole_note_name:
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
            elif other.whole_note_name == self.previous_whole_note.whole_note_name:
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

    for whole_note in WHOLE_NOTES:
        flat = Note(whole_note + "b")
        if flat.is_standard_flat:
            names.append(flat.name)

        names.append(whole_note)

        sharp = Note(whole_note + "#")
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
    def __init__(self, number):
        self.degree = self.get_degree(number)
        self.name = self.get_name()

    ####################################################################
    def get_degree(self, number):
        try:
            degree = int(number)
        except Exception as e:
            print('Provide a number for the interval, ie. for a Third, provide "3".')
            raise

        return degree

    ####################################################################
    def get_name(self):
        return self.degree


########################################################################
class Chord:

    ####################################################################
    def __init__(self, name):
        self.root_note, self.quality = get_note_and_quality_from_music_element(name)
        self.name = f'{self.root_note.name}{self.quality}'
        self.notes = self.generate_notes()

    ####################################################################
    def generate_notes(self):
        return tuple([self.root_note])


########################################################################
class Key:

    ####################################################################
    def __init__(self, name):
        self.root_note, quality = self.get_root_note_and_quality(name.strip())
        self.is_minor = quality == 'm'
        self.is_major = not self.is_minor
        self.steps = MINOR_KEY_STEPS if self.is_minor else MAJOR_KEY_STEPS
        self.notes = self._generate_notes()
        self.note_names = tuple(note.name for note in self.notes)

    ####################################################################
    def get_root_note_and_quality(self, key_name):
        note, quality = get_note_and_quality_from_music_element(key_name)
        try:
            assert quality in ('', 'm')
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
            for accidental in ('', '#', 'b', '##', 'bb'):
                next_note = Note(previous_note.next_whole_note.whole_note_name + accidental)
                if next_note == transposed:
                    transposed = next_note
                    break
            else:
                raise Exception('Should be unreachable code.')
            notes.append(transposed)
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
                    transposed_note = transposed_note.previous()
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
