# DJANGO IMPORTS
from django.views.generic import TemplateView


class DepositTemplateView(TemplateView):
    template_name = 'bookkeeping/deposit.html'
