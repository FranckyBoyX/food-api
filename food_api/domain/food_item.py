class FoodItem(object):

    def __init__(self, description, count):
        self._count = count
        self._description = description

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        if count < 0:
            count = 0
        self._count = count

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    def is_depleted(self):
        return self._count == 0
