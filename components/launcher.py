from model import DataModel

model = DataModel()
model.add_node(1, 1.03, 0.0, lambda t: 2 if 0 <= t < 8 or 20 <= t <= 24 else 10,
               lambda t: 0.1 * (2 if 0 <= t < 8 or 20 <= t <= 24 else 10))
model.add_node(2, 0.5, 0.0, lambda t: 4 if 0 <= t < 6 or 18 <= t <= 24 else 20,
               lambda t: 0.1 * (4 if 0 <= t < 6 or 18 <= t <= 24 else 20))
model.add_node(3, 0.5, 0.0, lambda t: 6 if 0 <= t < 8 or 20 <= t <= 24 else 30,
               lambda t: 0.1 * (6 if 0 <= t < 8 or 20 <= t <= 24 else 30))

model.add_edge(2, 3, 0.01 * 2, 0.01, 0.01 * 1.5)
model.add_edge(1, 3, 0.01, 0.01 * 2, 0.01 * 2.5)