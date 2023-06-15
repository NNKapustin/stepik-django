from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<int:month>/<int:day>/', views.get_info_by_date),
    path('types/', views.get_zodiac_types),
    path('types/<zodiac_type>/', views.get_signs_of_type, name='zodiac-of-type'),
    path('<int:zodiac_sign>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:zodiac_sign>/', views.get_info_about_sign_zodiac, name='horoscope-name'),
]
