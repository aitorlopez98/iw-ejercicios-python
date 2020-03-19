import math


class clsTriangulo:
    def __init__(self, cat1, cat2, base):
        self.cat1 = cat1
        self.cat2 = cat2
        self.base = base

    def area(self):
        _base = self.base
        _cat1 = self.cat1
        _cat2 = self.cat2
        s = _cat1 + _cat2 + _base
        a = (s*(s-_cat1)*(s-_cat2)*(s-_base))
        return math.sqrt(a)

    def forma(self):
        _cat1 = self.cat1
        _cat2 = self.cat2
        _base = self.base
        if _cat1 == _cat2 and _cat1 == _base:
            return "Triangulo equilatero"
        elif _cat1 == _cat2:
            return "Triangulo isosceles"
        else:
            return "Triangulo irregular"

    def perimetro(self):
        _cat1 = self.cat1
        _cat2 = self.cat2
        _base = self.base

        p = _cat1 + _cat2 + _base
        return p

cateto1 = float(input("Dato cateto 1: "))
cateto2 = float(input("Dato cateto 2: "))
hipo = float(input("Dato base: "))

tr = clsTriangulo(cateto1, cateto2, hipo)
op = input("Area-a/Forma-f/Perimetro-p: ")
op = op.lower()

if op.__eq__("a"):
    print(tr.area())
elif op.__eq__("f"):
    print(tr.forma())
elif op.__eq__("p"):
    print(tr.perimetro())
