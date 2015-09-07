from barcode import generate


class BankBarcode(object):

    def _check_length(self, name, value, expected_length, description):
        length = len(value)
        if length < expected_length:
            raise ValueError('{} is too short, {}'.format(name, description))
        elif length > expected_length:
            raise ValueError('{} is too long, {}'.format(name, description))
        elif length == expected_length:
            return True

    def save(self, path):
        writer_options = {'font_size': 6}
        generate(
            'code128',
            self.code(),
            output=path,
            writer_options=writer_options
        )
