# DJANGO IMPORTS
from django.urls import path

# LOCAL IMPORTS
from bookkeeping.api.views import (
    DepositListCreateAPIView,
    MealListCreateAPIView
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
]
