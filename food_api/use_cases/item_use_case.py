class ItemUseCase(object):

    def __init__(self, repo):
        self.repo = repo

    def list_items(self):
        return self.repo.list()

    def increment_item_count(self, item):
        item.increment_count()
        self.repo.update(item)

    def decrement_item_count(self, item):
        item.decrement_count()
        self._update_if_not_depleted(item)

    def change_description(self, item, description):
        item.set_description(description)
        self.repo.update(item)

    def change_count(self, item, count):
        item.set_count(count)
        self._update_if_not_depleted(item)

    def add_item(self, item):
        self.repo.add(item)

    def remove_item(self, item):
        self.repo.remove(item)

    def _update_if_not_depleted(self, item):
        if item.is_depleted():
            self.repo.remove(item)
        else:
            self.repo.update(item)
