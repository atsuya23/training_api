from django.db import models
from django.contrib import admin
from django.utils import timezone
from dateutil.relativedelta import relativedelta


class Goal(models.Model):
    day = models.DateField(auto_now=True)
    content = models.TextField(max_length=100)
    length = models.PositiveIntegerField(null=True, blank=True)
    deadline = models.DateField(default=timezone.now())
    done = models.BooleanField(default=False)

    def __str__(self):
        if self.length:
            return f"{self.length} month goal : {self.content} ({self.day})"
        else:
            return f"By {self.deadline} goal : {self.content} ({self.day}"


class Memo(models.Model):
    day = models.DateField(auto_now=True)
    memo = models.TextField(max_length=100)

    def __str__(self):
        return self.memo


class Measurement(models.Model):
    day = models.DateField(default=timezone.now())
    chest = models.PositiveIntegerField()
    left_arm = models.PositiveIntegerField()
    right_arm = models.PositiveIntegerField()
    body_weight = models.PositiveIntegerField()

    def __str__(self):
        return f"measured at {self.day}"


