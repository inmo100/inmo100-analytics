import datetime
import pandas as pd
from django.utils import timezone
from project.models import Project
import os.path
from os import remove
from .forms import *
from .models import *
import hashlib

def fix_data_csv(arr,project_field):
    iterable = 10
    count = Equipment.objects.count()
    iterable2 = iterable+count
    project = Project.objects.get(id=project_field)
    prototypes = Prototype.objects.filter(project_field = project_field).order_by("id")
    prototypes_count = Prototype.objects.filter(project_field = project_field).order_by("id")
    iterable3 = 0
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

        prototype = prototypes[iterable3]
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
        equipments = EquipmentQuantity.objects.filter(prototype=prototype).order_by('id')
        for equipment in equipments:
            if(i[iterable] == 'null' or i[iterable] == 0):
                equipment.quantity = 0
                equipment.save()
                iterable = iterable + 1
            else:
                equipment.quantity = i[iterable]
                equipment.save()
                iterable = iterable+1
        iterable = 10
        triangulos = Triangulo.objects.filter(prototype = prototype).order_by("id")
        for triangulo in triangulos:
            if(i[iterable2] == 'null'):
                material = Material.objects.get(name='No existe')
                triangulo.material = material
                triangulo.save()
                iterable2 = iterable2+1
            else:
                if(Material.objects.filter(name=i[iterable2]).exists() == False):
                    material = Material.objects.get(name='No existe')
                    triangulo.material = material
                    triangulo.save()
                    iterable2 = iterable2+1
                else:
                    material = Material.objects.get(name=i[iterable2])
                    triangulo.material = material
                    triangulo.save()
                    iterable2 = iterable2+1
        iterable2 = iterable+count
        historical = Historical.objects.filter(prototype=prototype).latest('date')
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
        iterable3 = iterable3+1


def update_data_csv(arr,project_field):
    iterable = 10
    count = Equipment.objects.count()
    iterable2 = iterable+count
    project = Project.objects.get(id=project_field)
    prototypes = Prototype.objects.filter(project_field = project_field).order_by("id")
    prototypes_count = Prototype.objects.filter(project_field = project_field).order_by("id").count()
    equipments_general = Equipment.objects.all().order_by('id')
    finishings_general = Finishing.objects.all().order_by('id')
    bandera = 0
    iterable3 = 0
    
    for i in arr:
        if((iterable3+1)<=prototypes_count):
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

            prototype = prototypes[iterable3]
            prototype.segment_field = segment
            prototype.project_field = project
            prototype.name = i[0]
            if(i[2] == 'null'):
                if(prototype.total_units == 0):
                    bandera = bandera+1
                prototype.total_units = 0
            else:
                if(prototype.total_units == i[2]):
                    bandera = bandera+1
                prototype.total_units = i[2]
            prototype.m2_terrain = i[4]
            prototype.m2_constructed = i[5]
            prototype.m2_habitable = i[6]
            prototype.floors = i[7]
            prototype.propertyType = property_type
            prototype.save()
            equipments = EquipmentQuantity.objects.filter(prototype=prototype).order_by('id')
            for equipment in equipments:
                if(i[iterable] == 'null' or i[iterable] == 0):
                    equipment.quantity = 0
                    equipment.save()
                    iterable = iterable + 1
                else:
                    equipment.quantity = i[iterable]
                    equipment.save()
                    iterable = iterable+1
            iterable = 10
            triangulos = Triangulo.objects.filter(prototype = prototype).order_by("id")
            for triangulo in triangulos:
                if(i[iterable2] == 'null'):
                    material = Material.objects.get(name='No existe')
                    triangulo.material = material
                    triangulo.save()
                    iterable2 = iterable2+1
                else:
                    if(Material.objects.filter(name=i[iterable2]).exists() == False):
                        material = Material.objects.get(name='No existe')
                        triangulo.material = material
                        triangulo.save()
                        iterable2 = iterable2+1
                    else:
                        material = Material.objects.get(name=i[iterable2])
                        triangulo.material = material
                        triangulo.save()
                        iterable2 = iterable2+1
            iterable2 = iterable+count
            historical_old = Historical.objects.filter(prototype=prototype).latest('date')
            if(i[1] == 'null'):
                i[1] = 0
            if(historical_old.price == i[1]):
                bandera = bandera+1
            if(bandera != 2):
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
            
            iterable3 = iterable3+1
            bandera = 0
        else:
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
            for equipment in equipments_general:
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
            for finishing in finishings_general:
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
    filename = hashlib.md5(str(datetime.now()).encode("utf-8")).hexdigest()
    filename = 'media/'+filename
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    try:
        df = pd.read_csv(filename)
        df = df.fillna("null")
        template = pd.read_csv('media/plantilla_prototipos2.csv')

        remove(filename)

        for column in template.columns.values:
            if column not in df.columns.values:
                return 1
        
        df = df.values.tolist()
        if not df:
            return 3
        
        #That if compares if is to create prototyes or to update prototypes
        try:
            if(action=='c'):
                save_data_csv(df,project_field)
            elif(action=='u'):
                update_data_csv(df,project_field)
            elif(action=="f"):
                fix_data_csv(df,project_field)
        except:
            return 4

        del df
        return 0
    except:
        remove(filename)
        return 2

#Function that create a csv with all the equipments from the database.
def download_csv():
#if the file exist we remove it in order to generetare a new one with all the database updates
    if(os.path.isfile("media/plantilla_prototipos2.csv")):
        remove("media/plantilla_prototipos2.csv")
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
    template.to_csv("media/plantilla_prototipos2.csv",sep=",",index=False,encoding="utf-8")

def delete_csv(project_id):
    project = Project.objects.get(id=project_id)
    nombre = "plantilla_prototipos_"+project.name
    if(os.path.isfile("media/"+nombre+".csv")):
        remove("media/"+nombre+".csv")

#Function that create a csv with all the equipments from the database.
def update_download_csv(project_id):
    project = Project.objects.get(id=project_id)
    nombre = "plantilla_prototipos_"+project.name
#if the file exist we remove it in order to generetare a new one with all the database updates
    delete_csv(project_id)
    template = pd.DataFrame()
    prototypes = Prototype.objects.filter(project_field=project)
    equipments_count = Equipment.objects.count()
    arr = {}
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
                equipments_p = EquipmentQuantity.objects.filter(prototype = prototype).order_by("id")
        else:
            equipments_p = EquipmentQuantity.objects.filter(prototype = prototype).order_by("id")
        historicals = Historical.objects.filter(prototype=prototype).latest('date')
        arr = {"Nombre":prototype.name,"Precio":historicals.price,"Unidades_Totales":prototype.total_units,"Unidades_Vendidas":prototype.total_units-historicals.available_units,"m2_Terreno":prototype.m2_terrain,"m2_Construidos":prototype.m2_constructed,"m2_Habitables":prototype.m2_habitable,"No_Pisos":prototype.floors,"Segmento":prototype.segment_field,"Tipo de Propiedad":prototype.propertyType}
        triangulos = Triangulo.objects.filter(prototype = prototype).order_by("id")
        for equipment_p in equipments_p:
            arr[equipment_p.equipment] = equipment_p.quantity
        for triangulo in triangulos:
            arr[triangulo.finishings] = triangulo.material
        template = template.append(arr, ignore_index=True)
        #template = pd.concat(template, arr)
    template.to_csv("media/"+nombre+".csv",sep=",",index=False,encoding="utf-8")



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

def bring_prototypes(prototypes):
    if(prototypes == []):
        return 'null'
    if(prototypes == 'null'):
        return 'null'
    equipments_count = Equipment.objects.count()
    for prototype in prototypes:
        equipments_q_count = EquipmentQuantity.objects.filter(prototype = prototype).count()
        hsitorical_count = Historical.objects.filter(prototype=prototype).count()
        triangulo_count = Triangulo.objects.filter(prototype=prototype).count()
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
        try:
            historical = Historical.objects.filter(prototype=prototype).latest('date')
        except:
            return None
        price = historical.price
        units_sold = prototype.total_units - historical.available_units
        absorcion_historica = units_sold/diff_month(Historical.objects.filter(prototype=prototype).earliest('date').date)
        meses_inventario = historical.available_units/absorcion_historica
        sell_flow = units_sold/prototype.total_units
        setattr(prototype,'price',price)
        setattr(prototype,'units_sold',units_sold)
        setattr(prototype,'materials',materials)
        setattr(prototype,'equipments_q',equipments_q)
        setattr(prototype,'histabs',absorcion_historica)
        setattr(prototype,'meses_inventario',meses_inventario)
        setattr(prototype,'sell_flow',sell_flow)
    return prototypes


def check_arguments(argument):
    if(len(argument) == 2):
        if (argument[0] == '' or argument[1] == ''):
            return []
    if(argument == []):
        return argument
    arr = []
    for i in argument:
        arr.append(float(i))
    return arr


def diff_month(d2):
    d1 = datetime.today()
    dif = (d1.year - d2.year) * 12 + d1.month - d2.month
    if(dif == 0):
        dif = dif+1
    return dif
