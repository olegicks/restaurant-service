from django.urls import path
from .views import IndexView, DishTypeListView, DishListView, DishDetailView

app_name = "restaurant"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("dish_type/", DishTypeListView.as_view(),
         name="dish_type-list"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),

]
