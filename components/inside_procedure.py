from common import check_eps
from components.common import get_current_omega
from models.QModel import QModel


def find_c(Q):
    return reduce(lambda x, value: x + value ** 2, Q.itervalues(), 0)


def projector(q, Q_max):
    return {k: (-1 if v < 0 else 1) * min(abs(v), abs(Q_max[k])) if k in Q_max else v for k, v in q.items()}


def get_p(i, q_model, node):
    p = 0.0
    q = q_model.get_sum(i)
    if (node.D == 0.0 and node.G == 0.0) or (node.A != 0.0 and node.B != 0.0 and q >= 0.5 * (node.D / node.G - node.B) / node.A):
        p = 2 * node.A * q + node.B
    elif (node.A == 0.0 and node.B == 0.0) or (q < node.G * node.B - node.D):
        p = (q + node.D) / node.G
    else:
        p = (q + 0.5 * node.B / node.A + node.D) / (0.5 / node.A + node.G)
    return 0.0 if p < 0 else p

def get_gradient_w(model, q_model):
    return {k: get_p(k[1], q_model, model.nodes[k[1]]) - get_p(k[0], q_model, model.nodes[k[0]]) - v.e_tr for k, v in model.edges.items()}

def get_S(model, q_model):
    return get_gradient_w(model, q_model)


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
