from django.db import models
from django.db.models import Count, Q
from django.db.models.functions import Concat
from .models import *
from pprint import pprint
import numpy

class PrototypesManager(models.Manager):
    #Managers for prtotoypes

    def listar_prototipos(self):
        return self.all()
    def listar_prototipos_equipamiento(self):
        prototypes = self.all()
        return prototypes
    def contar_equipamientos(self):
        prototypes = self.annotate(
            num_equipments = Count('prototipo_equipamiento')
        )
        for i in prototypes:
            print(i.num_equipments)
    def prototipos_filtrados(self,ids1,ids2):
        if(ids1==[] and ids2==[]):
            return self.all()
        if(ids1[0] == 'null' and ids2[0] == 'null'):
            return None
        if(ids1==[]):
            ids2 = numpy.unique(ids2)
            prototypes = []
            for i in ids2:
                prototypes.append(self.get(id=i))
            return prototypes
        if(ids2==[]):
            ids1 = numpy.unique(ids1)
            prototypes = []
            for i in ids1:
                prototypes.append(self.get(id=i))
            return prototypes
        ids = list(set(ids1) & set(ids2))
        prototypes = []
        for i in ids:
            prototypes.append(self.get(id=i))
        return prototypes
class EquipmentQuantityManager(models.Manager):
    #Managers for equipment quantity

    def equipment_filter(self, equipments):
        if(equipments == []):
            arr = []
            prototypes = self.all()
            for i in prototypes:
                arr.append(i.prototype.id)
            return arr
        arr2 = []
        for i in equipments:
            helper = []
            query = self.filter(
                Q(equipment=i) & Q(quantity__gt = 0)
            )
            for j in query:
                helper.append(j.prototype.id)
            arr2.append(helper)
        cant = len(arr2)
        cant = cant-1
        for j in range(cant):
            helper = list(set(arr2[j]) & set(arr2[j+1]))
        if(helper==[]):
            helper = ['null']
        return helper

class TrianguloManager(models.Manager):
    def triangulo_filter(self,materials):
        helper = 0
        if(materials == []):
            arr = []
            prototypes = self.all()
            for i in prototypes:
                arr.append(i.prototype.id)
            return arr
        arr2 = []
        for i in materials:
            helper = []
            query = self.filter(
                Q(material=i)
            )
            for j in query:
                helper.append(j.prototype.id)
            arr2.append(helper)
        cant = len(arr2)
        cant = cant-1
        for j in range(cant):
            helper = list(set(arr2[j]) & set(arr2[j+1]))
        if(helper==[]):
            helper = ['null']
        return helper