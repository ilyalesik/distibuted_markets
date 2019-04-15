from components.models.IndicatorModel import IndicatorModel
from components.models.calc_dt import calc_dt
from components.planning_external_procedure import start_external_procedure


def upper_bound(model, resultForAllInd1, T, i):
    result = resultForAllInd1['tw']
    for k, v in model.edges.items():
        for t in range(0, T):
            ind = model.indicators[k][t]
            if ind == 0:
                result += calc_dt(i, t, T) * v.c
    return result


def fork(model, resultForAllInd1, T, eps, c, i, alpha, q_initial, projector):
    terminal_value = start_external_procedure(model, T, eps, c, i, alpha, q_initial, projector)
    forks = model.fork(T)
    max_upper_bound_value = 0
    max_upper_bound_item = None

    for fork_item in forks:
        fork_item_upper_bound = upper_bound(fork_item, resultForAllInd1, T, i)
        if max_upper_bound_value < fork_item_upper_bound:
            max_upper_bound_value = fork_item_upper_bound
            max_upper_bound_item = fork_item

    if ((terminal_value['tw'] - max_upper_bound_value) / max_upper_bound_value) < eps:
        print "stop!"
        return max_upper_bound_value, max_upper_bound_item
    else:
        fork(max_upper_bound_item, resultForAllInd1, T, eps, c, i, alpha, q_initial, projector)


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

    return fork(model, resultForAllInd1, T, eps, c, i, alpha, q_initial, projector)

    #q = start_external_procedure(model, T, eps, c, i, alpha, q_initial, projector)
    #print q