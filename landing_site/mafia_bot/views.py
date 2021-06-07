from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def main_sample(request):
    return HttpResponse("главная страница")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
