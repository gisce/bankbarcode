from expects import expect, raise_error
from bankbarcode.bankbarcode import BankBarcode

with description('BankBarcode'):
    with it('doesn\'t have code generation method'):
        error = 'This method is not implemented!'

        def callback():
            return BankBarcode().code()

        expect(callback).to(raise_error(NotImplementedError, error))

    with it('can\'t create barcode without code generation method'):
        path = '/tmp/mybarcode'
        error = 'This method is not implemented!'

        def callback():
            return BankBarcode().save(path)

        expect(callback).to(raise_error(NotImplementedError, error))

    with it('can\'t create SVG without code generation method'):
        error = 'This method is not implemented!'

        def callback():
            return BankBarcode().svg()

        expect(callback).to(raise_error(NotImplementedError, error))
