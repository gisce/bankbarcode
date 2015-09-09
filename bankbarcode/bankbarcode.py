from barcode import generate
from StringIO import StringIO


class BankBarcode(object):
    """
    Base class for barcodes
    """

    def _check_length(self, name, value, expected_length, description):
        """
        Check length of a value.

        :param name: name of the value
        :param value: the value itself
        :param expected_length: the expected length of the value
        :param description: definition of the expected value
        :return: True if value have the expected length, otherwise False
        """
        length = len(value)
        if length < expected_length:
            raise ValueError('{} is too short, {}'.format(name, description))
        elif length > expected_length:
            raise ValueError('{} is too long, {}'.format(name, description))
        elif length == expected_length:
            return True

    def code(self):
        """
        Code generation. To implement in child classes
        """
        raise NotImplementedError('This method is not implemented!')

    def save(self, path):
        """
        Save barcode in SVG format.

        :param path: path to SVG file without ".svg" extension
        :return: a string with the name of the file generated
        """
        writer_options = {'font_size': 6}
        return generate(
            'code128',
            self.code(),
            output=path,
            writer_options=writer_options
        )

    def svg(self):
        """
        Generate a SVG with the barcode.

        :return: a string with the barcode in SVG format
        """
        f = StringIO()
        self.save(f)
        return f.getvalue()
