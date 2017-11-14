# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import (render, redirect)

from app.models import EBook
from app.forms import (EbookConverterForm, EBookForm)


def ebook_viewer(request):
    ebook = EBook.objects.first()

    if request.method == 'POST':
        welut_form = EbookConverterForm(request.POST, request.FILES)
        ebook_form = EBookForm(request.POST)

        if welut_form.is_valid() and ebook_form.is_valid():
            ebook_file = welut_form.save()
            ebook_info = ebook_form.save(commit=False)
            ebook_info.ebook_file = ebook_file
            ebook_info.save()
            return redirect('.')
    else:
        welut_form = EbookConverterForm()
        ebook_form = EBookForm()

    context = {'ebook': ebook, 'welut_form': welut_form, 'ebook_form': ebook_form}
    return render(request, 'ebook_viewer.html', context)
