import unittest

from components.inside_procedure import find_c


class TestCommon(unittest.TestCase):

    def test_c(self):
        Q = {(1, 2): 1, (2, 3): 2, (3, 4): 3}
        self.assertEqual(find_c(Q), 14)
