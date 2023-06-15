from django.urls import path
from . import views


urlpatterns = [
    path('<int:day>/', views.get_todo_list_by_number),
    path('<str:day>/', views.get_todo_list, name='day-url'),
]
