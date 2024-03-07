# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='bankbarcode',
    version='0.3.0',
    packages=find_packages(),
    url='https://github.com/gisce/bankbarcode',
    license='GNU Affero General Public License v3',
    author='GISCE-TI, S.L.',
    author_email='devel@gisce.net',
    # We need python-barcode v0.8, to have Code128 (EAN128), not released yet
    # https://bitbucket.org/whitie/python-barcode/issues/16/pypi-08-release-request
    install_requires=[
        'python-barcode==0.8.0',
        'six'
    ],
    description='barcodes for financial documents'
)
