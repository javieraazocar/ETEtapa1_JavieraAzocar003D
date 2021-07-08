from django.db import models
import uuid

from django.db.models.fields import CharField 


# Create your models here.
class Proovedor(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='Identificador')
    nomCompleto = models.CharField(max_length=50, verbose_name="Nombre Completo")
    telefono    = models.CharField(max_length=12, verbose_name="Telefono")
    direccion   = models.CharField(max_length=50, verbose_name="Direccion")
    email       = models.CharField(max_length=50, verbose_name="Email")
    pais        = models.CharField(max_length=50, verbose_name="Pais")
    contra      = models.CharField(max_length=8, verbose_name="Contrasenna")
    moneda      = models.CharField(max_length=7, verbose_name="Moneda")
    img         = models.ImageField(upload_to='web/img', null=True, blank=True)

    def __str__(self):
        return self.id