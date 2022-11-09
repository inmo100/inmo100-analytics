from django.shortcuts import render
from django.views.generic import ListView
from .forms import *
from django.shortcuts import redirect
from .models import *
from .helpers import *

class CreatePrototype(ListView):
    template_name = 'pages/form_prototype.html'
    model = Segment
    def get(self,request,*args,**kwargs):
        download_csv()
        return render(request,self.template_name,context={
            'list_segment':Segment.objects.all(),
            'id':self.kwargs['id']
            })
    def post(self,request,*args,**kwargs):
        csv_import = CSV_Form(request.POST, request.FILES)
        project_field = request.POST['project_field']
        if csv_import.is_valid():
                handle_uploaded_file(request.FILES['csv'],project_field,'c')
                return redirect("prototypes")
        else:
            return render(request,self.template_name,context={'Prueba':'No se pudo'})


class PrototypesListView(ListView):
    template_name = 'pages/prototypes.html'
    model = Prototype
    def get(self, request, *args,**kwargs):
        return render(request,self.template_name,context={
            'prototype_list': Prototype.objects.all(),
        })


class UpdatePrototype(ListView):
    template_name = 'pages/form_update_prototypes.html'
    model = Segment
    def get(self,request,*args,**kwargs):
        download_csv()
        return render(request,self.template_name,context={
            'id':self.kwargs['id']
            })
    def post(self,request,*args,**kwargs):
        csv_import = CSV_Form(request.POST, request.FILES)
        project_field = request.POST['project_field']
        if csv_import.is_valid():
                handle_uploaded_file(request.FILES['csv'],project_field,'u')
                return redirect("prototypes")
        else:
            return render(request,self.template_name,context={'Prueba':'No se pudo'})