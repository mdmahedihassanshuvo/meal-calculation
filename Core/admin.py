# DJANGO IMPORTS
from django.contrib import admin

# LOCAL IMPORTS
from Core.models import (
    CustomUser,
    MenuSection,
    MenuItem
)


@admin.register(CustomUser)
class CustomUserModelAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name']
    search_fields = ['id', 'email']
    ordering = ['-id']


@admin.register(MenuSection)
class MenuSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'is_draft',]
    search_fields = ['title']
    ordering = ['order']
    list_filter = ['is_active', 'is_draft']
    list_editable = ['order', 'is_active', 'is_draft']


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    fk_name = 'parent'
    extra = 0
    fields = ['title', 'url_name', 'icon_class', 'order', 'is_active']
    ordering = ['order']
    show_change_link = True


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'section', 'parent', 'url_name', 'order', 'is_active', 'is_draft' # noqa
    ]
    search_fields = ['title', 'url_name']
    ordering = ['section__order', 'order']
    list_filter = ['section', 'is_active', 'is_draft']
    list_editable = ['order', 'is_active', 'is_draft']
    filter_horizontal = ['groups']
    inlines = [MenuItemInline]
