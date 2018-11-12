from components.inside_procedure import start_internal_procedure, calc_p
from components.models.EdgeModel import EdgeModel
from components.models.IndicatorModel import IndicatorModel
from components.models.InputModel import InputModel
from components.models.NodeModel import NodeModel
from components.planning_external_procedure import start_external_procedure, get_q_slice

# Irkutsk oblast
node1_vrp = [
    100.0, 119.5, 139.4,
    162.3, 177.3, 200.1,
    219.4466667, 239.3552381, 259.2638095,
    279.172381, 299.0809524, 318.9895238
]
node1 = NodeModel()\
    .set_A(-0.000109707)\
    .set_B(8.453462922)\
    .set_D(lambda t: -4333.41 + 41.18 * node1_vrp[t])\
    .set_G(lambda t: 1.96)


# SAHA republic
node9_vrp = [
    100, 117.9, 148.5,
    165.4, 174.3, 201.6,
    220.6933333, 240.5247619, 260.3561905,
    280.187619, 300.0190476, 319.8504762
]
node9 = NodeModel()\
    .set_A(-0.000864439)\
    .set_B(2.814784174)\
    .set_D(lambda t: 1353.56 + 4.78 * node9_vrp[t])\
    .set_G(lambda t: 38.44)


# missing: node 6 = 9, 8 = 1
q2p = 0.018900343642611683

edge1_9 = EdgeModel().set_b(q2p * 3200).set_c(1760000).set_e_tr(14.24)

indicators = IndicatorModel((1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0))

far_east_model = InputModel()
far_east_model\
    .add_node(1, node1)\
    .add_node(9, node9)\
    .add_edge(1, 9, edge1_9)\
    .add_indicators(1, 9, indicators)