
    **Welut** is a ebook converter


Requirements
=============

* **ebook-convert:** ``$ sudo apt install calibre`` - *convert epub & mobi to pdf.*
* **pdftocairo:** ``$ sudo apt install -y poppler-utils`` - *convert pdf to images*


Installation
------------------------------

Welut is available directly from `PyPI`_:

1. Installing the package.

::

    $ pip install welut


2. Don't forget to add ``'welut'`` to your ``'INSTALLED_APPS'``.

::

    # settings.py
    INSTALLED_APPS = [
        ....
        'welut',
    ]


3. Doing makemigrations & migrate

::

    ./manage.py makemigrations welut
    ./manage.py migrate welut



Configuration (``settings.py``)
---------------------------------------

::

    WELUT_EXTENSIONS = ['.pdf', '.epub', '.mobi']         # support file extensions
    WELUT_REMOVED_EXTENSIONS = ['.pdf', '.epub', '.mobi'] # file to remove after uploaded
    WELUT_IMAGES_EXTENSION = '.png'                       # format images extension


Usage
------------------------------

You can using ``ForeignKey`` or ``OneToOneField``.

::

    from django.db import models
    from welut.models import EbookConverter


    class EBook(models.Model):
        title = models.CharField(max_length=200)
        ebook_file = models.ForeignKey(EbookConverter, related_name='ebook_file')
        created = models.DateTimeField(auto_now_add=True)
        modified = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.title

        def get_files(self):
            """ return list images of ebook per-page """
            return self.ebook_file.get_files()



.. _PyPI: https://pypi.python.org/pypi/welut
