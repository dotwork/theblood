from the_blood.models import *


class ComposedNote(Note):

    def __init__(self, note, octave):
        super().__init__(note=Note(note))
        self.octave = Octave(octave)
        pitch_name = f'{self.name}{self.octave}'
        self.pitch = Pitch(PitchMap[pitch_name])

    def __str__(self):
        return f'{self.name}{self.octave}'


def note(_note, octave):
    return ComposedNote(Note(_note), Octave(octave))
