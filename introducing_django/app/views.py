from django.shortcuts import render, reverse
from django.http import HttpResponse
from datetime import datetime
import os


# Create your views here.
def home_view(request):
    template_name = "home.html"

    pages = {
        "Главная страница": reverse("home"),
        "Показать текущее время": reverse("time"),
        "Показать содержимое рабочей директории": reverse("workdir"),
    }

    context = {
        "pages": pages,
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now()
    msg = f"Текущая дата и время: {current_time.strftime('%Y-%m-%d %H:%M:%S')}"
    msg += "<br><br><a href='/'>Назад на главную</a>"
    return HttpResponse(msg)


def workdir_view(request):
    files = os.listdir()
    html = "<h1>Файлы в папке:</h1><col>"
    for file in files:
        html += f"<li>{file}</li>"
    html += "</col>"

    html += "<br><br><a href='/'>Назад на главную</a>"

    return HttpResponse(html)
