from common import check_eps


def find_c(Q):
    return reduce(lambda x, value: x + value ** 2, Q.itervalues(), 0)


def projector(q, Q_max):
    return {k: (-1 if v < 0 else 1) * min(abs(v), abs(Q_max[k])) if k in Q_max else v for k, v in q.items()}


def start_internal_procedure(model, Q, eps):
    q = {k: 0.0 for k, v in model.edges}
    counter = 0
    q_prev = None

    while not check_eps(q, q_prev, eps):
        q_prev = q
        # todo eval new q
