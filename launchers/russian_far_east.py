from components.planning_external_procedure import start_external_procedure
from launchers.russian_far_east_model_reduced import far_east_model

T = 10
q = start_external_procedure(far_east_model, T, 0.0001, 0.1)
print '----------------------'
print q