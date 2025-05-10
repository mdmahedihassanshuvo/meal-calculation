# DJANGO IMPORTS
from django.db import models
from django.utils.translation import gettext_lazy as _

# LOCAL IMPORTS
from member.models import CommonModel, Member


class Deposit(CommonModel):
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='deposits',
        verbose_name=_('Name')
    )
    amount = models.DecimalField(
        _('Deposit Amount'),
        max_digits=12,
        decimal_places=3,
        null=True,
        blank=True
    )
    deposite_date = models.DateField(
        _('Diposit Date')
    )

    def __str__(self):
        return f"{self.name} - {self.amount}"
