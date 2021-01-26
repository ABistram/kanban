from django.db import models

# Create your models here.


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


class Table(models.Model):
    title = models.CharField(max_length=100)