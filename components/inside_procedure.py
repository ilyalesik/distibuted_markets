from common import check_eps
from components.common import get_current_omega
from models.QModel import QModel


def find_c(Q):
    return reduce(lambda x, value: x + value ** 2, Q.itervalues(), 0)


def projector(q, Q_max):
    return {k: (-1 if v < 0 else 1) * min(abs(v), abs(Q_max[k])) if k in Q_max else v for k, v in q.items()}


def find_min_g(model, q_model):
    min_G = None
    subgradient_G = None
    for k_node, v_node in model.nodes.items():
        g1 = q_model.get_sum(k_node) - v_node.G * v_node.B + v_node.D
        g2 = 0.5 * (v_node.D / v_node.G - v_node.B) / v_node.A - q_model.get_sum(k_node)
        if g1 < g2 and ((min_G is None) or g1 < min_G):
            min_G = g1
            subgradient_G = q_model.get_subgradient(k_node)
        elif g2 < g1 and ((min_G is None) or g2 < min_G):
            min_G = g2
            subgradient_G = q_model.get_subgradient(k_node)
    return subgradient_G, min_G


def get_p(i, q_model, node):
    return (q_model.get_sum(i) + 0.5 * node.B / node.A + node.D) / (0.5 / node.A + node.G)

def get_gradient_w(model, q_model):
    return {k: get_p(k[1], q_model, model.nodes[k[1]]) - get_p(k[0], q_model, model.nodes[k[0]]) for k, v in model.edges.items()}

def get_S(model, q_model):
    min_G = find_min_g(model, q_model)
    if min_G[1] >= 0:
        return get_gradient_w(model, q_model)
    return min_G[0]


def start_internal_procedure(model, Q_max, eps):
    c = find_c(Q_max)
    q = {k: 0.0 for k, v in model.edges.items()}
    counter = 1
    q_prev = None

    while not check_eps(q, q_prev, eps):
        q_prev = q
        q_model = QModel(q)
        s = get_S(model, q_model)
        omega = get_current_omega(counter, c)
        q = projector({k: v + omega * s[k] for k, v in q_prev.items()}, Q_max)
        counter += 1

    return q

def calc_p(model, q):
    q_model = QModel(q)
    return {k: get_p(k, q_model, v) for k, v in model.nodes.items()}
