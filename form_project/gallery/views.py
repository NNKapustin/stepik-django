from django.shortcuts import render
from django.views import View
from . import forms
from . import models
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView


# class GalleryView(View):
#     def get(self, request):
#         form = forms.GalleryUploadForm()
#         return render(request, 'gallery/load_file.html', {'form': form})
#
#     def post(self, request):
#         form = forms.GalleryUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_image = models.Gallery(image=form.cleaned_data['image'])
#             new_image.save()
#             return HttpResponseRedirect('/load_image')
#         return render(request, 'gallery/load_file.html', {'form': form})


class CreateGalleryView(CreateView):
    model = models.Gallery
    form_class = forms.GalleryUploadForm
    template_name = 'gallery/load_file.html'
    success_url = '/load_image'


class ListGallery(ListView):
    model = models.Gallery
    template_name = 'gallery/list_file.html'
    context_object_name = 'files'
