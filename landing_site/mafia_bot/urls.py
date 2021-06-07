from .views import *
from django.urls import path

urlpatterns = [
    path("", main_sample, name="main_sample")
]
