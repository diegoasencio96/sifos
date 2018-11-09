
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView, RedirectView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from apps.usuario.models import Donador

from django.http import JsonResponse

def login(request):
    return render(request, 'login.html')

def perfil(request):
    return render(request, 'usuario/perfil.html')

def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'existe': Donador.objects.filter(correo_electronico=email).exists()
    }
    return JsonResponse(data)