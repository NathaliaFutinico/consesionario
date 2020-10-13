from django.contrib import admin
from .models import Venta

# Register your models here.
class VentaAdmin(admin.ModelAdmin):

    list_display = ('fecha','cliente','vehiculo','valorpagar','tipopago')


admin.site.register(Venta, VentaAdmin) 
