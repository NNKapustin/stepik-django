from django import forms
from . import models


class GalleryUploadForm(forms.ModelForm):
    class Meta:
        model = models.Gallery
        fields = '__all__'
