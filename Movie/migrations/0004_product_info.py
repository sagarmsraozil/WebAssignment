# Generated by Django 3.0.2 on 2020-01-28 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0003_auto_20200124_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('title_img', models.CharField(max_length=2086)),
                ('img1', models.CharField(max_length=2086)),
                ('img2', models.CharField(max_length=2086)),
                ('img3', models.CharField(max_length=2086)),
                ('img4', models.CharField(max_length=2086)),
                ('img5', models.CharField(max_length=2086)),
                ('img6', models.CharField(max_length=2086)),
            ],
        ),
    ]
