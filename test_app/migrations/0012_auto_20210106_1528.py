# Generated by Django 3.1.4 on 2021-01-06 15:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0011_auto_20210106_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 6, 15, 28, 22, 17535, tzinfo=utc)),
        ),
    ]