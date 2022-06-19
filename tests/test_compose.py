from unittest import TestCase

from composer.compose import ComposedNote
from the_blood.models import *


class TestComposedNote(TestCase):

    def test_from_pitch(self):
        pitch440 = Pitch(440)
        octave4 = Octave(4)
        a4 = ComposedNote('A', octave4)

        composed_note = ComposedNote.from_pitch(pitch440, available_notes=Key('A').notes)

        self.assertEqual(octave4, composed_note.octave)
        self.assertEqual(A, composed_note.note)
        self.assertEqual(pitch440, composed_note.pitch)
        self.assertEqual(a4, composed_note)
