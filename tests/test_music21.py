import os

from music21 import corpus, configure, environment
import unittest


#######################################################################
class TestMusic21(unittest.TestCase):

    ####################################################################
    def setUp(self):
        environment.set('musicxmlPath', os.path.dirname(__file__))
        configure.run()

    ####################################################################
    def test_analyze_key(self):
        s = corpus.parse('bach/bwv65.2.xml')
        key = s.analyze('key')
        self.assertEqual('A minor', key.name)
        s.show()
