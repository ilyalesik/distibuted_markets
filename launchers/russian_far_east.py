from components.models.EdgeModel import EdgeModel
from components.models.IndicatorModel import IndicatorModel
from components.models.InputModel import InputModel
from components.models.NodeModel import NodeModel
from components.planning_external_procedure import start_external_procedure

# Irkutsk oblast
node1_vrp = [
    458774.9, 224364.2, 261550.4,
    304545.5, 332700.5, 375481.9,
    321390.1333, 320005.5333, 318620.9333,
    317236.3333, 315851.7333, 314467.1333
]
node1 = NodeModel()\
    .set_A(1.03)\
    .set_D(lambda t: -4333.41 + 41.18 * node1_vrp[t])\
    .set_G(lambda t: 1.96)