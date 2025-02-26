from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from restaurant.models import DishType, Dish


DISH_URL = reverse("restaurant:dish-list")
DISH_TYPE_URL = reverse("restaurant:dish_type-list")
COOK_URL = reverse("restaurant:cook-list")


class TestSearchViews(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="TestUser",
            password="TestPassword",
        )
        self.client.force_login(self.user)

    def test_search_dish_by_model(self):

        dish_type = DishType.objects.create(name="TestDishType")
        Dish.objects.create(name="Test1", price=123, dish_type=dish_type)
        Dish.objects.create(name="Test2", price=123, dish_type=dish_type)
        Dish.objects.create(name="Test3", price=123, dish_type=dish_type)
        response = self.client.get(DISH_URL, {"name": "2"})
        queryset = response.context["object_list"]
        self.assertEqual(len(queryset), 2)

    def test_search_dish_type_by_name(self):

        DishType.objects.create(
            name="Test1",
        )
        DishType.objects.create(
            name="Test2",
        )
        DishType.objects.create(
            name="Test3",
        )
        response = self.client.get(DISH_TYPE_URL, {"name": "2"})
        queryset = response.context["object_list"]
        self.assertEqual(len(queryset), 2)

    def test_search_cook_by_username(self):

        get_user_model().objects.create_user(
            username="TestUser1",
            password="TestPassword1",
            years_of_experience=3,
        )
        get_user_model().objects.create_user(
            username="TestUser2",
            password="TestPassword2",
            years_of_experience=4,
        )
        get_user_model().objects.create_user(
            username="TestUser3",
            password="TestPassword3",
            years_of_experience=5,
        )
        response = self.client.get(COOK_URL, {"username": "2"})
        queryset = response.context["object_list"]
        self.assertEqual(len(queryset), 2)
