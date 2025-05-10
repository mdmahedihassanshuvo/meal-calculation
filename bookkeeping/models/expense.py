# DJANGO IMPORTS
from django.db import models
from django.utils.translation import gettext_lazy as _

# LOCAL IMPORTS
from member.models import CommonModel, Member


class Expense(CommonModel):
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='expenses',
        verbose_name=_('Name'),
        null=True,
        blank=True
    )
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

    class Meta:
        ordering = ['-expense_date']

    def __str__(self):
        return f"{self.member} - {self.amount}"
