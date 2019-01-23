import collections
from decimal import Decimal

from data import SHARP, FLAT, IN_TUNE, NATURAL_NOTES, SHARPS_AND_FLATS, PITCHES, MAJOR_KEY_STEPS, \
    MINOR_KEY_STEPS, MAJOR, MINOR, WHOLE_STEP, HALF_STEP, QUALITIES
from errors import InvalidNoteError, InvalidKeyError, InvalidQualityError


#######################################################################
def clean_quality(quality):
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
        quality = clean_quality(note_with_octave[1:-1])  # any/every thing in the middle
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
    quality = clean_quality(quality)

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


########################################################################
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


########################################################################
class Interval:

    ####################################################################
    def __init__(self, number, quality=''):
        self.degree = int(number)
        self.quality = clean_quality(quality)


MajorThird = Interval(3)
MinorThird = Interval(3, quality='min')
# PerfectFifth = Interval(5, quality='perfect')


########################################################################
class Key:
    STEPS_MAP = {
        MAJOR: MAJOR_KEY_STEPS,
        MINOR: MINOR_KEY_STEPS,
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
    def __str__(self):
        return self.name

    ####################################################################
    def _generate_notes(self):
        # We already know the root note, so create a list starting with that
        notes = [self.root_note]
        # Get the base pitch to start with from our root note
        pitch = self.root_note.fundamental

        # A key has a set of whole and half steps that determine what notes
        # fall into the key, starting from the root note. Iterate through
        # each step to add each successive note to the key.
        for step in self.steps:

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
class Chord:
    pass


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
