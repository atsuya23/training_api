# Generated by Django 3.1 on 2022-02-11 10:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20220211_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='day',
            field=models.DateField(default=datetime.datetime(2022, 2, 11, 10, 4, 40, 79260, tzinfo=utc)),
        ),
    ]
