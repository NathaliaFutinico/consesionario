from django.db import models
from vehiculo.models import Vehiculo
from venta.models import Venta

# Create your models here.
class Ventaxvehiculo(models.Model):
    idvehiculo = models.ForeignKey(Vehiculo, models.DO_NOTHING, db_column='idvehiculo')
    idventa = models.ForeignKey(Venta, models.DO_NOTHING, db_column='idventa')

    class Meta:
        db_table = 'ventaxvehiculo'

