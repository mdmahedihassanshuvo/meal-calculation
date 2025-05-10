# DJANGO IMPORTS
from django.db import models
from django.utils.translation import gettext_lazy as _

# LOCAL IMPORTS
from member.models import CommonModel


class Expense(CommonModel):
    amount = models.DecimalField(
        _('Expense Amount'),
        max_digits=12,
        decimal_places=3,
        null=True,
        blank=True
    )
    expense_date = models.DateField(
        _('Expense Date')
    )

    def __str__(self):
        return str(self.amount)
