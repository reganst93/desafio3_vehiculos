from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True)
    marca = models.CharField(max_length=20, null=False, blank=False)
    modelo = models.CharField(max_length=20, null=False, blank=False)
    año = models.IntegerField(max_length=4,null=False, blank=False)

class Chofer(models.Model):
    rut = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(null=False,blank=False)
    vehiculo_id = models.OneToOneField(Vehiculo, on_delete=models.CASCADE, primary_key=True)


class RegistroContabilidad(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_compra = models.DateField(null=False, blank=False)
    valor = models.FloatField(null=False, blank=False)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    
  
