from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib import messages
from .forms import *
from .models import *
from .helpers import *
    
#Class based view to create prototypes
class CreatePrototype(ListView):
    template_name = 'pages/create_prototype.html'
    #Overwriting the method get from the class
    def get(self,request,*args,**kwargs):
        download_csv()
        project = Project.objects.get(id=self.kwargs['id'])

        prototypes = recreate_prototypes(self.kwargs['id'])
        finishings = Finishing.objects.order_by("id")
        equipments = Equipment.objects.all().order_by('id')

        return render(request,self.template_name,context={
            'id':self.kwargs['id'],
            'proyecto': project,
            'prototype_list': prototypes,
            'finishings_type': finishings,
            'equipments': equipments,
            })
    #Overwriting the method post from the class
    def post(self,request,*args,**kwargs):
        csv_import = CSV_Form(request.POST, request.FILES)
        project_field = request.POST['project_field']

        prototypes = recreate_prototypes(project_field)
        finishings = Finishing.objects.order_by("id")
        equipments = Equipment.objects.all().order_by('id')
        project = Project.objects.get(id=self.kwargs['id'])
        
        if csv_import.is_valid():
                response = handle_uploaded_file(request.FILES['csv'],project_field,'c')
                if response == 1:
                    messages.success(request, ("Formato de Plantilla invalida"))
                    return render(request, self.template_name, context={
                        'proyecto': project,
                        'prototype_list': prototypes,
                        'finishings_type': finishings,
                        'equipments': equipments,
                        }) 
                else: 
                    messages.success(request, ("Plantilla se pudo actualizar"))
                    return render(request, self.template_name, context={
                        'proyecto': project,
                        'prototype_list': prototypes,
                        'finishings_type': finishings,
                        'equipments': equipments,
                        })
        else:
            messages.success(request, ("Formato incorrecto"))
            return render(request,self.template_name,context={
                        'proyecto': project,
                        'prototype_list': prototypes,
                        'finishings_type': finishings,
                        'equipments': equipments,
                        })

#class based view to list all prototypes
class PrototypesListView(ListView):
    template_name = 'pages/prototypes.html'
    model = Prototype
    def get(self, request):
        finishings = Finishing.objects.order_by("id")
        prototypes = Prototype.objects.all()
        equipments = Equipment.objects.all().order_by('id')
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

        return render(request,self.template_name,context={
            'prototype_list': prototypes,
            'finishings_type': finishings,
            'equipments': equipments,
        })

#Class based view to update prototype
class UpdatePrototype(ListView):
    template_name = 'pages/form_update_prototypes.html'
    model = Segment
    #Overwriting the method get from the class
    def get(self,request,*args,**kwargs):
        download_csv()
        return render(request,self.template_name,context={
            'id':self.kwargs['id']
            })
    #Overwriting the method post from the class
    def post(self,request,*args,**kwargs):
        csv_import = CSV_Form(request.POST, request.FILES)
        project_field = request.POST['project_field']
        if csv_import.is_valid():
                handle_uploaded_file(request.FILES['csv'],project_field,'u')
                return redirect("prototypes")
        else:
            return render(request,self.template_name,context={'Prueba':'No se pudo'})
