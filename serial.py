class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    #static variable

    start_number = 0 #100 => 101 => 102

    def __init__(self, start):
        """Constructing a serial generator"""

        self.start = start
        SerialGenerator.start_number = start


    def generate(self):
        """Incrementing start number by 1"""
        if SerialGenerator.start_number == self.start:
            SerialGenerator.start_number += 1
            return self.start

        SerialGenerator.start_number += 1
        return SerialGenerator.start_number - 1

    def reset(self):
        """Reset start number to original val"""

        SerialGenerator.start_number = self.start
