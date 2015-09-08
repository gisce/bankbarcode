from expects import expect, be_true
from bankbarcode.cuaderno57 import Recibo507
from os.path import isfile


with description('Recibo507 of cuaderno57'):
    with before.all:
        entity = '01234567'
        suffix = '023'
        ref = '12345678901'
        notice = '123456'
        amount = '6543.21'
        self.example_c57 = Recibo507(entity, suffix, ref, notice, amount)

        entity = '22350466'
        suffix = '501'
        ref = '00000000015'
        notice = '300815'
        amount = '53.98'
        self.example1 = Recibo507(entity, suffix, ref, notice, amount)

        entity = '22350466'
        suffix = '501'
        ref = '00000000401'
        notice = '300815'
        amount = '37.62'
        self.example2 = Recibo507(entity, suffix, ref, notice, amount)

    with context('save barcode'):
        with it('accomplish the example of cuaderno57.pdf'):
            path = '/tmp/example-c57'
            self.example_c57.save(path)
            expect(isfile(path+'.svg')).to(be_true)

        with it('accomplish another example'):
            path = '/tmp/example1'
            self.example1.save(path)
            expect(isfile(path+'.svg')).to(be_true)

        with it('accomplish another example'):
            path = '/tmp/example2'
            self.example2.save(path)
            expect(isfile(path+'.svg')).to(be_true)
