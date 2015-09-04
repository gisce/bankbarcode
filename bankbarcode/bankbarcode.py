class BankBarcode():

    def _check_length(self, name, value, expected_length, description):
        length = len(value)
        if length < expected_length:
            raise ValueError('{} is too short, {}'.format(name, description))
        elif length > expected_length:
            raise ValueError('{} is too long, {}'.format(name, description))
        elif length == expected_length:
            return True
