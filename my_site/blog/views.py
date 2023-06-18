from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request, 'blog/index.html')


def blog(request):
    return render(request, 'blog/list_detail.html')


def get_post_info(request, name_post):
    return render(request, 'blog/detail_by_name.html', context={'name': name_post})


def get_post_info_by_number(request, number_post):
    return render(request, 'blog/detail_by_number.html', context={'number': number_post})
