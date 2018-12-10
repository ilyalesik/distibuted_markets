from components.inside_procedure import start_internal_procedure, calc_p
from components.models.EdgeModel import EdgeModel
from components.models.IndicatorModel import IndicatorModel
from components.models.InputModel import InputModel
from components.models.NodeModel import NodeModel
from components.planning_external_procedure import start_external_procedure, get_q_slice

# Irkutsk oblast
node1 = NodeModel()\
    .set_A(-0.000109707)\
    .set_B(8.453462922)\


# Krasnoyarsky kray
node3 = NodeModel()\
    .set_A(-8.07931E-05)\
    .set_B(5.0541046)

node6 = NodeModel()\
    .set_A(-0.000864439)\
    .set_B(2.814784174)\


# Irkutsk oblast
node8_vrp = [
    100.0, 119.5, 139.4,
    162.3, 177.3, 200.1,
    219.4466667, 239.3552381, 259.2638095,
    279.172381, 299.0809524, 318.9895238
]
node8 = NodeModel()\
    .set_D(lambda t: -4333.41 + 41.18 * node8_vrp[t])\
    .set_G(lambda t: 1.96)

# SAHA republic
node9_vrp = [
    100, 117.9, 148.5,
    165.4, 174.3, 201.6,
    220.6933333, 240.5247619, 260.3561905,
    280.187619, 300.0190476, 319.8504762
]
node9 = NodeModel()\
    .set_D(lambda t: 1353.56 + 4.78 * node9_vrp[t])\
    .set_G(lambda t: 38.44)

# Sahalinkaya oblast
node10_vrp = [
    100, 124.3, 153,
    163.6, 171.2, 203.7,
    219.6133333, 238.7504762, 257.887619,
    277.0247619, 296.1619048, 315.2990476
]
node10 = NodeModel()\
    .set_D(lambda t: 13123.3 + 12.73 * node10_vrp[t])\
    .set_G(lambda t: 86.21)

# Habarovsky cry
node11_vrp = [
    100, 95.8, 108.3,
    118.7, 135, 148.9,
    155.0333333, 165.6761905, 176.3190476,
    186.9619048, 197.6047619, 208.247619
]
node11 = NodeModel()\
    .set_D(lambda t: -625.39 + 20.47 * node11_vrp[t])\
    .set_G(lambda t: 71.70)


q2p = 0.018900343642611683

edge1_8 = EdgeModel().set_b(q2p * 100).set_c(55000).set_e_tr(0.445)
edge3_1 = EdgeModel().set_b(q2p * 1100).set_c(605000).set_e_tr(4.895)
edge1_6 = EdgeModel().set_b(q2p * 3200).set_c(1760000).set_e_tr(14.24)
edge8_9 = EdgeModel().set_b(q2p * 3200).set_c(1760000).set_e_tr(14.24)
edge11_10 = EdgeModel().set_b(q2p * 1551).set_c(853050).set_e_tr(6.90195)
edge8_11 = EdgeModel().set_b(q2p * 3212).set_c(1766600).set_e_tr(14.2934)

indicators = IndicatorModel((0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0))

far_east_model = InputModel()
far_east_model\
    .add_node(1, node1)\
    .add_node(3, node3)\
    .add_node(6, node6)\
    .add_node(8, node8)\
    .add_node(9, node9)\
    .add_node(10, node10)\
    .add_node(11, node11)\
    .add_edge(1, 8, edge1_8)\
    .add_edge(3, 1, edge3_1)\
    .add_edge(6, 1, edge1_6)\
    .add_edge(8, 9, edge8_9)\
    .add_edge(11, 10, edge11_10)\
    .add_edge(8, 11, edge8_11)\
    .add_indicators(1, 8, indicators)\
    .add_indicators(3, 1, indicators)\
    .add_indicators(6, 1, indicators)\
    .add_indicators(8, 9, indicators)\
    .add_indicators(11, 10, indicators)\
    .add_indicators(8, 11, indicators)