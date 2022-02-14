from django.utils import timezone
from django.contrib import admin
from django.db import models


TRAINING_TYPE = [
    ('benchPress', 'ベンチプレス'),
    ('dumbbellPress', 'ダンベルプレス'),
    ('decline_benchPress', 'デクラインベンチプレス'),
    ('dumbbellFly', 'ダンベルフライ'),
    ('chinning', 'チンニング'),

]
TRAINING_PHASE = [
    ('normal', '基本'),
    ('highWeight', '高重量'),
    ('lowWeight', '低重量'),
]


class Training(models.Model):
    day = models.DateField(default=timezone.now())
    type = models.CharField(max_length=30, choices=TRAINING_TYPE)
    phase = models.CharField(max_length=30, choices=TRAINING_PHASE, default='normal')
    weight = models.PositiveIntegerField()
    rep = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.type} : {self.weight} * {self.rep}"


class Measurement(models.Model):
    day = models.DateField(default=timezone.now())
    chest = models.PositiveIntegerField()
    left_arm = models.PositiveIntegerField()
    right_arm = models.PositiveIntegerField()
    body_weight = models.PositiveIntegerField()

    def __str__(self):
        return f"measured at {self.day}"






