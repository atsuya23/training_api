from django.contrib import admin
from .models import Day, Training, Measurement


# 管理サイト名
admin.site.site_header = '筋トレ記録　登録'

# サイト管理名
admin.site.index_title = '記録'


class TrainingInline(admin.TabularInline):
    model = Training
    fk_name = "day"
    extra = 4


class DayAdmin(admin.ModelAdmin):
    fieldsets = [
        ('DAY', {'fields': ['day']}),
    ]
    inlines = [TrainingInline]
    list_display = ('day',)
    list_filter = ('day',)
    search_fields = ('day',)


class TrainingAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Training', {'fields': ['day', 'type', 'phase', 'weight', 'rep']})
    ]
    list_display = ('day', 'type', 'phase', 'weight', 'rep')
    list_filter = ('day', 'type', 'phase')
    search_fields = ('day', 'type', 'phase', 'weight', 'rep')


class MeasurementAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Measurement', {'fields': ['chest', 'left_arm', 'right_arm', 'body_weight']})
    ]
    list_display = ('chest', 'left_arm', 'right_arm', 'body_weight')
    list_filter = ('chest', 'left_arm', 'right_arm', 'body_weight')
    search_fields = ('chest', 'left_arm', 'right_arm', 'body_weight')


admin.site.register(Day, DayAdmin)

admin.site.register(Training, TrainingAdmin)

admin.site.register(Measurement, MeasurementAdmin)
