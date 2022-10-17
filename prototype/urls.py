from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.CreatePrototype.as_view(),name='add_prototype'),
    path('detail/<id>', views.PrototypeView.as_view(), name='prototype-detail'),
]