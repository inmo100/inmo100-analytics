from django.urls import path
from . import views

urlpatterns = [
    path('add/<id>',views.CreatePrototype.as_view(),name='add_prototype'),
    path('', views.PrototypesListView.as_view(), name='prototypes'),
    path('update/<id>', views.UpdatePrototype.as_view(), name='update_prototype'),
    path('download_format/', views.download_csv, name='download_format'),
    path('', views.PrototypesList.as_view(), name='prototypes')
]
