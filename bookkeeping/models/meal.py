# DJANGO IMPORTS
from django.db import models
from django.utils.translation import gettext_lazy as _

# LOCAL IMPORTS
from member.models import CommonFieldModel, Member


class Meal(CommonFieldModel):
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='meals',
        verbose_name=_('Name')
    )
    meal_count = models.PositiveIntegerField(
        _('Number of Meals'),
        default=1
    )
    meal_date = models.DateField(
        _('Meal Date')
    )

    def __str__(self):
        return f"{self.member} - {self.meal_count} on {self.meal_date}"
