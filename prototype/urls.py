from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('add/<id>',views.CreatePrototype.as_view(),name='add_prototype'),
    path('', views.PrototypesListView.as_view(), name='prototypes'),
    path('update/<id>', views.UpdatePrototype.as_view(), name='update_prototype'),
    path('download_format/', views.download_csv, name='download_format'),
<<<<<<< HEAD

=======
>>>>>>> 7d8307eb048ba8618d69e71f1a5ae7f6e824de9f
]
