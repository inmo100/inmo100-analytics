from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectsList.as_view(), name='projects'),
    path('desarrolladoras', views.DevelopersList.as_view(), name='developers'),
    path('create', views.CreateProject.as_view(), name="project_create"),
    path('desarrolladoras/<int:pk>/', views.DevDetail.as_view(), name='dev_detail'),
    path('<int:pk>/', views.ProjectDetail.as_view(), name='project_detail'),
]
