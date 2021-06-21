from .views import *
from django.urls import path

urlpatterns = [
    path("", main_sample, name="main_sample"),
    path("second/", second, name="second"),
    path("third/", third, name="third")
]
