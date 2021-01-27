from django.contrib import admin
from .models import Item, Table, Field

# Register your models here.

admin.site.register(Item)
admin.site.register(Field)
admin.site.register(Table)