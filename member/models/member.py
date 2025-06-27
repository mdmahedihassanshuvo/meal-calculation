# DJANGO IMPORTS
from django.db import models
from django.utils.translation import gettext_lazy as _

# LOCAL IMPORTS
from Core.models import CustomUser, CommonFieldModel


class Member(CommonFieldModel):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='member_profile',
        null=True,
        blank=True
    )
    name = models.CharField(
        _('Name'),
        max_length=100
    )
    nickname = models.CharField(
        _('Nick Name'),
        max_length=100,
        null=True,
        blank=True
    )
    profile_image = models.ImageField(
        _('Profile Image'),
        upload_to='member_images/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    @property
    def total_deposit_amount(self):
        total = self.deposits.aggregate(total=models.Sum('amount'))['total']
        return total if total else 0.000

    @property
    def total_meal(self):
        total = self.meals.aggregate(total=models.Sum('meal_count'))['total']
        return total if total else 0

    @property
    def meal_charge(self):
        from bookkeeping.models import Expense, Meal
        total_expense = Expense.objects.aggregate(
            total=models.Sum('amount')
        )['total'] or 0
        total_meal = Meal.objects.aggregate(
            total=models.Sum('meal_count')
        )['total'] or 0

        if total_meal == 0:
            return 0.000

        meal_charge_per_meal = total_expense / total_meal

        return round(meal_charge_per_meal, 3)

    @property
    def total_expense_amount(self):
        total_expense = round(self.total_meal * self.meal_charge, 3)
        return total_expense if total_expense else 0.000
