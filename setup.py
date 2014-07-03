
from setuptools import setup

setup(
    name='django-jquery-ui',
    version='1.11.0',
    url='http://jqueryui.com/',
    description='Django package for jquery-ui: jQuery UI is a curated set of user interface interactions, effects, widgets, and themes built on top',
    author='Paul Bakaus',
    maintainer='AleXeY989',
    maintainer_email='alex1chupahin@ya.ru',
    license='MIT License',
    keywords=['django', 'jquery', 'jquery-ui'],
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['django_jquery_ui'],
    package_data={'django_jquery_ui': ['static/js/django_jquery_ui/*.js']}
)
