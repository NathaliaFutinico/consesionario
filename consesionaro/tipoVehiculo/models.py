from django.db import models

# Create your models here.
class Tipovehiculo(models.Model):
    nomtipoveh = models.CharField(db_column='nomTipoVeh', max_length=20)  # Field name made lowercase.

    class Meta:
        db_table = 'tipovehiculo'