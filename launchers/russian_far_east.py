from components.planning_external_procedure import start_external_procedure
from launchers.russian_far_east_model import far_east_model

T = 1
q = start_external_procedure(far_east_model, T, 0.01, 0.001)
print '----------------------'
print q