# coding=utf-8
from datetime import datetime

from bankbarcode import BankBarcode
from decimal import Decimal


class Recibo(BankBarcode):
    """
    Base class for receipts (recibos) of Cobros por ventanilla y autoservicio,
    serie normas y procedimientos bancarios, No57, Enero 2001
    """

    def _check_entity(self, value):
        """
        Check entity code (Número de la sociedad emisora)

        :param value: the entity code (Número de la sociedad emisora)
        :return: True if it have the expected length, otherwise False
        """
        name = 'entity'
        expected_length = 8
        description = 'entity should be a NIF/CIF, without the letter'
        return self._check_length(name, value, expected_length, description)

    def _check_suffix(self, value):
        """
        Check the suffix code (Sufijo)

        :param value: the suffix of the entity (Sufijo)
        :return: True if it have the expected length, otherwise False
        """
        name = 'suffix'
        expected_length = 3
        description = 'suffix lenth should be 3'
        return self._check_length(name, value, expected_length, description)

    def _check_ref(self, value):
        """
        Check the reference code (Número de referencia)

        :param value: the reference code (Número de referencia)
        :return: True if it have the expected length, otherwise False
        """
        name = 'ref'
        expected_length = 11
        description = 'ref lenth should be 11'
        return self._check_length(name, value, expected_length, description)

    def _check_notice(self, value):
        """
        Check the notice identification code (Identificación)

        :param value: the notice identification code (Identificación)
        :return: True if it have the expected length, otherwise False
        """
        name = 'notice'
        expected_length = 6
        description = 'notice lenth should be 6'
        return self._check_length(name, value, expected_length, description)

    def _check_amount(self, amount):
        """
        Check the amount (Importe)

        :param amount: the amount (Importe)
        :return: True if it have the expected length, otherwise False
        """
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

    def _check_due_date(self, due_date, suffix):
        """
        Check due date (Fecha limite) and suffix

        :param due_date: Due Date (Fecha limite)
        :return: True if due date is a Datetime or string with format '%Y-%m-%d'
                 and suffix bigger than 499, otherwise False
        """
        name = 'due_date'
        if due_date is None:
            return True
        if isinstance(due_date, basestring):
            try:
                date = datetime.strptime(due_date, '%Y-%m-%d')
            except:
                raise ValueError(
                    "{} must be string with format '%Y-%m-%d'".format(name))
        else:
            if not isinstance(due_date, datetime):
                raise ValueError('{} must be a Datetime'.format(name))

        if self._check_suffix(suffix) and int(suffix) <= 499:
            raise ValueError('suffix with due date must be bigger than 499')
        return True



class Recibo507(Recibo):
    """
    Receipt (Recibo) 507 for Recibos y otros (Cobros por Ventanilla y \
        Autoservicio, V2001)
    """

    def __init__(self, entity=None, suffix=None, ref=None, notice=None,
                 amount=None, due_date=None):
        """
        Create and object of Recibo507 with checked values.

        :param entity: the entity code (Número de la sociedad emisora)
        :param suffix: the suffix of the entity (Sufijo)
        :param ref: the reference code (Número de referencia)
        :param notice: the notice identification code (Identificación)
        :param amount: the amount (Importe)
        :param due_date: Due date (Fecha limite)
        :return: an object of Recibo507
        """
        self.entity = entity
        self.suffix = suffix
        self.ref = ref
        self.notice = notice
        self.amount = amount
        self.due_date = due_date

    @property
    def entity(self):
        """
        The entity code (Número de la sociedad emisora)

        :return: the entity code (Número de la sociedad emisora) as an string \
            with 8 characters
        """
        return self._entity.zfill(8)

    @entity.setter
    def entity(self, value):
        """
        Check the entity code (Número de la sociedad emisora) and store it

        :param value: the entity code (Número de la sociedad emisora)
        """
        if self._check_entity(value):
            self._entity = value

    @property
    def suffix(self):
        """
        The suffix (Sufijo)

        :return: the suffix (Sufijo) as an string with 3 characters
        """
        return self._suffix.zfill(3)

    @suffix.setter
    def suffix(self, value):
        """
        Check the suffix (Sufijo) and store it

        :param value: the suffix (Sufijo)
        """
        if self._check_suffix(value):
            self._suffix = value

    @property
    def ref(self):
        """
        The reference code (Número de referencia)

        :return: the reference code (Número de referencia) as an string with \
            11 characters
        """
        return self._ref.zfill(11)

    @ref.setter
    def ref(self, value):
        """
        Check the reference code (Número de referencia) and store it

        :param value: the reference code (Número de referencia)
        """
        if self._check_ref(value):
            self._ref = value

    @property
    def notice(self):
        """
        The notice identification code (Identificación)

        :return: the notice identification code (Identificación) as an string \
            with 6 characters
        """
        return self._notice.zfill(6)

    @notice.setter
    def notice(self, value):
        """
        Check the notice identification code (Identificación) and store it

        :param value: the notice identification code (Identificación)
        """
        if self._check_notice(value):
            self._notice = value

    @property
    def amount(self):
        """
        The amount (Importe)

        :return: the amount (Importe) as an string with 10 characters
        """
        return self._amount.zfill(10)

    @amount.setter
    def amount(self, value):
        """
        Check the amount (Importe) and store it

        :param value: the amount (Importe)
        """
        unicode_value = unicode(value)
        if self._check_amount(unicode_value):
            self._amount = unicode_value

    @property
    def due_date(self):
        """
        Due date (Fecha limite)

        :return: Datetime with Due date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        if due_date is None:
            self._due_date = None
        else:
            if self._check_due_date(due_date, self.suffix):
                if isinstance(due_date, basestring):
                    due_date = datetime.strptime(due_date, '%Y-%m-%d')
                self._due_date = due_date
                self._notice = self._due_date.strftime('%d%m%y')

    def amount100(self):
        """
        Remove the decimal point of the amount (Importe)

        :return: the amount (Importe) as an unicode string without decimal \
            point
        """
        return int(Decimal(self.amount) * 100)

    def checksum(self):
        """
        Generate the checksum (Dígitos de Control) to be added to reference \
            code (Número de referencia)

        :return: the checksum (Dígitos de Control) as an unicode string with \
            2 characters
        """
        sum = \
            int(self.entity) \
            + int(self.suffix) \
            + int(self.ref) \
            + int(self.notice) \
            + self.amount100()
        decimals = int(Decimal(sum) / 97 % 1 * 100)
        if not decimals:
            return '00'
        return unicode(100 - decimals).zfill(2)

    def code(self):
        """
        Generate the code for the barcode

        :return: an unicode string with the code for the barcode
        """
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
