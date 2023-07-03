from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_all_movies),
    path("movie/<slug:movie_slug>/", views.show_one_movie, name="movie-info"),
    path("directors/", views.AllDirectors.as_view()),
    path("directors/<int:pk>/", views.OneDirectorInfo.as_view(), name="dir-info"),
    path("actors/", views.AllActors.as_view()),
    path("actors/<int:pk>/", views.OneActorInfo.as_view(), name="actor-info"),
]
