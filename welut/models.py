# -*- coding: utf-8 -*-

import os
import ast

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .settings import WELUT_EXTENSIONS
from .converter import FileConverter


def conv_validators(value):
    ext = '%s' % os.path.splitext(value.name)[-1]
    if ext.lower() not in WELUT_EXTENSIONS:
        message = _('Invalid format, please choose: %(ext)s') % {'ext': WELUT_EXTENSIONS}
        raise ValidationError(message)


class EbookConverter(models.Model):
    path = models.FileField(_('Ebook file'), upload_to='ebooks/%Y/%m/%d',
                            validators=[conv_validators])
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return _('file: %(file)s') % {'file': self.id}

    def get_files(self):
        """ return path + filename for all files """
        if self.path is not None:
            try:
                imgs_path_name = os.path.splitext(self.path.name)[0]
                imgs_path_full = os.path.splitext(self.path.path)[0]
                listdir = [path for path in os.listdir(imgs_path_full)]
                return list(os.path.join(imgs_path_name, fname) for fname in listdir)
            except Exception:
                return list()
        return list()
    get_files.allow_tags = True
    get_files.short_description = _('List of files')

    def save(self, *args, **kwargs):
        super(EbookConverter, self).save(*args, **kwargs)
        fc = FileConverter()
        if not fc.convert(self.path):
            raise Exception(_('Cannot convert the file!'))
        return True

    class Meta:
        verbose_name = _('Ebook Converter')
        verbose_name_plural = _('Ebooks Converter')
        ordering = ['-created']
