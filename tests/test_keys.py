from unittest import TestCase

from models import Key, A, B, C, D, E, F, G, C_sharp, D_sharp, E_sharp, F_sharp, G_sharp, A_sharp, B_sharp


########################################################################
class TestKey(TestCase):

    ####################################################################
    def test_init__with_str(self):
        self.assertEqual(C, Key('C').root_note)

    ####################################################################
    def test_init__with_note_obj(self):
        self.assertEqual(C, Key(C).root_note)

    ####################################################################
    def test_generate_notes(self):
        key_notes = Key('C').notes
        expected = [C, D, E, F, G, A, B]
        self.assertEqual(expected, key_notes)

        key_notes = Key('C#').notes
        expected = [C_sharp, D_sharp, E_sharp, F_sharp, G_sharp, A_sharp, B_sharp]
        self.assertEqual(expected, key_notes)

    ####################################################################
    def test_note_names(self):
        names = Key('C').note_names
        expected = ('C', 'D', 'E', 'F', 'G', 'A', 'B')
        self.assertEqual(expected, names)

        names = Key('C♯').note_names
        expected = ('C♯', 'D♯', 'E♯', 'F♯', 'G♯', 'A♯', 'B♯')
        self.assertEqual(expected, names)
