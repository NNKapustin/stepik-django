from django.db import models


class Gallery(models.Model):
    image = models.FileField(upload_to='gallery_data')  # указываем название папки от корневой проекта
