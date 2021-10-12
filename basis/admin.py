from django.contrib import admin
from . import models
# Register your models here.
#admin.site.register(models.Education)


@admin.register(models.Education)
class EducationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('course_name', )}
    list_display = ('course_name', 'graduated', 'school_name')
    ordering = ('graduated', 'school_name')
    list_filter = ('graduated', 'school_name')
