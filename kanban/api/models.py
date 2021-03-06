from django.db import models

# Create your models here.
EPICS = "EP"
STORIES = "ST"
OTHER = "OT"
item_type_choices = [
    (EPICS, "Epics"),
    (STORIES, "Stories"),
    (OTHER, "Other")
]

MIXED = "MX"
LABEL = "LB"
STICKER = "ST"
field_type_choices = [
    (LABEL, "Label"),
    (STICKER, "Sticker"),
    (MIXED, "Mixed")
]
PRIVATE = "PV"
PUBLIC = "PB"
privacy_type_choices = [
    (PRIVATE, "Private"),
    (PUBLIC, "Public")
]


class Item(models.Model):
    item_type = models.CharField(
        max_length=32,
        choices=item_type_choices,
        default=EPICS
    )
    content = models.TextField(default="")
    field = models.ForeignKey('Field', on_delete=models.CASCADE)
    style = models.ForeignKey('Style', on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Field(models.Model):
    name = models.CharField(max_length=32)
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
    style = models.ForeignKey('Style', on_delete=models.CASCADE)

    def __str__(self):
        if self.field_type == "LB" or self.field_type == "MX":
            return self.label
        return self.name

    class Meta:
        ordering = ['positionY', 'positionX']


class Sheet(models.Model):
    title = models.CharField(max_length=100)
    privacy_type = models.CharField(
        max_length=32,
        choices=privacy_type_choices,
        default=PRIVATE
    )

    def __str__(self):
        return self.title


class Style(models.Model):
    # Stored as [number][unit]
    name = models.CharField(max_length=30)
    height = models.TextField()
    width = models.TextField()
    bgcolor = models.CharField(max_length=9)  # RGBA
    txtcolor = models.CharField(max_length=7)
    fontsize = models.TextField()
    border = models.TextField()

    def __str__(self):
        return self.name
