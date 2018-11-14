from components.models.IndicatorModel import IndicatorModel
from components.models.InputModel import InputModel
from launchers.russian_far_east_model import node1, node9, edge1_9

indicators = IndicatorModel((1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0))

far_east_model = InputModel()
far_east_model\
    .add_node(1, node1)\
    .add_node(9, node9)\
    .add_edge(1, 9, edge1_9)\
    .add_indicators(1, 9, indicators)