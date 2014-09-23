#!/bin/python3"

import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-swc-blog',
    packages=['swc_blog'],
    package_dir={'swc_blog': 'src/swc_blog'},
    package_data={'swc_blog': ['templates/*',
                           'static/swc_blog/css/bootstrap.min.css',
                           'static/swc_blog/css/theme.css',
                           'static/swc_blog/js/bootstrap.min.js',
                           'static/swc_blog/css/pygments/colorful.css']},
    version='0.1',
    license='MIT License',
    description='A simple Django weblog app.',
    long_description='',
    #url='http://www.example.com/',
    author='Stefan Wikner',
    author_email='stefan.wikner@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        #'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)