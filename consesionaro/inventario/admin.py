from django.contrib import admin
from .models import Inventario

# Register your models here.
class InventarioAdmin(admin.ModelAdmin):

    list_display = ('cantidad', 'idvehiculo')


admin.site.register(Inventario, InventarioAdmin) 
