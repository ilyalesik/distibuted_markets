from components.inside_procedure import start_internal_procedure, calc_p
from components.planning_external_procedure import start_external_procedure, get_q_slice
from launchers.russian_far_east_model_2node import far_east_model

T = 4
eps = 0.0001
Q = {
    (1, 9): 1667.1
}
model_fix_t = far_east_model.get_input_model_with_fix_t(0)
q = start_internal_procedure(model_fix_t, Q, eps)
print "q: ", q
p = calc_p(model_fix_t, q)
print "p: ", p
p_for_1250 = calc_p(model_fix_t, {(1, 9): 1250.71})
print "p_for_1250: ", p_for_1250