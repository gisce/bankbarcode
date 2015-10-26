from barcode import generate
from StringIO import StringIO


class BankBarcode(object):
    """
    Base class for barcodes
    """

    defaults = {
        'font_size': 6
    }

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

    def _strip_dotsvg(self, path):
        if isinstance(path, basestring) and path[-4:] == '.svg':
            new_path = path[:-4]
        else:
            new_path = path
        return new_path

    def code(self):
        """
        Code generation. To implement in child classes
        """
        raise NotImplementedError('This method is not implemented!')

    def save(self, path, writer_options=None):
        """
        Save barcode in SVG format.

        :param path: path to SVG file with or without ".svg" extension
        :param writer_options: Common options from pyBarcode \
            http://pythonhosted.org/pyBarcode/writers/index.html?#common-options
        :return: a string with the name of the file generated
        """
        path = self._strip_dotsvg(path)

        if writer_options is None:
            writer_options = self.defaults.copy()
        else:
            for k, v in self.defaults.items():
                writer_options.setdefault(k, v)

        return generate(
            'code128',
            self.code(),
            output=path,
            writer_options=writer_options
        )

    def svg(self, writer_options=None):
        """
        Generate a SVG with the barcode.

        :param writer_options: Common options from pyBarcode \
            http://pythonhosted.org/pyBarcode/writers/index.html?#common-options
        :return: a string with the barcode in SVG format
        """
        f = StringIO()
        self.save(f, writer_options)
        return f.getvalue()
