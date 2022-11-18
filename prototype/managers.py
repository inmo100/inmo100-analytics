from django.db import models
from django.db.models import Count, Q
from .models import *
import numpy

class PrototypesManager(models.Manager):
    #Managers for prtotoypes
    
    def floors_filter(self,floors):
        if(floors == []):
            arr = []
            prototypes = self.all()
            for i in prototypes:
                arr.append(i.prototype.id)
            return arr
        query = self.filter(
            floors = floors[0]
        )
        helper = []
        for j in query:
                helper.append(j.prototype.id)
        if(helper==[]):
            helper = ['null']
        return helper.sort()

    def m2_habitable_filter(self,m2_habitable):
        if(m2_habitable == []):
            arr = []
            prototypes = self.all()
            for i in prototypes:
                arr.append(i.prototype.id)
            return arr
        query = self.filter(
            Q(m2_habitable__gt = (m2_habitable[0]-1)) & Q(m2_habitable__lt = (m2_habitable[1]+1))
        )
        helper = []
        for j in query:
                helper.append(j.prototype.id)
        if(helper==[]):
            helper = ['null']
        return helper

    def m2_constructed_filter(self,m2_constructed):
        if(m2_constructed == []):
            arr = []
            prototypes = self.all()
            for i in prototypes:
                arr.append(i.prototype.id)
            return arr
        query = self.filter(
            Q(m2_constructed__gt = (m2_constructed[0]-1)) & Q(m2_constructed__lt = (m2_constructed[1]+1))
        )
        helper = []
        for j in query:
                helper.append(j.prototype.id)
        if(helper==[]):
            helper = ['null']
        return helper

    def m2_terrain_filter(self,m2_terrain):
        if(m2_terrain == []):
            arr = []
            prototypes = self.all()
            for i in prototypes:
                arr.append(i.prototype.id)
            return arr
        query = self.filter(
            Q(m2_terrain_gt = (m2_terrain[0]-1)) & Q(m2_terrain_lt = (m2_terrain[1]+1))
        )
        helper = []
        for j in query:
                helper.append(j.prototype.id)
        if(helper==[]):
            helper = ['null']
        return helper

    def total_units_filter(self,total_units):
        if(total_units == []):
            arr = []
            propertyTypes = self.all()
            for i in propertyTypes:
                arr.append(i.prototype.id)
            return arr
        query = self.filter(
            Q(total_units__gt = (total_units[0]-1)) & Q(total_units__lt = (total_units[1]+1))
        )
        helper = []
        for j in query:
                helper.append(j.prototype.id)
        if(helper==[]):
            helper = ['null']
        return helper

    def propertyType_filter(self,propertyTypes):
        if(propertyTypes == []):
            arr = []
            propertyTypes = self.all()
            for i in propertyTypes:
                arr.append(i.prototype.id)
            return arr
        for i in propertyTypes:
            helper = []
            query = self.filter(
                propertyType = i
            )
            for j in query:
                helper.append(j.prototype.id)
        if(helper==[]):
            helper = ['null']
        return helper

    def project_filter(self,projects):
        if(projects == []):
            arr = []
            projects = self.all()
            for i in projects:
                arr.append(i.prototype.id)
            return arr
        for i in projects:
            helper = []
            query = self.filter(
                project_field = i
            )
            for j in query:
                helper.append(j.prototype.id)
        if(helper==[]):
            helper = ['null']
        return helper
    
    def prototype_filter(self,prototypes):
        if(prototypes == []):
            arr = []
            prototypes = self.all()
            for i in prototypes:
                arr.append(i.prototype.id)
            return arr
        for i in prototypes:
            helper = []
            query = self.filter(
                id = i
            )
            for j in query:
                helper.append(j.prototype.id)
        if(helper==[]):
            helper = ['null']
        return helper
    def segment_filter(self,segments):
        if(segments == []):
            arr = []
            prototypes = self.all()
            for i in prototypes:
                arr.append(i.prototype.id)
            return arr
        for i in segments:
            helper = []
            query = self.filter(
                segment_field = i
            )
            for j in query:
                helper.append(j.prototype.id)
        if(helper==[]):
            helper = ['null']
        return helper


    def prototipos_filtrados_e_f(self,ids1,ids2):
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

class HistoricalManager(models.Manager):
    def price_filter(self,price,prototypes):
        if(price == []):
            arr = []
            for prototype in prototypes:
                historical = self.filter(prototype=prototype).latest('date')
                arr.append(historical.price)
            return arr
        arr = []
        for prototype in prototypes:
            historical = self.filter(prototype=prototype).latest('date')
            if(historical.price >= price[0] and historical.price <= price[1]):
                arr.append(historical.price)
        return arr
    
    def available_units_filter(self,units,prototypes):
        if(units == []):
            arr = []
            for prototype in prototypes:
                historical = self.filter(prototype=prototype).latest('date')
                arr.append(historical.available_units)
            return arr
        arr = []
        for prototype in prototypes:
            historical = self.filter(prototype=prototype).latest('date')
            if(historical.available_units >= units[0] and historical.available_units <= units[1]):
                arr.append(historical.available_units)
        return arr