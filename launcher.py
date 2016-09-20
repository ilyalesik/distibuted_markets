from components.models.DataModel import DataModel
from components.inside_procedure import start_internal_procedure
from components.external_procedure import start_external_procedure

#model = DataModel()
#model.add_node(1, 1.03, 0.0, 10.0, 1.0)
#model.add_node(2, 0.5, 0.0, 20.0, 2.0)
#model.add_node(3, 0.5, 0.0, 30.0, 3.0)
#
#model.add_edge(2, 1, 0.01 * 2, 0.01 * 2, 0.01 * 2)
#model.add_edge(2, 3, 0.01 * 2, 0.01, 0.01 * 1.5)
#model.add_edge(1, 3, 0.01, 0.01 * 2, 0.01 * 2.5)
#
#q = start_internal_procedure(model, {(2, 1): 0.6, (2, 3): 0.7273, (1, 3): 0.9546}, 0.0000001)
#print q
model = DataModel()
model.add_node(1, 1.03, 0.0, lambda t: 2 if 0 <= t < 8 or 20 <= t <= 24 else 10,
               lambda t: 0.1 * (2 if 0 <= t < 8 or 20 <= t <= 24 else 10))
model.add_node(2, 0.5, 0.0, lambda t: 4 if 0 <= t < 6 or 18 <= t <= 24 else 20,
               lambda t: 0.1 * (4 if 0 <= t < 6 or 18 <= t <= 24 else 20))
model.add_node(3, 0.5, 0.0, lambda t: 6 if 0 <= t < 8 or 20 <= t <= 24 else 30,
               lambda t: 0.1 * (6 if 0 <= t < 8 or 20 <= t <= 24 else 30))

model.add_edge(2, 3, 0.01 * 2, 0.01, 0.01 * 1.5)
model.add_edge(1, 3, 0.01, 0.01 * 2, 0.01 * 2.5)

projector = lambda q: {k: min(abs(v), 1.714) for k, v in q.items()}
q = start_external_procedure(model, 0.0000001, 0.1, projector)
print '----------------------'
print q