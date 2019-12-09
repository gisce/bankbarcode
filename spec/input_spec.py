from sys import maxsize
from expects import expect, be_true, raise_error
from random import randint
from bankbarcode.bankbarcode import BankBarcode

with description('Check input values'):

    with context('Length value checker'):

        with before.all:
            self.name = 'foo'
            self.description = 'bar'

        with before.each:
            self.value = unicode(randint(0, maxint))

        with it('return true for value with expected length'):
            expected_length = len(self.value)
            expect(BankBarcode()._check_length(self.name, self.value, expected_length, self.description)).to(be_true)

        with it('raise a value error for short value'):
            expected_length = len(self.value) + randint(1, 10)
            short_error = '{} is too short, {}'.format(self.name, self.description)

            def callback():
                BankBarcode()._check_length(self.name, self.value, expected_length, self.description)

            expect(callback).to(raise_error(ValueError, short_error))

        with it('raise a value error for long value'):
            expected_length = len(self.value) - randint(1, len(self.value))
            long_error = '{} is too long, {}'.format(self.name, self.description)

            def callback():
                BankBarcode()._check_length(self.name, self.value, expected_length, self.description)

            expect(callback).to(raise_error(ValueError, long_error))
