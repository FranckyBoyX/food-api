import time
from unittest import TestCase, mock

from food_api.domain.food_item import FoodItem
from food_api.use_cases.item_use_case import ItemUseCase


class TestItemUseCase(TestCase):

    def setUp(self):
        repo = mock.Mock()

        food_item1 = FoodItem("food item 1", 3, int(time.time()))
        food_item2 = FoodItem("food item 2", 5, int(time.time()))
        self.food_list = [food_item1, food_item2]

        repo.list.return_value = self.food_list
        self.my_item_use_case = ItemUseCase(repo)

    def test_list_items(self):
        items = self.my_item_use_case.list_items()

        self.assertListEqual(self.food_list, items)

