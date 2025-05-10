# DJANGO IMPORTS
from django.urls import path

# LOCAL IMPORTS
from bookkeeping.api.views import (
    DepositListCreateAPIView,
    MealListCreateAPIView,
    ExpenseListCreateAPIView
)


urlpatterns = [
    path(
        'deposit-list/',
        DepositListCreateAPIView.as_view(),
        name='deposit_list'
    ),
    path(
        'create-deposit/',
        DepositListCreateAPIView.as_view(),
        name='create_deposit'
    ),
    path(
        'meal-list/',
        MealListCreateAPIView.as_view(),
        name='meal_list'
    ),
    path(
        'create-meal/',
        MealListCreateAPIView.as_view(),
        name='create_meal'
    ),
    path(
        'expense-list/',
        ExpenseListCreateAPIView.as_view(),
        name='expense_list'
    ),
    path(
        'create-expense/',
        ExpenseListCreateAPIView.as_view(),
        name='create_expense'
    ),
]
