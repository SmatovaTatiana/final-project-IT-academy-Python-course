from django.contrib import admin
from . import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'subscribed_for_mailings', 'subscription_email', )
    ordering = ('user',)


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


@admin.register(models.Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('date', 'sender_email', 'name', 'subject')
    list_filter = ('date', )


@admin.register(models.UploadDocument)
class UploadDocumentAdmin(admin.ModelAdmin):
    list_display = ('date', 'file_name', 'document')
    list_filter = ('date', )


@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('date', 'project_name', 'description')
    list_filter = ('date', )
    prepopulated_fields = {'slug': ('project_name', )}


@admin.register(models.TopNews)
class TopNewsAdmin(admin.ModelAdmin):
    list_display = ('created', 'title', 'link')
    prepopulated_fields = {'slug': ('title',)}
