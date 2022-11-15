from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from .forms import *
from .helpers import *


class DataUpload(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('create-csv/', self.create_csv),
            path('update-csv/', self.update_csv),
            path('fix-csv/', self.fix_csv),
        ]
        return my_urls + urls
    
    def create_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES['csv_file']
            print(csv_file)
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        elif request.method == "GET":
            download_csv()

        form = CSV_Form()
        data = {"form":form}
        return render(request, 'admin/create_upload.html', data)
    
    def update_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES['csv_file']
            print(csv_file)
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CSV_Form()
        data = {"form":form}
        return render(request, 'admin/update_upload.html', data)

    def fix_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES['csv_file']
            print(csv_file)
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CSV_Form()
        data = {"form":form}
        return render(request, 'admin/fix_upload.html', data)

admin.site.register(Prototype)
admin.site.register(Material)
admin.site.register(Finishing)
admin.site.register(PropertyType)
admin.site.register(Segment)
admin.site.register(Equipment)
admin.site.register(EquipmentQuantity)
admin.site.register(Triangulo)
admin.site.register(Historical)