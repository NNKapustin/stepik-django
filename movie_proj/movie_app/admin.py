from django.contrib import admin
from .models import Movie
from django.db.models import QuerySet


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'rating', 'year', 'budget', 'currency', 'rating_status']
    list_editable = ['name', 'rating', 'year', 'budget', 'currency']
    ordering = ['name', 'rating']
    actions = ['set_currency']

    @admin.display(ordering='rating', description='status')
    def rating_status(self, movie: Movie):  # экземпляр класса - представитель класса Movie
        if movie.rating >= 85:
            return 'Great Movie!!!'
        elif movie.rating > 70:
            return 'Good Movie.'
        elif movie.rating > 50:
            return 'Can be watched, once.'
        else:
            return 'Never!'

    @admin.action(description='Set currency as USD')
    def set_currency(self, request, queryset: QuerySet):
        count = queryset.update(currency=Movie.USD)  # ссылаемся на константу, возвращает кол-во измененных записей
        self.message_user(request, message=f'Изменено записей - {count}')
