import unittest
from components.models.InputModel import InputModel

class TestDataModel(unittest.TestCase):

    def test_get_data_model_with_fix_t(self):
        model = InputModel()
        model.add_node(1, 1.03, 0.0, lambda t: 2 if 0 <= t < 8 or 20 <= t <= 24 else 10,
                       lambda t: 0.2 if 0 <= t < 8 or 20 <= t <= 24 else 1)
        model.add_node(2, 0.5, 0.0, lambda t: 4 if 0 <= t < 6 or 18 <= t <= 24 else 20,
                       lambda t: 0.4 if 0 <= t < 6 or 18 <= t <= 24 else 2)
        model.add_node(3, 0.5, 0.0, lambda t: 6 if 0 <= t < 8 or 20 <= t <= 24 else 30,
                       lambda t: 0.6 if 0 <= t < 8 or 20 <= t <= 24 else 3)

        model.add_edge(2, 3, 0.01 * 2, 0.01, 0.01 * 1.5)
        model.add_edge(1, 3, 0.01, 0.01 * 2, 0.01 * 2.5)

        new_model = model.get_data_model_with_fix_t(4)
        self.assertEqual(new_model.nodes, {
            1: {'A': 1.03, 'B': 0.0, 'D': 2, 'G': 0.2},
            2: {'A': 0.5, 'B': 0.0, 'D': 4, 'G': 0.4},
            3: {'A': 0.5, 'B': 0.0, 'D': 6, 'G': 0.6},
        })