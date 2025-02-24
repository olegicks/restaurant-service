from django.contrib.auth import get_user_model
from django.test import TestCase
from restaurant.models import DishType, Cook, Dish


class TestModels(TestCase):

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="TestManufacturer",
        )
        self.assertEqual(
            str(dish_type),
            f"{dish_type.name}"
        )

    def test_cook_str(self):
        dish_type = DishType.objects.create(
            name="TestManufacturer",
        )
        dish = Dish.objects.create(name="TestModel", price=123, dish_type=dish_type)
        self.assertEqual(
            str(dish),
            dish.name
        )

    def test_create_cook_with_years_of_experience(self):
        username = "Test"
        password = "Test1234"
        years_of_experience = 5
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience
        )
        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password))
        self.assertEqual(cook.years_of_experience, years_of_experience)
