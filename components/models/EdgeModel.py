
class EdgeModel:

    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.e_tr = 0.0
        pass

    def set_a(self, a):
        self.a = a
        return self

    def set_b(self, b):
        self.b = b
        return self

    def set_c(self, c):
        self.c = c
        return self

    def set_e_tr(self, e_tr):
        self.e_tr = e_tr
        return self