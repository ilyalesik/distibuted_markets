from components.planning_external_procedure import start_external_procedure
from launchers.russian_far_east_model_reduced import far_east_model

q_initial={(1, 8): 7000, (3, 1): 3300, (6, 1): 1500, (8, 9): 1400, (11, 10): 1400, (8, 11): 1900}

T = 10
q = start_external_procedure(far_east_model, T, 0.001, 0.1, 0.1, 0.01, q_initial)
print '----------------------'
print q