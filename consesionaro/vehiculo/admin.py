from django.contrib import admin
from .models import Vehiculo

# Register your models here.
class VehiculoAdmin(admin.ModelAdmin):

    list_display = ('tipo','nomvehiculo','preciovehiculo')


admin.site.register(Vehiculo, VehiculoAdmin) 
