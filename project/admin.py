from django.contrib import admin
from django.utils.html import format_html
from django.shortcuts import redirect, render
from django.urls import path, reverse
from django.contrib import messages
from .models import *
from prototype.forms import *
from prototype.helpers import *

# manage prototype data from admin
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'developer_field', 'colony_field', 'address', 'datos')

    # add custom urls to admin panel
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('<int:id>/create/', self.create_csv, name='crear'),
            path('<int:id>/update/', self.update_csv, name='actualizar'),
            path('<int:id>/fix/', self.fix_csv, name='arreglar'),
        ]
        return my_urls + urls

    # add custom buttons to project admin view
    def datos(self, obj):
        return format_html(
            '<a class="button" href={}>crear</a>&nbsp;'
            '<a class="button" href={}>actualizar</a>&nbsp;'
            '<a class="button" href={}>arreglar</a>',
            reverse('admin:crear', args=[obj.pk]),
            reverse('admin:actualizar', args=[obj.pk]),
            reverse('admin:arreglar', args=[obj.pk]),
        )
    
    # create prototypes for project
    # Use Case: 32
    def create_csv(self, request, id):
        if request.method == "POST":
            csv_import = CSV_Form(request.POST, request.FILES)
            if csv_import.is_valid():
                csv_file = request.FILES['csv_file']
                response = handle_uploaded_file(csv_file, id, 'c')
                
                if response == 1:
                    self.message_user(request, "Formato de plantilla invalida", level=messages.ERROR)
                    return redirect(".")
                elif response == 2:
                    self.message_user(request, "Formato no es csv", level=messages.ERROR)
                    return redirect(".")
                elif response == 3:
                    self.message_user(request, "Plantilla vacia", level=messages.ERROR)
                    return redirect(".")
                elif response == 4:
                    self.message_user(request, "Hubo un error, por favor asegura que el archivo este correcto. Recuerda que aqui solo se crean nuevos prototipos.", level=messages.ERROR)
                    return redirect(".")
                else:
                    self.message_user(request, "Tu plantilla se pudo subir")
                    return redirect("/admin/project/project")
            else:
                self.message_user(request, "Formato incorrecto", level=messages.ERROR)
                return redirect(".")

        elif request.method == "GET":
            download_csv()

        form = CSV_Form()
        data = {"form":form}
        return render(request, 'admin/create_upload.html', data)
    
    # update prototypes information
    # Use Case: 31
    def update_csv(self, request, id):
        if request.method == "POST":
            csv_import = CSV_Form(request.POST, request.FILES)
            if csv_import.is_valid():
                csv_file = request.FILES['csv_file']
                response = handle_uploaded_file(csv_file, id, 'u')
                if response == 1:
                    self.message_user(request, "Formato de plantilla invalida", level=messages.ERROR)
                    return redirect(".")
                elif response == 2:
                    self.message_user(request, "Formato no es csv", level=messages.ERROR)
                    return redirect(".")
                elif response == 3:
                    self.message_user(request, "Plantilla vacia", level=messages.ERROR)
                    return redirect(".")
                elif response == 4:
                    self.message_user(request, "Hubo un error, por favor revisa que no haya errores en el archivo", level=messages.ERROR)
                    return redirect(".")
                else:
                    self.message_user(request, "Tu plantilla se pudo subir")
                    return redirect("/admin/project/project")
            else:
                self.message_user(request, "Formato incorrecto", level=messages.ERROR)
                return redirect(".")

        elif request.method == "GET":
            delete_csv(id)
            update_download_csv(id)
        
        project = Project.objects.get(id=id)
        form = CSV_Form()
        data = {"form":form, 'file_name': 'plantilla_prototipos_'+project.name+'.csv'}
        return render(request, 'admin/update_upload.html', data)

    # fix recent mistake in data upload
    # Use Case: 23
    def fix_csv(self, request, id):
        if request.method == "POST":
            csv_import = CSV_Form(request.POST, request.FILES)
            if csv_import.is_valid():
                csv_file = request.FILES['csv_file']
                response = handle_uploaded_file(csv_file, id, 'f')
                if response == 1:
                    self.message_user(request, "Formato de plantilla invalida", level=messages.ERROR)
                    return redirect(".")
                elif response == 2:
                    self.message_user(request, "Formato no es csv", level=messages.ERROR)
                    return redirect(".")
                elif response == 3:
                    self.message_user(request, "Plantilla vacia", level=messages.ERROR)
                    return redirect(".")
                elif response == 4:
                    self.message_user(request, "Hubo un error, por favor revisa que no haya errores en el archivo", level=messages.ERROR)
                    return redirect(".")
                else:
                    self.message_user(request, "Tu plantilla se pudo subir")
                    return redirect("/admin/project/project")
            else:
                self.message_user(request, "Formato incorrecto", level=messages.ERROR)
                return redirect(".")
                
        elif request.method == "GET":
            delete_csv(id)
            update_download_csv(id)

        project = Project.objects.get(id=id)
        form = CSV_Form()
        data = {"form":form, 'file_name': 'plantilla_prototipos_'+project.name+'.csv'}
        return render(request, 'admin/fix_upload.html', data)

# register models
admin.site.register(Amenity)
admin.site.register(Developer)