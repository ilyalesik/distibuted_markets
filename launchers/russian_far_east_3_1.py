from components.inside_procedure import start_internal_procedure, calc_p
from components.models.IndicatorModel import IndicatorModel
from components.models.InputModel import InputModel
from components.planning_external_procedure import start_external_procedure
from launchers.russian_far_east_model import node3, node1, edge3_1

indicators = IndicatorModel((1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0))

far_east_model = InputModel()
far_east_model\
    .add_node(3, node3)\
    .add_node(1, node1)\
    .add_edge(3, 1, edge3_1)\
    .add_indicators(3, 1, indicators)

T = 1
q = start_external_procedure(far_east_model, T, 0.0001, 0.1)
print '----------------------'
print q