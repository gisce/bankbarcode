from sys import maxint
from expects import *
from random import randint, uniform, random
from bankbarcode.cuaderno57 import Recibo507

with description('Check input values for Recibo507'):

    with before.all:
        entity = '12345678'
        suffix = '123'
        ref = '12345678901'
        id = '123456'
        amount = '1'

        self.recibo507 = Recibo507(entity, suffix, ref, id, amount)

    with context('Check entity'):

        with it('return True if length of value is 8, a NIF/CIF, without the letter'):
            value = unicode(randint(0, 99999999)).zfill(8)
            expect(self.recibo507._check_entity(value)).to(be_true)

        with it('raise a value error if length of value is less than 8'):
            short_value = unicode(randint(0, 9999999))
            short_error = 'entity is too short, entity should be a NIF/CIF, without the letter'

            def callback():
                self.recibo507._check_entity(short_value)

            expect(callback).to(raise_error(ValueError, short_error))

        with it('raise a value error if length of value is greater than 8'):
            long_value = unicode(randint(100000000, maxint))
            long_error = 'entity is too long, entity should be a NIF/CIF, without the letter'

            def callback():
                self.recibo507._check_entity(long_value)

            expect(callback).to(raise_error(ValueError, long_error))

    with context('Check suffix'):

        with it('return True if the length of value is 3'):
            value = unicode(randint(0, 999)).zfill(3)
            expect(self.recibo507._check_suffix(value)).to(be_true)

        with it('raise a value error if length of value is less than 3'):
            short_value = unicode(randint(0, 99))

            def callback():
                self.recibo507._check_suffix(short_value)

            expect(callback).to(raise_error(ValueError, 'suffix is too short, suffix lenth should be 3'))

        with it('raise a value error if length of value is greater than 3'):
            long_value = unicode(randint(1000, maxint))

            def callback():
                self.recibo507._check_suffix(long_value)

            expect(callback).to(raise_error(ValueError, 'suffix is too long, suffix lenth should be 3'))

    with context('Check reference'):

        with it('return True if the length of value is 11'):
            value = unicode(randint(0, 9999999999)).zfill(11)
            expect(self.recibo507._check_ref(value)).to(be_true)

        with it('raise a value error if length of value is less than 11'):
            short_value = unicode(randint(0, 9999999999))

            def callback():
                self.recibo507._check_ref(short_value)

            expect(callback).to(raise_error(ValueError, 'ref is too short, ref lenth should be 11'))

        with it('raise a value error if length of value is greater than 11'):
            long_value = unicode(randint(100000000000, maxint))

            def callback():
                self.recibo507._check_ref(long_value)

            expect(callback).to(raise_error(ValueError, 'ref is too long, ref lenth should be 11'))

    with context('Check identification'):

        with it('return True if the length of value is 6'):
            value = unicode(randint(0, 999999)).zfill(6)
            expect(self.recibo507._check_id(value)).to(be_true)

        with it('raise a value error if length of value is less than 6'):
            short_value = unicode(randint(0, 99999))

            def callback():
                self.recibo507._check_id(short_value)

            expect(callback).to(raise_error(ValueError, 'id is too short, id lenth should be 6'))

        with it('raise a value error if length of value is greater than 6'):
            long_value = unicode(randint(1000000, maxint))

            def callback():
                self.recibo507._check_id(long_value)

            expect(callback).to(raise_error(ValueError, 'id is too long, id lenth should be 6'))

    with context('Check amount'):

        with it('return True if amount is a unicode with less than 100000000 with 2 decimals'):
            value = unicode(round(uniform(0, 99999999.99), 2))
            expect(self.recibo507._check_amount(value)).to(be_true)

        with it('return True is amount is a int less than 100000000'):
            value = randint(0, 99999999)
            expect(self.recibo507._check_amount(value)).to(be_true)

        with it('raise a value error if amount isn\'t less than 100000000'):
            big_value = unicode(round(uniform(100000000, maxint), 2))

            def callback():
                self.recibo507._check_amount(big_value)

            expect(callback).to(raise_error(ValueError, 'amount is too big'))

        with it('raise a value error if amount have more than 2 decimals'):
            float_value = unicode(round(random(), randint(3, 10)))

            def callback():
                self.recibo507._check_amount(float_value)

            expect(callback).to(raise_error(ValueError, 'amount have more than 2 decimals'))
