from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProjectView.as_view(),name='projects'),
    path('add', views.CreateProject.as_view(), name="project_add"),
    path('<pk>/', views.ProjectDetail.as_view(), name='project-detail')
]