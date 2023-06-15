from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

import datetime

zodiac_dict = {
    'aries': "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    'taurus': "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    'gemini': "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    'cancer': "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    'leo': "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    'virgo': "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    'libra': "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    'scorpio': "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    'sagittarius': "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    'capricorn': "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    'aquarius': "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    'pisces': "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}

zodiac_types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}

zodiac_dates = {
    'aries': [80, 110],
    'taurus': [111, 141],
    'gemini': [142, 172],
    'cancer': [173, 203],
    'leo': [204, 233],
    'virgo': [234, 266],
    'libra': [267, 296],
    'scorpio': [297, 326],
    'sagittarius': [327, 356],
    'capricorn': [357, 20],
    'aquarius': [21, 50],
    'pisces': [51, 79]
}


def index(request):
    zodiacs = list(zodiac_dict)
    li_elements = ""
    for sign in zodiacs:
        redirect_url = reverse('horoscope-name', args=[sign])
        li_elements += f"<li><a href='{redirect_url}'>{sign.title()}</a></li>"
    response = f"<ol>{li_elements}</ol>"
    return HttpResponse(response)


def get_zodiac_types(request):
    types = list(zodiac_types)
    li_elements = ""
    for item in types:
        redirect_url = reverse('zodiac-of-type', args=[item])
        li_elements += f"<li><a href='{redirect_url}'>{item.title()}</a></li>"
    response = f"<ul>{li_elements}</ul>"
    return HttpResponse(response)


def get_signs_of_type(request, zodiac_type):
    list_of_type = zodiac_types.get(zodiac_type)
    li_elements = ""
    for item in list_of_type:
        redirect_url = reverse('horoscope-name', args=[item])
        li_elements += f"<li><a href='{redirect_url}'>{item.title()}</a></li>"
    response = f"<ul>{li_elements}</ul>"
    return HttpResponse(response)


def get_info_about_sign_zodiac(request, zodiac_sign: str):
    description = zodiac_dict.get(zodiac_sign)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f"Неизвестный знак зодиака - {zodiac_sign}")


def get_info_about_sign_zodiac_by_number(request, zodiac_sign: int):
    if 1 <= zodiac_sign <= len(zodiac_dict):
        zodiac = list(zodiac_dict)[zodiac_sign - 1]
        redirect_url = reverse('horoscope-name', args=[zodiac])
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f"Неизвестный номер знака зодиака - {zodiac_sign}")


def get_info_by_date(request, month, day):
    if not (1 <= month <= 12 and 1 <= day <= 31):
        return HttpResponseNotFound(f"Указана не корректная дата - {day}.{month}")
    date = datetime.date(2023, month, day)
    day_number = date.timetuple().tm_yday
    response = ''
    for key, val in zodiac_dates.items():
        if val[0] <= day_number <= val[1]:
            response = key
    redirect_url = reverse('horoscope-name', args=[response])
    return HttpResponseRedirect(redirect_url)

