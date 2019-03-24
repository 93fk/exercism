from __future__ import division

def gcd(n, d):
    if d == 0:
        return n
    else:
        return gcd(d, n % d)

class Rational(object):

    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    
    def __eq__(self, other):
        gdc_self = gcd(self.numer, self.denom)
        gdc_other = gcd(other.numer, other.denom)
        self_numer = self.numer/gdc_self
        self_denom = self.denom/gdc_self
        other_numer = other.numer/gdc_other
        other_denom = other.denom/gdc_other
        return self_numer == other_numer and self_denom == other_denom

    def __repr__(self): 
        gcd_ = gcd(self.numer, self.denom)
        numer = self.numer/gcd_
        denom = self.denom/gcd_
        return f'{numer}/{denom}'

    def __add__(self, other):
        numer = (self.numer * other.denom + other.numer * self.denom)
        denom = (self.denom * other.denom)
        return Rational(numer, denom)

    def __sub__(self, other):
        numer = (self.numer * other.denom - other.numer * self.denom)
        denom = (self.denom * other.denom)
        return Rational(numer, denom)

    def __mul__(self, other):
        numer = (self.numer * other.numer)
        denom = (self.denom * other.denom)
        return Rational(numer, denom)

    def __truediv__(self, other):
        if self.denom * other.denom != 0:
            numer = (self.numer * other.denom)
            denom = (self.denom * other.numer)
            return Rational(numer, denom)
        else:
            raise(ValueError('You can\'t divide by 0'))

    def __abs__(self):
        numer = abs(self.numer)
        denom = abs(self.denom)
        return Rational(numer, denom)

    def __pow__(self, power):
        if power >= 0:
            numer = self.numer**power
            denom = self.denom**power
        else:
            numer = self.denom**abs(power)
            denom = self.numer**abs(power)
        return Rational(numer, denom)

    def __rpow__(self, base):
        return (base**self.numer)**(1/self.denom)


