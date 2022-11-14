from django.urls import path
from . import views
from .views import filter_view


urlpatterns = [
    # path('', views.ProjectsList.as_view(), name='projects'),
    path('', views.DevelopersList.as_view(), name='developers'),
    path('create', views.CreateProject.as_view(), name="project_create"),
    path('<int:pk>/', views.ProjectDetail.as_view(), name='project_detail'),
    # path('sofia',views.FilterView.as_view(),name="sofia"),
    path('filters', filter_view, name="filter"),
]
