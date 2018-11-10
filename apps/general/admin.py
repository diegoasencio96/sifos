from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from apps.usuario.models import *

@admin.register(Donador)
class Donador(ImportExportActionModelAdmin):
    pass
