# Generated by Django 3.1.4 on 2021-01-06 15:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0013_auto_20210106_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
