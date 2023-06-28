from django.db import models
from django.urls import reverse
from django.utils.text import slugify


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
    rating = models.IntegerField()
    year = models.IntegerField(null=True, blank=True)  # Может быть null или пустым
    budget = models.IntegerField(default=1000000)
    currency = models.CharField(max_length=3, choices=CURRENCY, default=RUB)
    slug = models.SlugField(default='', null=False, unique=True, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('movie-info', args=[self.slug])

    def __str__(self):
        return f"{self.name} - {self.rating}%, {self.budget}, {self.year}"
