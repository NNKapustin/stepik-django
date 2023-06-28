from django.shortcuts import render, get_object_or_404
from .models import Movie
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
