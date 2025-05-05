from django.contrib import admin

# LOCAL IMPORTS
from Core.models import (
    CustomUser,
    # UserCategory
)


@admin.register(CustomUser)
class CustomUserModelAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'full_name'
    ]
    search_fields = ['id', 'email',]
    ordering = ['-id',]
