"""Tools for working with Temperatures.

Author: Tyler Baker
Class: CSI-260-02
Assignment: Week 11 Lab
Due Date: April 4, 2019 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""


class Temperature:
    """Represents a temperature."""

    def __init__(self, degrees=0.0):
        """Initialize temperature with specified degrees celsius.

        Args:
            degrees: number of degrees celsius
        """
        self.celsius = degrees

    def __str__(self):
        """Convert temperature to string."""
        return f'{self.celsius}°C'

    def __repr__(self):
        """Convert temperature to an appropriate representation."""
        return f'Temperature({self.celsius})'

    def __float__(self):
        """Allow float conversion from temperature."""
        return float(self.celsius)

    def __int__(self):
        """Allow int conversion from temperature."""
        return int(self.celsius)

    def __eq__(self, other):
        """Determine if two temperatures are equal."""
        return float(self) == float(other)

    def __lt__(self, other):
        """Determine if one temperature is less than the other."""
        return float(self) < float(other)

    def __gt__(self, other):
        """Determine if one temperature is greater than the other."""
        return float(self) > float(other)

    def __add__(self, other):
        """Use addition with temperature."""
        return Temperature(float(self) + float(other))

    def __radd__(self, other):
        """Use addition with temperature."""
        return self + other

    def __sub__(self, other):
        """Use subtraction with temperature."""
        return Temperature(float(self) - float(other))

    def __rsub__(self, other):
        """Use subtraction with temperature."""
        return Temperature(float(other) - float(self))

    def __iadd__(self, other):
        """Use in place addition with temperature."""
        self.celsius = self + other
        return self

    def __isub__(self, other):
        """Use in place subtraction with temperature."""
        self.celsius = self - other
        return self

    def __ge__(self, other):
        """Determine of one temperature is greater than or equal to a value."""
        return self > other or self == other

    def __le__(self, other):
        """Determine of one temperature is less than or equal to a value."""
        return self < other or self == other

    def __hash__(self):
        """Use hash with temperature."""
        return hash(str(self))
