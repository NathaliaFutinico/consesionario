from django.db import models
from empleado.models import Empleado
from cliente.models import Cliente

# Create your models here.

class Cita(models.Model): 
    fecha = models.DateTimeField()
    asesor = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='asesor')
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente')

    class Meta:
        db_table = 'cita' 