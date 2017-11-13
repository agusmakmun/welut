# -*- coding: utf-8 -*-

from django.conf import settings

WELUT_EXTENSIONS = getattr(settings, 'WELUT_EXTENSIONS', ['.pdf', '.epub', '.mobi'])
WELUT_REMOVED_EXTENSIONS = getattr(settings, 'WELUT_REMOVED_EXTENSIONS', ['.pdf', '.epub', '.mobi'])
WELUT_IMAGES_EXTENSION = getattr(settings, 'WELUT_IMAGE_EXTENSION', '.png')
