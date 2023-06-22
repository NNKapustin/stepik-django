from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='split') # имя для вызова в html, если не указать name оно возьмет название функции
@stringfilter # гарантирует получение строки в value
def split(value, key=' '):
    return value.split(key)


@register.filter(name='times')
def times(value):
    return list(range(value))


@register.filter(name='filter_range')
def filter_range(start, stop):
    return list(range(start, stop))
