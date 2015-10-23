from datetime import datetime

from expects import expect, equal, raise_error
from bankbarcode.cuaderno57 import Recibo507

with description('Recibo507 with due date of cuaderno57'):
    with it('Validate than suffix is less than 500'):
        def callback():
            entity = '01234567'
            suffix = '023'
            ref = '12345678901'
            notice = '123456'
            amount = '6543.21'
            due_date = datetime(2015, 11, 01)
            recibo = Recibo507(entity, suffix, ref, notice, amount, due_date)
        expect(callback).to(
            raise_error(ValueError,
                        'suffix with due date must be bigger than 499'))

    with it('Overwrites introduced notice for due date DDMMAA'):
        entity = '22350466'
        suffix = '501'
        ref = '00000000015'
        notice = '300815'
        amount = '53.98'
        due_date = datetime(2015, 11, 01)
        recibo = Recibo507(entity, suffix, ref, notice, amount, due_date)
        expect(recibo.notice).not_to(equal(notice))
        expect(recibo.notice).to(equal(due_date.strftime('%d%m%y')))

