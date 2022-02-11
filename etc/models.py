from django.db import models
from django.contrib import admin
from django.utils import timezone
from dateutil.relativedelta import relativedelta


class DayEtc(models.Model):
    day_etc = models.DateField(default=timezone.now())

    def __str__(self):
        return str(self.day_etc)


class Goal(models.Model):
    day_etc = models.ForeignKey(DayEtc, on_delete=models.CASCADE)
    content = models.TextField(max_length=100)
    length = models.PositiveIntegerField(null=True, blank=True)
    deadline = models.DateField(default=timezone.now())
    done = models.BooleanField(default=False)

    def __str__(self):
        if self.length:
            return f"{self.length} month goal : {self.content} ({self.day_etc})"
        else:
            return f"By {self.deadline} goal : {self.content} ({self.day_etc}"


class Memo(models.Model):
    day_etc = models.ForeignKey(DayEtc, on_delete=models.CASCADE)
    memo = models.TextField(max_length=100)

    def __str__(self):
        return self.memo


