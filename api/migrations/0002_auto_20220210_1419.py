# Generated by Django 3.1 on 2022-02-10 05:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='day',
            field=models.DateField(default=datetime.datetime(2022, 2, 10, 5, 19, 7, 273359, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='training',
            name='type',
            field=models.CharField(choices=[('benchPress', 'ベンチプレス'), ('dumbbellPress', 'ダンベルプレス'), ('decline_benchPress', 'デクラインベンチプレス'), ('dumbbellFly', 'ダンベルフライ'), ('chinning', 'チンニング')], max_length=30),
        ),
    ]
