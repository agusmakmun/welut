# -*- coding: utf-8 -*-

import os
import shutil
import subprocess

from .settings import (WELUT_REMOVED_EXTENSIONS, WELUT_IMAGES_EXTENSION)


class FileConverter(object):

    def __init__(self):
        pass

    def get_file_extension(self, value):
        """ return .pdf, .epub, .mobi """
        return '%s' % os.path.splitext(value)[-1]

    def get_final_filename(self, path, ext='.pdf'):
        """ rename filename from .epub, .mobi to specific file, default: .pdf """
        filename = path.split('/')[-1]
        file_extension = self.get_file_extension(filename)
        return filename.replace(file_extension, ext)

    def convert(self, _file):
        # eg: '/path/to/env-welut/welut/welut_demo/media/ebooks/2017/11/13/nama-file.epub'
        epub_file_full_path = _file.path

        # eg: ('/path/to/env-welut/welut/welut_demo/media/ebooks/2017/11/13/', 'nama-file.epub')
        splited_path = os.path.split(epub_file_full_path)
        current_path, origin_filename = splited_path[0], splited_path[-1]

        pdf_file = self.get_final_filename(epub_file_full_path, '.pdf')
        pdf_file_full_path = os.path.join(current_path, pdf_file)

        try:
            subprocess.call(['ebook-convert', epub_file_full_path, pdf_file_full_path])
            subprocess.call(['pdftocairo', '-png', pdf_file_full_path, current_path])

            # try to move all .png files from previous path to next path
            # ('/path/to/env-welut/welut/welut_demo/media/ebooks/2017/11', '13')
            prev_path_splited = os.path.split(current_path)
            prev_path, next_path = prev_path_splited[0], prev_path_splited[-1]

            # move all files to new destination path
            list_filenames = []
            for fname in os.listdir(prev_path):
                # 'nama-file'
                next_path_by_file = os.path.basename(os.path.splitext(epub_file_full_path)[0])

                # '/path/to/env-welut/welut/welut_demo/media/ebooks/2017/11/nama-file/13-01.png'
                next_path_by_file = '%s/%s/%s' % (current_path, next_path_by_file, fname)

                # to check whenever new path is not created yet
                # '/path/to/env-welut/welut/welut_demo/media/ebooks/2017/11/nama-file/'
                next_path_dirname = os.path.split(next_path_by_file)[0]
                if not os.path.exists(next_path_dirname):
                    os.makedirs(next_path_dirname)

                # start path before moving the files
                source = os.path.join(prev_path, fname)
                destination = next_path_by_file
                if os.path.isfile(source) and self.get_file_extension(source) == WELUT_IMAGES_EXTENSION:
                    shutil.move(source, destination)
                    list_filenames.append(fname)

            # removing all file uploaded with specific extensions
            # this condition is process as last condition
            for ext in WELUT_REMOVED_EXTENSIONS:
                if os.path.isfile(epub_file_full_path):
                    if ext == '.epub' or ext == '.mobi':
                        os.remove(epub_file_full_path)
                    elif ext == '.pdf':
                        os.remove(pdf_file_full_path)

            return sorted(list_filenames)

        except Exception as e:
            raise e
