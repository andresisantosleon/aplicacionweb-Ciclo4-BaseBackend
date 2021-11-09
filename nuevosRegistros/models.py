#from django.db import models

# Create your models here.
from django.db import models
from datetime import date
#from django.contrib.auth.models import User

# Modelo de materia prima
class materiaPrima(models.Model):
    objects = None
    materiaPrimaId = models.AutoField(primary_key=True)
    materiaPrima_codigo = models.IntegerField(default=0)
    materiaPrima_categoria_id = models.CharField(max_length=15, default=0)
    materiaPrima_descripcion = models.CharField(max_length=10, default="---", help_text="Por favor ingrese una descripción")
    materiaPrima_existencias = models.IntegerField(default=0)
    materiaPrima_unidad = models.CharField(max_length=5, default=0, help_text="ingrese las unidades de materia prima")

# Modelo de proveedores
class proveedores(models.Model):
    objects = None
    proveedorId = models.AutoField(primary_key=True)
    proveedor_Name = models.CharField(max_length=60, default='0')
    proveedor_Telefono = models.IntegerField(null=True, blank=True)
    proveedor_Direccion = models.CharField(max_length=50, default='0')
    proveedor_Email = models.CharField(max_length=50, default='0')
    proveedor_Nit = models.CharField(max_length=50, null=True, blank=True)

# Modelo de movimiento de inventarios

"""
class movimientos(models.Model):
    pass

"""
class movimientos(models.Model):
    objects = None
    entradaMateriaPrimaId = models.AutoField(primary_key=True)
    idMateriaPrima = models.ForeignKey(materiaPrima, related_name="refMateriaprima", on_delete=models.CASCADE)
    movimientoProveedor = models.ForeignKey(proveedores, related_name="refProveedor", on_delete=models.CASCADE)
    movimientoFecha = models.DateField(help_text="Por favor indique la fecha del movimiento", default=date.today)
    movimientoLote = models.CharField(max_length= 10, default="", help_text="Por favor ingrese el lote")
    movimientoCantidad = models.IntegerField(default=0, help_text="Por favor ingrese la cantidad total de unidades de materia prima a registrar")
    movimientoPrecioUnitario = models.FloatField(default=0, help_text="Por favor ingrese el precio unitario de la materia prima")
    movimientoTipo = models.IntegerField(default=0)


p = proveedores(proveedor_Name="Felipe Suarez", proveedor_Telefono=31325, proveedor_Direccion="Cll. 12A # 8-76", proveedor_Email="suarezp@gmail.com", proveedor_Nit="213434465-2")
p.save()

m=materiaPrima()
m.save()
