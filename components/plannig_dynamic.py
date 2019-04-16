from components.models.IndicatorModel import IndicatorModel
from components.models.calc_dt import calc_dt
from components.planning_external_procedure import start_external_procedure


class NodeSetItem:

    def __init__(self):
        self.is_terminal = False
        self.upper_bound = 0
        self.model = None

    def set_is_terminal(self, is_terminal):
        self.is_terminal = is_terminal
        return self

    def set_upper_boundl(self, _upper_bound):
        self.upper_bound = _upper_bound
        return self

    def set_model(self, model):
        self.model = model
        return self


def upper_bound(model, resultForAllInd1, T, i):
    result = resultForAllInd1['tw']
    for k, v in model.edges.items():
        for t in range(0, T):
            ind = model.indicators[k][t]
            if ind == 0:
                result += calc_dt(i, t, T) * v.c
    return result


def _process(current_node_set):
    pass


def _next(current_node_set):
    _process(current_node_set)


def start_dynamic(model, T, eps, c, i, alpha=0.02, q_initial = None, projector=lambda x: x):
    indicators1 = IndicatorModel([1 for t in range(0, T + 2)])
    for k, v in model.edges.items():
        model.set_indicators(k, indicators1)\

    resultForAllInd1 = start_external_procedure(model, T, eps, c, i, alpha, q_initial, projector)
    print "result for all ind=1:"
    print resultForAllInd1

    indicators0 = IndicatorModel([0 for t in range(0, T + 2)])
    for k, v in model.edges.items():
        model.set_indicators(k, indicators0)

    indicators0_value = start_external_procedure(model, T, eps, c, i, alpha, q_initial, projector)

    root_node_set_item = NodeSetItem().set_is_terminal(True).set_upper_boundl(indicators0_value["tw"]).set_model(model)

    current_node_set = [root_node_set_item]

    while True:
        result = _next(current_node_set)
        if not (result is None):
            return result