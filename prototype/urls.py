from django.urls import path
from .views import *


urlpatterns = [
    path('add/<id>', CreatePrototype.as_view(), name='add_prototype'),
    path('', PrototypesList.as_view(), name='prototypes'),
    path('update/<id>', UpdatePrototype.as_view(), name='update_prototype'),
    path('fix/<id>', FixPrototype.as_view(), name='fix_prototype'),
    path('download_format/', download_csv, name='download_format'),
]
