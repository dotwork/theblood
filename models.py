HALF_STEP = 1
WHOLE_STEP = 2
WHOLE_NOTES = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'A')

SHARPS_AND_FLATS = {
    'sharp': '♯',
    'flat': '♭',
    '♯': '♯',
    '♭': '♭',
    '#': '♯',
    'b': '♭',
}


########################################################################
class Note:

    ####################################################################
    def __init__(self, note):
        if isinstance(note, Note):
            self.name = note.name
        else:
            name = note[:1].upper().strip()
            remainder = note[1:].replace("-", "").replace("_", "").lower().strip()
            if remainder:
                modifier = SHARPS_AND_FLATS[remainder]
            else:
                modifier = ''
            self.name = '{}{}'.format(name, modifier)

    ####################################################################
    @property
    def is_sharp(self):
        return self.name.endswith('♯')

    ####################################################################
    @property
    def is_flat(self):
        return not self.is_sharp

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
    @property
    def alias(self):
        if self.is_sharp:
            return Transposer([self.next_whole_note]).down.half_step
        elif self.is_flat:
            return Transposer([self.previous_whole_note]).up.half_step
        else:
            return None

    ####################################################################
    def __eq__(self, other):
        if isinstance(other, str):
            other = Note(other)
        elif not isinstance(other, Note):
            err = 'Cannot compare type {note} to type {other}'
            raise TypeError(err.format(note=type(self), other=type(other)))

        if self.name == other.name:
            return True
        else:
            if other.whole_note_name == self.next_whole_note.whole_note_name:
                if other.is_flat:
                    return True
            elif other.whole_note_name == self.previous_whole_note.whole_note_name:
                if other.is_sharp:
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
    def steps(self, num_whole=0, num_half=0):
        num_half_as_int = int(num_half)
        assert num_half == num_half_as_int
        self._steps = num_whole + (num_half/2)
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
        transposed = []
        semitones = self._get_number_of_semitones()
        for note in self.notes:
            i = self._get_current_index(note)

            if self.transpose_up:
                diff = len(NOTES) - i
                if diff <= semitones:
                    i = semitones - diff
                else:
                    i += semitones
            else:
                assert self.transpose_down
                i -= semitones

            transposed_note = NOTES[i]
            transposed.append(transposed_note)

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
        self.root = root_note
        self.notes = self.generate_notes(Note(root_note))

    ####################################################################
    @classmethod
    def generate_notes(cls, root_note):
        notes = [root_note]
        whole = 0
        half = 0
        for step in (WHOLE_STEP, WHOLE_STEP, HALF_STEP, WHOLE_STEP, WHOLE_STEP, WHOLE_STEP):
            whole += 1 if step == WHOLE_STEP else 0
            half += 1 if step == HALF_STEP else 0
            notes.append(Transposer(root_note).up.steps(num_whole=whole, num_half=half))
        return notes
