import unittest

from mingus.containers import Track, Bar

from composer.translators.text import TextTranslator
from the_blood.models import *


#######################################################################
class TestText(unittest.TestCase):

    ####################################################################
    def test_key(self):
        # Divisible by 4: C major
        text = 'This is a sentence'
        key = TextTranslator(text).key
        self.assertEqual(Key('C'), key)

        # Divisible by 2: A minor
        text = 'It was a good sentence'
        key = TextTranslator(text).key
        self.assertEqual(Key('Am'), key)

    ####################################################################
    def test_time_signature(self):
        # If even number: 4/4
        text = 'This is a sentence'
        time_signature = TextTranslator(text).time_signature
        self.assertEqual('4/4', time_signature)

        # If divisible by 3: 3/4
        text = 'The sentence was dope'
        time_signature = TextTranslator(text).time_signature
        self.assertEqual('3/4', time_signature)

    ####################################################################
    def test_chords(self):
        text = 'This is a sentence'
        translator = TextTranslator(text)
        chord_this, chord_is, chord_a, chord_sentence = translator.chords

        # First chord should be the key's tonic
        self.assertEqual(Key('C'), translator.key)
        self.assertEqual((C, E, G), chord_this)

        # Remaining chords should be calculated from letters
        self.assertEqual((D, G), chord_is)
        self.assertEqual((C, ), chord_a)
        self.assertEqual((G, B, A, E), chord_sentence)

        track = Track()
        bar = Bar()
        bar.place_notes([str(n) for n in chord_this[:2]], 4)
        bar.place_notes([str(chord_this[-1])], 2)
        track.add_bar(bar)

        bar = Bar()
        bar.place_notes([str(n) for n in chord_is], 2)
        track.add_bar(bar)

        bar = Bar()
        bar.place_notes([str(chord_a[0])], 1)
        track.add_bar(bar)

        bar = Bar()
        bar.place_notes([str(n) for n in chord_sentence], 4)
        track.add_bar(bar)

        # MidiFile.write_Track('test_midi.mid', verbose=True)

    ####################################################################
    def test_melody(self):
        text = 'This is a sentence'
        translator = TextTranslator(text)
        expected = [
            (A, C, D, G),
            (D, G),
            (C, ),
            (G, G, B, A, G, B, E, G)
        ]
        self.assertEqual(expected, translator.melody)
