import random
from common import check_eps
from inside_procedure import start_internal_procedure, calc_p


def calc_delta_tw_stochastic_gradient(model, Q, eps):
    t = random.uniform(0, 24)
    model_fix_t = model.get_data_model_with_fix_t(t)
    q = start_internal_procedure(model_fix_t, Q, eps)
    p = calc_p(model, q)
    return {k: 24 * (p[k[1]] - p[k[0]]) - (2 * v['a'] * Q[k] + v['b']) for k, v in model.edges.items()}


def start_external_procedure(model, eps):
    q = {k: 0.0 for k, v in model.edges.items()}
    counter = 0
    q_prev = None

    while not check_eps(q, q_prev, eps):
        q_prev = q
        delta_w = calc_delta_tw_stochastic_gradient(model, q, eps)
        #todo eval new q
