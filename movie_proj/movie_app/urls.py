from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_all_movies),
    path("movie/<slug:movie_slug>/", views.show_one_movie, name="movie-info"),
    path("directors/", views.show_all_directors),
    path("directors/<int:dir_id>/", views.show_director_info, name="dir-info"),
    path("actors/", views.show_all_actors),
    path("actors/<int:actor_id>/", views.show_actor_info, name="actor-info"),
]
