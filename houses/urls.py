from django.urls import path

from .views import HouseList, HouseDetail

urlpatterns = [
    path("<int:pk>", HouseDetail.as_view()),
    path("", HouseList.as_view())
]
