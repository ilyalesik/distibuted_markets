import unittest

from components.common import check_eps


class TestCommon(unittest.TestCase):
    def test_check_eps_1(self):
        Q = {(1, 2): 1.34, (2, 3): 2.67, (3, 4): 3.897}
        Q_prev = {(1, 2): 1.36, (2, 3): 2.65, (3, 4): 3.894}
        self.assertTrue(check_eps(Q, Q_prev, 0.5))

    def test_check_eps_2(self):
        Q = {(1, 2): 1.34, (2, 3): 2.67, (3, 4): 3.897}
        Q_prev = {(1, 2): 1.3499999, (2, 3): 2.66, (3, 4): 3.897}
        self.assertTrue(check_eps(Q, Q_prev, 0.01))

    def test_check_eps_3(self):
        Q = {(1, 2): 1.34, (2, 3): 2.67, (3, 4): 3.897}
        Q_prev = {(1, 2): 1.35, (2, 3): 2.66, (3, 4): 3.897}
        self.assertFalse(check_eps(Q, Q_prev, 0.01))
