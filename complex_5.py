class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im < 0:
            return str(self.re) + '-' + str(-self.im)+ 'i'
        else:
            return str(self.re) + '-' + str(-self.im) + 'i'

    # member1
    def __add__(self, c): # return self+c
        return Complex(self.re + c.re, self.im + c.im)

    # member2
    def __sub__(self, c): # return self-c
        return Complex(self.re - c.re, self.im - c.im)

        # member3
    def __mul__(self, c): # return self*c
        return Complex(self.re*c.re - self.im*c.im, self.re*c.im + self.im*c.re)


c1 = Complex(1,2)
c2 = Complex(2,-2)
print(c1+c2)
print(c1-c2)
print(c1*c2)
