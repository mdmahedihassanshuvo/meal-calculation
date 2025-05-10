# DJANGO IMPORTS
from django.urls import path

# LOCAL IMPORTS
from bookkeeping.views import (
    DepositTemplateView,
    MealTemplateView,
    ExpenseTemplateView
)

app_name = 'bookkeeping'

urlpatterns = [
    path(
        'deposit/',
        DepositTemplateView.as_view(),
        name='deposit'
    ),
    path(
        'meal/',
        MealTemplateView.as_view(),
        name='meal'
    ),
    path(
        'expense/',
        ExpenseTemplateView.as_view(),
        name='expense'
    ),
]
