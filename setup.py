#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup
setup(
    name='rbox_htmldiff',
    version='0.0.1',
    py_modules=['rbox_htmldiff', ],
    install_requires=[
        # -*- Extra requirements: -*-
    ],
)
