# Generated by Django 3.1 on 2022-02-11 10:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('etc', '0004_auto_20220211_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayetc',
            name='day_etc',
            field=models.DateField(default=datetime.datetime(2022, 2, 11, 10, 6, 50, 949250, tzinfo=utc)),
        ),
    ]
