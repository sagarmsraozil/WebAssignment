# Generated by Django 3.0.2 on 2020-02-04 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0044_auto_20200204_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviebook',
            name='Booked_date',
        ),
        migrations.RemoveField(
            model_name='moviebook',
            name='Expiry_date',
        ),
    ]
