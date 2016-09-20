
class DataModel:
    nodes = {}
    edges = {}

    def __init__(self):
        pass

    def add_node(self, number, A, B, D, G):
        self.nodes[number] = {'A': A, 'B': B, 'D': D, 'G': G}

    def add_edge(self, number_1, number_2, a, b, c):
        if number_1 == number_2:
            return
        key = (number_1, number_2)
        self.edges[key] = {'a': a, 'b': b, 'c': c}

    def get_data_model_with_fix_t(self, t):
        new_model = DataModel()
        new_model.nodes = {k: {'A': v['A'], 'B': v['B'], 'D': v['D'](t), 'G': v['G'](t)} for k, v in self.nodes.items()}
        new_model.edges = self.edges
        return new_model
