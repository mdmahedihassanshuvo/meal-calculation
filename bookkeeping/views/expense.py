# DJANGO IMPORTS
from django.views.generic import TemplateView


class ExpenseTemplateView(TemplateView):
    template_name = 'bookkeeping/expense.html'
