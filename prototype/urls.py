from django.urls import path
from . import views

urlpatterns = [
    path('add/<id>',views.CreatePrototype.as_view(),name='add_prototype'),
]