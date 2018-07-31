

class NodeModel:
    A = 0.0
    B = 0.0
    D = lambda t: 0.0
    G = lambda t: 0.0

    def __init__(self):
        pass

    def setA(self, A):
        self.A = A
        return self

    def setB(self, B):
        self.B = B
        return self

    def setD(self, D):
        self.D = D
        return self

    def setG(self, G):
        self.G = G
        return self