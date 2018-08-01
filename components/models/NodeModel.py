

class NodeModel:
    A = 0.0
    B = 0.0
    D = lambda t: 0.0
    G = lambda t: 0.0

    def __init__(self):
        pass

    def set_A(self, A):
        self.A = A
        return self

    def set_B(self, B):
        self.B = B
        return self

    def set_D(self, D):
        self.D = D
        return self

    def set_G(self, G):
        self.G = G
        return self

    def get_model_with_fix_t(self, t):
        return NodeModel().set_A(self.A).set_B(self.B).set_D(self.D(t)).set_G(self.G(t))