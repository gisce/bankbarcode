# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='bankbarcode',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/gisce/bankbarcode',
    license='GNU Affero General Public License v3',
    author='Simó Albert i Beltran',
    author_email='sim6@probeta.net',
    install_requires=[
        'pybarcode'
    ],
    description='barcodes for financial documents'
)
