# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import EbookConverter


class EbookConverterAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'path', 'created', 'modified']
    readonly_fields = ['get_files']


admin.site.register(EbookConverter, EbookConverterAdmin)
