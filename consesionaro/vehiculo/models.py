from django.db import models
from tipoVehiculo.models import Tipovehiculo


# Create your models here.
class Vehiculo(models.Model):
    tipo = models.ForeignKey(Tipovehiculo, models.DO_NOTHING, db_column='tipo')
    nomvehiculo = models.CharField(db_column='nomVehiculo', max_length=20)  # Field name made lowercase.
    preciovehiculo = models.FloatField(db_column='precioVehiculo')  # Field name made lowercase.
    
    class Meta:
        db_table = 'vehiculo'