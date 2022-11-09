from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('add/<id>',views.CreatePrototype.as_view(),name='add_prototype'),
    path('', views.PrototypesListView.as_view(), name='prototypes'),
    path('update/<id>', views.UpdatePrototype.as_view(), name='update_prototype'),
    path('download_format/', views.download_csv, name='download_format'),
<<<<<<< HEAD
    path('filters', filter_view, name="filter"),
    
=======
>>>>>>> 397b116e8d3f15a418ce09adaf353b047f8d1001

]
