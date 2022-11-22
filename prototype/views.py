from tabnanny import check
from django.shortcuts import render
from django_filters.views import FilterView
from django.views.generic import ListView
from django.contrib import messages
from django.shortcuts import redirect
from .filter import PrototypeFilter
from .forms import *
from .models import *
from .helpers import *

class CreatePrototype(ListView):
    template_name = 'pages/create_prototype.html'
    
    def get(self,request,*args,**kwargs):
        download_csv()
        project = Project.objects.get(id=self.kwargs['id'])
        prototypes = recreate_prototypes(self.kwargs['id'])
        finishings = Finishing.objects.order_by("id")
        equipments = Equipment.objects.all().order_by('id')

        return render(request, self.template_name, context={
            'id': self.kwargs['id'],
            'proyecto': project,
            'prototypes_filter': prototypes,
            'finishings_type': finishings,
            'equipments': equipments,
            })
    
    def post(self,request,*args,**kwargs):
        csv_import = CSV_Form(request.POST, request.FILES)
        project_field = request.POST['project_field']
        project = Project.objects.get(id=self.kwargs['id'])
        finishings = Finishing.objects.order_by("id")
        equipments = Equipment.objects.all().order_by('id')
        if csv_import.is_valid():
            response = handle_uploaded_file(
                request.FILES['csv'], project_field, 'c')
            prototypes = recreate_prototypes(self.kwargs['id'])

            context = {
                'id': self.kwargs['id'],
                'proyecto': project,
                'prototypes_filter': prototypes,
                'finishings_type': finishings,
                'equipments': equipments,
            }

            if response == 1:
                messages.success(request, ("Formato de Plantilla invalida"))
                return render(request, self.template_name, context)

            elif response == 2:
                messages.success(request, ("Formato no es csv"))
                return render(request, self.template_name, context)

            elif response == 3:
                messages.success(request, ("Plantilla vacia"))
                return render(request, self.template_name, context)
            elif response == 4:
                messages.success(
                    request, ("Hubo un error, por favor revisa que no haya errores en el archivo"))
                return render(request, self.template_name, context)
            else:
                messages.success(request, ("Plantilla se pudo actualizar"))
                return render(request, self.template_name, context)
        else:
            prototypes = recreate_prototypes(self.kwargs['id'])
            messages.success(request, ("Formato incorrecto"))
            return render(request, self.template_name, context={
                'id': self.kwargs['id'],
                'proyecto': project,
                'prototypes_filter': prototypes,
                'finishings_type': finishings,
                'equipments': equipments,
            })

# class based view to list all prototypes
# class PrototypesListView(ListView):
#     template_name = 'pages/prototypes.html'
#     model = Prototype
#     def get(self, request):
#         finishings = Finishing.objects.order_by("id")
#         equipments = Equipment.objects.all().order_by('id')
#         prototypes_filter = recreate_prototypes(0)
#         print(prototypes_filter)
#         return render(request,self.template_name,context={
#             'prototypes_filter': prototypes_filter,
#             'finishings_type': finishings,
#             'equipments': equipments,
#         })

# Class based view to update prototype


class UpdatePrototype(ListView):
    template_name = 'pages/update_prototypes.html'
    model = Segment
    # Overwriting the method get from the class

    def get(self, request, *args, **kwargs):
        delete_csv(self.kwargs['id'])
        update_download_csv(self.kwargs['id'])
        project = Project.objects.get(id=self.kwargs['id'])
        prototypes = recreate_prototypes(self.kwargs['id'])
        finishings = Finishing.objects.order_by("id")
        equipments = Equipment.objects.all().order_by('id')

        return render(request, self.template_name, context={
            'id': self.kwargs['id'],
            'proyecto': project,
            'project_name': project.name,
            'prototypes_filter': prototypes,
            'finishings_type': finishings,
            'equipments': equipments,
            'file_name': 'plantilla_prototipos_'+project.name+'.csv',
        })
    # Overwriting the method post from the class

    def post(self, request, *args, **kwargs):
        csv_import = CSV_Form(request.POST, request.FILES)
        project_field = request.POST['project_field']
        finishings = Finishing.objects.order_by("id")
        equipments = Equipment.objects.all().order_by('id')
        project = Project.objects.get(id=self.kwargs['id'])

        if csv_import.is_valid():
            response = handle_uploaded_file(
                request.FILES['csv'], project_field, 'u')
            prototypes = recreate_prototypes(self.kwargs['id'])
            context = {
                'id': self.kwargs['id'],
                'proyecto': project,
                'project_name': project.name,
                'prototypes_filter': prototypes,
                'finishings_type': finishings,
                'equipments': equipments,
                'file_name': 'plantilla_prototipos_'+project.name+'.csv',
            }
            if response == 1:
                messages.success(request, ("Formato de Plantilla invalida"))
                return render(request, self.template_name, context)
            elif response == 2:
                messages.success(request, ("Plantilla no es csv"))
                return render(request, self.template_name, context)
            elif response == 3:
                messages.success(request, ("Plantilla vacia"))
                return render(request, self.template_name, context)
            elif response == 4:
                messages.success(
                    request, ("Hubo un error, por favor revisa que no haya errores en la plantilla"))
                return render(request, self.template_name, context)
            else:
                messages.success(request, ("Plantilla se pudo actualizar"))
                return render(request, self.template_name, context)
        else:
            prototypes = recreate_prototypes(self.kwargs['id'])
            messages.success(request, ("Formato incorrecto"))
            return render(request, self.template_name, context={
                'id': self.kwargs['id'],
                'proyecto': project,
                'project_name': project.name,
                'prototypes_filter': prototypes,
                'finishings_type': finishings,
                'equipments': equipments,
                'file_name': 'plantilla_prototipos_'+project.name+'.csv',
            })

# Class based view to fix prototype


class FixPrototype(ListView):
    template_name = 'pages/fix_prototypes.html'
    model = Segment
    #Overwriting the method get from the class
    def get(self,request,*args,**kwargs):
        delete_csv(self.kwargs['id'])
        update_download_csv(self.kwargs['id'])
        project = Project.objects.get(id=self.kwargs['id'])
        prototypes = recreate_prototypes(self.kwargs['id'])
        finishings = Finishing.objects.order_by("id")
        equipments = Equipment.objects.all().order_by('id')

        return render(request, self.template_name, context={
            'id': self.kwargs['id'],
            'proyecto': project,
            'project_name': project.name,
            'prototypes_filter': prototypes,
            'finishings_type': finishings,
            'equipments': equipments,
        })

    #Overwriting the method post from the class
    def post(self,request,*args,**kwargs):
        csv_import = CSV_Form(request.POST, request.FILES)
        project_field = request.POST['project_field']
        if csv_import.is_valid():
            handle_uploaded_file(request.FILES['csv'], project_field, 'f')
            return redirect("prototypes")
        else:
            return render(request, self.template_name, context={'Prueba': 'No se pudo'})


"""class PrototypesList(FilterView):
    model = Prototype
    template_name: str = 'pages/prototypes/home.html'
    filterset_class = PrototypeFilter
    context_object_name = 'prototypes_list'"""

class PrototypesList(ListView):
    template_name = 'pages/prototypes/home.html'
    def get(self, request, *args, **kwargs):
        #------------------------------------------------------------------------
        # This is for the select form
        prototypes_form = Prototype.objects.all()
        projects_form = Project.objects.all()
        segment_form = Segment.objects.all()
        propertyType_form = PropertyType.objects.all()
        #------------------------------------------------------------------------
        prototypes_id = request.GET.getlist('prototype')
        prototypes_id = check_arguments(prototypes_id)
        projects_id = request.GET.getlist('project')
        projects_id = check_arguments(projects_id)
        segments_id = request.GET.getlist('segment')
        segments_id = check_arguments(segments_id)
        propertyTypes = request.GET.getlist('propertyType')
        propertyTypes = check_arguments(propertyTypes)
        total_units = [request.GET.get('total_units_min',''),request.GET.get('total_units_max','')]
        total_units = check_arguments(total_units)
        sold_units = [request.GET.get('sold_units_min',''),request.GET.get('sold_units_max','')]
        sold_units = check_arguments(sold_units)
        prototypes = Prototype.objects.project_filter(projects_id)
        prototypes = Prototype.objects.prototype_filter(prototypes,prototypes_id)
        prototypes = Prototype.objects.segment_filter(segments_id,prototypes)
        prototypes = Prototype.objects.propertyType_filter(propertyTypes,prototypes)
        prototypes = Prototype.objects.total_units_filter(total_units,prototypes)
        prototypes = Prototype.objects.total_units(prototypes)
        prototypes = Historical.objects.available_units_filter(sold_units,prototypes)
        #------------------------------------------------------------------------
        #This line needs to be at the end of the filtering section
        prototypes = Prototype.objects.get_prototypes(prototypes)
        #------------------------------------------------------------------------
        
        equipments = Equipment.objects.all().order_by('id')
        finishings = Finishing.objects.all().order_by('id')
        prototypes_list = bring_prototypes(prototypes)
        return render(request, self.template_name, context={
            'prototypes_list':prototypes_list,
            'equipments':equipments,
            'finishings':finishings,
            'prototypes_form':prototypes_form,
            'projects_form':projects_form,
            'segment_form':segment_form,
            'propertyType_form':propertyType_form,
        })
