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
    .set_A(-0.000109707)\
    .set_B(8.453462922)\
    .set_D(lambda t: -4333.41 + 41.18 * node1_vrp[t])\
    .set_G(lambda t: 1.96)

# INK
node2 = NodeModel()\
    .set_A(-0.000215307)\
    .set_B(8.972875855)

# Krasnoyarsky kray
node3 = NodeModel()\
    .set_A(-8.07931E-05)\
    .set_B(5.0541046)

# Vankorneft
node4 = NodeModel()\
    .set_A(-5.50176E-05)\
    .set_B(7.796642159)

# Taymirgaz
node5 = NodeModel()\
    .set_A(0.000344828)\
    .set_B(-17.08092826)

# SurgutNefteGaz Yakytia
node7 = NodeModel()\
    .set_A(-0.001414107)\
    .set_B(4.730167224)

# SAHA republic
node9_vrp = [
    328201.7, 403658.5, 508674.4,
    566387, 597037.4, 690642.5,
    760772.2467, 830773.7695, 900775.2924,
    970776.8152, 1040778.338, 1110779.861
]
node9 = NodeModel()\
    .set_A(-0.000864439)\
    .set_B(2.814784174)\
    .set_D(lambda t: 1353.56 + 4.78 * node9_vrp[t])\
    .set_G(lambda t: 38.44)

# Sahalinkaya oblast
node10_vrp = [
    392380.1, 487659.5, 600247.9,
    641886.4, 671743.6, 799165.4,
    861628.88, 936709.3743, 1011789.869,
    1086870.363, 1161950.857, 1237031.351
]
node10 = NodeModel()\
    .set_D(lambda t: 13123.3 + 12.73 * node10_vrp[t])\
    .set_G(lambda t: 86.21)

# Habarovsky cry
node11_vrp = [
    276895.4, 353590.3, 399594.2,
    437994.3, 498067.2, 549289.3,
    602618.48, 655012.7743, 707407.0686,
    759801.3629, 812195.6571, 864589.9514
]
node11 = NodeModel()\
    .set_D(lambda t: -625.39 + 20.47 * node11_vrp[t])\
    .set_G(lambda t: 71.70)

# Primorsky cry
node12_vrp = [
    368996.7, 470679.2, 549722.8,
    557489.3, 577473.9, 643464.9,
    698020.2933, 746605.7676,  795191.2419,
    843776.7162, 892362.1905, 940947.6648
]
node12 = NodeModel()\
    .set_D(lambda t: -4230.52 + 45.44 * node12_vrp[t])\
    .set_G(lambda t: 181.91)

# missing: node 6 = 9, 8 = 1
q2p = 0.018900343642611683

edge2_1 = EdgeModel().set_b(q2p * 1200).set_c(660000).set_e_tr(5.34)
edge3_1 = EdgeModel().set_b(q2p * 1100).set_c(605000).set_e_tr(4.895)
edge4_5 = EdgeModel().set_b(q2p * 410).set_c(225500).set_e_tr(1.8245)
edge5_3 = EdgeModel().set_b(q2p * 1501).set_c(825550).set_e_tr(6.67945)
edge7_9 = EdgeModel().set_b(q2p * 100).set_c(55000).set_e_tr(0.445)
edge1_9 = EdgeModel().set_b(q2p * 3200).set_c(1760000).set_e_tr(14.24)
edge11_10 = EdgeModel().set_b(q2p * 1551).set_c(853050).set_e_tr(6.90195)
edge1_11 = EdgeModel().set_b(q2p * 3212).set_c(1766600).set_e_tr(14.2934)
edge11_12 = EdgeModel().set_b(q2p * 754).set_c(414700).set_e_tr(3.3553)

indicators = IndicatorModel((1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0))

model = InputModel()
model\
    .add_node(1, node1)\
    .add_node(2, node2)\
    .add_node(3, node3)\
    .add_node(4, node4)\
    .add_node(5, node5)\
    .add_node(7, node7)\
    .add_node(9, node9)\
    .add_node(10, node10)\
    .add_node(11, node11)\
    .add_node(12, node12)\
    .add_edge(2, 1, edge2_1)\
    .add_edge(3, 1, edge3_1)\
    .add_edge(4, 5, edge4_5)\
    .add_edge(5, 3, edge5_3)\
    .add_edge(7, 9, edge7_9)\
    .add_edge(1, 9, edge1_9)\
    .add_edge(11, 10, edge11_10)\
    .add_edge(1, 11, edge1_11)\
    .add_edge(11, 12, edge11_12)\
    .add_indicators(2, 1, indicators)\
    .add_indicators(3, 1, indicators)\
    .add_indicators(4, 5, indicators)\
    .add_indicators(5, 3, indicators)\
    .add_indicators(7, 9, indicators)\
    .add_indicators(1, 9, indicators)\
    .add_indicators(11, 10, indicators)\
    .add_indicators(1, 11, indicators)\
    .add_indicators(11, 12, indicators)

T = 1
q = start_external_procedure(model, T, 0.01, 0.001)
print '----------------------'
print q