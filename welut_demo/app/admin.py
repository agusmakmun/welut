# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from app.models import EBook


class EbookAdmin(admin.ModelAdmin):
    raw_id_fields = ['ebook_file']


admin.site.register(EBook, EbookAdmin)
