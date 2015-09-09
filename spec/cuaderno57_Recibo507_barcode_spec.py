from expects import expect, be_true, contain
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
            provided_filename = '/tmp/example-c57'
            generated_filename = self.example_c57.save(provided_filename)
            expect(isfile(generated_filename)).to(be_true)

        with it('accomplish another example'):
            provided_filename = '/tmp/example1'
            generated_filename = self.example1.save(provided_filename)
            expect(isfile(generated_filename)).to(be_true)

        with it('accomplish another example'):
            provided_filename = '/tmp/example2'
            generated_filename = self.example2.save(provided_filename)
            expect(isfile(generated_filename)).to(be_true)

    with context('SVG barcode'):
        with it('accomplish the example of cuaderno57.pdf'):
            svg = self.example_c57.svg()
            expect(svg).to(contain('<svg','</svg>'))

        with it('accomplish another example'):
            path = '/tmp/example1'
            svg = self.example1.svg()
            expect(svg).to(contain('<svg','</svg>'))

        with it('accomplish another example'):
            path = '/tmp/example2'
            svg = self.example2.svg()
            expect(svg).to(contain('<svg', '</svg>'))
