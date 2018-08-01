import unittest

from components.inside_procedure import find_c, projector, start_internal_procedure, calc_p
from components.models.EdgeModel import EdgeModel
from components.models.InputModel import InputModel
from components.models.NodeModel import NodeModel


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

    def test_calc_p(self):
        node1 = NodeModel() \
            .set_A(1.0) \
            .set_D(10.0) \
            .set_G(1.0)

        node2 = NodeModel() \
            .set_A(0.5) \
            .set_D(20.0) \
            .set_G(2.0)

        node3 = NodeModel() \
            .set_A(0.5) \
            .set_D(30.0) \
            .set_G(3.0)

        edge21 = EdgeModel().set_a(0.01 * 2).set_b(0.01 * 2).set_c(0.01 * 2)
        edge23 = EdgeModel().set_a(0.01 * 2).set_b(0.01).set_c(0.01 * 1.5)
        edge13 = EdgeModel().set_a(0.01).set_b(0.01 * 2).set_c(0.01 * 2.5)

        model = InputModel()
        model \
            .add_node(1, node1) \
            .add_node(2, node2) \
            .add_node(3, node3) \
            .add_edge(2, 1, edge21) \
            .add_edge(2, 3, edge23) \
            .add_edge(1, 3, edge13)

        q = {(2, 1): 4, (2, 3): 5, (1, 3): 6}
        self.assertEqual({1: 8.0, 2: 9.666666666666666, 3: 4.75}, calc_p(model, q))



class TestInsideProcedure(unittest.TestCase):

    def test_check_sample(self):
        node1 = NodeModel() \
            .set_A(1.03) \
            .set_D(10.0) \
            .set_G(1.0)

        node2 = NodeModel() \
            .set_A(0.5) \
            .set_D(20.0) \
            .set_G(2.0)

        node3 = NodeModel() \
            .set_A(0.5) \
            .set_D(30.0) \
            .set_G(3.0)

        edge21 = EdgeModel().set_a(0.01 * 2).set_b(0.01 * 2).set_c(0.01 * 2)
        edge23 = EdgeModel().set_a(0.01 * 2).set_b(0.01).set_c(0.01 * 1.5)
        edge13 = EdgeModel().set_a(0.01).set_b(0.01 * 2).set_c(0.01 * 2.5)

        model = InputModel()
        model \
            .add_node(1, node1) \
            .add_node(2, node2) \
            .add_node(3, node3) \
            .add_edge(2, 1, edge21)\
            .add_edge(2, 3, edge23) \
            .add_edge(1, 3, edge13)

        q = start_internal_procedure(model, {(2, 1): 0.6, (2, 3): 0.7273, (1, 3): 0.9546}, 0.0000001)
        self.assertEqual({(1, 3): 0.9546, (2, 3): 0.7273, (2, 1): 0.4625408183122532}, q)