import unittest

from components.models.EdgeModel import EdgeModel
from components.models.ForkableInputModel import ForkableInputModel
from components.models.IndicatorModel import IndicatorModel
from components.models.NodeModel import NodeModel


class TestForkableInputModel(unittest.TestCase):

    def test_fork_2_node_2_time(self):
        node2 = NodeModel()

        node3 = NodeModel()

        edge23 = EdgeModel()
        indicators23 = IndicatorModel((0, 0))

        model = ForkableInputModel()
        model \
            .add_node(2, node2) \
            .add_node(3, node3) \
            .add_edge(2, 3, edge23) \
            .add_indicators(2, 3, indicators23)
        fork_result =  model.fork(2)
        self.assertEqual(fork_result[0].indicators[(2, 3)].indicator_items, [1, 0])
        self.assertEqual(fork_result[1].indicators[(2, 3)].indicator_items, [0, 1])

    def test_fork_3_node_2_time(self):
        node1 = NodeModel()
        node2 = NodeModel()
        node3 = NodeModel()

        edge12 = EdgeModel()
        edge23 = EdgeModel()
        indicators23 = IndicatorModel([0, 0])

        model = ForkableInputModel()
        model \
            .add_node(1, node1) \
            .add_node(2, node2) \
            .add_node(3, node3) \
            .add_edge(1, 2, edge12) \
            .add_edge(2, 3, edge23) \
            .add_indicators(1, 2, indicators23) \
            .add_indicators(2, 3, indicators23)
        fork_result =  model.fork(2)

        self.assertEqual(fork_result[0].indicators[(1, 2)].indicator_items, [1, 0])
        self.assertEqual(fork_result[0].indicators[(2, 3)].indicator_items, [0, 0])

        self.assertEqual(fork_result[1].indicators[(1, 2)].indicator_items, [0, 1])
        self.assertEqual(fork_result[1].indicators[(2, 3)].indicator_items, [0, 0])

        self.assertEqual(fork_result[2].indicators[(1, 2)].indicator_items, [0, 0])
        self.assertEqual(fork_result[2].indicators[(2, 3)].indicator_items, [1, 0])

        self.assertEqual(fork_result[3].indicators[(1, 2)].indicator_items, [0, 0])
        self.assertEqual(fork_result[3].indicators[(2, 3)].indicator_items, [0, 1])
