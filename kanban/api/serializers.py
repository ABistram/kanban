from rest_framework import serializers

from .models import Item, Field, Sheet, Style


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('item_type', 'content', 'field', 'style')