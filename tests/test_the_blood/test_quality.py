from unittest import TestCase

from the_blood.models import *


#######################################################################
class TestQuality(TestCase):

    ####################################################################
    def test_equal(self):
        self.assertEqual(Quality('minor'), Quality('m'))
