from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

menu = [{"title": "Главная", "url_name": "main_sample"},
        {"title": "second", "url_name": "second"},
        {"title": "third", "url_name": "third"}]


def main_sample(request):
    context = {"menu": menu, "title": "один", "modes": ["common", "extreme", "special", "random"]}
    return render(request, "mafia_bot/main_sample.html", context=context)


def second(request):
    context = {"menu": menu, "title": "два"}
    return render(request, "mafia_bot/second.html", context=context)


def third(request):
    context = {"menu": menu, "title": "три"}
    return render(request, "mafia_bot/third.html", context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
