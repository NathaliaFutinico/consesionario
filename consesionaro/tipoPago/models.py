from django.db import models

# Create your models here.
class Tipodepago(models.Model):
    nombretipopago = models.CharField(db_column='nombreTipoPago', max_length=30)  # Field name made lowercase.

    class Meta:
        db_table = 'tipodepago'