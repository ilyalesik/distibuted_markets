
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
