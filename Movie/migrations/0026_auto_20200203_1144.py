# Generated by Django 3.0.2 on 2020-02-03 05:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0025_auto_20200203_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviebook',
            name='Booked_date',
            field=models.DateField(default=datetime.datetime(2020, 2, 3, 11, 44, 50, 900538)),
        ),
        migrations.AlterField(
            model_name='moviebook',
            name='Expiry_date',
            field=models.DateField(default=datetime.datetime(2020, 2, 3, 11, 44, 50, 900538)),
        ),
    ]
