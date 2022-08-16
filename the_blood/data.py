IN_TUNE = "In Tune"
MIDDLE_OCTAVE = 4

NATURAL_NOTES = ('A', 'B', 'C', 'D', 'E', 'F', 'G')

NATURAL = ''
FLAT = 'b'
SHARP = '#'
DOUBLE_FLAT = 'bb'
DOUBLE_SHARP = '##'
MAJOR = ''
MAJOR_ABBREVIATION = 'maj'
MINOR = 'm'
SEVENTH = '7'
NINTH = '9'
ELEVENTH = '11'

SHARPS_AND_FLATS = {
    '##': DOUBLE_SHARP,
    'double sharp': DOUBLE_SHARP,

    'bb': DOUBLE_FLAT,
    'double flat': DOUBLE_FLAT,

    '#': SHARP,
    'sharp': SHARP,

    'b': FLAT,
    'flat': FLAT,
}


QUALITIES = SHARPS_AND_FLATS.copy()
QUALITIES.update({
    'natural': 'natural',

    '': MAJOR,
    'major': MAJOR,
    'maj': MAJOR,

    'minor': MINOR,
    'min': MINOR,
    'm': MINOR,

    '7': SEVENTH,
    'maj7': MAJOR_ABBREVIATION + SEVENTH,
    'minor7': MINOR + SEVENTH,
    'min7': MINOR + SEVENTH,
    'm7': MINOR + SEVENTH,

    '9': NINTH,
    'minor9': MINOR + NINTH,
    'min9': MINOR + NINTH,
    'm9': MINOR + NINTH,

    '11': ELEVENTH,
    'minor11': MINOR + ELEVENTH,
    'min11': MINOR + ELEVENTH,
    'm11': MINOR + ELEVENTH,
})


def __get_pitches():
    import collections
    return collections.OrderedDict((
        ('B#0/C0/Dbb0', 16.35),
        ('C#0/Db0', 17.32),
        ('C##0/D0/Ebb0', 18.35),
        ('D#0/Eb0/Fbb0', 19.45),
        ('D##0/E0/Fb0', 20.60),
        ('E#0/F0/Gbb0', 21.83),
        ('E##0/F#0/Gb0', 23.12),
        ('F##0/G0/Abb0', 24.50),
        ('G#0/Ab0', 25.96),
        ('G##0/A0/Bbb0', 27.50),
        ('A#0/Bb0/Cbb0', 29.14),
        ('A##0/B0/Cb0', 30.87),
        ('B#1/C1/Dbb1', 32.70),
        ('C#1/Db1', 34.65),
        ('C##1/D1/Ebb1', 36.71),
        ('D#1/Eb1/Fbb1', 38.89),
        ('D##1/E1/Fb1', 41.20),
        ('E#1/F1/Gbb1', 43.65),
        ('E##1/F#1/Gb1', 46.25),
        ('F##1/G1/Abb1', 49.00),
        ('G#1/Ab1', 51.91),
        ('G##1/A1/Bbb1', 55.00),
        ('A#1/Bb1/Cbb1', 58.27),
        ('A##1/B1/Cb1', 61.74),
        ('B#2/C2/Dbb1', 65.41),
        ('C#2/Db2', 69.30),
        ('C##2/D2/Ebb2', 73.42),
        ('D#2/Eb2/Fbb2', 77.78),
        ('D##2/E2/Fb2', 82.41),
        ('E#2/F2/Gbb2', 87.31),
        ('E##2/F#2/Gb2', 92.50),
        ('F##2/G2/Abb2', 98.00),
        ('G#2/Ab2', 103.83),
        ('G##2/A2/Bbb2', 110.00),
        ('A#2/Bb2/Cbb2', 116.54),
        ('A##2/B2/Cb2', 123.47),
        ('B#3/C3/Dbb3', 130.81),
        ('C#3/Db3', 138.59),
        ('C##3/D3/Ebb3', 146.83),
        ('D#3/Eb3/Fbb3', 155.56),
        ('D##3/E3/Fb3', 164.81),
        ('E#3/F3/Gbb3', 174.61),
        ('E##3/F#3/Gb3', 185.00),
        ('F##3/G3/Abb3', 196.00),
        ('G#3/Ab3', 207.65),
        ('G##3/A3/Bbb3', 220.00),
        ('A#3/Bb3/Cbb3', 233.08),
        ('A##3/B3/Cb3', 246.94),
        ('B#4/C4/Dbb4', 261.63),
        ('C#4/Db4', 277.18),
        ('C##4/D4/Ebb4', 293.66),
        ('D#4/Eb4/Fbb4', 311.13),
        ('D##4/E4/Fb4', 329.63),
        ('E#4/F4/Gbb4', 349.23),
        ('E##4/F#4/Gb4', 369.99),
        ('F##4/G4/Abb4', 392.00),
        ('G#4/Ab4', 415.30),
        ('G##4/A4/Bbb4', 440.00),
        ('A#4/Bb4/Cbb4', 466.16),
        ('A##4/B4/Cb4', 493.88),
        ('B#5/C5/Dbb5', 523.25),
        ('C#5/Db5', 554.37),
        ('C##5/D5/Ebb5', 587.33),
        ('D#5/Eb5/Fbb5', 622.25),
        ('D##5/E5/Fb5', 659.25),
        ('E#5/F5/Gbb5', 698.46),
        ('E##5/F#5/Gb5', 739.99),
        ('F##5/G5/Abb5', 783.99),
        ('G#5/Ab5', 830.61),
        ('G##5/A5/Bbb5', 880.00),
        ('A#5/Bb5/Cbb5', 932.33),
        ('A##5/B5/Cb5', 987.77),
        ('B#6/C6/Dbb6', 1046.50),
        ('C#6/Db6', 1108.73),
        ('C##6/D6/Ebb6', 1174.66),
        ('D#6/Eb6/Fbb6', 1244.51),
        ('D##6/E6/Fb6', 1318.51),
        ('E#6/F6/Gbb6', 1396.91),
        ('E##6/F#6/Gb6', 1479.98),
        ('F##6/G6/Abb6', 1567.98),
        ('G#6/Ab6', 1661.22),
        ('G##6/A6/Bbb6', 1760.00),
        ('A#6/Bb6/Cbb6', 1864.66),
        ('A##6/B6/Cb6', 1975.53),
        ('B#7/C7/Dbb7', 2093.00),
        ('C#7/Db7', 2217.46),
        ('C##7/D7/Ebb7', 2349.32),
        ('D#7/Eb7/Fbb7', 2489.02),
        ('D##7/E7/Fb7', 2637.02),
        ('E#7/F7/Gbb7', 2793.83),
        ('E##7/F#7/Gb7', 2959.96),
        ('F##7/G7/Abb7', 3135.96),
        ('G#7/Ab7', 3322.44),
        ('G##7/A7/Bbb7', 3520.00),
        ('A#7/Bb7/Cbb7', 3729.31),
        ('A##7/B7/Cb7', 3951.07),
        ('B#8/C8/Dbb8', 4186.01),
        ('C#8/Db8', 4434.92),
        ('C##8/D8/Ebb8', 4698.63),
        ('D#8/Eb8/Fbb8', 4978.03),
        ('D##8/E8/Fb8', 5274.04),
        ('E#8/F8/Gbb8', 5587.65),
        ('E##8/F#8/Gb8', 5919.91),
        ('F##8/G8/Abb8', 6271.93),
        ('G#8/Ab8', 6644.88),
        ('G##8/A8/Bbb8', 7040.00),
        ('A#8/Bb8/Cbb8', 7458.62),
        ('A##8/B8/Cb8', 7902.13),
    ))


PITCHES = __get_pitches()


SCALE_NAMES = {
    "major": MAJOR,
    "maj": MAJOR,
    "": MAJOR,

    "minor": MINOR,
    "min": MINOR,
    "m": MINOR
}

MAJOR_SCALE_NAME = 'Major'
MINOR_SCALE_NAME = 'Minor'

IONIAN_SCALE_NAME = 'Ionian'
DORIAN_SCALE_NAME = 'Dorian'
PHRYGIAN_SCALE_NAME = 'Phrygian'
LYDIAN_SCALE_NAME = 'Lydian'
MIXOLYDIAN_SCALE_NAME = 'Mixolydian'
AEOLIAN_SCALE_NAME = 'Aeolian'
LOCRIAN_SCALE_NAME = 'Locrian'

MODE_NAMES = (IONIAN_SCALE_NAME, DORIAN_SCALE_NAME, PHRYGIAN_SCALE_NAME,
              LYDIAN_SCALE_NAME, MIXOLYDIAN_SCALE_NAME, AEOLIAN_SCALE_NAME,
              LOCRIAN_SCALE_NAME)
