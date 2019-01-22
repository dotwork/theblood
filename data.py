import collections
from decimal import Decimal

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

PITCHES = collections.OrderedDict((
    ('B#0/C0', Decimal('16.35')),
    ('C#0/Db0', Decimal('17.32')),
    ('D0', Decimal('18.35')),
    ('D#0/Eb0', Decimal('19.45')),
    ('E0/Fb0', Decimal('20.60')),
    ('E#0/F0', Decimal('21.83')),
    ('F#0/Gb0', Decimal('23.12')),
    ('G0', Decimal('24.50')),
    ('G#0/Ab0', Decimal('25.96')),
    ('A0', Decimal('27.50')),
    ('A#0/Bb0', Decimal('29.14')),
    ('B0/Cb0', Decimal('30.87')),
    ('B#1/C1', Decimal('32.70')),
    ('C#1/Db1', Decimal('34.65')),
    ('D1', Decimal('36.71')),
    ('D#1/Eb1', Decimal('38.89')),
    ('E1/Fb1', Decimal('41.20')),
    ('E#1/F1', Decimal('43.65')),
    ('F#1/Gb1', Decimal('46.25')),
    ('G1', Decimal('49.00')),
    ('G#1/Ab1', Decimal('51.91')),
    ('A1', Decimal('55.00')),
    ('A#1/Bb1', Decimal('58.27')),
    ('B1/Cb1', Decimal('61.74')),
    ('C2', Decimal('65.41')),
    ('C#2/Db2', Decimal('69.30')),
    ('D2', Decimal('73.42')),
    ('D#2/Eb2', Decimal('77.78')),
    ('E2/Fb2', Decimal('82.41')),
    ('E#2/F2', Decimal('87.31')),
    ('F#2/Gb2', Decimal('92.50')),
    ('G2', Decimal('98.00')),
    ('G#2/Ab2', Decimal('103.83')),
    ('A2', Decimal('110.00')),
    ('A#2/Bb2', Decimal('116.54')),
    ('B2/Cb2', Decimal('123.47')),
    ('B#3/C3', Decimal('130.81')),
    ('C#3/Db3', Decimal('138.59')),
    ('D3', Decimal('146.83')),
    ('D#3/Eb3', Decimal('155.56')),
    ('E3/Fb3', Decimal('164.81')),
    ('E#3/F3', Decimal('174.61')),
    ('F#3/Gb3', Decimal('185.00')),
    ('G3', Decimal('196.00')),
    ('G#3/Ab3', Decimal('207.65')),
    ('A3', Decimal('220.00')),
    ('A#3/Bb3', Decimal('233.08')),
    ('B3/Cb3', Decimal('246.94')),
    ('B#4/C4', Decimal('261.63')),
    ('C#4/Db4', Decimal('277.18')),
    ('D4', Decimal('293.66')),
    ('D#4/Eb4', Decimal('311.13')),
    ('E4/Fb4', Decimal('329.63')),
    ('E#4/F4', Decimal('349.23')),
    ('F#4/Gb4', Decimal('369.99')),
    ('G4', Decimal('392.00')),
    ('G#4/Ab4', Decimal('415.30')),
    ('A4', Decimal('440.00')),
    ('A#4/Bb4', Decimal('466.16')),
    ('B4/Cb4', Decimal('493.88')),
    ('B#5/C5', Decimal('523.25')),
    ('C#5/Db5', Decimal('554.37')),
    ('D5', Decimal('587.33')),
    ('D#5/Eb5', Decimal('622.25')),
    ('E5/Fb5', Decimal('659.25')),
    ('E#5/F5', Decimal('698.46')),
    ('F#5/Gb5', Decimal('739.99')),
    ('G5', Decimal('783.99')),
    ('G#5/Ab5', Decimal('830.61')),
    ('A5', Decimal('880.00')),
    ('A#5/Bb5', Decimal('932.33')),
    ('B5/Cb5', Decimal('987.77')),
    ('B#6/C6', Decimal('1046.50')),
    ('C#6/Db6', Decimal('1108.73')),
    ('D6', Decimal('1174.66')),
    ('D#6/Eb6', Decimal('1244.51')),
    ('E6/Fb6', Decimal('1318.51')),
    ('E#6/F6', Decimal('1396.91')),
    ('F#6/Gb6', Decimal('1479.98')),
    ('G6', Decimal('1567.98')),
    ('G#6/Ab6', Decimal('1661.22')),
    ('A6', Decimal('1760.00')),
    ('A#6/Bb6', Decimal('1864.66')),
    ('B6/Cb6', Decimal('1975.53')),
    ('B#7/C7', Decimal('2093.00')),
    ('C#7/Db7', Decimal('2217.46')),
    ('D7', Decimal('2349.32')),
    ('D#7/Eb7', Decimal('2489.02')),
    ('E7/Fb7', Decimal('2637.02')),
    ('E#7/F7', Decimal('2793.83')),
    ('F#7/Gb7', Decimal('2959.96')),
    ('G7', Decimal('3135.96')),
    ('G#7/Ab7', Decimal('3322.44')),
    ('A7', Decimal('3520.00')),
    ('A#7/Bb7', Decimal('3729.31')),
    ('B7/Cb7', Decimal('3951.07')),
    ('B#8/C8', Decimal('4186.01')),
    ('C#8/Db8', Decimal('4434.92')),
    ('D8', Decimal('4698.63')),
    ('D#8/Eb8', Decimal('4978.03')),
    ('E8/Fb8', Decimal('5274.04')),
    ('E#8/F8', Decimal('5587.65')),
    ('F#8/Gb8', Decimal('5919.91')),
    ('G8', Decimal('6271.93')),
    ('G#8/Ab8', Decimal('6644.88')),
    ('A8', Decimal('7040.00')),
    ('A#8/Bb8', Decimal('7458.62')),
    ('B8/Cb8', Decimal('7902.13')),
))
