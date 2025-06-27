# DJANGO IMPORTS
from django.db import models
from django.utils.translation import gettext_lazy as _

# LOCAL IMPORTS
from member.models import CommonFieldModel


class Designation(CommonFieldModel):
    name = models.CharField(
        _('Designation'), max_length=255,
        null=True, blank=True
    )
    bn_name = models.CharField(
        _('Designation(Bangla)'), max_length=255, null=True, blank=True)
    code = models.CharField(
        _('code'), max_length=255,
        null=True, blank=True, unique=True,
        help_text='1001 for Executive Engineer'
    )

    def __str__(self):
        """User model string representation"""
        return str(self.name)
