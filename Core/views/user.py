# DJANGO IMPORTS
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse

# REST_FRAMEWORK IMPORTS
from rest_framework.views import APIView


class RegisterView(TemplateView):
    template_name = 'Core/register.html'


class LoginView(TemplateView):
    template_name = 'Core/login.html'


class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('Core:login'))
