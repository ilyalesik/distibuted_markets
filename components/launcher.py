from model import DataModel
from inside_procedure import start_internal_procedure

model = DataModel()
model.add_node(1, 1.03, 0.0, 10.0, 1.0)
model.add_node(2, 0.5, 0.0, 20.0, 2.0)
model.add_node(3, 0.5, 0.0, 30.0, 3.0)

model.add_edge(2, 1, 0.01 * 2, 0.01 * 2, 0.01 * 2)
model.add_edge(2, 3, 0.01 * 2, 0.01, 0.01 * 1.5)
model.add_edge(1, 3, 0.01, 0.01 * 2, 0.01 * 2.5)

q = start_internal_procedure(model, {(2, 1): 0.6, (2, 3): 0.7273, (1, 3): 0.9546}, 0.0000001)
print q