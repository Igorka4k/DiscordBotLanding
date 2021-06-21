from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

menu = [{"title": "Главная", "url_name": "main_sample"},
        {"title": "second", "url_name": "second"},
        {"title": "third", "url_name": "third"}]


def main_sample(request):
    return render(request, "landing/main_sample.html", context={"menu": menu, "title": "один"})


def second(request):
    return render(request, "landing/second.html", context={"menu": menu, "title": "два"})


def third(request):
    return render(request, "landing/third.html", context={"menu": menu, "title": "три"})


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
