from django.urls import path
from . import views


urlpatterns = [
    path("<int:number_post>/", views.get_post_info_by_number),
    path("<name_post>/", views.get_post_info),
]