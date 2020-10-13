from django.contrib import admin
from .models import Tipodepago

# Register your models here.
class TipodepagoAdmin(admin.ModelAdmin):

    list_display = ('nombretipopago',)


admin.site.register(Tipodepago, TipodepagoAdmin) 
