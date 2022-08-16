MIDI_TO_PITCH_MAP = {
    127: 12543.85,  # G9
    126: 11839.82,  # F#9/Gb9
    125: 11175.30,  # F9
    124: 10548.08,  # E9
    123: 9956.06,  # D#9/Eb9
    122: 9397.27,  # D9
    121: 8869.84,  # C#9/Db9
    120: 8372.02,  # C9
    119: 7902.13,  # B8
    118: 7458.62,  # A#8/Bb8
    117: 7040.00,  # A8
    116: 6644.88,  # G#8/Ab8
    115: 6271.93,  # G8
    114: 5919.91,  # F#8/Gb8
    113: 5587.65,  # F8
    112: 5274.04,  # E8
    111: 4978.03,  # D#8/Eb8
    110: 4698.64,  # D8
    109: 4434.92,  # C#8/Db8
    108: 4186.01,  # C8
    107: 3951.07,  # B7
    106: 3729.31,  # A#7/Bb7
    105: 3520.00,  # A7
    104: 3322.44,  # G#7/Ab7
    103: 3135.96,  # G7
    102: 2959.96,  # F#7/Gb7
    101: 2793.83,  # F7
    100: 2637.02,  # E7
    99: 2489.02,  # D#7/Eb7
    98: 2349.32,  # D7
    97: 2217.46,  # C#7/Db7
    96: 2093.00,  # C7
    95: 1975.53,  # B6
    94: 1864.66,  # A#6/Bb6
    93: 1760.00,  # A6
    92: 1661.22,  # G#6/Ab6
    91: 1567.98,  # G6
    90: 1479.98,  # F#6/Gb6
    89: 1396.91,  # F6
    88: 1318.51,  # E6
    87: 1244.51,  # D#6/Eb6
    86: 1174.66,  # D6
    85: 1108.73,  # C#6/Db6
    84: 1046.50,  # C6
    83: 987.77,  # B5
    82: 932.33,  # A#5/Bb5
    81: 880.00,  # A5
    80: 830.61,  # G#5/Ab5
    79: 783.99,  # G5
    78: 739.99,  # F#5/Gb5
    77: 698.46,  # F5
    76: 659.26,  # E5
    75: 622.25,  # D#5/Eb5
    74: 587.33,  # D5
    73: 554.37,  # C#5/Db5
    72: 523.25,  # C5
    71: 493.88,  # B4
    70: 466.16,  # A#4/Bb4
    69: 440.00,  # A4
    68: 415.30,  # G#4/Ab4
    67: 392.00,  # G4
    66: 369.99,  # F#4/Gb4
    65: 349.23,  # F4
    64: 329.63,  # E4
    63: 311.13,  # D#4/Eb4
    62: 293.66,  # D4
    61: 277.18,  # C#4/Db4
    60: 261.63,  # C4
    59: 246.94,  # B3
    58: 233.08,  # A#3/Bb3
    57: 220.00,  # A3
    56: 207.65,  # G#3/Ab3
    55: 196.00,  # G3
    54: 185.00,  # F#3/Gb3
    53: 174.61,  # F3
    52: 164.81,  # E3
    51: 155.56,  # D#3/Eb3
    50: 146.83,  # D3
    49: 138.59,  # C#3/Db3
    48: 130.81,  # C3
    47: 123.47,  # B2
    46: 116.54,  # A#2/Bb2
    45: 110.00,  # A2
    44: 103.83,  # G#2/Ab2
    43: 98.00,  # G2
    42: 92.50,  # F#2/Gb2
    41: 87.31,  # F2
    40: 82.41,  # E2
    39: 77.78,  # D#2/Eb2
    38: 73.42,  # D2
    37: 69.30,  # C#2/Db2
    36: 65.41,  # C2
    35: 61.74,  # B11
    34: 58.27,  # A#1/Bb1
    33: 55.00,  # A11
    32: 51.91,  # G#1/Ab1
    31: 49.00,  # G11
    30: 46.25,  # F#1/Gb1
    29: 43.65,  # F11
    28: 41.20,  # E11
    27: 38.89,  # D#1/Eb1
    26: 36.71,  # D11
    25: 34.65,  # C#1/Db1
    24: 32.70,  # C11
    23: 30.87,  # B02
    22: 29.14,  # A#0/Bb0
    21: 27.50,  # A02
    20: 25.96,
    19: 24.50,
    18: 23.12,
    17: 21.83,
    16: 20.60,
    15: 19.45,
    14: 18.35,
    13: 17.32,
    12: 16.35,
    11: 15.43,
    10: 14.57,
    9: 13.75,
    8: 12.98,
    7: 12.25,
    6: 11.56,
    5: 10.91,
    4: 10.30,
    3: 9.72,
    2: 9.18,
    1: 8.66,
    0: 8.18,
}

PITCH_TO_MIDI_MAP = {
    12543.85: 127,  # G9
    11839.82: 126,  # F#9/Gb9
    11175.30: 125,  # F9
    10548.08: 124,  # E9
    9956.06: 123,  # D#9/Eb9
    9397.27: 122,  # D9
    8869.84: 121,  # C#9/Db9
    8372.02: 120,  # C9
    7902.13: 119,  # B8
    7458.62: 118,  # A#8/Bb8
    7040.00: 117,  # A8
    6644.88: 116,  # G#8/Ab8
    6271.93: 115,  # G8
    5919.91: 114,  # F#8/Gb8
    5587.65: 113,  # F8
    5274.04: 112,  # E8
    4978.03: 111,  # D#8/Eb8
    4698.64: 110,  # D8
    4434.92: 109,  # C#8/Db8
    4186.01: 108,  # C8
    3951.07: 107,  # B7
    3729.31: 106,  # A#7/Bb7
    3520.00: 105,  # A7
    3322.44: 104,  # G#7/Ab7
    3135.96: 103,  # G7
    2959.96: 102,  # F#7/Gb7
    2793.83: 101,  # F7
    2637.02: 100,  # E7
    2489.02: 99,  # D#7/Eb7
    2349.32: 98,  # D7
    2217.46: 97,  # C#7/Db7
    2093.00: 96,  # C7
    1975.53: 95,  # B6
    1864.66: 94,  # A#6/Bb6
    1760.00: 93,  # A6
    1661.22: 92,  # G#6/Ab6
    1567.98: 91,  # G6
    1479.98: 90,  # F#6/Gb6
    1396.91: 89,  # F6
    1318.51: 88,  # E6
    1244.51: 87,  # D#6/Eb6
    1174.66: 86,  # D6
    1108.73: 85,  # C#6/Db6
    1046.50: 84,  # C6
    987.77: 83,  # B5
    932.33: 82,  # A#5/Bb5
    880.00: 81,  # A5
    830.61: 80,  # G#5/Ab5
    783.99: 79,  # G5
    739.99: 78,  # F#5/Gb5
    698.46: 77,  # F5
    659.26: 76,  # E5
    622.25: 75,  # D#5/Eb5
    587.33: 74,  # D5
    554.37: 73,  # C#5/Db5
    523.25: 72,  # C5
    493.88: 71,  # B4
    466.16: 70,  # A#4/Bb4
    440.00: 69,  # A4
    415.30: 68,  # G#4/Ab4
    392.00: 67,  # G4
    369.99: 66,  # F#4/Gb4
    349.23: 65,  # F4
    329.63: 64,  # E4
    311.13: 63,  # D#4/Eb4
    293.66: 62,  # D4
    277.18: 61,  # C#4/Db4
    261.63: 60,  # C4
    246.94: 59,  # B3
    233.08: 58,  # A#3/Bb3
    220.00: 57,  # A3
    207.65: 56,  # G#3/Ab3
    196.00: 55,  # G3
    185.00: 54,  # F#3/Gb3
    174.61: 53,  # F3
    164.81: 52,  # E3
    155.56: 51,  # D#3/Eb3
    146.83: 50,  # D3
    138.59: 49,  # C#3/Db3
    130.81: 48,  # C3
    123.47: 47,  # B2
    116.54: 46,  # A#2/Bb2
    110.00: 45,  # A2
    103.83: 44,  # G#2/Ab2
    98.00: 43,  # G2
    92.50: 42,  # F#2/Gb2
    87.31: 41,  # F2
    82.41: 40,  # E2
    77.78: 39,  # D#2/Eb2
    73.42: 38,  # D2
    69.30: 37,  # C#2/Db2
    65.41: 36,  # C2
    61.74: 35,  # B11
    58.27: 34,  # A#1/Bb1
    55.00: 33,  # A11
    51.91: 32,  # G#1/Ab1
    49.00: 31,  # G11
    46.25: 30,  # F#1/Gb1
    43.65: 29,  # F11
    41.20: 28,  # E11
    38.89: 27,  # D#1/Eb1
    36.71: 26,  # D11
    34.65: 25,  # C#1/Db1
    32.70: 24,  # C11
    30.87: 23,  # B02
    29.14: 22,  # A#0/Bb0
    27.50: 21,  # A02
    25.96: 20,
    24.50: 19,
    23.12: 18,
    21.83: 17,
    20.60: 16,
    19.45: 15,
    18.35: 14,
    17.32: 13,
    16.35: 12,
    15.43: 11,
    14.57: 10,
    13.75: 9,
    12.98: 8,
    12.25: 7,
    11.56: 6,
    10.91: 5,
    10.30: 4,
    9.72: 3,
    9.18: 2,
    8.66: 1,
    8.18: 0,
}
