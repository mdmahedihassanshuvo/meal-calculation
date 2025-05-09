# DJANGO IMPORTS
from django.urls import path

# LOCAL IMPORTS
from bookkeeping.api.views import DepositListCreateAPIView


urlpatterns = [
    path(
        'deposit-list/<int:member_id>/',
        DepositListCreateAPIView.as_view(),
        name='deposit_list'
    ),
    path(
        'create-deposit/',
        DepositListCreateAPIView.as_view(),
        name='create_deposit'
    ),
]
