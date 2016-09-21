import unittest
from components.models.QModel import QModel

class TestQModel(unittest.TestCase):

    def test_get_sum_int(self):
        Q = {(2, 1): 7, (2, 3): 43, (1, 3): 3}
        qmodel = QModel(Q)
        self.assertEqual(qmodel.get_sum(1), -4)

    def test_get_sum_int_2(self):
        Q = {(2, 3): 43, (1, 3): 3}
        qmodel = QModel(Q)
        self.assertEqual(qmodel.get_sum(2), 43)
        self.assertEqual(qmodel.get_sum(1), 3)
        self.assertEqual(qmodel.get_sum(3), -46)