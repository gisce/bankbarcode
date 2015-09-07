from expects import expect, equal
from bankbarcode.cuaderno57 import Recibo507

with description('Checksum Recibo507 of cuaderno57'):
    with it('accomplish the example of cuaderno57.pdf'):
        entity = '01234567'
        suffix = '023'
        ref = '12345678901'
        notice = '123456'
        amount = '6543.21'
        checksum = '74'
        expect(Recibo507(entity, suffix, ref, notice, amount).checksum()).to(equal(checksum))

    with it('accomplish another example'):
        entity = '22350466'
        suffix = '501'
        ref = '00000000015'
        notice = '300815'
        amount = '53.98'
        checksum = '68'
        expect(Recibo507(entity, suffix, ref, notice, amount).checksum()).to(equal(checksum))

    with it('accomplish another example'):
        entity = '22350466'
        suffix = '501'
        ref = '00000000401'
        notice = '300815'
        amount = '37.62'
        checksum = '56'
        expect(Recibo507(entity, suffix, ref, notice, amount).checksum()).to(equal(checksum))
