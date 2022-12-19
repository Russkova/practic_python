class Complex:

    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag


    def __abs__(self):
        return (self.real ** 2 + self.imag ** 2) ** (1 / 2)

    def __eq__(self, other):
        return str(self) == str(other)

    def __str__(self):
        if self.real == 0:
            return str(self.imag) + 'i'
        if self.imag == 0:
            return str(self.real)
        if self.imag == 1:
            return str(self.real) + '+' + 'i'
        if self.imag == -1:
            return str(self.real) + '-' + 'i'
        if self.imag > 0:
            return str(self.real) + '+' + str(self.imag) + 'i'
        if self.imag < 0:
            return str(self.real) + str(self.imag) + 'i'


    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.imag * other.real + self.real * other.imag)

    def __truediv__(self, other):
        return Complex(
            (self.real * other.real + self.imag * other.imag) / (other.real ** 2 + other.imag ** 2),
            (other.real * self.imag - self.real * other.imag) / (other.real ** 2 + other.imag ** 2))

