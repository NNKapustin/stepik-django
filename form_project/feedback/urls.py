from django.urls import path
from . import views

urlpatterns = [
    path("", views.FeedbackIndex.as_view()),
    path("done/", views.DoneView.as_view()),
    path("<int:pk>/", views.UpdateFeedback.as_view()),
    path("list/", views.ListFeedBack.as_view()),
    path("detail/<int:pk>/", views.DetailFeedBack.as_view())
]
