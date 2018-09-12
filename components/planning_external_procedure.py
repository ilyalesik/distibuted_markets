import random
from common import check_eps, isclose
from components.common import get_current_omega
from inside_procedure import start_internal_procedure, calc_p

def get_q_slice(model, t, dQ):
    return {
        k: reduce(lambda x, tau: x + dQ[k][tau], range(0, t), 0) for k, v in model.edges.items()
    }

def calc_W_gradient(model, t, dQ, eps):
    model_fix_t = model.get_input_model_with_fix_t(t)
    Q_slice_t = get_q_slice(model, t, dQ)
    q = start_internal_procedure(model_fix_t, Q_slice_t, eps)
    p = calc_p(model_fix_t, q)
    return {k: (abs(p[k[1]] - p[k[0]]) - (2 * v.a * Q_slice_t[k] + v.b))for k, v in model.edges.items()}

def calc_gradient(model, T, dQ, eps):
    w_gradient_by_t = list((calc_W_gradient(model, t, dQ, eps) for t in range(0, T +1)))
    return {
        k: list((reduce(lambda x, tau: x + w_gradient_by_t[tau][k], range(t, T), 0) if (model.indicators[k][t] > 0) else 0 for t in range(0, T +1)))  for k, v in model.edges.items()
    }


def check_eps_for_T(q, q_prev, eps, T):
    if q_prev is None:
        return False
    for key in q.keys():
        for t in range(0, T + 1):
            if not isclose(q[key][t], q_prev[key][t], abs_tol=eps):
                return False
    return True

def start_external_procedure(model, T, eps, c, projector=lambda x: x):
    dq = {k: list((0.0 for t in range(0, T + 1))) for k, v in model.edges.items()}
    counter = 1
    dq_prev = None

    while not check_eps_for_T(dq, dq_prev, eps, T):
        dq_prev = dq
        gradient = calc_gradient(model, T, dq, eps)
        omega = get_current_omega(counter, c)
        dq = projector({k: list((v[t] + omega * gradient[k][t] for t in range(0, T + 1))) for k, v in dq_prev.items()})
        counter += 1
        print dq

    print 'counter: ', counter
    return dq
