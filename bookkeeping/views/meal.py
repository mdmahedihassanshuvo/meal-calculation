# DJANGO IMPORTS
from django.views.generic import TemplateView


class MealTemplateView(TemplateView):
    template_name = 'bookkeeping/meal.html'
