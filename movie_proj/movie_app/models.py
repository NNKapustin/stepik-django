from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_url(self):
        return reverse('dir-info', args=[self.id])


class DressingRoom(models.Model):
    floor = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return f"Гримерка: этаж {self.floor}, номер {self.number}"


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER = [
        (MALE, 'Man'),
        (FEMALE, 'Woman'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER, default=MALE)
    dressing = models.OneToOneField(DressingRoom,
                                    on_delete=models.SET_NULL,
                                    null=True, blank=True)  # null=True т.к. SET_NULL

    def __str__(self):
        if self.gender == self.MALE:
            return f"Актер {self.first_name} {self.last_name}"
        else:
            return f"Актриса {self.first_name} {self.last_name}"

    def get_url(self):
        return reverse('actor-info', args=[self.id])


class Movie(models.Model):
    EURO = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY = [
        (EURO, 'Euro'),
        (USD, 'Dollars'),
        (RUB, 'Rubles'),
    ]
    name = models.CharField(max_length=40, unique=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)  # Может быть null или пустым
    budget = models.IntegerField(default=1000000, validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CURRENCY, default=RUB)
    slug = models.SlugField(default='', null=False, db_index=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)

    def get_url(self):
        return reverse('movie-info', args=[self.slug])

    def __str__(self):
        return f"{self.name} - {self.rating}%, {self.budget}, {self.year}"
