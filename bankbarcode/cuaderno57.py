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

    def _check_notice(self, value):
        name = 'notice'
        expected_length = 6
        description = 'notice lenth should be 6'
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


class Recibo507(Recibo):

    def __init__(self, entity, suffix, ref, notice, amount):
        self.entity = entity
        self.suffix = suffix
        self.ref = ref
        self.notice = notice
        self.amount = amount

    @property
    def entity(self):
        return self._entity.zfill(8)

    @entity.setter
    def entity(self, value):
        if self._check_entity(value):
            self._entity = value

    @property
    def suffix(self):
        return self._suffix.zfill(3)

    @suffix.setter
    def suffix(self, value):
        if self._check_suffix(value):
            self._suffix = value

    @property
    def ref(self):
        return self._ref.zfill(11)

    @ref.setter
    def ref(self, value):
        if self._check_ref(value):
            self._ref = value

    @property
    def notice(self):
        return self._notice.zfill(6)

    @notice.setter
    def notice(self, value):
        if self._check_notice(value):
            self._notice = value

    @property
    def amount(self):
        return self._amount.zfill(10)

    @amount.setter
    def amount(self, value):
        unicode_value = unicode(value)
        if self._check_amount(unicode_value):
            self._amount = unicode_value

    def amount100(self):
        return int(Decimal(self.amount) * 100)

    def checksum(self):
        sum = \
            int(self.entity) \
            + int(self.suffix) \
            + int(self.ref) \
            + int(self.notice) \
            + self.amount100()
        decimals = int(Decimal(sum) / 97 % 1 * 100)
        return unicode(100 - decimals).zfill(2)

    def code(self):
        id_application = u'90'
        format_type = u'507'
        parity = u'0'

        amount100 = unicode(self.amount100()).zfill(10)

        code = (
            '{id_application}'
            '{format_type}'
            '{s.entity}'
            '{s.suffix}'
            '{s.ref}'
            '{checksum}'
            '{s.notice}'
            '{amount100}'
            '{parity}'
        ).format(
            id_application=id_application,
            format_type=format_type,
            s=self,
            checksum=self.checksum(),
            amount100=amount100,
            parity=parity
        )

        return code
