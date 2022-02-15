from django.contrib import admin
from .models import Training


# 管理サイト名
admin.site.site_header = '筋トレ記録　登録'

# サイト管理名
admin.site.index_title = '記録'


class TrainingAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Training', {'fields': ['type', 'phase', 'weight', 'rep']}),
        ('Day', {'fields': ['day']})
    ]
    list_display = ('day', 'type', 'phase', 'weight', 'rep')
    list_filter = ('day', 'type', 'phase')
    search_fields = ('day', 'type', 'phase', 'weight', 'rep')


admin.site.register(Training, TrainingAdmin)


