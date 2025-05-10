# DJANGO IMPORTS
from django.contrib import admin

# LOCAL IMPORTS
from bookkeeping.models import Deposit, Meal, Expense


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ['id', 'member', 'amount', 'deposite_date']
    search_fields = ['deposite_date', 'member']
    ordering = ['-id',]


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['id', 'member', 'meal_count', 'meal_date']
    search_fields = ['meal_date', 'member']
    ordering = ['-id',]


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount', 'expense_date']
    search_fields = ['expense_date',]
    ordering = ['-id',]
