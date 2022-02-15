from django.contrib import admin
from .models import Goal, Memo, Measurement


class GoalAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Goal', {'fields': ['length', 'deadline', 'done']}),
        ('About', {'fields': ['content']})
    ]
    list_display = ('day', 'length', 'deadline', 'done')
    list_filter = ('day', 'length', 'deadline', 'done')
    search_fields = ('day', 'length', 'deadline', 'done')


class MemoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('', {'fields': ['memo']})
    ]


class MeasurementAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Measurement', {'fields': ['chest', 'left_arm', 'right_arm', 'body_weight']}),
        ('Day', {'fields': ['day']})
    ]
    list_display = ('chest', 'left_arm', 'right_arm', 'body_weight', 'day')
    list_filter = ('chest', 'left_arm', 'right_arm', 'body_weight', 'day')
    search_fields = ('chest', 'left_arm', 'right_arm', 'body_weight', 'day')


admin.site.register(Goal, GoalAdmin)

admin.site.register(Memo, MemoAdmin)

admin.site.register(Measurement, MeasurementAdmin)
