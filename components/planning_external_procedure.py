import random
from common import check_eps, isclose
from components.common import get_current_omega
from inside_procedure import start_internal_procedure, calc_p

def get_q_slice(model, t, Q):
    return {
        k: Q[k][t] for k, v in model.edges.items()
    }

def calc_W_gradient(model, t, Q, eps):
    model_fix_t = model.get_input_model_with_fix_t(t)
    Q_slice_t = get_q_slice(model, t, Q)
    q = start_internal_procedure(model_fix_t, Q_slice_t, eps)
    p = calc_p(model_fix_t, q)
    return {k: abs(p[k[1]] - p[k[0]]) - model.indicators[k][t] * (2 * v.a * Q_slice_t[k] + v.b) for k, v in model.edges.items()}

def calc_gradient(model, T, Q, eps):
    w_gradient_by_t = list((calc_W_gradient(model, t, Q, eps) for t in range(0, T +1)))
    return {
        k: list((w_gradient_by_t[t][k] for t in range(0, T +1))) for k, v in model.edges.items()
    }


def find_min_g(model, T, Q):
    max_G = None
    subgradient_G = None
    for edge_key, edge in model.edges.items():
        for t in range(0, T):
            g = Q[edge_key][t] - Q[edge_key][t + 1]
            if (max_G is None) or g > max_G:
                max_G = g
                subgradient_G = {k: list((-1 if k == edge_key and t >= _t + 1 else 1 if k == edge_key and t <= _t else 0 for _t in range(0, T + 1))) for k, v in model.edges.items()}
    return subgradient_G, max_G


def get_S(model, T, Q, eps):
    max_G = find_min_g(model, T, Q)
    if max_G[1] <= 0:
        return calc_gradient(model, T, Q, eps)
    return max_G[0]


def check_eps_for_T(q, q_prev, eps, T):
    if q_prev is None:
        return False
    for key in q.keys():
        for t in range(0, T + 1):
            if not isclose(q[key][t], q_prev[key][t], abs_tol=eps):
                return False
    return True

def start_external_procedure(model, T, eps, c, projector=lambda x: x):
    q = {k: list((0.0 for t in range(0, T + 1))) for k, v in model.edges.items()}
    counter = 1
    q_prev = None

    while not check_eps_for_T(q, q_prev, eps, T):
        q_prev = q
        delta_tw = get_S(model, T, q, eps)
        omega = get_current_omega(counter, c)
        q = projector({k: list((v[t] + omega * delta_tw[k][t] for t in range(0, T + 1))) for k, v in q_prev.items()})
        counter += 1
        print q

    print 'counter: ', counter
    return q
