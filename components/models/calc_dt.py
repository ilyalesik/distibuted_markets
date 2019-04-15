
def calc_dt(i, t, T):
    if t == T - 1:
        return 1 / (i * (1 + i) ** t)
    return (1 / (1 + i)) ** t