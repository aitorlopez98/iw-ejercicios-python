class clsVehiculo:
    def __init__(self, marca):
        self.kilometros = 0
        self.marca = marca

    def andar(self, kilometros):
        self.kilometros += kilometros

class clsCoche(clsVehiculo):
    def __init__(self, matricula, marca):
        clsVehiculo.__init__(self, marca)
        self.matricula = matricula
        self.gasolina = 0

    def suficiente(self, gasolina, kilometros):
        max_km = gasolina / 0.1
        if kilometros <= max_km:
            return True
        return False

    def avanzar(self, kilometros):
        if self.suficiente(self.gasolina, kilometros):
            self.gasolina -= (kilometros*0.1)
            self.andar(kilometros)
        else:
            print("Hace falta gasolina")

    def repostar(self, gasolina):
        self.gasolina += gasolina

class clsBicicleta(clsVehiculo):
    def __init__(self, marca):
        clsVehiculo.__init__(self, marca)
        self.aire = 50

    def hinchar_ruedas(self):
        self.aire = 50

    def pedalear(self, kilometros):
        if self.aire >= kilometros:
            self.aire -= kilometros
            self.andar(kilometros)
        else:
            print("Hay que hinchar las ruedas")

op = input("C-coche/B-bicicleta: ")
op = op.lower()
if op.__eq__("c"):
    matri = input("¿Matricula?: ")
    marca = input("¿Marca?: ")
    c1 = clsCoche(matri, marca)
    c1.repostar(50)
    km = float(input("KM a recorrer"))
    c1.avanzar(km)
    print(f"KM recorridos: {c1.kilometros} -- Gasolina: {c1.gasolina}")
    km = float(input("KM a recorrer"))
    c1.avanzar(km)
    print(f"KM recorridos: {c1.kilometros} -- Gasolina: {c1.gasolina}")

if op.__eq__("b"):
    marca = input("¿Marca?: ")
    b1 = clsBicicleta(marca)
    km = float(input("KM a recorrer"))
    b1.pedalear(km)
    print(f"KM recorridos: {b1.aire}")
    km = float(input("KM a recorrer"))
    b1.pedalear(km)
    print(f"KM recorridos: {b1.aire}")
