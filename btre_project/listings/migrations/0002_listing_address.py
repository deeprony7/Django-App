# Generated by Django 3.1.3 on 2020-12-06 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='address',
            field=models.CharField(default='Norwood', max_length=200),
            preserve_default=False,
        ),
    ]
