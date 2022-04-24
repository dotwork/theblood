import unittest

from music21 import converter, corpus, stream
from music21.note import Note


#######################################################################
@unittest.skip('none of this works')
class TestMusic21(unittest.TestCase):

    ####################################################################
    def test_analyze_key(self):
        s = corpus.parse('bach/bwv65.2.xml')
        key = s.analyze('key')
        self.assertEqual('A minor', key.name)
        s.show()

    ####################################################################
    def test_read_scurvy_rickets_musicxml(self):
        go_play = '/home/carlos/Downloads/Extraordinary.musicxml'
        s = converter.parse(go_play)
        key = s.analyze('key')
        s.show()
        self.fail('this test fails. says key is F Major.')
        self.assertEqual('C major', key.name)

    ####################################################################
    def test_write_arpeggio(self):
        f = Note("F4")
        a = Note("A4")
        c = Note("C5")
        f.duration.quarterLength = 4
        a.duration.quarterLength = 4
        c.duration.quarterLength = 4
        arpeggio = stream.Stream()
        for note in [f, a, c]:
            arpeggio.append(note)
        arpeggio.show()
