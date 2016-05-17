
import unittest

from modeful import sign

class SignTestCase(unittest.TestCase):

    def test_sign(self):
        cases = [(-1000, -1),
                 (-1, -1),
                 (0, 1),
                 (1, 1),
                 (1000, 1)]
        for x, expected in cases:
            self.assertEqual(expected, sign(x))
