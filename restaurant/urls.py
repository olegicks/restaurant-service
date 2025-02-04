from django.urls import path
from .views import IndexView

app_name = "restaurant"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
