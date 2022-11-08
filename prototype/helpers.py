import datetime
import pandas as pd
from django.utils import timezone
from project.models import Project
import os.path
from os import remove
from .forms import *
from .models import *

#Funciton that recieves the project id in order to delete all prototypes related to the project
def delete_prototypes(project_fields):
    project_prototypes = Prototype.objects.filter(project_field = project_fields)
    for i in project_prototypes:
        equipment_quantity = EquipmentQuantity.objects.filter(prototype = i)
        equipment_quantity.delete()
    project_prototypes.delete()
    
#Function that recieves a list with all the rows from csv and the project field in order to register all the prototypes related
# to a projet
def save_data_csv(arr,project_field):
    equipments = Equipment.objects.all().order_by('id')
    finishings = Finishing.objects.all().order_by('id')
    iterable = 10
    count = Equipment.objects.count()
    iterable2 = iterable+count
    project = Project.objects.get(id=project_field)
    for i in arr:
        if(i[8] == 'null'):
            segment = Segment.objects.get(name='No existe')    
        else:
            if(Segment.objects.filter(name=i[8]).exists() == False):
                segment = Segment.objects.get(name="No existe")
            else:
                segment = Segment.objects.get(name=i[8])
        
        if(i[9] == 'null'):
            property_type = PropertyType.objects.get(name='No existe')
        else:
            if(PropertyType.objects.filter(name=i[9]).exists() == False):
                property_type = PropertyType.objects.get(name='No existe')
            else:
                property_type = PropertyType.objects.get(name=i[9])

        prototype = Prototype()
        prototype.segment_field = segment
        prototype.project_field = project
        prototype.name = i[0]
        if(i[2] == 'null'):
            prototype.total_units = 0
        else:
            prototype.total_units = i[2]
        prototype.m2_terrain = i[4]
        prototype.m2_constructed = i[5]
        prototype.m2_habitable = i[6]
        prototype.floors = i[7]
        prototype.propertyType = property_type
        prototype.save()
        prototype = Prototype.objects.get(name=i[0],project_field = project_field)
        #For that iterate equipments in order to save it to the respective prototype
        for equipment in equipments:
            if(i[iterable] == 'null' or i[iterable] == 0):
                equipment_quantity = EquipmentQuantity()
                equipment_quantity.equipment = equipment
                equipment_quantity.prototype = prototype
                equipment_quantity.quantity = 0
                equipment_quantity.save()
                iterable = iterable + 1
            else:
                equipment_quantity = EquipmentQuantity()
                equipment_quantity.equipment = equipment
                equipment_quantity.prototype = prototype
                equipment_quantity.quantity = i[iterable]
                equipment_quantity.save()
                iterable = iterable+1
        iterable = 10
#For that iterate finishings in order to save it to the respective prototype
        for finishing in finishings:
            if(i[iterable2] == 'null'):
                triangulo = Triangulo()
                triangulo.finishings = finishing
                material = Material.objects.get(name='No existe')
                triangulo.material = material
                triangulo.prototype = prototype
                triangulo.save()
                iterable2 = iterable2+1
            else:
                if(Material.objects.filter(name=i[iterable2]).exists() == False):
                    triangulo = Triangulo()
                    triangulo.finishings = finishing
                    material = Material.objects.get(name='No existe')
                    triangulo.material = material
                    triangulo.prototype = prototype
                    triangulo.save()
                    iterable2 = iterable2+1
                else:
                    triangulo = Triangulo()
                    triangulo.finishings = finishing
                    material = Material.objects.get(name=i[iterable2])
                    triangulo.material = material
                    triangulo.prototype = prototype
                    triangulo.save()
                    iterable2 = iterable2+1
        iterable2 = iterable+count
#To insert into datatable Historical
        historical = Historical()
        historical.prototype = prototype
        if(i[1] == 'null'):
            historical.price = 0
        else:
            historical.price = i[1]
        if(i[2]<i[3]):
            historical.available_units = 0
        else:
            historical.available_units = i[2]-i[3]
        historical.date = datetime.now(tz=timezone.utc)
        historical.save()

#Function that handles csv options
def handle_uploaded_file(f,project_field,action):  
    with open('static/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)
    df = pd.read_csv('static/'+f.name)
    remove('static/'+f.name)
    df = df.fillna("null")
    template = pd.read_csv('static/plantilla_prototipos2.csv')
    for column in template.columns.values:
        if column not in df.columns.values:
            return 1
    
    df = df.values.tolist()
    
    #That if compares if is to create prototyes or to update prototypes
    if(action=='c'):
        save_data_csv(df,project_field)
    elif(action=='u'):
        delete_prototypes(project_field)
        save_data_csv(df,project_field)
    del df

#Function that create a csv with all the equipments from the database.
def download_csv():
#if the file exist we remove it in order to generetare a new one with all the database updates
    if(os.path.isfile("static/plantilla_prototipos2.csv")):
        remove("static/plantilla_prototipos2.csv")
#We bring all the equipments on the database ordered by the id
#This is important because indicates the order of the uploaded data
    equipments = Equipment.objects.all().order_by('id')
    finishings = Finishing.objects.all().order_by('id')
#Read the template
    template = pd.read_csv("static/plantilla_prototipos.csv")
#Create a variable arr that contains nothing
    arr = [""]
#Iterate all equipments
    for equipment in equipments:
#Save the equipment name as a header on the template with nothing in order to put
#Just the header
        template[equipment.name] = arr
#The same thing done as above
    for finishing in finishings:
        template[finishing.name] = arr
#Delete the first raw that contains , in order to save it clean
    template = template.drop(0)
    template.to_csv("static/plantilla_prototipos2.csv",sep=",",index=False,encoding="utf-8")

#function that returns a list of all prototypes or a projects prototypes
def recreate_prototypes(id):
        if id == 0:
            prototypes = Prototype.objects.all()
        else:
            prototypes = Prototype.objects.filter(project_field=id)

        equipments_count = Equipment.objects.count()
        for prototype in prototypes:
            equipments_q_count = EquipmentQuantity.objects.filter(prototype = prototype).count()
            if(equipments_count>equipments_q_count):
                limit = equipments_count-equipments_q_count
                equipments_ids = Equipment.objects.all().order_by("-id")[:limit]
                for equipments_id in reversed(equipments_ids):
                    missing_equipments = EquipmentQuantity()
                    missing_equipments.prototype = prototype
                    missing_equipments.equipment = equipments_id
                    missing_equipments.quantity = 0
                    missing_equipments.save()
                equipments_q = EquipmentQuantity.objects.filter(prototype = prototype).order_by('id')
            else:
                equipments_q = EquipmentQuantity.objects.filter(prototype = prototype).order_by('id')
            materials = Triangulo.objects.filter(prototype = prototype).order_by('id')
            historical = Historical.objects.filter(prototype=prototype).latest('date')
            price = historical.price
            units_sold = prototype.total_units - historical.available_units
            setattr(prototype,'price',price)
            setattr(prototype,'units_sold',units_sold)
            setattr(prototype,'materials',materials)
            setattr(prototype,'equipments_q',equipments_q)
        return prototypes
    