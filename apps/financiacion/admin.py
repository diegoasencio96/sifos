from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from apps.financiacion.models import *

@admin.register(Donacion)
class Donacion(ImportExportActionModelAdmin):
    pass
