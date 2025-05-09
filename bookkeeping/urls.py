# DJANGO IMPORTS
from django.urls import path

# LOCAL IMPORTS
from bookkeeping.views import DepositTemplateView

app_name = 'bookkeeping'

urlpatterns = [
    path(
        'deposit/',
        DepositTemplateView.as_view(),
        name='deposit'
    )
]
