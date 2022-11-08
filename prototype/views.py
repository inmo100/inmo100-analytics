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
        project = Project.objects.get(id=self.kwargs['id'])
        finishings = Finishing.objects.order_by("id")
        equipments = Equipment.objects.all().order_by('id')

        if csv_import.is_valid():
                response = handle_uploaded_file(request.FILES['csv'],project_field,'c')
                prototypes = recreate_prototypes(self.kwargs['id'])

                if response == 1:
                    messages.success(request, ("Formato de Plantilla invalida"))
                    return render(request, self.template_name, context={
                        'id':self.kwargs['id'],
                        'proyecto': project,
                        'prototype_list': prototypes,
                        'finishings_type': finishings,
                        'equipments': equipments,
                        })
                else: 
                    messages.success(request, ("Plantilla se pudo actualizar"))
                    return render(request, self.template_name, context={
                        'id':self.kwargs['id'],
                        'proyecto': project,
                        'prototype_list': prototypes,
                        'finishings_type': finishings,
                        'equipments': equipments,
                        })
        else:
            prototypes = recreate_prototypes(self.kwargs['id'])
            messages.success(request, ("Formato incorrecto"))
            return render(request,self.template_name,context={
                        'id':self.kwargs['id'],
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
        equipments = Equipment.objects.all().order_by('id')
        prototypes = recreate_prototypes(0)
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
