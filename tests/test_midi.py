import unittest
from unittest import TestCase

from adafruit_midi.note_on import NoteOn

from composer.compose import ComposedNote
from composer.midi import NOTE_CHANNEL_1_ON, MidiNote, get_duration_seconds
from composer.midi_data import MIDI_TO_PITCH_MAP


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

    def test_sequence(self):
        """
        https://www.cs.cmu.edu/~music/cmsip/readings/MIDI%20tutorial%20for%20programmers.html
                # t=0 : 0x90 - 0x40 - 0x40 (Start of E3 note, pitch = 64)
            t=0 : 0x90 - 0x43 - 0x40 (Start of G3 note, pitch= 67)
            t=1 : 0x80 - 0x43 - 0x00 (End of G3 note, pitch=67)
            t=1 : 0x90 - 0x45 - 0x40 (Start of A3 note, pitch=69)
            t=2 : 0x80 - 0x45 - 0x00 (End of A3 note, pitch=69)
                # t=2 : 0x80 - 0x40 - 0x00 (End of E3 note, pitch=64)
                # t=2 : 0x90 - 0x3C - 0x40 (Start of C3 note, pitch = 60)
            t=2 : 0x90 - 0x47 - 0x40 (Start of B3 note, pitch= 71)
            t=3 : 0x80 - 0x47 - 0x00 (End of B3 note, pitch= 71)
            t=3 : 0x90 - 0x48 - 0x40 (Start of C4 note, pitch= 72)
            t=4 : 0x80 - 0x48 - 0x00 (End of C4 note, pitch= 72)
                # t=4 : 0x80 - 0x3C - 0x40 (End of C3 note, pitch = 60)
        """
        velocity = 64

        # G
        midi_note = MidiNote(ComposedNote('G', octave=4), velocity, duration=1)
        self.assertEqual(67, midi_note.number)
        self.assertEqual(392.00, MIDI_TO_PITCH_MAP[67])
        self.assertEqual(392.00, midi_note.note.pitch)

        start = midi_note.get_start_command()
        self.assertEqual(velocity, start.velocity)
        self.assertEqual(midi_note.number, start.note)

        end = midi_note.get_end_command(force=True)
        self.assertEqual(64, end.velocity)
        self.assertEqual(midi_note.number, end.note)

        # A
        midi_note = MidiNote(ComposedNote('A', octave=4), velocity, duration=1)
        self.assertEqual(69, midi_note.number)
        self.assertEqual(440.00, MIDI_TO_PITCH_MAP[69])
        self.assertEqual(440.00, midi_note.note.pitch)

        start = midi_note.get_start_command()
        self.assertEqual(velocity, start.velocity)
        self.assertEqual(midi_note.number, start.note)

        end = midi_note.get_end_command(force=True)
        self.assertEqual(64, end.velocity)
        self.assertEqual(midi_note.number, end.note)

    @unittest.skip('started using adafruit instead')
    def test_sequence_bytestrings(self):
        """
        https://www.cs.cmu.edu/~music/cmsip/readings/MIDI%20tutorial%20for%20programmers.html
                # t=0 : 0x90 - 0x40 - 0x40 (Start of E3 note, pitch = 64)
            t=0 : 0x90 - 0x43 - 0x40 (Start of G3 note, pitch= 67)
            t=1 : 0x80 - 0x43 - 0x00 (End of G3 note, pitch=67)
            t=1 : 0x90 - 0x45 - 0x40 (Start of A3 note, pitch=69)
            t=2 : 0x80 - 0x45 - 0x00 (End of A3 note, pitch=69)
                # t=2 : 0x80 - 0x40 - 0x00 (End of E3 note, pitch=64)
                # t=2 : 0x90 - 0x3C - 0x40 (Start of C3 note, pitch = 60)
            t=2 : 0x90 - 0x47 - 0x40 (Start of B3 note, pitch= 71)
            t=3 : 0x80 - 0x47 - 0x00 (End of B3 note, pitch= 71)
            t=3 : 0x90 - 0x48 - 0x40 (Start of C4 note, pitch= 72)
            t=4 : 0x80 - 0x48 - 0x00 (End of C4 note, pitch= 72)
                # t=4 : 0x80 - 0x3C - 0x40 (End of C3 note, pitch = 60)
        """
        velocity = 64
        midi_notes = [
            MidiNote(ComposedNote('G', octave=4), velocity, duration=1),
            MidiNote(ComposedNote('A', octave=4), velocity, duration=1),
            MidiNote(ComposedNote('B', octave=4), velocity, duration=1),
            MidiNote(ComposedNote('C', octave=5), velocity, duration=1),
        ]
        commands = []
        for midi_note in midi_notes:
            commands.append(midi_note.get_start_command())
            commands.append(midi_note.get_end_command(force=True))

        self.assertEqual(('0x90', '0x43', '0x40'), tuple(hex(c) for c in commands[0]))
        self.assertEqual(('0x80', '0x43', '0x40'), tuple(hex(c) for c in commands[1]))
        self.assertEqual(('0x90', '0x45', '0x40'), tuple(hex(c) for c in commands[2]))
        self.assertEqual(('0x80', '0x45', '0x40'), tuple(hex(c) for c in commands[3]))
        self.assertEqual(('0x90', '0x47', '0x40'), tuple(hex(c) for c in commands[4]))
        self.assertEqual(('0x80', '0x47', '0x40'), tuple(hex(c) for c in commands[5]))
        self.assertEqual(('0x90', '0x48', '0x40'), tuple(hex(c) for c in commands[6]))
        self.assertEqual(('0x80', '0x48', '0x40'), tuple(hex(c) for c in commands[7]))
