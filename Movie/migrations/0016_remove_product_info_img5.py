# Generated by Django 3.0.2 on 2020-02-02 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0015_product_info_img5'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_info',
            name='img5',
        ),
    ]
