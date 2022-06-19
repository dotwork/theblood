from the_blood.models import *


class ComposedNote(Note):

    def __init__(self, note, octave):
        self.note = Note(note)
        self.octave = Octave(octave)
        super().__init__(note=self.note)
        self.pitch = Pitch(PitchMap[self.note, self.octave])

    def __str__(self):
        return f'{self.name}{self.octave}'

    def __repr__(self):
        return f'ComposedNote("{self.note}", {self.octave})'

    @classmethod
    def from_pitch(cls, pitch, available_notes):
        note = super().from_pitch(pitch, available_notes)
        for _note, octave in PitchMap[pitch]:
            if _note == note:
                return ComposedNote(note, octave)
        raise UnavailableNoteError(f'Failed to compose note for pitch {pitch} with available notes {available_notes}.')
