from components.models.EdgeModel import EdgeModel
from components.models.IndicatorModel import IndicatorModel
from components.models.InputModel import InputModel
from components.models.NodeModel import NodeModel
from components.planning_external_procedure import start_external_procedure

node2 = NodeModel()\
    .set_A(0.5)\
    .set_D(lambda t: 4 if 0 <= t < 6 or 18 <= t <= 24 else 20)\
    .set_G(lambda t: 0.1 * (4 if 0 <= t < 6 or 18 <= t <= 24 else 20))

node3 = NodeModel()\
    .set_A(0.5)\
    .set_D(lambda t: 6 if 0 <= t < 8 or 20 <= t <= 24 else 30)\
    .set_G(lambda t: 0.1 * (6 if 0 <= t < 8 or 20 <= t <= 24 else 30))

edge23 = EdgeModel().set_a(0.01 * 2).set_b(0.01).set_c(0.01 * 1.5)
indicators23 = IndicatorModel((0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0))

model = InputModel()
model\
    .add_node(2, node2)\
    .add_node(3, node3)\
    .add_edge(2, 3, edge23)\
    .add_indicators(2, 3, indicators23)

T = 10
q = start_external_procedure(model, T, 0.000001, 0.1)
print '----------------------'
print q
