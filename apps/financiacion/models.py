from django.db import models
from django.utils.timezone import now
from apps.usuario.models import Donador

# Create your models here.
class Donacion(models.Model):
    valor = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateTimeField(default=now, blank=True)
    donador = models.ForeignKey(Donador, blank=False, null=False)

    class Meta:
        db_table = 'financiacion_donacion'

    def __str__(self):
        return "{0}".format(self.nombre)