from django.contrib import admin
from .models import Goal, Memo


class GoalAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Goal', {'fields': ['length', 'deadline']}),
        ('About', {'fields': ['content']})
    ]
    list_display = ('day', 'length', 'deadline')
    list_filter = ('day', 'length', 'deadline')
    search_fields = ('day', 'length', 'deadline')


class MemoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('', {'fields': ['memo']})
    ]


admin.site.register(Goal, GoalAdmin)

admin.site.register(Memo, MemoAdmin)
