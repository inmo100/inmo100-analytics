from atexit import register
import site
from django.contrib import admin
from location.models import *

# Register your models here.

admin.site.register(State)
admin.site.register(Corridor)
admin.site.register(Municipality)
admin.site.register(Colony)