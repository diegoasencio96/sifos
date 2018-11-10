from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from apps.terreno.models import *

@admin.register(Poligono)
class Poligono(ImportExportActionModelAdmin):
    pass

@admin.register(PuntoSiembra)
class PuntoSiembra(ImportExportActionModelAdmin):
    pass

@admin.register(Siembra)
class Siembra(ImportExportActionModelAdmin):
    pass