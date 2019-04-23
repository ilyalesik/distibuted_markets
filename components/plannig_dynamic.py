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

    def set_upper_bound(self, _upper_bound):
        self.upper_bound = _upper_bound
        return self

    def set_model(self, model):
        self.model = model
        return self


def upper_bound(model, result_for_all_ind_1, T, i):
    result = result_for_all_ind_1['tw']
    for k, v in model.edges.items():
        for t in range(0, T):
            ind = model.indicators[k][t]
            if ind == 0:
                result += calc_dt(i, t, T) * v.c
    return result


def _process(current_node_set,result_for_all_ind_1, T, eps, c, i, alpha, q_initial, projector):
    max_node = None
    for set_item in current_node_set:
        if not set_item.is_terminal and  (max_node is None or max_node.upper_bound < set_item.upper_bound):
            max_node = set_item

    print "fork node %s" % reduce(lambda prev, key: prev + key.__str__() + ":" + max_node.model.indicators[key].__str__() + "; ", max_node.model.indicators, "")
    new_models = max_node.model.fork(T)
    node_set_without_max = filter(lambda set_item: set_item != max_node, current_node_set)
    new_node_set = [NodeSetItem()
                        .set_is_terminal(False)
                        .set_upper_bound(upper_bound(new_model, result_for_all_ind_1, T, i))
                        .set_model(new_model) for new_model in new_models]
    terminal_value = start_external_procedure(max_node.model, T, eps, c, i, alpha, q_initial, projector)
    terminal_node_set_item = NodeSetItem().set_is_terminal(True).set_upper_bound(terminal_value["tw"]).set_model(max_node.model)
    return node_set_without_max + new_node_set + [terminal_node_set_item]



def _next(current_node_set, result_for_all_ind_1, T, eps, c, i, alpha, q_initial, projector):
    new_node_set = _process(current_node_set, result_for_all_ind_1, T, eps, c, i, alpha, q_initial, projector)
    max_node = None
    for set_item in new_node_set:
        if max_node is None or max_node.upper_bound < set_item.upper_bound:
            max_node = set_item

    if max_node is None:
        return None

    terminals = filter(lambda set_item: set_item.is_terminal, current_node_set)
    for node in terminals:
        if max_node.upper_bound <= node.upper_bound:
            return max_node
    return None



def start_dynamic(model, T, eps, c, i, alpha=0.02, q_initial = None, projector=lambda x: x):
    indicators1 = IndicatorModel([1 for t in range(0, T + 2)])
    for k, v in model.edges.items():
        model.set_indicators(k, indicators1)\

    result_for_all_ind_1 = start_external_procedure(model, T, eps, c, i, alpha, q_initial, projector)
    print "result for all ind=1:"
    print result_for_all_ind_1

    indicators0 = IndicatorModel([0 for t in range(0, T + 2)])
    for k, v in model.edges.items():
        model.set_indicators(k, indicators0)

    root_node_set_item = NodeSetItem().set_is_terminal(False).set_model(model)

    current_node_set = [root_node_set_item]

    while True:
        current_node_set = _process(current_node_set, result_for_all_ind_1, T, eps, c, i, alpha, q_initial, projector)
        max_node = None
        for set_item in current_node_set:
            if max_node is None or max_node.upper_bound < set_item.upper_bound:
                max_node = set_item
        terminals = filter(lambda set_item: set_item.is_terminal, current_node_set)
        for node in terminals:
            if max_node.upper_bound <= node.upper_bound:
                return max_node