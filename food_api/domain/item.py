class Item(object):

    def __init__(self, description, count):
        self.count = count
        self.description = description

    def increment_count(self):
        self.count += 1

    def decrement_count(self):
        self.count -= 1
        if self.count < 0:
            self.count = 0

    def set_count(self, count):
        new_count = 0
        if new_count > 0:
            new_count = count
        self.count = new_count

    def set_description(self, description):
        self.description = description
