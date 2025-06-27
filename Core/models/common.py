# DJANGO IMPORTS
from django.db import models


class CommonFieldModel(models.Model):
    order = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    is_member = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_draft = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        'Core.CustomUser',
        on_delete=models.CASCADE,
        related_name='%(class)s_created_by',
        null=True,
        blank=True
    )

    class Meta:
        abstract = True
