# Generated by Django 3.0.2 on 2020-01-29 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0005_auto_20200129_1417'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]