# Generated by Django 3.0.2 on 2020-02-02 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0019_auto_20200202_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviebook',
            name='Booked_date',
            field=models.DateField(default='XXXX-XX-XX'),
        ),
        migrations.AlterField(
            model_name='moviebook',
            name='Expiry_date',
            field=models.DateField(default='XXXX-XX-XX'),
        ),
    ]