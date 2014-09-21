import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='blog',
    packages=['blog'],
    package_dir={'blog': 'src/blog'},
    package_data={'blog': ['templates/*',
                           'static/blog/css/bootstrap.min.css',
                           'static/blog/css/theme.css',
                           'static/blog/js/bootstrap.min.js',
                           'static/blog/css/pygments/colorful.css']},
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