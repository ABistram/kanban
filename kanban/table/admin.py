from django.contrib import admin
from .models import Item, Sheet, Field


# Register your models here.

class ItemsInLine(admin.StackedInline):
    model = Item
    extra = 2


class FieldAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General information', {'fields': ['name', 'field_type', 'label']}),
        ('Layout', {'fields': ['positionX', 'positionY', 'rowspan', 'colspan']})
    ]
    inlines = [ItemsInLine]
    list_display = ('name', 'field_type', 'label')
    search_fields = ['sheet__title']


class FieldsInLine(admin.TabularInline):
    model = Field
    extra = 3


class SheetAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Size', {'fields': ['sizeX', 'sizeY']}),
        ('Accessibility', {'fields': ['privacy_type'], 'classes': ['collapse']})
    ]
    inlines = [FieldsInLine]
    list_display = ('title', 'sizeX', 'sizeY', 'privacy_type')
    search_fields = ['title']


class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_type', 'content')
    search_fields = ['field__sheet__title']


admin.site.register(Item, ItemAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(Sheet, SheetAdmin)
