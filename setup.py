
from setuptools import setup

setup(
<<<<<<< HEAD
    name='django-jquery-ui',
    version='1.11.0',
    url='http://jqueryui.com/',
    description='Django package for jquery-ui: jQuery UI is a curated set of user interface interactions, effects, widgets, and themes built on top',
    author='Paul Bakaus',
    maintainer='AleXeY989',
    maintainer_email='alex1chupahin@ya.ru',
    license='MIT License',
    keywords=['django', 'jquery', 'jquery-ui'],
=======
    name='django-lightbox',
    version='2.7.1',
    url='https://github.com/AleXeY989/django-lightbox.git',
    description='Django package for jquery-lightbox: A lightweight customizable lightbox plugin for jQuery',
    author='Lokesh Dhakar',
    maintainer='AleXeY989',
    maintainer_email='alex1chupahin@ya.ru',
    license='MIT License',
    keywords=['django', 'jquery', 'lightbox'],
>>>>>>> a79d3a67c1933b53ee0dce3f61d6722341c850f5
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
<<<<<<< HEAD
    packages=['django_jquery_ui'],
    package_data={'django_jquery_ui': ['static/js/django_jquery_ui/*.js']}
=======
    packages=['django-lightbox'],
    package_data={'django_lightbox': ['static/js/*.js']}
>>>>>>> a79d3a67c1933b53ee0dce3f61d6722341c850f5
)
