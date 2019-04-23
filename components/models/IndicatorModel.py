
class IndicatorModel:
    indicator_items = {}

    def __init__(self, items):
        self.indicator_items = items

    def __getitem__(self, i):
        return self.indicator_items[i]

    def __str__(self):
        return "(" + reduce(lambda prev, item: str(item) if prev is None else prev + "," + str(item), self.indicator_items, None) + ")"