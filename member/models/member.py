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
    image = models.ImageField(
        _('Image'),
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
