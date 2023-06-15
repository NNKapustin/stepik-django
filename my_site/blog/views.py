from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return HttpResponse("Главная страница")


def blog(request):
    return HttpResponse("Все посты блога")


def get_post_info(request, name_post):
    return HttpResponse(f"Информация о посте {name_post}")


def get_post_info_by_number(request, number_post):
    return HttpResponse(f"Здесь содержится информация о посте под номером {number_post}")
