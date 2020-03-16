class clsCoche:

    matricula = ""
    marca = ""
    kilometros_recorridos = 0
    gasolina = 0
    litros = 0

    def __init__(self, matricula, marca, kilometros_recorridos, gasolina, litros):
        self.matricula = matricula
        self.marca = marca
        self.kilometros_recorridos = float(kilometros_recorridos)
        self.gasolina = gasolina
        self.litros = litros

    def datos(self, matricula, marca):
        matricula = input("Matricula del coche: ")
        marca = input("Marcac del coche: ")

    def avanzar(self, kilometros_recorridos, gasolina):
        km = float(input("Cantidad de kilometros a conducir: "))
        if self.repostar(self, self.litros, gasolina, km):
            litros = gasolina - km*0.1

        kilometros_recorridos = kilometros_recorridos + km+0.1

    def repostar(self, litros, gasolina, km):
        _km = km
        _gasolina = gasolina
        _litros = litros

        _litros = gasolina - km*0.1
        if _litros > 0:
            print("Puedes avanzar")
            return True
        else:
            print("Hay que repostar")
            return False

c1 = clsCoche
c1.datos(self, matricula, marca)
c1.avanzar()
