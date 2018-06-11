HALF_STEP = 1
WHOLE_STEP = 2


########################################################################
class Note:

    ####################################################################
    def __init__(self, name, as_flat=None):
        self.name = name.upper().strip()
        self.as_flat = as_flat.upper().strip() if as_flat else ''

    ####################################################################
    def __str__(self):
        return self.name

    ####################################################################
    def __repr__(self):
        return 'Note("{name}")'.format(name=self.name)

    ####################################################################
    def __eq__(self, other):
        if isinstance(other, str):
            return (self.name == other.upper()) or (self.as_flat == other.upper())
        elif isinstance(other, Note):
            return (self.name == other.name) or (self.as_flat == other.name)
        else:
            err = 'Cannot compare type {note} to type {other}'
            raise TypeError(err.format(note=type(self), other=type(other)))


########################################################################
A = Note('A')
A_sharp = Note('A♯', 'B♭')
B = Note('B')
C = Note('C')
C_sharp = Note('C♯', 'D♭')
D = Note('D')
D_sharp = Note('D♯', 'E♭')
E = Note('E')
F = Note('F')
F_sharp = Note('F♯', 'G♭')
G = Note('G')
G_sharp = Note('G♯', 'A♭')

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
    def __init__(self, note):
        self.note = note
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
    def _get_current_index(self):
        for i, note in enumerate(NOTES):
            if self.note == note:
                return i
        raise Exception('Could not find {note} in {notes}'.format(note=self.note, notes=NOTES))

    ####################################################################
    def _transpose(self):
        semitones = self._get_number_of_semitones()
        i = self._get_current_index()

        if self.transpose_up:
            diff = len(NOTES) - i
            if diff <= semitones:
                i = semitones - diff
            else:
                i += semitones
        else:
            assert self.transpose_down
            i -= semitones

        note = NOTES[i]
        return note


########################################################################
class Transposers:

    ####################################################################
    def __init__(self, transpose_objs):
        self.transposers = tuple(transpose_objs)

    ####################################################################
    @property
    def up(self):
        for t in self.transposers:
            setattr(t, 'transpose_up', True)
            setattr(t, 'transpose_down', False)
        return self

    ####################################################################
    @property
    def down(self):
        for t in self.transposers:
            setattr(t, 'transpose_up', False)
            setattr(t, 'transpose_down', True)
        return self

    ####################################################################
    @property
    def third(self):
        transposed_notes = []
        for t in self.transposers:
            transposed_notes.append(t.third)
        return transposed_notes

    ####################################################################
    @property
    def fifth(self):
        transposed_notes = []
        for t in self.transposers:
            transposed_notes.append(t.fifth)
        return transposed_notes


########################################################################
def transpose(note):
    return Transposer(note)


########################################################################
def transpose_multiple(*notes):
    return Transposers([Transposer(n) for n in notes])


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
