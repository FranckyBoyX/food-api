class FoodItem(object):

    def __init__(self, description, count, added_date):
        self._count = count
        self._description = description
        self._added_date = added_date

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

    @property
    def added_date(self):
        return self._added_date

    def is_depleted(self):
        return self._count == 0
