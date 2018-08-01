from components.models.NodeModel import NodeModel


class InputModel:
    nodes = {}
    edges = {}
    indicators = {}

    def __init__(self):
        pass

    def add_node(self, number, node):
        self.nodes[number] = node
        return self

    def add_edge(self, number_1, number_2, edge):
        if number_1 == number_2:
            return self
        key = (number_1, number_2)
        self.edges[key] = edge
        return self

    def add_indicators(self, number_1, number_2, indicators):
        if number_1 == number_2:
            return self
        key = (number_1, number_2)
        self.indicators[key] = indicators
        return self

    def get_input_model_with_fix_t(self, t):
        new_model = InputModel()
        new_model.nodes = {k: v.get_model_with_fix_t(t) for k, v in self.nodes.items()}
        new_model.edges = self.edges
        return new_model
