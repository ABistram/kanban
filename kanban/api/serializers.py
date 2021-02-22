from rest_framework import serializers
from django.db.models import Q

from .models import Item, Field, Sheet, Style, item_type_choices, field_type_choices, privacy_type_choices


class StyleSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    height = serializers.CharField(style={'base_template': 'textarea.html'})
    width = serializers.CharField(style={'base_template': 'textarea.html'})
    bgcolor = serializers.CharField(max_length=9)
    txtcolor = serializers.CharField(max_length=7)
    fontsize = serializers.CharField(style={'base_template': 'textarea.html'})
    border = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        return Style.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.height = validated_data.get('height', instance.height)
        instance.width = validated_data.get('width', instance.width)
        instance.bgcolor = validated_data.get('bgcolor', instance.bgcolor)
        instance.txtcolor = validated_data.get('txtcolor', instance.txtcolor)
        instance.fontsize = validated_data.get('fontsize', instance.fontsize)
        instance.border = validated_data.get('border', instance.border)
        instance.save()
        return instance

    def delete(self, instance):
        return Style.objects.filter(pk=instance.id).delete()

    class Meta:
        model = Style
        fields = ('id', 'name', 'height', 'width', 'bgcolor', 'txtcolor', 'fontsize', 'border')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    item_type = serializers.ChoiceField(choices=item_type_choices, default='EP')
    content = serializers.CharField()
    field = serializers.SlugRelatedField(
        many=False,
        queryset=Field.objects.all().filter(Q(field_type="MX") | Q(field_type="ST")),
        read_only=False,
        slug_field='name'
    )
    style = serializers.SlugRelatedField(
        many=False,
        queryset=Style.objects.all(),
        read_only=False,
        slug_field='name'
    )

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.item_type = validated_data.get('item_type', instance.item_type)
        instance.content = validated_data.get('content', instance.content)
        instance.field = validated_data.get('field', instance.field)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

    def delete(self, instance):
        return Item.objects.filter(pk=instance.id).delete()

    class Meta:
        model = Item
        fields = ('id', 'item_type', 'content', 'field', 'style')


class SheetSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    privacy_type = serializers.ChoiceField(choices=privacy_type_choices)

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.privacy_type = validated_data.get('privacy_type', instance.privacy_type)
        instance.save()
        return instance

    def delete(self, instance):
        return Item.objects.filter(pk=instance.id).delete()

    class Meta:
        model = Sheet
        fields = ('id', 'title', 'privacy_type')


class FieldSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=32)
    field_type = serializers.ChoiceField(choices=field_type_choices)
    label = serializers.CharField(max_length=256)
    positionX = serializers.IntegerField()
    positionY = serializers.IntegerField()
    rowspan = serializers.IntegerField(default=1)
    colspan = serializers.IntegerField(default=1)
    sheet = serializers.SlugRelatedField(
        many=False,
        queryset=Sheet.objects.all(),
        read_only=False,
        slug_field='title'
    )
    style = serializers.SlugRelatedField(
        many=False,
        queryset=Style.objects.all(),
        read_only=False,
        slug_field='name'
    )
    parent = serializers.SlugRelatedField(
        many=False,
        queryset=Field.objects.all(),
        read_only=False,
        slug_field='name',
        required=False,
        allow_null=True
    )

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.field_type = validated_data.get('field_type', instance.field_type)
        instance.label = validated_data.get('label', instance.label)
        instance.positionX = validated_data.get('positionX', instance.positionX)
        instance.positionY = validated_data.get('positionY', instance.positionY)
        instance.rowspan = validated_data.get('rowspan', instance.rowspan)
        instance.colspan = validated_data.get('colspan', instance.colspan)
        instance.sheet = validated_data.get('sheet', instance.sheet)
        instance.style = validated_data.get('sheet', instance.style)
        instance.parent = validated_data.get('sheet', instance.parent)
        instance.save()
        return instance

    def delete(self, instance):
        return Item.objects.filter(pk=instance.id).delete()

    class Meta:
        model = Field
        fields = ('id', 'name', 'field_type', 'label', 'positionX', 'positionY',
                  'rowspan', 'colspan', 'sheet', 'parent', 'style')
