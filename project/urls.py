from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateDeveloper.as_view(), name="developer_add"),
]