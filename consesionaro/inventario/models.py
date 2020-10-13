from django.db import models
from vehiculo.models import Vehiculo

# Create your models here.
class Inventario(models.Model):
    cantidad = models.IntegerField()
    idvehiculo = models.ForeignKey(Vehiculo, models.DO_NOTHING, db_column='idvehiculo')

    class Meta:
        db_table = 'inventario'
