HALF_STEP = .5
WHOLE_STEP = 1
WHOLE_NOTES = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'A')

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
class Note:

    ####################################################################
    def __init__(self, note):
        if isinstance(note, Note):
            self.name = note.name
            self.accidental = note.accidental
        else:
            name = note[:1].upper().strip()
            remainder = note[1:].replace("-", "").replace("_", "").lower().strip()
            if remainder:
                accidental = SHARPS_AND_FLATS[remainder]
            else:
                accidental = ''
            self.name = '{}{}'.format(name, accidental)
            self.accidental = accidental

    ####################################################################
    @property
    def is_standard_flat(self):
        return self.is_flat and self.name not in (B.name, E.name)

    ####################################################################
    @property
    def is_standard_sharp(self):
        return self.is_sharp and self.name not in (B_sharp.name, E_sharp.name)

    ####################################################################
    @property
    def is_B_or_E(self):
        return self.name in (B.name, E.name)

    ####################################################################
    def next(self):
        if self.is_standard_flat:
            whole_note = Note(self.whole_note_name)
            return whole_note
        elif self.is_standard_sharp or self.is_B_or_E:
            return self.next_whole_note
        elif self == B_sharp:
            return C_sharp
        elif self == E_sharp:
            return F_sharp
        elif self.is_double_sharp:
            return Note(self.next_whole_note.whole_note_name + '#')
        else:
            return Note(self.name + "#")

    ####################################################################
    def previous(self):
        if self.is_standard_flat:
            return self.previous_whole_note
        elif self.is_sharp:
            whole_note = Note(self.whole_note_name)
            return whole_note
        elif self == C:
            return B
        elif self == F:
            return E
        else:
            assert self.name in WHOLE_NOTES
            return Note(self.name + "♭")

    ####################################################################
    @property
    def is_natural(self):
        return not self.accidental

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
        return 'Note("{name}")'.format(name=self.name)

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
                    if self.is_sharp:
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
                    if other.is_sharp:
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
        as_int = int(semitones)
        error = 'Invalid number of semitones: {semitones}, steps={steps}'
        error = error.format(semitones=semitones, steps=self._steps)
        assert semitones == as_int, error
        return as_int

    ####################################################################
    def _get_current_index(self, note):
        for i, _note in enumerate(NOTES):
            if _note == note:
                return i
        raise Exception('Could not find {note} in {notes}'.format(note=note, notes=NOTES))

    ####################################################################
    def _transpose(self):
        """
                # for note in self.notes:
        #     i = self._get_current_index(note)
        #
        #     if self.transpose_up:
        #         diff = len(NOTES) - i
        #         if diff <= semitones:
        #             i = semitones - diff
        #         else:
        #             i += semitones
        #     else:
        #         assert self.transpose_down
        #         i -= semitones
        #
        #     transposed_note = NOTES[i]

        """
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

            # find the version of this note that starts with the next whole note.
            # ie. if the previous note was a C of some kind (C, C#, Cb, etc.)
            # find the version of this note that starts with the next whole note, D something
            # previous_note = tra

        return transposed


########################################################################
def transpose(*notes):
    _notes = []
    for n in notes:
        if isinstance(n, (str, Note)):
            _notes.append(n)
        else:
            _notes.extend(list(n))
    return Transposer(_notes)


########################################################################
class Key:

    ####################################################################
    def __init__(self, root_note):
        self.root_note = Note(root_note)
        self.notes = self._generate_notes()
        self.note_names = tuple(note.name for note in self.notes)

    ####################################################################
    def __str__(self):
        return f'Key of {self.root_note.name}'

    ####################################################################
    def _generate_notes(self):
        notes = [self.root_note]
        for step in (WHOLE_STEP, WHOLE_STEP, HALF_STEP, WHOLE_STEP, WHOLE_STEP, WHOLE_STEP):
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
