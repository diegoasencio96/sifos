from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from apps.terreno.models import Poligono

def index(request):
    obj = Poligono.objects.all()
    obj_nombre = Poligono.nombre
    obj_coordenadas_puntos = Poligono.coordenadas_puntos
    obj_area = Poligono.area
    obj_perimetro = Poligono.perimetro
    obj_tipo_patron = Poligono.tipo_patron
    obj_municipio = Poligono.municipio
    obj_usuario = Poligono.usuario

    for abc in obj:
        obj_nombre = abc.nombre
        obj_coordenadas_puntos = abc.coordenadas_puntos
        obj_area = abc.area
        obj_perimetro= abc.perimetro
        obj_tipo_patron = abc.tipo_patron
        obj_municipio = abc.municipio
        obj_usuario = abc.usuario

    context = {
        "obj":obj,
        "obj_nombre":obj_nombre,
        "obj_coordenadas_puntos":obj_coordenadas_puntos,
        "obj_area":obj_area,
        "obj_perimetro":obj_perimetro,
        "obj_tipo_patron":obj_tipo_patron,
        "obj_municipio":obj_municipio,
        "obj_usuario":obj_usuario
    }
    return render(request, "terreno/index.html", context)

def registro(request):
    return render(request, "terreno/registrar.html")