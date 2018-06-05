import traceback
from unittest import TestCase

from models import transpose, A, A_sharp, B, C, C_sharp, D, D_sharp, F, E, F_sharp, G, G_sharp, transpose_multiple


########################################################################
def add_args_to_error_msg(func):
    def wrapper(*args, **kwargs):
        arguments = list(args[1:])
        arguments.append(kwargs)
        try:
            func(*args, **kwargs)
        except Exception:
            msg = "{original_message}\nCalled with args: {args}"
            print(msg.format(original_message=traceback.format_exc(), args=arguments))
            import time
            time.sleep(5)
            raise
    return wrapper



########################################################################
class TestTranspose(TestCase):

    ####################################################################
    def test_transpose_with_str(self):
        self.assertEqual(B, transpose('D♯').down.third)

    ####################################################################
    @add_args_to_error_msg
    def assertEqual(self, expected, actual, msg=None):
        super(TestTranspose, self).assertEqual(expected, actual, msg=msg)

    ####################################################################
    def test_transpose_up_a_third(self):
        for transposed, original in (
            (A, F),
            (A_sharp, F_sharp),
            (B, G),
            (C, G_sharp),
            (C_sharp, A),
            (D, A_sharp),
            (D_sharp, B),
            (E, C),
            (F, C_sharp),
            (F_sharp, D),
            (G, D_sharp),
            (G_sharp, E),
        ):
            self.assertEqual(transposed, transpose(original).up.third)

    ####################################################################
    def test_transpose_down_a_third(self):
        for transposed, original in (
            (C_sharp, F),
            (D, F_sharp),
            (D_sharp, G),
            (E, G_sharp),
            (F, A),
            (F_sharp, A_sharp),
            (G, B),
            (G_sharp, C),
            (A, C_sharp),
            (A_sharp, D),
            (B, D_sharp),
            (C, E),
        ):
            self.assertEqual(transposed, transpose(original).down.third)

    ####################################################################
    def test_transpose_up_a_fifth(self):
        for transposed, original in (
            (C, F),
            (C_sharp, F_sharp),
            (D, G),
            (D_sharp, G_sharp),
            (E, A),
            (F, A_sharp),
            (F_sharp, B),
            (G, C),
            (G_sharp, C_sharp),
            (A, D),
            (A_sharp, D_sharp),
            (B, E),
        ):
            self.assertEqual(transposed, transpose(original).up.fifth)

    ####################################################################
    def test_transpose_down_a_fifth(self):
        for transposed, original in (
            (A_sharp, F),
            (B, F_sharp),
            (C, G),
            (C_sharp, G_sharp),
            (D, A),
            (D_sharp, A_sharp),
            (E, B),
            (F, C),
            (F_sharp, C_sharp),
            (G, D),
            (G_sharp, D_sharp),
            (A, E),
        ):
            self.assertEqual(transposed, transpose(original).down.fifth)


########################################################################
class TestTransposeMultiple(TestCase):

    ####################################################################
    def test_transpose_multiple_notes_up_a_third(self):
        transposed = transpose_multiple(B, G, A).up.third
        self.assertEqual([D_sharp, B, C_sharp], transposed)

    ####################################################################
    def test_transpose_multiple_notes_down_a_third(self):
        transposed = transpose_multiple(B, G, A).down.third
        expected = [G, D_sharp, F]
        self.assertEqual(expected, transposed)

    ####################################################################
    def test_transpose_multiple_notes_up_a_fifth(self):
        transposed = transpose_multiple(B, G, A).up.fifth
        expected = [F_sharp, D, E]
        self.assertEqual(expected, transposed)
