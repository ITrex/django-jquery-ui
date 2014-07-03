
from setuptools import setup

setup(
    name='django-jquery-ui',
    version='1.5.10',
    url='https://github.com/AleXeY989/django-jquery-ui',
    description='Django package for jquery-colorbox: A lightweight customizable lightbox plugin for jQuery',
    author='Jack Moore',
    maintainer='AleXeY989',
    maintainer_email='alex1chupahin@ya.ru',
    license='MIT License',
    keywords=['django', 'jquery'],
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
    packages=['django-jquery-ui'],
    package_data={'django_jquery_ui': ['static/js/*.js']}
)
