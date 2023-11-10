from django.contrib import admin
from . import models


class TextInformationAdmin(admin.ModelAdmin):
    list_display = ('header', 'text')


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('school', 'course', 'duration', 'date', 'image')

admin.site.register(models.TextInformation, TextInformationAdmin)
admin.site.register(models.Certificate, CertificateAdmin)