# BankBarcode
Python library to generate barcodes for financial documents

Currently only the following codes are implemented:

* cuaderno57, Cobros por ventanilla y autoservicio, serie normas y procedimientos bancarios, No57, Enero 2001
  * Recibo507, Recibos y otros (Cobros por Ventanilla y Autoservicio, V2001)

Feel free to implement more.

```
from bankbarcode.cuaderno57 import Recibo507
entity = '01234567'
suffix = '023'
ref = '12345678901'
id = '123456'
amount = '6543.21'

# get checksum value
checksum = Recibo507(entity, suffix, ref, id, amount).checksum()

# save barcocde as /tmp/mybarcode.svg
path = '/tmp/mybarcode'
Recibo507(entity, suffix, ref, id, amount).save(path)
```
