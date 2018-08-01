from components.models.EdgeModel import EdgeModel
from components.models.IndicatorModel import IndicatorModel
from components.models.InputModel import InputModel
from components.models.NodeModel import NodeModel
from components.planning_external_procedure import start_external_procedure

node1 = NodeModel()\
    .set_A(1.03)\
    .set_D(lambda t: 10 if 0 <= t < 5 else 20)\
    .set_G(lambda t: 0.1 * (10 if 0 <= t < 5 else 20))

node2 = NodeModel()\
    .set_A(0.5)\
    .set_D(lambda t: 5 if 0 <= t < 7 else 10)\
    .set_G(lambda t: 0.1 * (5 if 0 <= t < 7 else 10))

edge12 = EdgeModel().set_a(0.01 * 2).set_b(0.01).set_c(0.01 * 1.5)
indicators12 = IndicatorModel((0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0))

model = InputModel()
model\
    .add_node(1, node1)\
    .add_node(2, node2)\
    .add_edge(1, 2, edge12)\
    .add_indicators(1, 2, indicators12)

T = 10
q = start_external_procedure(model, T, 0.000001, 0.1)
print '----------------------'
print q
