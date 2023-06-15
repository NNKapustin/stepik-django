from django.urls import path
from . import views


urlpatterns = [
    path('rectangle/<int:width>/<int:height>/', views.rectangle_area, name='url-rectangle'),
    path('square/<int:width>/', views.square_area, name='url-square'),
    path('circle/<int:radius>/', views.circle_area, name='url-circle'),
    path('get_rectangle_area/<int:width>/<int:height>/', views.get_rectangle_area),
    path('get_square_area/<int:width>/', views.get_square_area),
    path('get_circle_area/<int:radius>/', views.get_circle_area),
]