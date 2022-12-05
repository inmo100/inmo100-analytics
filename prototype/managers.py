from django.db import models
from django.db.models import Count, Q
from .models import *
import numpy

class PrototypesManager(models.Manager):
    #Managers for prtotoypes
    
    def floors_filter(self,floors,prototypes):
        if(floors == [] and prototypes[0]!= 'null'):
            return prototypes
        if(floors == [] and prototypes[0] == 'null'):
            return ['null']
        print(floors)
        query = self.filter(
            Q(floors__gt = (floors[0])-1) & Q(floors__lt = (floors[1])+1)
        )
        helper = []
        for j in query:
                helper.append(j.prototype.id)
        if(helper==[]):
            helper = ['null']
        if(prototypes!= [] and helper != ['null']):
            helper2 = list(set(prototypes) & set(helper))
            return helper2
        return helper

    def m2_habitable_filter(self,m2_habitable,prototypes):
        if(m2_habitable == [] and prototypes[0]!= 'null'):
            return prototypes
        if(m2_habitable == [] and prototypes[0] == 'null'):
            return ['null']
        query = self.filter(
            Q(m2_habitable__gt = (m2_habitable[0]-1)) & Q(m2_habitable__lt = (m2_habitable[1]+1))
        )
        helper = []
        for j in query:
                helper.append(j.prototype.id)
        if(helper==[]):
            helper = ['null']
        if(prototypes!= [] and helper != ['null']):
            helper2 = list(set(prototypes) & set(helper))
            return helper2
        return helper

    def m2_constructed_filter(self,m2_constructed,prototypes):
        if(m2_constructed == [] and prototypes[0]!= 'null'):
            return prototypes
        if(m2_constructed == [] and prototypes[0] == 'null'):
            return ['null']
        query = self.filter(
            Q(m2_constructed__gt = (m2_constructed[0])) & Q(m2_constructed__lt = (m2_constructed[1]))
        )
        helper = []
        for j in query:
                helper.append(j.prototype.id)
        if(helper==[]):
            helper = ['null']
        if(prototypes!= [] and helper != ['null']):
            helper2 = list(set(prototypes) & set(helper))
            return helper2
        return helper

    def m2_terrain_filter(self,m2_terrain,prototypes):
        if(m2_terrain == [] and prototypes[0]!= 'null'):
            return prototypes
        if(m2_terrain == [] and prototypes[0] == 'null'):
            return ['null']
        query = self.filter(
            Q(m2_terrain__gt = (m2_terrain[0])) & Q(m2_terrain__lt = (m2_terrain[1]))
        )
        helper = []
        for j in query:
                helper.append(j.prototype.id)
        if(helper==[]):
            helper = ['null']
        if(prototypes!= [] and helper != ['null']):
            helper2 = list(set(prototypes) & set(helper))
            return helper2
        return helper

    def total_units_filter(self,total_units,prototypes):
        if(total_units == [] and prototypes[0] != 'null'):
            return prototypes
        if(total_units == [] and prototypes[0] == 'null'):
            return ['null']
        query = self.filter(
            Q(total_units__gt = (total_units[0]-1)) & Q(total_units__lt = (total_units[1]+1))
        )
        helper = []
        for j in query:
            helper.append(j.prototype.id)
        if(helper==[]):
            helper = ['null']
        if(prototypes!= [] and helper != ['null']):
            helper2 = list(set(prototypes) & set(helper))
            return helper2
        return helper

    def propertyType_filter(self,propertyTypes,prototypes):
        if(propertyTypes == [] and prototypes[0] != 'null'):
            return prototypes
        if(propertyTypes == [] and prototypes[0] == 'null'):
            return ['null']
        for i in propertyTypes:
            helper = []
            query = self.filter(
                propertyType = i
            )
            for j in query:
                helper.append(j.prototype.id)
        if(helper==[]):
            helper = ['null']
        if((prototypes != [] and helper != []) or (prototypes!= [] and helper != ['null'])):
            helper2 = list(set(prototypes) & set(helper))
            if(helper2 == []):
                return ['null']
            return helper2
        return helper

    def project_filter(self,projects):
        if(projects == []):
            arr = []
            projects = self.all()
            for i in projects:
                arr.append(i.prototype.id)
            return arr
        helper = []
        for i in projects:
            query = self.filter(
                project_field = i
            )
            for j in query:
                helper.append(j.prototype.id)
        if(helper==[]):
            helper = ['null']
        return helper
    
    def prototype_filter(self,prototypes,prototypes2):
        try:
            if(prototypes[0] != 'null'  and prototypes2 != []):
                response = list(set(prototypes) & set(prototypes2))
                return response
            if(prototypes[0] == 'null'):
                return ['null']
            if(prototypes == []):
                arr = []
                prototypes = self.all()
                for i in prototypes:
                    arr.append(i.prototype.id)
                return arr
            helper = []
            for i in prototypes:
                query = self.filter(
                    id = i
                )
                for j in query:
                    helper.append(j.prototype.id)
            if(helper==[]):
                helper = ['null']
            return helper
        except:
            return 1
    def segment_filter(self,segments,prototypes):
        if(segments == [] and prototypes[0] != 'null'):
            return prototypes
        if(segments == [] and prototypes[0] == 'null'):
            return ['null']
        helper = []
        for i in segments:
            query = self.filter(
                segment_field = i
            )
            for j in query:
                helper.append(j.prototype.id)
        if(helper==[]):
            helper = ['null']
        if((prototypes != [] and helper != []) or (prototypes!= [] and helper != ['null'])):
            helper2 = list(set(prototypes) & set(helper))
            if(helper2 == []):
                return ['null']
            return helper2
        return helper
    
    def get_prototypes(self,prototypes_id):
        if (prototypes_id == []):
            return self.all()
        if(prototypes_id[0] == 'null'):
            return 'null'
        queryset = self.filter(id__in=prototypes_id)
        return queryset
    
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
    #This returns all total units from the prototypes given
    def total_units(self,prototypes):
        if(prototypes == []):
            query = self.all()
            for prototype in query:
                prototypes.append(prototype.id)
        if (prototypes[0] == 'null'):
            return ['null']
        dictionary = dict()
        for prototype in prototypes:
            dictionary[prototype] = self.get(id=prototype).total_units
        return dictionary
    
class EquipmentQuantityManager(models.Manager):
    #Managers for equipment quantity

    def equipment_filter(self, equipments,prototypes):
        if(equipments == [] and prototypes[0] != 'null'):
            return prototypes
        if(equipments == [] and prototypes[0] == 'null'):
            return ['null']
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
        if(prototypes!= [] and helper != ['null']):
            helper2 = list(set(prototypes) & set(helper))
            if(helper2 == []):
                return ['null']
            return helper2
        return helper

class TrianguloManager(models.Manager):
    def triangulo_filter(self,materials,prototypes):
        if(materials == [] and prototypes[0] != 'null'):
            return prototypes
        if(materials == [] and prototypes[0] == 'null'):
            return ['null']
        arr2 = []
        helper = []
        for i in materials:
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
        if(prototypes!= [] and helper != ['null']):
            helper2 = list(set(prototypes) & set(helper))
            if(helper2 == []):
                return ['null']
            return helper2
        return helper

class HistoricalManager(models.Manager):
    def price_filter(self,price,prototypes):
        if(price == [] and prototypes[0] == 'null'):
            return ['null']
        if(price == [] and prototypes[0]!='null'):
            return prototypes
        arr = []
        for prototype in prototypes:
            historical = self.filter(prototype=prototype).latest('date')
            if(historical.price >= price[0] and historical.price <= price[1]):
                arr.append(prototype)
        return arr
    
    def available_units_filter(self,units,prototypes):
        if (isinstance(prototypes,dict) == False):
            if((units == [] and prototypes[0] != 'null')):
                arr = []
                for clave in prototypes:
                    arr.append(clave)
                return arr
            if(units == [] and prototypes[0] == 'null'):
                return ['null']
        arr = []
        if(units == []):
            for clave in prototypes:
                arr.append(clave)
            return arr
        for clave in prototypes:
            historical = self.filter(prototype=clave).latest('date')
            sold_units = prototypes[clave]-historical.available_units
            if(sold_units >= units[0] and sold_units <= units[1]):
                arr.append(clave)
        if(arr==[]):
            return ['null']
        return arr