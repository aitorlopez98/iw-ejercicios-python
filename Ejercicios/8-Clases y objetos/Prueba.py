class Coche:
    def __init__(self, matricula, marca):
        self.matricula = matricula
        self.marca = marca
        self.kilometros_recorridos = 0
        self.gasolina = 0

    def gasolina_suficiente(self, kilometros, gasolina):
        max_kilometros = gasolina / 0.1
        if(kilometros <= max_kilometros):
            return True
        return False


    def avanzar(self, kilometros):
        if self.gasolina_suficiente(kilometros, self.gasolina):
            self.gasolina -= (kilometros * 0.1)
            self.kilometros_recorridos += kilometros
        else:
            print("Es necesario repostar para recorrerla cantidad indicada de kilómetros")

    def repostar(self, gasolina):
        self.gasolina += gasolina


coche = Coche("1616GIR", "Audi")
coche.repostar(50)
print(f"Km. recorridos = {coche.kilometros_recorridos} -- Gasolina = {coche.gasolina}")
coche.avanzar(100)
print(f"Km. recorridos = {coche.kilometros_recorridos} -- Gasolina = {coche.gasolina}")
coche.avanzar(40)
print(f"Km. recorridos = {coche.kilometros_recorridos} -- Gasolina = {coche.gasolina}")
coche.avanzar(180)
print(f"Km. recorridos = {coche.kilometros_recorridos} -- Gasolina = {coche.gasolina}")

coche.avanzar(1800)
print(f"Km. recorridos = {coche.kilometros_recorridos} -- Gasolina = {coche.gasolina}")
