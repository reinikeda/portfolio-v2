from django.contrib import admin
from . import models


class TextInformationAdmin(admin.ModelAdmin):
    list_display = ('header', 'text')


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('school', 'course', 'duration', 'date', 'image')


class ProjectInformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date', 'link')


class ScreenshotAdmin(admin.ModelAdmin):
    list_display = ('project', 'image')

admin.site.register(models.TextInformation, TextInformationAdmin)
admin.site.register(models.Certificate, CertificateAdmin)
admin.site.register(models.ProjectInformation, ProjectInformationAdmin)
admin.site.register(models.Screenshot, ScreenshotAdmin)