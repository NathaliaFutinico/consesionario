from django.contrib import admin
from .models import Cliente

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):

    list_display = ('nombres', 'apellidos', 'tipodocumento','numdocumento','direccion','email')


admin.site.register(Cliente, ClienteAdmin) 
