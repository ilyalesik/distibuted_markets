from components.inside_procedure import start_internal_procedure, calc_p
from components.planning_external_procedure import start_external_procedure, get_q_slice
from launchers.russian_far_east_model import far_east_model

T = 1
eps = 0.001
Q = {
    (2, 1): 1251.1,
    (3, 1): 10606.6,
    (4, 5): 6933.6,
    (5, 3): 2205.2,
    (7, 9): 704.2,
    (1, 9): 1667.1,
    (11, 10): 14010.6,
    (1, 11): 1828.0,
    (11, 12): 490.6
}
model_fix_t = far_east_model.get_input_model_with_fix_t(0)
q = start_internal_procedure(model_fix_t, Q, eps)
print "q: ", q
p = calc_p(model_fix_t, q)
print "p: ", p