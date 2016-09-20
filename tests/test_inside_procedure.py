import unittest

from components.inside_procedure import find_c, projector, start_internal_procedure
from components.models.DataModel import DataModel


class TestInsideProcedureCommon(unittest.TestCase):

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

class TestInsideProcedure(unittest.TestCase):

    def test_check_sample(self):
        model = DataModel()
        model.add_node(1, 1.03, 0.0, 10.0, 1.0)
        model.add_node(2, 0.5, 0.0, 20.0, 2.0)
        model.add_node(3, 0.5, 0.0, 30.0, 3.0)

        model.add_edge(2, 1, 0.01 * 2, 0.01 * 2, 0.01 * 2)
        model.add_edge(2, 3, 0.01 * 2, 0.01, 0.01 * 1.5)
        model.add_edge(1, 3, 0.01, 0.01 * 2, 0.01 * 2.5)

        q = start_internal_procedure(model, {(2, 1): 0.6, (2, 3): 0.7273, (1, 3): 0.9546}, 0.0000001)
        self.assertEqual(q, {(1, 3): 0.9546, (2, 3): 0.7273, (2, 1): 0.4625408183122532})