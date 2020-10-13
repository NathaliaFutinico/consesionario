from django.contrib import admin
from .models import Cita

# Register your models here.
class CitaAdmin(admin.ModelAdmin):

    list_display = ('fecha', 'asesor', 'cliente')


admin.site.register(Cita, CitaAdmin) 
