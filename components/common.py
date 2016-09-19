def check_eps(q, q_prev, eps):
    if q_prev is None:
        return False
    for key in q.keys():
        if abs(q[key] - q_prev[key]) > eps:
            return False
    return True