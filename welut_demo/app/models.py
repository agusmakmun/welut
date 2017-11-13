# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from welut.models import EbookConverter


class EBook(models.Model):
    title = models.CharField(max_length=200)
    ebook_file = models.ForeignKey(EbookConverter, related_name='ebook_file')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
