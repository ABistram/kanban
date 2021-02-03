from django.contrib import admin
from .models import Item, Sheet, Field, Style

# Register your models here.

admin.site.register(Item)
admin.site.register(Sheet)
admin.site.register(Field)
admin.site.register(Style)
