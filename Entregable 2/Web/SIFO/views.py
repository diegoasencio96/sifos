
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.views.generic import FormView, RedirectView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

class Login(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = '/poligono/seguimiento'

    def form_valid(self, form):
        return super(Login, self).form_valid(form)

    def form_invalid(self, form):
        return super(Login, self).form_invalid(form)
