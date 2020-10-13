from django.db import models
from cliente.models import Cliente
from tipoPago.models import Tipodepago

# Create your models here.
class Venta(models.Model):
    fecha = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente')
    vehiculo = models.CharField(max_length=10)
    valorpagar = models.FloatField(db_column='valorPagar')  # Field name made lowercase.
    tipopago = models.ForeignKey(Tipodepago, models.DO_NOTHING, db_column='tipoPago')  # Field name made lowercase.

    class Meta:
        db_table = 'venta'