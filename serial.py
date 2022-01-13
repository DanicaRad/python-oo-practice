"""Python serial number generator."""

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
    def __init__(self, start):
        """Creates serialized numbers from start with increment of 1"""
        self.start = start
        self.next = start

    def __repr__(self):
        return f"SerialGenerator(start={self.start}, next={self.next}"

    def generate(self):
        """Generates next number in serial sequence"""
        next = self.next
        self.next += 1
        return next

    def reset(self):
        """Resets serial sequence back to start for generate()"""
        self.next = self.start

