from django.urls import path
from . import views

urlpatterns = [
    path('add/<id>',views.CreatePrototype.as_view(),name='add_prototype'),
    path('update/<id>', views.UpdatePrototype.as_view(), name='update_prototype'),
    path('download_format/', views.download_csv, name='download_format'),
"""     path('detail/<id>', views.PrototypeView.as_view(), name='prototype-detail'), """
]
