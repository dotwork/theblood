from the_blood.models import *


class ComposedNote(Note):

    def __init__(self, note, octave):
        self.note = Note(note)
        self.octave = Octave(octave)
        super().__init__(note=self.note)
        self.pitch = Pitch(PitchMap((self.note, self.octave)))

    def __str__(self):
        return '{name}{octave}'.format(name=self.name, octave=self.octave)

    def __repr__(self):
        return 'ComposedNote("{name}", {octave})'.format(name=self.name, octave=self.octave)

    @classmethod
    def from_pitch(cls, pitch, available_notes):
        note = super().from_pitch(pitch, available_notes)
        for _note, octave in PitchMap(pitch):
            if _note == note:
                return ComposedNote(note, octave)
        error = 'Failed to compose note for pitch {pitch} with available notes {available_notes}.'
        raise UnavailableNoteError(error.format(pitch=pitch, available_notes=available_notes))
