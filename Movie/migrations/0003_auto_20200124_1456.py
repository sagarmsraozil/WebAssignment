# Generated by Django 3.0.2 on 2020-01-24 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0002_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='movie_details',
            field=models.TextField(),
        ),
    ]
