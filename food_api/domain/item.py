class Item(object):

    def __init__(self, description, count):
        self.count = count
        self.description = description

    def increment_count(self):
        self._set_count(self.count + 1)

    def decrement_count(self):
        self._set_count(self.count - 1)

    def set_count(self, count):
        self._set_count(count)

    def set_description(self, description):
        self.description = description

    def is_depleted(self):
        return self.count == 0

    def _set_count(self, count):
        if count < 0:
            count = 0
        self.count = count
