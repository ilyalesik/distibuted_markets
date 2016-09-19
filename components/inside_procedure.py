from common import check_eps
from models.QModel import QModel


def find_c(Q):
    return reduce(lambda x, value: x + value ** 2, Q.itervalues(), 0)


def projector(q, Q_max):
    return {k: (-1 if v < 0 else 1) * min(abs(v), abs(Q_max[k])) if k in Q_max else v for k, v in q.items()}


def get_current_omega(k, c):
    return c * k ** (-0.75)


def find_min_g(model, q_model):
    min_G = None
    subgradient_G = None
    for k_node, v_node in model.nodes.items():
        g1 = q_model.get_sum(k_node) + v_node['D']
        g2 = 0.5 * v_node['D'] / v_node['G'] * v_node['A'] - q_model.get_sum(k_node)
        if g1 < g2 and ((min_G is None) or g1 < min_G):
            min_G = g1
            subgradient_G = q_model.get_subgradient(k_node)
        elif g2 < g1 and ((min_G is None) or g2 < min_G):
            min_G = g1
            subgradient_G = q_model.get_subgradient(k_node)
    return subgradient_G, min_G



def start_internal_procedure(model, Q_max, eps):
    q = {k: 0.0 for k, v in model.edges}
    q_model = QModel(q)
    counter = 0
    q_prev = None

    while not check_eps(q, q_prev, eps):
        q_prev = q
        # todo eval new q
