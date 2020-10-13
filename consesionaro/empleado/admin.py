from django.contrib import admin
from .models import Empleado

# Register your models here.
class EmpleadoAdmin(admin.ModelAdmin):

    list_display = ('nombres', 'apellidos', 'tipodocumento','numdocumento','horario')


admin.site.register(Empleado, EmpleadoAdmin) 
