# Generated by Django 3.0.2 on 2020-02-04 06:15

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0027_auto_20200204_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviebook',
            name='Booked_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='moviebook',
            name='Expiry_date',
            field=models.DateField(default=datetime.datetime(2020, 2, 4, 12, 0, 36, 515052)),
        ),
    ]
