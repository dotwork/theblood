from collections import OrderedDict, defaultdict
from decimal import Decimal

from errors import InvalidNoteError, InvalidKeyError, InvalidQualityError

IN_TUNE = "In Tune"

NATURAL_NOTES = ('A', 'B', 'C', 'D', 'E', 'F', 'G')

NATURAL = ''
FLAT = '♭'
SHARP = '♯'
DOUBLE_FLAT = '♭♭'
DOUBLE_SHARP = '♯♯'

NOTE_QUALITIES = ('♭♭', '♭', '', '♯', '♯♯')

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
    '': 'maj',
    'major': 'maj',
    'maj': 'maj',

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

PITCHES = OrderedDict((
    ('C0', Decimal('16.35')),
    ('C#0/Db0 ', Decimal('17.32')),
    ('D0', Decimal('18.35')),
    ('D#0/Eb0 ', Decimal('19.45')),
    ('E0', Decimal('20.60')),
    ('F0', Decimal('21.83')),
    ('F#0/Gb0 ', Decimal('23.12')),
    ('G0', Decimal('24.50')),
    ('G#0/Ab0 ', Decimal('25.96')),
    ('A0', Decimal('27.50')),
    ('A#0/Bb0 ', Decimal('29.14')),
    ('B0', Decimal('30.87')),
    ('C1', Decimal('32.70')),
    ('C#1/Db1 ', Decimal('34.65')),
    ('D1', Decimal('36.71')),
    ('D#1/Eb1 ', Decimal('38.89')),
    ('E1', Decimal('41.20')),
    ('F1', Decimal('43.65')),
    ('F#1/Gb1 ', Decimal('46.25')),
    ('G1', Decimal('49.00')),
    ('G#1/Ab1 ', Decimal('51.91')),
    ('A1', Decimal('55.00')),
    ('A#1/Bb1 ', Decimal('58.27')),
    ('B1', Decimal('61.74')),
    ('C2', Decimal('65.41')),
    ('C#2/Db2 ', Decimal('69.30')),
    ('D2', Decimal('73.42')),
    ('D#2/Eb2 ', Decimal('77.78')),
    ('E2', Decimal('82.41')),
    ('F2', Decimal('87.31')),
    ('F#2/Gb2 ', Decimal('92.50')),
    ('G2', Decimal('98.00')),
    ('G#2/Ab2 ', Decimal('103.83')),
    ('A2', Decimal('110.00')),
    ('A#2/Bb2 ', Decimal('116.54')),
    ('B2', Decimal('123.47')),
    ('C3', Decimal('130.81')),
    ('C#3/Db3 ', Decimal('138.59')),
    ('D3', Decimal('146.83')),
    ('D#3/Eb3 ', Decimal('155.56')),
    ('E3', Decimal('164.81')),
    ('F3', Decimal('174.61')),
    ('F#3/Gb3 ', Decimal('185.00')),
    ('G3', Decimal('196.00')),
    ('G#3/Ab3 ', Decimal('207.65')),
    ('A3', Decimal('220.00')),
    ('A#3/Bb3 ', Decimal('233.08')),
    ('B3', Decimal('246.94')),
    ('C4', Decimal('261.63')),
    ('C#4/Db4 ', Decimal('277.18')),
    ('D4', Decimal('293.66')),
    ('D#4/Eb4 ', Decimal('311.13')),
    ('E4', Decimal('329.63')),
    ('F4', Decimal('349.23')),
    ('F#4/Gb4 ', Decimal('369.99')),
    ('G4', Decimal('392.00')),
    ('G#4/Ab4 ', Decimal('415.30')),
    ('A4', Decimal('440.00')),
    ('A#4/Bb4 ', Decimal('466.16')),
    ('B4', Decimal('493.88')),
    ('C5', Decimal('523.25')),
    ('C#5/Db5 ', Decimal('554.37')),
    ('D5', Decimal('587.33')),
    ('D#5/Eb5 ', Decimal('622.25')),
    ('E5', Decimal('659.25')),
    ('F5', Decimal('698.46')),
    ('F#5/Gb5 ', Decimal('739.99')),
    ('G5', Decimal('783.99')),
    ('G#5/Ab5 ', Decimal('830.61')),
    ('A5', Decimal('880.00')),
    ('A#5/Bb5 ', Decimal('932.33')),
    ('B5', Decimal('987.77')),
    ('C6', Decimal('1046.50')),
    ('C#6/Db6 ', Decimal('1108.73')),
    ('D6', Decimal('1174.66')),
    ('D#6/Eb6 ', Decimal('1244.51')),
    ('E6', Decimal('1318.51')),
    ('F6', Decimal('1396.91')),
    ('F#6/Gb6 ', Decimal('1479.98')),
    ('G6', Decimal('1567.98')),
    ('G#6/Ab6 ', Decimal('1661.22')),
    ('A6', Decimal('1760.00')),
    ('A#6/Bb6 ', Decimal('1864.66')),
    ('B6', Decimal('1975.53')),
    ('C7', Decimal('2093.00')),
    ('C#7/Db7 ', Decimal('2217.46')),
    ('D7', Decimal('2349.32')),
    ('D#7/Eb7 ', Decimal('2489.02')),
    ('E7', Decimal('2637.02')),
    ('F7', Decimal('2793.83')),
    ('F#7/Gb7 ', Decimal('2959.96')),
    ('G7', Decimal('3135.96')),
    ('G#7/Ab7 ', Decimal('3322.44')),
    ('A7', Decimal('3520.00')),
    ('A#7/Bb7 ', Decimal('3729.31')),
    ('B7', Decimal('3951.07')),
    ('C8', Decimal('4186.01')),
    ('C#8/Db8 ', Decimal('4434.92')),
    ('D8', Decimal('4698.63')),
    ('D#8/Eb8 ', Decimal('4978.03')),
    ('E8', Decimal('5274.04')),
    ('F8', Decimal('5587.65')),
    ('F#8/Gb8 ', Decimal('5919.91')),
    ('G8', Decimal('6271.93')),
    ('G#8/Ab8 ', Decimal('6644.88')),
    ('A8', Decimal('7040.00')),
    ('A#8/Bb8 ', Decimal('7458.62')),
    ('B8', Decimal('7902.13')),
))


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
        note_names = FUNDAMENTAL_PITCH_TO_NOTES_MAP[self.hz]
        return [Note(n) for n in note_names]

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

        for hz in FUNDAMENTAL_PITCH_TO_NOTES_MAP:
            if hz > self.hz:
                increased += 1
            if increased == semitones:
                break

        return Pitch(hz)


NOTE_TO_FUNDAMENTAL_PITCH_MAP = OrderedDict((
    ('B♯', Decimal('16.35')),
    ('C', Decimal('16.35')),
    ('C♯', Decimal('17.32')),
    ('D♭', Decimal('17.32')),
    ('D', Decimal('18.35')),
    ('D♯', Decimal('19.45')),
    ('E♭', Decimal('19.45')),
    ('E', Decimal('20.60')),
    ('F♭', Decimal('20.60')),
    ('E♯', Decimal('21.83')),
    ('F', Decimal('21.83')),
    ('F♯', Decimal('23.12')),
    ('G♭', Decimal('23.12')),
    ('G', Decimal('24.50')),
    ('G♯', Decimal('25.96')),
    ('A♭', Decimal('25.96')),
    ('A', Decimal('27.50')),
    ('A♯', Decimal('29.14')),
    ('B♭', Decimal('29.14')),
    ('B', Decimal('30.87')),
    ('C♭', Decimal('30.87')),
    ('B♯', Decimal('32.70')),
    ('C', Decimal('32.70')),
))

FUNDAMENTAL_PITCH_TO_NOTES_MAP = defaultdict(list)
for _note, _pitch in NOTE_TO_FUNDAMENTAL_PITCH_MAP.items():
    FUNDAMENTAL_PITCH_TO_NOTES_MAP[_pitch].append(_note)


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

        self.fundamental = Pitch(NOTE_TO_FUNDAMENTAL_PITCH_MAP[self.name])

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
        'maj': MAJOR_KEY_STEPS,
        'min': MINOR_KEY_STEPS,
    }

    ####################################################################
    def __init__(self, name):
        root, quality = get_note_and_quality_from_music_element(name.strip())
        self.root_note = root
        self.quality = quality
        self.steps = self.STEPS_MAP[self.quality]
        self.notes = self._generate_notes()

    ####################################################################
    @classmethod
    def get_root_note_and_quality(cls, key_name):
        note, quality = get_note_and_quality_from_music_element(key_name)
        return note, quality

    ####################################################################
    def __str__(self):
        return f'Key of {self.root_note.name}'

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
