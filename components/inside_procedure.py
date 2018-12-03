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
    for node_key, node in model.nodes.items():
        g1 = None
        g2 = None
        if (node.D != 0.0 and node.G != 0.0 and node.A != 0.0 and node.B != 0.0):
            g1 = q_model.get_sum(node_key) - node.G * node.B + node.D
            g2 = 0.5 * (node.D / node.G - node.B) / node.A - q_model.get_sum(node_key)
        elif (node.A == 0.0 and node.B == 0.0):
            g1 = q_model.get_sum(node_key)
        elif (node.D == 0.0 and node.G == 0.0):
            g2 = -q_model.get_sum(node_key)
        if (g1 < g2 or (g2 is None)) and ((min_G is None) or g1 < min_G):
            min_G = g1
            subgradient_G = q_model.get_subgradient(node_key)
        elif (g2 < g1 or (g1 is None)) and ((min_G is None) or g2 < min_G):
            min_G = g2
            subgradient_G = q_model.get_subgradient(node_key)
    return subgradient_G, min_G


def get_p(i, q_model, node):
    p = 0.0
    q = q_model.get_sum(i)
    if (node.D == 0.0 and node.G == 0.0):
        p = 2 * node.A * q + node.B
    elif (node.A == 0.0 and node.B == 0.0):
        p = (q + node.D) / node.G
    else:
        p = (q + 0.5 * node.B / node.A + node.D) / (0.5 / node.A + node.G)
    return p

def get_gradient_w(model, q_model):
    return {k: get_p(k[1], q_model, model.nodes[k[1]]) - get_p(k[0], q_model, model.nodes[k[0]]) - v.e_tr for k, v in model.edges.items()}

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
