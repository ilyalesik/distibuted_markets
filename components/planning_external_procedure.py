import random
from common import check_eps, isclose
from components.common import get_current_omega
from inside_procedure import start_internal_procedure, calc_p

def get_q_slice(model, t, dQ):
    return {
        k: reduce(lambda x, tau: x + dQ[k][tau], range(0, t + 1), 0) for k, v in model.edges.items()
    }

def calc_W_gradient(model, t, dQ, eps):
    model_fix_t = model.get_input_model_with_fix_t(t)
    Q_slice_t = get_q_slice(model, t, dQ)
    q = start_internal_procedure(model_fix_t, Q_slice_t, eps)
    p = calc_p(model_fix_t, q)
    pr = reduce(lambda x, (k, v): x + 0.25 * p[k] ** 2 / v.A - 0.5 * v.B / v.A * p[k] if v.A != 0 else 0, model_fix_t.nodes.items(), 0)
    cs = reduce(lambda x, (k, v): x + 0.5 * v.D ** 2 / v.G - v.D * p[k] + 0.5 * v.G * p[k] ** 2 if v.G != 0 else 0,
                model_fix_t.nodes.items(), 0)
    prt = reduce(lambda x, (k, v): x + (p[k[1]] - p[k[0]]) * q[k], model_fix_t.edges.items(), 0)
    e = reduce(lambda x, (k, v): x + v.a * dQ[k][t] ** 2 + v.b * dQ[k][t], model_fix_t.edges.items(), 0)
    tw = (pr + cs + prt) - e
    return {
        'gradient': {k: (p[k[1]] - p[k[0]] - (2 * v.a * Q_slice_t[k] + v.b + v.e_tr))for k, v in model.edges.items()},
        'tw': tw
    }

def calc_gradient(model, T, dQ, eps):
    w_gradient_by_t = list((calc_W_gradient(model, t, dQ, eps) for t in range(0, T +1)))
    return {
        'gradient': {k: list((reduce(lambda x, tau: x + w_gradient_by_t[tau]['gradient'][k], range(t, T), 0) if (model.indicators[k][t] > 0) else 0 for t in range(0, T +1)))  for k, v in model.edges.items()},
        'tw': reduce(lambda x, t: x + w_gradient_by_t[t]['tw'], range(0, T + 1), 0)
    }


def check_eps_for_T(q, q_prev, eps, T):
    if q_prev is None:
        return False
    for key in q.keys():
        for t in range(0, T + 1):
            if not isclose(q[key][t], q_prev[key][t], abs_tol=eps):
                return False
    return True


def calc_conditions(model, T, dQ, eps):
    w_gradient_by_t = list((calc_W_gradient(model, t, dQ, eps) for t in range(0, T + 1)))
    return {
        k: list(
            (reduce(lambda x, tau: x + w_gradient_by_t[tau][k], range(t, T), 0) - (v.b) if (model.indicators[k][t] > 0) else 0
             for t in range(0, T + 1))) for k, v in model.edges.items()
    }


def start_external_procedure(model, T, eps, c, projector=lambda x: x):
    dq = {k: list((0.0 for t in range(0, T + 1))) for k, v in model.edges.items()}
    counter = 1
    dq_prev = None
    max_tw = None
    tw = None

    while True:
        dq_prev = dq
        gradient = calc_gradient(model, T, dq, eps)
        omega = get_current_omega(counter, c)
        dq = projector({k: list((v[t] + omega * abs(gradient['gradient'][k][t]) for t in range(0, T + 1))) for k, v in dq_prev.items()})
        counter += 1
        tw = gradient['tw']
        print 'tw', tw
        if (max_tw is not None) and (tw > max_tw) and (tw - max_tw < eps):
            break
        if max_tw is None or tw > max_tw:
            max_tw = tw
        print dq

    print 'counter: ', counter
    print 'conditions: ', calc_conditions(model, T, dq, eps)
    return dq
