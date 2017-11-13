from setuptools import (setup, find_packages)
from welut import (__VERSION__, __AUTHOR__, __AUTHOR_EMAIL__)


def get_requirements():
    return open('requirements.txt').read().splitlines()


setup(
    name='welut',
    version=__VERSION__,
    packages=find_packages(exclude=["*demo"]),
    include_package_data=True,
    zip_safe=False,
    description='Welut is a ebook converter',
    url='https://github.com/agusmakmun/welut',
    download_url='https://github.com/agusmakmun/welut/tarball/v%s' % __VERSION__,
    keywords=['welut'],
    long_description=open('README.rst').read(),
    license='MIT',
    author=__AUTHOR__,
    author_email=__AUTHOR_EMAIL__,
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Environment :: Web Environment',
    ],
    install_requires=get_requirements(),
)
