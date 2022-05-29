from unittest import TestCase

from composer.compose import ComposedNote
from composer.midi import NOTE_CHANNEL_1_ON, MidiNote, get_duration_seconds


class TestMidi(TestCase):

    def test_send_notes_on_or_off(self):
        expected_midi_number = 52
        velocity = 100

        e3 = ComposedNote('E', octave=3)
        midi_note = MidiNote(e3, velocity, duration=1)
        self.assertEqual(e3, midi_note.note)
        self.assertEqual(expected_midi_number, midi_note.number)

        send_note_on = bytes([NOTE_CHANNEL_1_ON, midi_note.number, velocity])
        self.assertEqual(bytes([0x90, expected_midi_number, 100]), send_note_on)

        send_note_off = bytes([NOTE_CHANNEL_1_ON, midi_note.number, 0])
        self.assertEqual(bytes([0x90, expected_midi_number, 0]), send_note_off)

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
