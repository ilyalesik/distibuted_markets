
class QModel:
    q_items = {}

    def __init__(self, Q=None):
        if Q is not None:
            self.q_items = Q


    def get_sum(self, i):
        return reduce(lambda x, (k, v): x + (0 if i not in k else (v if k[0] == i else -v)), self.q_items.items(), 0)
