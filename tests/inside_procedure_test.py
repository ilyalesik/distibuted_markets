import unittest

from components.inside_procedure import find_c, projector


class TestCommon(unittest.TestCase):

    def test__find_c(self):
        Q = {(1, 2): 1, (2, 3): 2, (3, 4): 3}
        self.assertEqual(find_c(Q), 14)

    def test_projector(self):
        q = {(1, 2): 1.5, (2, 3): -2, (3, 4): 3, (4, 5): 2.1}
        Q_max = {(1, 2): 1.3, (2, 3): 3, (3, 4): -2, (4, 5): 2.3}
        self.assertEqual(projector(q, Q_max), {(1, 2): 1.3, (2, 3): -2, (3, 4): 2, (4, 5): 2.1})

    def test_projector_with_zero(self):
        q = {(1, 2): 0, (2, 3): 1}
        Q_max = {(1, 2): 1, (2, 3): 0}
        self.assertEqual(projector(q, Q_max), {(1, 2): 0, (2, 3): 0})

    def test_projector_without_projector_item(self):
        q = {(1, 2): 1, (2, 3): 2}
        Q_max = {(1, 2): 0.5}
        self.assertEqual(projector(q, Q_max), {(1, 2): 0.5, (2, 3): 2})