from django.contrib import admin
from .models import Item, Field, Sheet, Style

# Register your models here.


admin.site.register(Item)
admin.site.register(Field)
admin.site.register(Sheet)
admin.site.register(Style)
