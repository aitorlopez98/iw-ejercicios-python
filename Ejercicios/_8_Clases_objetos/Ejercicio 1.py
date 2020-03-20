class clsCoche:
    def __init__(self, matricula, marca):
        self.matricula = matricula
        self.marca = marca
        self.kilometros_recorridos = 0
        self.gasolina = 0

    def suficiente(self, gasolina, kilometros):
        max_km = gasolina / 0.1
        if kilometros <= max_km:
            return True
        return False

    def avanzar(self, kilometros):
        if self.suficiente(self.gasolina, kilometros):
            self.gasolina -= (kilometros*0.1)
            self.kilometros_recorridos += kilometros
        else:
            print("Hace falta gasolina")

    def repostar(self, gasolina):
        self.gasolina += gasolina

c1 = clsCoche("0908IKJ", "Tesla")
c1.repostar(100)
print(f"KM: {c1.kilometros_recorridos} -- Gasolina: {c1.gasolina}")
c1.avanzar(150)
print(f"KM: {c1.kilometros_recorridos} -- Gasolina: {c1.gasolina}")
c1.avanzar(600)
print(f"KM: {c1.kilometros_recorridos} -- Gasolina: {c1.gasolina}")
c1.avanzar(200)
print(f"KM: {c1.kilometros_recorridos} -- Gasolina: {c1.gasolina}")
