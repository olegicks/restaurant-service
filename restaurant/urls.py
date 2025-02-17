from django.urls import path
from .views import (
    IndexView,
    DishTypeListView,
    DishListView,
    DishDetailView,
    CookListView,
    CookDetailView,
)

app_name = "restaurant"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("dish_type/", DishTypeListView.as_view(),
         name="dish_type-list"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),

]
