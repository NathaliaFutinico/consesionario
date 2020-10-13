from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    tipodocumento = models.CharField(db_column='tipoDocumento', max_length=10)  # Field name made lowercase.
    numdocumento = models.IntegerField(db_column='numDocumento')  # Field name made lowercase.
    direccion = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = 'cliente'

    def __str__(self):
        return self.nombres+" "+self.apellidos
