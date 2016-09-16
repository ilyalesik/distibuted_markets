import random


def check_eps(q, q_prev, eps):
    if q_prev is None:
        return False
    for key in q.keys():
        if abs(q[key] - q_prev[key]) > eps:
            return False
    return True


def calc_delta_w_gradient(model, q):
    t = random.uniform(0, 24)


def start_external_procedure(model, eps):
    q = {k: 0.0 for k, v in model.edges}
    counter = 0
    q_prev = None

    while not check_eps(q, q_prev, eps):
        q_prev = q
        delta_w = calc_delta_w_gradient(model, q)
