from barcode import generate


class BankBarcode(object):
    """
    Base class for barcodes
    """

    def _check_length(self, name, value, expected_length, description):
        """
        Check length of a value.

        :param name: name of the value
        :param value: the value itself
        :param expected_length: the expected lenght of the value
        :param description: definition of the expected value
        :return: True if value have the expected lenght, otherwise False
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
        """
        writer_options = {'font_size': 6}
        generate(
            'code128',
            self.code(),
            output=path,
            writer_options=writer_options
        )
