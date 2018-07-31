from components.models.EdgeModel import EdgeModel
from components.models.InputModel import InputModel
from components.inside_procedure import start_internal_procedure
from components.external_procedure import start_external_procedure
from components.models.NodeModel import NodeModel

node1 = NodeModel()\
    .setA(1.03)\
    .setD(lambda t: 2 if 0 <= t < 8 or 20 <= t <= 24 else 10)\
    .setG(lambda t: 0.1 * (2 if 0 <= t < 8 or 20 <= t <= 24 else 10))

node2 = NodeModel()\
    .setA(0.5)\
    .setD(lambda t: 4 if 0 <= t < 6 or 18 <= t <= 24 else 20)\
    .setG(lambda t: 0.1 * (4 if 0 <= t < 6 or 18 <= t <= 24 else 20))

node3 = NodeModel()\
    .setA(0.5)\
    .setD(lambda t: 6 if 0 <= t < 8 or 20 <= t <= 24 else 30)\
    .setG(lambda t: 0.1 * (6 if 0 <= t < 8 or 20 <= t <= 24 else 30))

edge23 = EdgeModel().set_a(0.01 * 2).set_b(0.01).set_c(0.01 * 1.5)
edge13 = EdgeModel().set_a(0.01).set_b(0.01 * 2).set_c(0.01 * 2.5)

model = InputModel()
model\
    .add_node(1, node1)\
    .add_node(2, node2)\
    .add_node(3, node3)\
    .add_edge(2, 3, edge23)\
    .add_edge(1, 3, edge13)

projector = lambda q: {k: min(abs(v), 1.714) for k, v in q.items()}
q = start_external_procedure(model, 0.000001, 0.1, projector)
print '----------------------'
print q