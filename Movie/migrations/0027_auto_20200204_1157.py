# Generated by Django 3.0.2 on 2020-02-04 06:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0026_auto_20200203_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviebook',
            name='Booked_date',
            field=models.DateField(default=datetime.datetime(2020, 2, 4, 11, 57, 28, 48413)),
        ),
        migrations.AlterField(
            model_name='moviebook',
            name='Expiry_date',
            field=models.DateField(default=datetime.datetime(2020, 2, 4, 11, 57, 28, 48413)),
        ),
    ]
