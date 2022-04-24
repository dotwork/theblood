from unittest import TestCase
from composer.midi import NOTE_CHANNEL_1_ON, MidiNote, get_duration_seconds
from the_blood.models import Note


class TestMidi(TestCase):

    def test_send_notes_on_or_off(self):
        expected_midi_number = 40
        velocity = 100

        e3 = Note('E', octave=3)
        midi_note = MidiNote(e3)
        self.assertEqual(e3, midi_note.note)
        self.assertEqual(expected_midi_number, midi_note.number)

        note_40_on_velocity_100 = [NOTE_CHANNEL_1_ON, midi_note.number, velocity]
        result = bytes(note_40_on_velocity_100)
        self.assertEqual(bytes([0x90, expected_midi_number, 100]), result)

        note_40_on_velocity_0 = [NOTE_CHANNEL_1_ON, midi_note.number, 0]
        result = bytes(note_40_on_velocity_0)
        self.assertEqual(bytes([0x90, expected_midi_number, 0]), result)

    def test_get_duration_seconds(self):
        bpm = 120

        note_value = 4
        self.assertEqual(4, note_value)
        duration_in_seconds = get_duration_seconds(note_value, bpm)
        self.assertEqual(.5, duration_in_seconds)

        note_value = 8
        self.assertEqual(8, note_value)
        duration_in_seconds = get_duration_seconds(note_value, bpm)
        self.assertEqual(.25, duration_in_seconds)

        note_value = 16
        self.assertEqual(16, note_value)
        duration_in_seconds = get_duration_seconds(note_value, bpm)
        self.assertEqual(.125, duration_in_seconds)

        note_value = 32
        self.assertEqual(32, note_value)
        duration_in_seconds = get_duration_seconds(note_value, bpm)
        self.assertEqual(.0625, duration_in_seconds)

        note_value = 2
        self.assertEqual(2, note_value)
        duration_in_seconds = get_duration_seconds(note_value, bpm)
        self.assertEqual(1, duration_in_seconds)

        note_value = 1
        self.assertEqual(1, note_value)
        duration_in_seconds = get_duration_seconds(note_value, bpm)
        self.assertEqual(2, duration_in_seconds)
