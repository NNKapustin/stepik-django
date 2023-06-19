from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('people/', views.get_people_list)
]
