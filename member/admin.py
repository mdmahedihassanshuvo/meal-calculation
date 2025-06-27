# DJANGO IMPORTS
from django.contrib import admin

# LOCAL IMPORTS
from member.models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'is_member',
        'is_manager'
    ]
    search_fields = ['id', 'name']
    ordering = ['-id',]
