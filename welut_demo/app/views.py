# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from app.models import EBook


def ebook_viewer(request):
    ebook = EBook.objects.first()
    return render(request, 'ebook_viewer.html', {'ebook': ebook})
