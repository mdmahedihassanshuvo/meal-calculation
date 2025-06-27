from django.contrib import admin

# LOCAL IMPORTS
from organogram.models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'group_name', 'order', 'is_active', 'is_draft',
    ]
    search_fields = ['group_name']
    ordering = ['order']
    list_filter = ['is_active', 'is_draft']
    filter_horizontal = ['Member']
    list_editable = ['order', 'is_active', 'is_draft']
