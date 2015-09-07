from expects import expect, be_true
from bankbarcode.cuaderno57 import Recibo507
from os.path import isfile

with description('Save barcode of Recibo507 of cuaderno57'):
    with it('accomplish the example of cuaderno57.pdf'):
        entity = '01234567'
        suffix = '023'
        ref = '12345678901'
        notice = '123456'
        amount = '6543.21'
        path = '/tmp/example-c57'
        Recibo507(entity, suffix, ref, notice, amount).save(path)
        expect(isfile(path+'.svg')).to(be_true)

    with it('accomplish another example'):
        entity = '22350466'
        suffix = '501'
        ref = '00000000015'
        notice = '300815'
        amount = '53.98'
        path = '/tmp/example1'
        Recibo507(entity, suffix, ref, notice, amount).save(path)
        expect(isfile(path+'.svg')).to(be_true)

    with it('accomplish another example'):
        entity = '22350466'
        suffix = '501'
        ref = '00000000401'
        notice = '300815'
        amount = '37.62'
        path = '/tmp/example2'
        Recibo507(entity, suffix, ref, notice, amount).save(path)
        expect(isfile(path+'.svg')).to(be_true)
