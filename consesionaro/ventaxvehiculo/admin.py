from django.contrib import admin
from .models import Ventaxvehiculo

# Register your models here.
class VentaxvehiculoAdmin(admin.ModelAdmin):

    list_display = ('idvehiculo','idventa')


admin.site.register(Ventaxvehiculo, VentaxvehiculoAdmin) 
