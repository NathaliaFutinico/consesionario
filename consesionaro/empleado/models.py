from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    tipodocumento = models.CharField(db_column='tipoDocumento', max_length=100)  # Field name made lowercase.
    numdocumento = models.IntegerField(db_column='numDocumento')  # Field name made lowercase.
    horario = models.CharField(max_length=30)

    class Meta:
        db_table = 'empleado'