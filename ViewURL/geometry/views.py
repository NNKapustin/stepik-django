from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from math import pi


def rectangle_area(request, width, height):
    return HttpResponse(f"Площадь прямоугольника размером {width}x{height} равна {width * height}")


def square_area(request, width):
    return HttpResponse(f"Площадь квадрата размером {width}x{width} равна {width ** 2}")


def circle_area(request, radius):
    return HttpResponse(f"Площадь круга радиуса {radius} равна {pi * radius ** 2:.2f}")


# можно использовать HttpResponseRedirect или redirect, но используем в одном проекте один способ
def get_rectangle_area(request, width, height):
    url_redirect = reverse('url-rectangle', args=[width, height])
    return HttpResponseRedirect(url_redirect)


def get_square_area(request, width):
    url_redirect = reverse('url-square', args=[width])
    return redirect(url_redirect)


def get_circle_area(request, radius):
    url_redirect = reverse('url-circle', args=[radius])
    return redirect(url_redirect, permanent=True)
