# Generated by Django 3.1.5 on 2021-02-03 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0004_auto_20210203_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='style',
            name='bgcolor',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='style',
            name='txtcolor',
            field=models.CharField(max_length=7),
        ),
    ]