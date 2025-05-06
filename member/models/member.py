# DJANGO IMPORTS
from django.db import models
from django.utils.translation import gettext_lazy as _


class CommonModel(models.Model):
    order = models.CharField(max_length=50)
    create_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_draft = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Member(CommonModel):
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

    def __str__(self):
        return self.name


class Deposit(CommonModel):
    name = models.ForeignKey(
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
