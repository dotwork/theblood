import unittest
from models import Key, Game, C, E, G, D, B, A


#######################################################################
class TestGame(unittest.TestCase):

    ####################################################################
    def test_key(self):
        # Divisible by 4: C major
        text = 'This is a sentence'
        key = Game(text).key
        self.assertEqual(Key('C'), key)

        # Divisible by 2: A minor
        text = 'It was a good sentence'
        key = Game(text).key
        self.assertEqual(Key('Am'), key)

    ####################################################################
    def test_time_signature(self):
        # If even number: 4/4
        text = 'This is a sentence'
        time_signature = Game(text).time_signature
        self.assertEqual('4/4', time_signature)

        # If divisible by 3: 3/4
        text = 'The sentence was dope'
        time_signature = Game(text).time_signature
        self.assertEqual('3/4', time_signature)

    ####################################################################
    def test_chords(self):
        text = 'This is a sentence'
        game = Game(text)
        chord_this, chord_is, chord_a, chord_sentence = game.chords

        # First chord should be the key's tonic
        self.assertEqual(Key('C'), game.key)
        self.assertEqual((C, E, G), chord_this)

        # Remaining chords should be calculated from letters
        self.assertEqual((D, G), chord_is)
        self.assertEqual((C, ), chord_a)
        self.assertEqual((G, B, A, E), chord_sentence)

    ####################################################################
    def test_melody(self):
        text = 'This is a sentence'
        game = Game(text)
        expected = [
            (A, C, D, G),
            (D, G),
            (C, ),
            (G, G, B, A, G, B, E, G)
        ]
        self.assertEqual(expected, game.melody)
