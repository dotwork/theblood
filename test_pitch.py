from decimal import Decimal
from unittest import TestCase

from models import Pitch


FOUR_PLACES = Decimal(10) ** -4


#######################################################################
class TestPitch(TestCase):
    """
    https://pages.mtu.edu/~suits/notefreqs.html
    """

    ####################################################################
    def test_(self):
        last_name = None
        last_hz = None
        for name, hz in Pitch.pitches.items():
            if last_hz:
                percent = Decimal(hz)/Decimal(last_hz)
                self.assertAlmostEqual(Decimal('1.0595'), percent.quantize(FOUR_PLACES), places=3)
                print(name, percent)
            last_name = name
            last_hz = hz
