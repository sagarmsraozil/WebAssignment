# Generated by Django 3.0.2 on 2020-01-31 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0012_product_info_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_info',
            name='user',
        ),
    ]
