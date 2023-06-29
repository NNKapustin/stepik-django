from django.contrib import admin
from .models import Movie, Director, Actor, DressingRoom
from django.db.models import QuerySet


admin.site.register(Director)
admin.site.register(Actor)
# admin.site.register(DressingRoom)


@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):
    list_display = ['floor', 'number', 'actor']


class RatingFilter(admin.SimpleListFilter):
    title = 'rating custom filter'  # отображаемое название
    parameter_name = 'rating'  # название параметра из lookups

    def lookups(self, request, model_admin):  # задает отображаемые категории
        return [
            ('<40', 'Trash'),
            ('40-59', 'Can be watched once'),
            ('60-79', 'Good movies'),
            ('>=80', 'Great movies')
        ]

    def queryset(self, request, queryset: QuerySet):  # в self.value() приходит значение параметра из lookups
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        elif self.value() == '40-59':
            return queryset.filter(rating__lt=60)
        elif self.value() == '60-79':
            return queryset.filter(rating__lt=80)
        elif self.value() == '>=80':
            return queryset.filter(rating__gte=80)
        else:
            return queryset


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['name', 'rating']
    # exclude = ['slug']
    readonly_fields = ['budget']
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['actors']
    list_display = ['id', 'name', 'rating', 'year', 'budget', 'currency', 'rating_status', 'director']
    list_editable = ['name', 'rating', 'year', 'budget', 'currency', 'director']
    ordering = ['name', 'rating']
    actions = ['set_currency']
    search_fields = ['name']
    list_filter = ['name', 'currency', RatingFilter]

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
