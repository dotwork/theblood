import string

from the_blood.models import Key, Chord


#######################################################################
def divisible_by(word, i):
    return (len(word) % i) == 0


#######################################################################
class TextTranslator:

    ####################################################################
    def __init__(self, text):
        self.text = text
        self.words = self.text.split(' ')
        self.key = self._calculate_key()
        self.chords = self._calculate_chords()
        self.melody = self._calculate_melody()
        self.time_signature = self._calculate_time_signature()

    ####################################################################
    def _calculate_key(self):
        first_word = self.words[0]
        if divisible_by(first_word, 4):
            return Key('C')
        elif divisible_by(first_word, 2):
            return Key('Am')
        elif divisible_by(first_word, 3):
            # Update this with logic for number of sharps/flats
            return Key('A')
        else:
            raise NotImplementedError()

    ####################################################################
    def _calculate_time_signature(self):
        first_word = self.words[0]
        if divisible_by(first_word, 2):
            return '4/4'
        elif divisible_by(first_word, 3):
            return '3/4'
        else:
            raise NotImplementedError()

    ####################################################################
    def _calculate_chords(self):
        chords = [Chord(self.key.name).triad]
        for word in self.words[1:]:
            chord = []
            for char in word:
                note = self._get_note_from_char(char)
                if note and note not in chord:
                    chord.append(note)
            chords.append(tuple(chord))
        return chords

    ####################################################################
    def _calculate_melody(self):
        melody = []
        for word in self.words:
            phrase = []
            for char in word:
                note = self._get_note_from_char(char)
                if note:
                    phrase.append(note)
            melody.append(tuple(phrase))
        return melody

    ####################################################################
    def _get_note_from_char(self, char):
        char = char.lower()
        if char in string.ascii_lowercase:
            i = string.ascii_lowercase.index(char)
            while i > 6:
                i -= 7
            note = self.key.scale[i]
            return note
        raise NotImplementedError(f"Don't know how to convert {char} yet.")
