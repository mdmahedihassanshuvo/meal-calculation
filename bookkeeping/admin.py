# DJANGO IMPORTS
from django.contrib import admin

# LOCAL IMPORTS
from bookkeeping.models import Deposit


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount', 'deposite_date']
    search_fields = ['deposite_date',]
    ordering = ['-id',]
