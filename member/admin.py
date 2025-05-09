# DJANGO IMPORTS
from django.contrib import admin

# LOCAL IMPORTS
from member.models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name'
    ]
    search_fields = ['id', 'name']
    ordering = ['-id',]
