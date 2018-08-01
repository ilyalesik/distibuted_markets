
class IndicatorModel:
    indicator_items = {}

    def __init__(self, items):
        self.indicator_items = items

    def __getitem__(self, i):
        return self.indicator_items[i]