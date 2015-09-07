from expects import *
from bankbarcode.cuaderno57 import Recibo507

with description('Code generation for Recibo507 of cuaderno57'):
    with it('accomplish an example'):
        entity = '22350466'
        suffix = '501'
        ref = '00000000015'
        notice = '300815'
        amount = '53.98'
        code = '9050722350466501000000000156830081500000053980'
        expect(Recibo507(entity, suffix, ref, notice, amount).code()).to(equal(code))

    with it('accomplish another example'):
        entity = '22350466'
        suffix = '501'
        ref = '00000000401'
        notice = '300815'
        amount = '37.62'
        code = '9050722350466501000000004015630081500000037620'
        expect(Recibo507(entity, suffix, ref, notice, amount).code()).to(equal(code))
