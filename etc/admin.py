from django.contrib import admin
from .models import DayEtc, Goal, Memo


class DayEtcAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Day', {'fields': ['day_etc']})
    ]


class GoalAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Goal', {'fields': ['day_etc', 'length', 'deadline']}),
        ('About', {'fields': ['content']})
    ]
    list_display = ('day_etc', 'length', 'deadline')
    list_filter = ('day_etc', 'length', 'deadline')
    search_fields = ('day_etc', 'length', 'deadline')


class MemoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('', {'fields': ['day_etc', 'memo']})
    ]


admin.site.register(DayEtc, DayEtcAdmin)

admin.site.register(Goal, GoalAdmin)

admin.site.register(Memo, MemoAdmin)
