from components.inside_procedure import start_internal_procedure
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
Q = {
    (1, 9): 113.46322991782966
}
model_fix_t = far_east_model.get_input_model_with_fix_t(0)
q = start_internal_procedure(model_fix_t, Q, 0.0001)

#q = start_external_procedure(far_east_model, T, 0.0001, 0.1)
print '----------------------'
print q