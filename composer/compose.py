from the_blood.models import *


class ComposedNote(Note):

    def __init__(self, note, octave):
        super().__init__(note=Note(note))
        self.octave = Octave(octave)
        pitch_name = f'{self.name}{self.octave}'
        self.pitch = Pitch(PitchMap[pitch_name])

    def __str__(self):
        return f'{self.name}{self.octave}'

    @classmethod
    def from_pitch(cls, pitch, key):
        if not isinstance(key, Key):
            key = Key(key)
        for note in key.notes:
            name, quality = note.natural_name, note.quality
            for matching_name, matching_quality, octave in pitch.note_info:
                if matching_name == name and matching_quality == quality:
                    return ComposedNote(note, octave=octave)
        raise Exception(f'Could not find note for pitch {pitch} in key {key}. '
                        f'Note options for pitch are {", ".join(key.note_names)}')

