# Generated by Django 3.0.2 on 2020-02-03 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0022_auto_20200202_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviebook',
            name='Time',
        ),
        migrations.AlterField(
            model_name='moviebook',
            name='Booked_date',
            field=models.DateField(default='2020/02/02'),
        ),
        migrations.AlterField(
            model_name='moviebook',
            name='Expiry_date',
            field=models.DateField(default='2020/02/02'),
        ),
    ]