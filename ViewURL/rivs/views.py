from django.shortcuts import render
from dataclasses import dataclass


@dataclass
class Info:
    year: int
    city: str
    film: str


def index(request):
    info = Info(1964, 'Бейрут', 'На гребне волны')
    data = {
        'year_born': info.year,
        'city_born': info.city,
        'movie_name': info.film,
    }
    return render(request, 'rivs/index.html', context=data)
