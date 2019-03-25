"""Tools for working with Temperatures."""


class Temperature:
    """Represents a temperature."""

    def __init__(self, degrees=0):
        """Initialize temperature with specified degrees celsius.

        Args:
            degrees: number of degrees celsius
 
        """
        self.celsius = degrees

    def __str__(self):
        """Convert temperature to string"""
        return f'{self.celsius}°C'

    def __repr__(self):
        """Convert temperature to an appropriate representation"""
        return f'Temperature({self.celsius})'

    def __float__(self):
        """Allow float conversion with temperature"""
        return float(self.celsius)

    def __eq__(self, other):
        """Determine if two temperatures are equal"""
        return float(self) == float(other)

    def __lt__(self, other):
        """Determine if one temperature is less than the other"""
        return float(self) < float(other)

    def __gt__(self, other):
        """Determine if one temperature is greater than the other"""
        return float(self) > float(other)

    def __add__(self, other):
        """Use addition with temperature"""
        return Temperature(float(self) + float(other))

    def __sub__(self, other):
        """Use subtraction with temperature"""
        return Temperature(float(self) - float(other))

    def __iadd__(self, other):
        """Use in place addition with temperature"""
        self.celsius = self + other

    def __isub__(self, other):
        """Use in place subtraction with temperature"""
        self.celsius = self - other

    def __hash__(self):
        """Use hash with temperature"""
        pass
