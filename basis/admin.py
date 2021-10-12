from django.contrib import admin
from . import models
# Register your models here.
# admin.site.register(models.Education)


@admin.register(models.Education)
class EducationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('course_name', )}
    list_display = ('course_name', 'graduated', 'school_name')
    ordering = ('graduated', 'school_name')
    list_filter = ('graduated', 'school_name')


@admin.register(models.Experience)
class ExperienceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('company_name', 'position', )}
    list_display = ('company_name', 'position', 'start_date', 'end_date')
    ordering = ('company_name', 'position')
    list_filter = ('position', )
