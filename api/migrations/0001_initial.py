# Generated by Django 3.1 on 2022-02-09 13:28

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=datetime.datetime(2022, 2, 9, 13, 28, 9, 810486, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('benchPress', 'ベンチプレス'), ('dumbbellPress', 'ダンベルプレス'), ('dumbbellFly', 'ダンベルフライ'), ('chinning', 'チンニング')], max_length=30)),
                ('phase', models.CharField(choices=[('normal', '基本'), ('highWeight', '高重量'), ('lowWeight', '低重量')], default='normal', max_length=30)),
                ('weight', models.PositiveIntegerField()),
                ('rep', models.PositiveIntegerField()),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.day')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chest', models.PositiveIntegerField()),
                ('left_arm', models.PositiveIntegerField()),
                ('right_arm', models.PositiveIntegerField()),
                ('body_weight', models.PositiveIntegerField()),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.day')),
            ],
        ),
    ]