from django.urls import path
from . import views


urlpatterns = [
    path('',views.DeveloperView.as_view(),name='developer_home'),
    path('add', views.CreateDeveloper.as_view(), name="developer_add"),
]