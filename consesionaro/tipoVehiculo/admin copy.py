from django.contrib import admin
from .models import Tipovehiculo

# Register your models here.
class TipovehiculoAdmin(admin.ModelAdmin):

    list_display = ('nomtipoveh')


admin.site.register(Tipovehiculo, TipovehiculoAdmin) 
