# Generated by Django 3.0.2 on 2020-01-31 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0010_auto_20200131_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_info',
            name='user',
        ),
    ]
