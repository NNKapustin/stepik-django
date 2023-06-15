from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

todo_list = {
    'monday': "Дела на понедельник.",
    'tuesday': "Дела на вторник.",
    'wednesday': "Дела на среду.",
    'thursday': "Дела на четверг.",
    'friday': "Дела на пятницу.",
    'saturday': "Дела на субботу.",
    'sunday': "Дела на воскресенье."
}


def get_todo_list(request, day):
    what_to_do = todo_list.get(day)
    if what_to_do:
        return HttpResponse(what_to_do)
    else:
        return HttpResponseNotFound(f"Неизвестный день недели - {day}")


def get_todo_list_by_number(request, day):
    if 1 <= day <= 7:
        day_name = list(todo_list)[day - 1]
        redirect_url = reverse('day-url', args=[day_name])
        return redirect(redirect_url)
    else:
        return HttpResponseNotFound(f"Неверный номер дня - {day}")
