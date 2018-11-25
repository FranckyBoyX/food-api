class FoodItem(object):

    def __init__(self, description, count):
        self.count = count
        self.description = description

    @property
    def count(self):
        return self.count()

    @count.setter
    def count(self, count):
        if count < 0:
            count = 0
        self.count = count

    @property
    def description(self):
        return self.description

    @description.setter
    def description(self, description):
        self.description = description

    def is_depleted(self):
        return self.count == 0
