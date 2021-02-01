from django.db import models

# Create your models here.
"""
Sheet
-id(PK)
-title
-sizeX
-sizeY
-type(private/public)

Field
-id(PK)
-name
-type
-label
-positionX
-positionY
-rowspan(def 1)
-colspan(def 1)
-table(FK to Table)

Item
-id(PK)
-type
-content
-field(FK to Field)
"""


class Item(models.Model):
    EPICS = "EP"
    STORIES = "ST"
    OTHER = "OT"
    item_type_choices = [
        (EPICS, "Epics"),
        (STORIES, "Stories"),
        (OTHER, "Other")
    ]
    item_type = models.CharField(
        max_length=32,
        choices=item_type_choices,
        default=EPICS
    )
    content = models.TextField(default="")
    field = models.ForeignKey('Field', on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Field(models.Model):
    name = models.CharField(max_length=32)
    MIXED = "MX"
    LABEL = "LB"
    STICKER = "ST"
    field_type_choices = [
        (LABEL, "Label"),
        (STICKER, "Sticker"),
        (MIXED, "Mixed")
    ]
    field_type = models.CharField(
        max_length=32,
        choices=field_type_choices,
        default=LABEL
    )
    label = models.CharField(max_length=256)
    positionX = models.IntegerField()
    positionY = models.IntegerField()
    rowspan = models.IntegerField(default=1)
    colspan = models.IntegerField(default=1)
    sheet = models.ForeignKey('Sheet', on_delete=models.CASCADE)
    parent = models.ForeignKey('Field', models.SET_NULL, null=True)

    def __str__(self):
        if self.field_type == "LB" or self.field_type == "MX":
            return self.label
        return self.name


class Sheet(models.Model):
    title = models.CharField(max_length=100)
    sizeX = models.IntegerField()
    sizeY = models.IntegerField()
    PRIVATE = "PV"
    PUBLIC = "PB"
    privacy_type_choices = [
        (PRIVATE, "Private"),
        (PUBLIC, "Public")
    ]
    privacy_type = models.CharField(
        max_length=32,
        choices=privacy_type_choices,
        default=PRIVATE
    )

    def __str__(self):
        return self.title
