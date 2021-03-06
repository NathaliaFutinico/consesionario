# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cita(models.Model):
    fecha = models.DateTimeField()
    asesor = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='asesor')
    cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='cliente')

    class Meta:
        managed = False
        db_table = 'cita'


class Cliente(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    tipodocumento = models.CharField(db_column='tipoDocumento', max_length=10)  # Field name made lowercase.
    numdocumento = models.IntegerField(db_column='numDocumento')  # Field name made lowercase.
    direccion = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cliente'


class Empleado(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    tipodocumento = models.CharField(db_column='tipoDocumento', max_length=100)  # Field name made lowercase.
    numdocumento = models.IntegerField(db_column='numDocumento')  # Field name made lowercase.
    horario = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'empleado'
 

class Inventario(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    cantidad = models.IntegerField()
    idvehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='idvehiculo')

    class Meta:
        managed = False
        db_table = 'inventario'


class Tipodepago(models.Model):
    nombretipopago = models.CharField(db_column='nombreTipoPago', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipodepago'


class Tipovehiculo(models.Model):
    id = models.OneToOneField('Vehiculo', models.DO_NOTHING, db_column='id', primary_key=True)
    nomtipoveh = models.CharField(db_column='nomTipoVeh', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipovehiculo'


class Vehiculo(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    tipo = models.ForeignKey(Tipovehiculo, models.DO_NOTHING, db_column='tipo')
    nomvehiculo = models.CharField(db_column='nomVehiculo', max_length=20)  # Field name made lowercase.
    preciovehiculo = models.FloatField(db_column='precioVehiculo')  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'vehiculo'


class Venta(models.Model):
    fecha = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente')
    vehiculo = models.CharField(max_length=10)
    valorpagar = models.FloatField(db_column='valorPagar')  # Field name made lowercase.
    tipopago = models.ForeignKey(Tipodepago, models.DO_NOTHING, db_column='tipoPago')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'venta'


class Ventaxvehiculo(models.Model):
    id = models.IntegerField(primary_key=True)
    idvehiculo = models.ForeignKey(Vehiculo, models.DO_NOTHING, db_column='idvehiculo')
    idventa = models.ForeignKey(Venta, models.DO_NOTHING, db_column='idventa')

    class Meta:
        managed = False
        db_table = 'ventaxvehiculo'
