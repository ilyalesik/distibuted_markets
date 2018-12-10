from components.planning_external_procedure import start_external_procedure
from launchers.russian_far_east_model import far_east_model

T = 10
q = start_external_procedure(far_east_model, T, 0.001, 0.1, 0.001)
print '----------------------'
print q