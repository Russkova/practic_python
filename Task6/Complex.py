class Complex:

    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def add(self, number):
        return Complex(self.real + number.real, self.imag + number.imag)

    def sub(self, number):
        return Complex(self.real - number.real, self.imag - number.imag)

    def mul(self, number):
        return Complex(self.real * number.real - self.imag * number.imag,
                       self.imag * number.real + self.real * number.imag)

    def div(self, number):
        return Complex(
            (self.real * number.real + self.imag * number.imag) / (number.real ** 2 + number.imag ** 2),
            (number.real * self.imag - self.real * number.imag) / (number.real ** 2 + number.imag ** 2))

    def abs(self):
        return (self.real ** 2 + self.imag ** 2) ** (1 / 2)


    def __eq__(self, number):
        return self.real == number.real and self.imag == number.imag


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

