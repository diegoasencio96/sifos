from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from apps.general.models import *

@admin.register(Municipio)
class Municipio(ImportExportActionModelAdmin):
    pass

@admin.register(Especie)
class Especie(ImportExportActionModelAdmin):
    pass

@admin.register(EspecieMunicipio)
class EspecieMunicipio(ImportExportActionModelAdmin):
    pass

@admin.register(TipoPatron)
class TipoPatron(ImportExportActionModelAdmin):
    pass

@admin.register(Robot)
class Robot(ImportExportActionModelAdmin):
    pass