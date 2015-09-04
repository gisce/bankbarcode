from bankbarcode import BankBarcode
from decimal import Decimal


class Recibo(BankBarcode):

    def _check_entity(self, value):
        name = 'entity'
        expected_length = 8
        description = 'entity should be a NIF/CIF, without the letter'
        return self._check_length(name, value, expected_length, description)

    def _check_suffix(self, value):
        name = 'suffix'
        expected_length = 3
        description = 'suffix lenth should be 3'
        return self._check_length(name, value, expected_length, description)

    def _check_ref(self, value):
        name = 'ref'
        expected_length = 11
        description = 'ref lenth should be 11'
        return self._check_length(name, value, expected_length, description)

    def _check_id(self, value):
        name = 'id'
        expected_length = 6
        description = 'id lenth should be 6'
        return self._check_length(name, value, expected_length, description)

    def _check_amount(self, amount):
        name = 'amount'
        decimal = Decimal(amount)
        if decimal.as_tuple().exponent < -2:
            raise ValueError('{} have more than 2 decimals'.format(name))
        if decimal > 99999999.99:
            raise ValueError('{} is too big'.format(name))
        value = unicode(int(decimal * 100)).zfill(10)
        expected_length = 10
        description = 'amount lenth should be 10'
        return self._check_length(name, value, expected_length, description)