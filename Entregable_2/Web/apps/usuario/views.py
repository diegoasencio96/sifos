from django.urls import reverse


def perfil(request):
    return render(request, 'usuario/perfil.html')

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render

from django.views.generic import FormView, RedirectView

# Authentication imports
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from apps.usuario.models import Donador
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url =  reverse_lazy("terreno_seguimiento")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    pattern_name = 'user_login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

class LoginRequiredMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('user_login'))
        else:
            return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

## Método que obtiene el detalle de usuario logueado
def perfil(request):
    usuario = User.objects.filter(username=request.user).first()
    return render(request, "usuario/perfil.html", {"usuario": usuario})
def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'existe': User.objects.filter(email=email).exists()
            #Donador.objects.filter(correo_electronico=email).exists()
    }
    return JsonResponse(data)