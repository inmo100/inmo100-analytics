from django.db import models
from django.db.models import Count
from django.db.models.functions import Concat
from .models import *
from pprint import pprint

class EquipmentManager(models.Manager):
    #Managers for equipments in prototype

    def listar_prototipos(self):
        return self.all()
    def listar_prototipos_equipamiento(self):
        prototype =  self.all()
        return prototype