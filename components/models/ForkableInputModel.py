from components.models.IndicatorModel import IndicatorModel
from components.models.InputModel import InputModel


class ForkableInputModel(InputModel):

    def __init__(self):
        InputModel.__init__(self)

    def cloneWithNewIndicators(self, k, indicators):
        newModel = InputModel()
        newModel.nodes = self.nodes
        newModel.edges = self.nodes,
        newModel.indicators = self.indicators.copy()
        newModel.indicators[k] = indicators
        return newModel

    def fork(self, T):
        new_items = []
        for k in self.indicators:
            for t in range(0, T):
                if self.indicators[k][t] == 0:
                    new_indicators = IndicatorModel([self.indicators[k][t1] if t1 != t else 1 for t1 in range(0, T)])
                    new_node = self.cloneWithNewIndicators(k, new_indicators)
                    new_items.append(new_node)
        return new_items
