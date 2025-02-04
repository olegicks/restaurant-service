from django.urls import path
from .views import IndexView, DishTypeListView

app_name = "restaurant"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("dish_type/", DishTypeListView.as_view(),
         name="dish_type-list"),
]
