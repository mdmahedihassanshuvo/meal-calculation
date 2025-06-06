# DJANGO IMPORTS
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class DepositTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'bookkeeping/deposit.html'
