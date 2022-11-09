from django.urls import path
from . import views
from .views import filter_view


urlpatterns = [
    path('',views.ProjectView.as_view(),name='projects'),
    path('add', views.CreateProject.as_view(), name="project_add"),
    # path('detalle/<pk>/', views.ProjectDetail.as_view(), name='project-detail'),
    # path('sofia',views.FilterView.as_view(),name="sofia"),
    path('filters', filter_view, name="filter"),
]