import random
from common import check_eps
from components.common import get_current_omega
from inside_procedure import start_internal_procedure, calc_p


def calc_delta_tw_stochastic_gradient(model, Q, eps):
    t = random.uniform(0, 24)
    model_fix_t = model.get_data_model_with_fix_t(t)
    q = start_internal_procedure(model_fix_t, Q, eps)
    p = calc_p(model_fix_t, q)
    pr = reduce(lambda x, (k, v): x + 0.25 * p[k] ** 2 / v['A'], model_fix_t.nodes.items(), 0)
    cs = reduce(lambda x, (k, v): x + 0.5 * v['D'] ** 2 / v['G'] - v['D'] * p[k] + 0.5 * v['G'] * p[k] ** 2, model_fix_t.nodes.items(), 0)
    prt = reduce(lambda x, (k, v): x + (p[k[1]] - p[k[0]]) * q[k], model_fix_t.edges.items(), 0)
    e = reduce(lambda x, (k, v): x + v['a'] * Q[k] ** 2 + v['b'] * Q[k] + v['c'], model_fix_t.edges.items(), 0)
    tw = 24 * (pr + cs + prt) - e
    return {
        'gradient': {k: 24 * (p[k[1]] - p[k[0]]) - (2 * v['a'] * Q[k] + v['b']) for k, v in model.edges.items()},
        't': t,
        'tw': tw
    }


def start_external_procedure(model, eps, c, projector=lambda x: x):
    q = {k: 0.0 for k, v in model.edges.items()}
    counter = 1
    q_prev = None

    while not check_eps(q, q_prev, eps):
        q_prev = q
        delta_tw_dict = calc_delta_tw_stochastic_gradient(model, q, eps)
        delta_tw = delta_tw_dict['gradient']
        omega = get_current_omega(counter, c)
        q = projector({k: v + omega * delta_tw[k] for k, v in q_prev.items()})
        counter += 1
        print q, ' :: ', delta_tw_dict['tw'], ' :: ', delta_tw_dict['t']

    print 'counter: ', counter
    return q
