===========
BankBarcode
===========

.. image:: https://travis-ci.org/gisce/bankbarcode.svg?branch=master
    :target: https://travis-ci.org/gisce/bankbarcode

Python library to generate barcodes for financial documents

Currently only the following codes are implemented:

* cuaderno57, Cobros por ventanilla y autoservicio, serie normas y procedimientos bancarios, No57, Enero 2001

  * Recibo507, Recibos y otros (Cobros por Ventanilla y Autoservicio, V2001)

Feel free to implement more.

.. code-block:: python

    from bankbarcode.cuaderno57 import Recibo507
    entity = '01234567'
    suffix = '023'
    ref = '12345678901'
    notice = '123456'
    amount = '6543.21'

    recibo507 = Recibo507(entity, suffix, ref, notice, amount)

    # get checksum value
    checksum = recibo507.checksum()

    # save barcocde as /tmp/mybarcode.svg
    provided_filename = '/tmp/mybarcode.svg'
    generated_filename = recibo507.save(provided_filename)

    # get a string with the barcode in SVG fromat
    svg = recibo507.svg()

Read the documentation at http://bankbarcode.readthedocs.org
