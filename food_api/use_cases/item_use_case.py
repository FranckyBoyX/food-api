
class ItemUseCase(object):

    def __init__(self, repo):
        self.repo = repo

    def list_items(self):
        return self.repo.list()

    def increment_item_count(self, food_item):
        food_item.count += 1
        self.repo.update(food_item)

    def decrement_item_count(self, food_item):
        food_item.count -= 1
        self._update_if_not_depleted(food_item)

    def change_description(self, food_item, description):
        food_item.description(description)
        self.repo.update(food_item)

    def add_item(self, food_item):
        self.repo.add(food_item)

    def remove_item(self, food_item):
        self.repo.remove(food_item)

    def _update_if_not_depleted(self, food_item):
        if food_item.is_depleted():
            self.repo.remove(food_item)
        else:
            self.repo.update(food_item)
