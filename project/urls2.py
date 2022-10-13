from django.urls import path
from . import views

urlpatterns = [
    path('add', views.ProjectView.as_view(), name="project_add"),
]