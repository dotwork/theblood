from the_blood.models import *


class ComposedNote(Note):

    def __init__(self, note, octave):
        self.__note = Note(note)
        self.octave = Octave(octave)
        super().__init__(note=self.__note)
        self.pitch = Pitch(PitchMap[self.__note, self.octave])

    def __str__(self):
        return f'{self.name}{self.octave}'

    def __repr__(self):
        return f'ComposedNote("{self.__note}", {self.octave})'

    @classmethod
    def from_pitch(cls, pitch, key):
        note = super().from_pitch(pitch, key)
        return ComposedNote(note, pitch.octave)
