# https://music.stackexchange.com/questions/73110/what-are-the-interval-patterns-for-the-modes
# IONIAN_INTERVALS = (W, W, H, W, W, W, H)
# DORIAN_INTERVALS = (W, H, W, W, W, H, W)
# PHRYGIAN_INTERVALS = (H, W, W, W, H, W, W)
# LYDIAN_INTERVALS = (W, W, W, H, W, W, H)
# MIXOLYDIAN_INTERVALS = (W, W, H, W, W, H, W)
# AEOLIAN_INTERVALS = (W, H, W, W, H, W, W)
# LOCRIAN_INTERVALS = (H, W, W, H, W, W, W)
#
# SCALE_TO_INTERVALS_MAP = {
#     MAJOR_SCALE_NAME: MAJOR_INTERVALS,
#     MINOR_SCALE_NAME: MINOR_INTERVALS,
    # IONIAN_SCALE_NAME: IONIAN_INTERVALS,
    # DORIAN_SCALE_NAME: DORIAN_INTERVALS,
    # PHRYGIAN_SCALE_NAME: PHRYGIAN_INTERVALS,
    # LYDIAN_SCALE_NAME: LYDIAN_INTERVALS,
    # MIXOLYDIAN_SCALE_NAME: MIXOLYDIAN_INTERVALS,
    # AEOLIAN_SCALE_NAME: AEOLIAN_INTERVALS,
    # LOCRIAN_SCALE_NAME: LOCRIAN_INTERVALS,
# }
#
# KEY_INTERVALS_TO_NAME_MAP = {
#     MAJOR_INTERVALS: MAJOR_SCALE_NAME,
#     MINOR_INTERVALS: MINOR_SCALE_NAME,
# }
#
# MODAL_INTERVALS_TO_NAME_MAP = {
#     IONIAN_INTERVALS: IONIAN_SCALE_NAME,
#     DORIAN_INTERVALS: DORIAN_SCALE_NAME,
#     PHRYGIAN_INTERVALS: PHRYGIAN_SCALE_NAME,
#     LYDIAN_INTERVALS: LYDIAN_SCALE_NAME,
#     MIXOLYDIAN_INTERVALS: MIXOLYDIAN_SCALE_NAME,
#     AEOLIAN_INTERVALS: AEOLIAN_SCALE_NAME,
#     LOCRIAN_INTERVALS: LOCRIAN_SCALE_NAME,
# }
#
#
# finger_positions = ('tonic', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
#                     'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth', 'thirteenth',
#                     'fourteenth', 'fifteenth', 'sixteenth')


# IonianScale = ScalePattern(IONIAN_SCALE_NAME)
# DorianScale = ScalePattern(DORIAN_SCALE_NAME)
# PhrygianScale = ScalePattern(PHRYGIAN_SCALE_NAME)
# LydianScale = ScalePattern(LYDIAN_SCALE_NAME)
# MixolydianScale = ScalePattern(MIXOLYDIAN_SCALE_NAME)
# AeolianScale = ScalePattern(AEOLIAN_SCALE_NAME)
# LocrianScale = ScalePattern(LOCRIAN_SCALE_NAME)
#
# MODAL_SCALES = (IonianScale, DorianScale, PhrygianScale,
#                 LydianScale, MixolydianScale, AeolianScale, LocrianScale)


#
#
# ########################################################################
# class Chord:
#
#     ####################################################################
#     def __init__(self, name, key=None):
#         root, quality = _get_note_and_quality_from_music_element(name.strip())
#         self.root_note = root
#         self.quality = quality
#         self.is_minor = MAJOR_ABBREVIATION not in quality and MINOR in quality
#         self.is_major = not self.is_minor
#         self.name = '{root}{quality}'.format(root=root, quality=quality)
#         self.key_specified = key is not None
#         self.key = Key(key) if key else self.default_key
#         self.notes = self._generate_notes()
#
#     ####################################################################
#     @property
#     def default_key(self):
#         quality = MINOR if self.is_minor else MAJOR
#         name = '{root}{quality}'.format(root=self.root_note.name, quality=quality)
#         key = Key(name)
#         return key
#
#     ####################################################################
#     @property
#     def triad(self):
#         return (self.key.scale.first,
#                 self.key.scale.third,
#                 self.key.scale.fifth)
#
#     ####################################################################
#     def _generate_notes(self):
#         notes = list(self.triad)
#         if self.seventh:
#             notes.append(self.seventh)
#         return tuple(notes)
#
#     ####################################################################
#     @property
#     def seventh(self):
#         scale = self.key.scale
#         if self.quality == SEVENTH or self.quality == MINOR + SEVENTH:
#             return scale.minor_seventh
#         elif self.quality == MAJOR_ABBREVIATION + SEVENTH:
#             return scale.major_seventh
#         return None
#
#
# ########################################################################
# class Transpose:
#
#     ####################################################################
#     def __init__(self, *notes, quality_to_use=None):
#         self._raw_notes = tuple(Note(n) for n in notes)
#         self.quality_to_use = quality_to_use
#         for note in self._raw_notes:
#             if note.quality and note.quality in QUALITIES:
#                 self.quality_to_use = note.quality
#                 break
#
#         self._transposed_notes = []
#         self.transpose_up = False
#         self.transpose_down = False
#         self._steps = ()
#
#     ####################################################################
#     def _semitones(self):
#         semitones = sum(self._steps)
#         return int(semitones)
#
#     ####################################################################
#     def steps(self, *steps):
#         self._steps = tuple(steps)
#         return self._transpose()
#
#     ####################################################################
#     @property
#     def up(self):
#         self.transpose_up = True
#         self.transpose_down = False
#         return self
#
#     ####################################################################
#     @property
#     def down(self):
#         self.transpose_down = True
#         self.transpose_up = False
#         return self
#
#     ####################################################################
#     @property
#     def half_step(self):
#         self._steps = (H, )
#         return self._transpose()
#
#     ####################################################################
#     @property
#     def whole_step(self):
#         self._steps = (W, )
#         return self._transpose()
#
#     ####################################################################
#     @property
#     def third(self):
#         self._steps = (W, W)
#         return self._transpose()
#
#     ####################################################################
#     @property
#     def minor_third(self):
#         self._steps = (W, H)
#         return self._transpose()
#
#     ####################################################################
#     @property
#     def fifth(self):
#         self._steps = (W, W, W, H)
#         return self._transpose()
#
#     ####################################################################
#     def octave(self):
#         self._steps = (W, W, W, W, W, W)
#         return self._transpose()
#
#     ####################################################################
#     def _transpose(self):
#         transposed = []
#         for note in self._raw_notes:
#             if self.transpose_up:
#                 transposed_pitch = note.fundamental.increase(self._semitones())
#             else:
#                 transposed_pitch = note.fundamental.decrease(self._semitones())
#             matches = PitchMap[transposed_pitch]
#             best_match = None
#             for match in matches:
#                 octave = int(match[-1])
#                 matching_note = Note(match[:-1], octave=octave)
#                 if matching_note.is_natural:
#                     best_match = matching_note
#                     break
#
#                 if self.quality_to_use and matching_note.quality == self.quality_to_use:
#                     best_match = matching_note
#                 elif best_match:
#                     if not (best_match.is_standard_flat or best_match.is_standard_sharp):
#                         best_match = matching_note
#                 elif not best_match:
#                     best_match = matching_note
#             error = 'Failed to find note with pitch {transposed_pitch}. Tried {matches}'
#             assert best_match is not None, error.format(transposed_pitch=transposed_pitch, matches=matches)
#             transposed.append(best_match)
#         self._transposed_notes = transposed
#         return self._transposed_notes
