# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='bankbarcode',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/gisce/bankbarcode',
    license='GNU Affero General Public License v3',
    author='GISCE-TI, S.L.',
    author_email='devel@gisce.net',
    install_requires=[
        'pybarcode>=0.8b1'
    ],
    description='barcodes for financial documents'
)
