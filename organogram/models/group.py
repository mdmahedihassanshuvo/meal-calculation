# DJANGO IMPORTS
from django.db import models

# LOCAL IMPORTS
from member.models import Member, CommonFieldModel


class Group(CommonFieldModel):
    Member = models.ManyToManyField(
        Member,
        related_name='groups',
        blank=True
    )
    group_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.group_name}"
