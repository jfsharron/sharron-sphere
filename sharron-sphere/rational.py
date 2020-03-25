"""
File:       rational.py
Resources to manipulate rational numbers.
"""

class Rational(object):
    """ Represents a rational number."""

    def __init__(self, numer, denom):
        """ 
        Constructor; Creates a rational number with the given numerator and 
        denominator and reduces it to lowest terms.
        """
        self.numer = numer
        self.denom = denom
        self._reduce()

    def numerator(self):
        """
        Returns the numerator.
        """
        return self.numer

    def denominator(self):
        """
        Returns the denominator.
        """
        return self.denom

    def __str__(self):
        """
        Returns the string representation of the number.
        """
        return str(self.numer) + "/" + str(self.denom)

    def _reduce(self):
        """
        Helper to reduce the number to lowest terms.
        """
        divisor = self._gcd(self.numer, self. denom)
        self.numer = self.numer // divisor
        self.denom = self.denom // divisor

    def _gcd(self, a, b):
        """
        Euclid's algorithm for greatest common divisor.
        """
        (a, b) = (max(a, b), min(a, b))
        while b > 0:
            (a, b) = (b, a % b)
        return a

    def __add__(self, other):
        """
        Returns the sum of rational numbers where 
        n1/d1 + n2/d2 = (n1*d2 + n2*d1)/(d1*d2)
        self is the left operand and other is the right operand.
        """
        newNumer = self.numer * other.denom + other.numer * self.denom
        newDenom = self.denom * other.denom
        return Rational(newNumer, newDenom)
