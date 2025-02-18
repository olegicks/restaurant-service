from django.urls import path
from .views import (
    IndexView,
    DishTypeListView,
    DishListView,
    DishDetailView,
    CookListView,
    CookDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
    toggle_dish_assign,
)

app_name = "restaurant"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("dish_type/", DishTypeListView.as_view(),
         name="dish_type-list"),
    path(
        "dish_type/create/",
        DishTypeCreateView.as_view(),
        name="dish_type-create",
    ),
    path(
        "dish_type/<int:pk>/update",
        DishTypeUpdateView.as_view(),
        name="dish_type-update",
    ),
    path(
        "dish_type/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish_type-delete"
    ),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path(
        "dishes/create/",
        DishCreateView.as_view(),
        name="dish-create",
    ),
    path(
        "dish/<int:pk>/update",
        DishUpdateView.as_view(),
        name="dish-update",
    ),
    path(
        "dishes/<int:pk>/toggle-assign/",
        toggle_dish_assign,
        name="toggle-dish-assign",
    ),
    path(
        "dish/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish-delete"
    ),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("cooks/", CookListView.as_view(), name="cook-list"),

    path(
        "cooks/create/",
        CookCreateView.as_view(),
        name="cook-create",
    ),
    path(
        "cook/<int:pk>/update",
        CookUpdateView.as_view(),
        name="cook-update",
    ),
    path(
        "cook/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete"
    ),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),

]
