from unittest import TestCase

from food_api.domain.food_item import FoodItem


class TestFoodItem(TestCase):

    def setUp(self):
        self.initial_description = "my food item"
        self.initial_count = 3
        self.my_food_item = FoodItem(self.initial_description, self.initial_count)

    def test_food_item_init(self):
        self.assertEqual(self.initial_description, self.my_food_item.description)
        self.assertEqual(self.initial_count, self.my_food_item.count)

    def test_update_count(self):
        new_count = 5
        self.my_food_item.count = new_count

        self.assertEqual(new_count, self.my_food_item.count)

    def test_update_count_below_zero(self):
        self.my_food_item.count = -5

        self.assertEqual(0, self.my_food_item.count)

    def test_update_description(self):
        new_description = "new description"
        self.my_food_item.description = new_description

        self.assertEqual(new_description, self.my_food_item.description)

    def test_when_depleted_then_return_true(self):
        self.my_food_item.count = 0

        self.assertTrue(self.my_food_item.is_depleted())

    def test_when_not_depleted_then_return_false(self):
        self.assertFalse(self.my_food_item.is_depleted())
