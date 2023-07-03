from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView

from . import forms
from . import models


# class FeedbackIndex(View):
#     def get(self, request):
#         form = forms.FeedbackForm()
#         return render(request, 'feedback/feedback.html', context={'form': form})
#
#     def post(self, request):
#         form = forms.FeedbackForm(request.POST)
#         if form.is_valid():  # если данные валидные
#             form.save()
#             return HttpResponseRedirect('/done')
#         return render(request, 'feedback/feedback.html', context={'form': form})

# class FeedbackIndex(FormView):
#     form_class = forms.FeedbackForm  # какую форму отображать
#     template_name = 'feedback/feedback.html'  # какой шаблон использовать
#     success_url = '/done'  # куда перенаправлять при успехе
#
#     def form_valid(self, form):  # что делать если форма валидная - аналог метода post
#         form.save()
#         return super().form_valid(form)

class FeedbackIndex(CreateView):
    model = models.Feedback  # какую модель привязать
    form_class = forms.FeedbackForm  # какую форму отображать
    template_name = 'feedback/feedback.html'  # какой шаблон использовать
    success_url = '/done'  # куда перенаправлять при успехе


class DoneView(TemplateView):
    template_name = 'feedback/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Ivan'
        context['date'] = '23.04.1987'
        return context


# class ListFeedBack(TemplateView):
#     template_name = 'feedback/list_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['feeds'] = models.Feedback.objects.order_by('rating')
#         return context

class ListFeedBack(ListView):
    template_name = 'feedback/list_feedback.html'
    model = models.Feedback
    context_object_name = 'feeds'

    def get_queryset(self):
        queryset = super().get_queryset()
        filtered_qs = queryset.filter(rating__gt=2)
        return filtered_qs


# class DetailFeedBack(TemplateView):
#     template_name = 'feedback/detail_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['feed'] = models.Feedback.objects.get(id=kwargs['id_feedback'])
#         return context

class DetailFeedBack(DetailView):
    template_name = 'feedback/detail_feedback.html'
    model = models.Feedback
    context_object_name = 'feed'


# class UpdateFeedback(View):
#     def get(self, request, id_feedback):
#         feed = models.Feedback.objects.get(id=id_feedback)
#         form = forms.FeedbackForm(instance=feed)
#         return render(request, 'feedback/feedback.html', context={'form': form})
#
#     def post(self, request, id_feedback):
#         feed = models.Feedback.objects.get(id=id_feedback)
#         form = forms.FeedbackForm(request.POST, instance=feed)
#         if form.is_valid():  # если данные валидные
#             form.save()
#             return HttpResponseRedirect('/done')
#         return render(request, 'feedback/feedback.html', context={'form': form})

class UpdateFeedback(UpdateView):
    model = models.Feedback
    form_class = forms.FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'
