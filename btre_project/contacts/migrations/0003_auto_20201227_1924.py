# Generated by Django 3.1.3 on 2020-12-27 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20201227_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='listing_id',
            field=models.IntegerField(blank=True),
        ),
    ]
