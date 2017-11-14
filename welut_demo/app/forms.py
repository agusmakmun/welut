# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from welut.models import EbookConverter
from app.models import EBook


class EbookConverterForm(forms.ModelForm):

    class Meta:
        model = EbookConverter
        fields = ['path', ]

    def __init__(self, *args, **kwargs):
        super(EbookConverterForm, self).__init__(*args, **kwargs)
        self.fields['path'].widget.attrs = {'class': 'form-control'}


class EBookForm(forms.ModelForm):

    class Meta:
        model = EBook
        fields = ['title', ]

    def __init__(self, *args, **kwargs):
        super(EBookForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {'class': 'form-control'}
