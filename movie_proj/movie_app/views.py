from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from django.db.models import F, Sum, Max, Min, Count, Avg, Value


def show_all_movies(request):
    movies = Movie.objects.order_by('name', 'rating')  # '-name' в обратном порядке
    # movies = Movie.objects.order_by(F('year').desc(nulls_last=True))
    # movies = Movie.objects.annotate(year_rating=F('year') + F('rating'))
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('id'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg
    })


def show_one_movie(request, movie_slug: str):
    movie = get_object_or_404(Movie, slug=movie_slug)
    return render(request, 'movie_app/one_movie.html', {'movie': movie})


def show_all_directors(request):
    directors = Director.objects.order_by('first_name')
    return render(request, 'movie_app/all_directors.html', {'directors': directors})


def show_director_info(request, dir_id: int):
    director = get_object_or_404(Director, id=dir_id)
    return render(request, 'movie_app/one_director.html', {'director': director})


def show_all_actors(request):
    actors = Actor.objects.order_by('first_name')
    return render(request, 'movie_app/all_actors.html', {'actors': actors})


def show_actor_info(request, actor_id: int):
    actor = get_object_or_404(Actor, id=actor_id)
    return render(request, 'movie_app/one_actor.html', {'actor': actor})
