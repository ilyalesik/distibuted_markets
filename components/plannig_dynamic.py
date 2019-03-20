from components.models.IndicatorModel import IndicatorModel
from components.planning_external_procedure import start_external_procedure


def start_dynamic(model, T, eps, c, i, alpha=0.02, q_initial = None, projector=lambda x: x):
    indicators1 = IndicatorModel([1 for t in range(0, T + 2)])
    for k, v in model.edges.items():
        model.set_indicators(k, indicators1)\

    resultForAllInd1 = start_external_procedure(model, T, eps, c, i, alpha, q_initial, projector)
    print resultForAllInd1

    indicators0 = IndicatorModel([0 for t in range(0, T + 2)])
    for k, v in model.edges.items():
        model.set_indicators(k, indicators0)

    resultForAllInd0 = start_external_procedure(model, T, eps, c, i, alpha, q_initial, projector)
    print resultForAllInd0

    #q = start_external_procedure(model, T, eps, c, i, alpha, q_initial, projector)
    #print q