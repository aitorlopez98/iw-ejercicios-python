import math


class clsPoligono:

    def __init__(self, color, lados):
        self.color = color
        self.lados = lados

    def perimetro(self):
        perimetro = 0
        for n in self.lados:
            perimetro += n

        return perimetro

class clsTriangulo(clsPoligono):

    def __init__(self, color, lados):
        clsPoligono.__init__(self, color, lados)

    def area(self):
        s = self.lados[0] + self.lados[1] + self.lados[2]
        a = (s*(s-self.lados[0])*(s-self.lados[1])*(s-self.lados[2]))
        return math.sqrt(a)

    def forma(self):

        if self.lados[0] == self.lados[1] and self.lados[0] == self.lados[2]:
            return "Triangulo equilatero"
        elif self.lados[0] == self.lados[1] or self.lados[0] == self.lados[2] or self.lados[1] == self.lados[2]:
            return "Triangulo isosceles"
        else:
            return "Triangulo irregular"

class clsCuadrado(clsPoligono):

    def __init__(self, color, lados):
        clsPoligono.__init__(self, color, lados)

    def area(self):
        return self.lados[0]**2


cateto1 = float(input("Dato cateto 1: "))
cateto2 = float(input("Dato cateto 2: "))
hipo = float(input("Dato base: "))
colort = input("Color del triangulo: ")
tr = clsTriangulo(colort, [cateto1, cateto2, hipo])
print(f"El area es: {tr.area()} La forma es: {tr.forma()} El perimetro es: {tr.perimetro()} El color es: {tr.color}")

lado = float(input("Tamaño lados pequeños: "))
colorc = input("Color del cuadrado: ")
c1 = clsCuadrado(colorc, [lado, lado, lado, lado])
print(f"El perimetro es: {c1.area()} El area es: {c1.perimetro()} El color es: {c1.color}")
