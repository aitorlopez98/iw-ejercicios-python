class clsRobot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def avanzar(self):
        self.x += 1

    def retorceder(self):
        self.x -= 1

    def izquierda(self):
        self.y -= 1

    def derecha(self):
        self.y += 1

    def posicion(self):
        _x = self.x
        _y = self.y
        print(f"La posicción (X,Y) es ({_x},{_y})")

    def movimientos(self):
        i = 0
        print("Los movimientos que has realizado son: ")
        while i < len(move) and move != "fin" and move != "inicio":
            if move[i].__eq__("a"):
                print("-Adelante")
            elif move[i].__eq__("r"):
                print("-Atras")
            elif move[i].__eq__("i"):
                print("-Izquierda")
            elif move[i].__eq__("d"):
                print("-Derecha")

            i += 1

    def inicio(self):
        _x = self.x
        _y = self.y

        ox = 0 - _x
        oy = 0 - _y
        if ox < 0:
            print(f"Retrocede {_x} veces")
        elif ox > 0:
            print(f"Adelante {ox} veces")
        else:
            print("Estas en 0 en el eje X")

        if oy < 0:
            print(f"Izquierda {_y} veces")
        elif oy > 0:
            print(f"Derecha {oy} veces")
        else:
            print("Estas en 0 en el eje Y")

r1 = clsRobot(0, 0)
move = ""

while move != "fin":
    move = input("A-adelante/R-retroceder/I-izquierda/D-derecha/INICIO-mov. hasta inicio/FIN-salir: ")
    i = 0
    if move.__eq__("fin"):
        print("Fin")

    while i < len(move) and move != "fin" and move != "inicio":
        move = move.lower()
        if move[i].__eq__("a"):
            r1.avanzar()
        elif move[i].__eq__("r"):
            r1.retorceder()
        elif move[i].__eq__("i"):
            r1.izquierda()
        elif move[i].__eq__("d"):
            r1.derecha()
        else:
            print("ERROR")
            break

        i += 1

    r1.posicion()
    if move != "fin":
        r1.movimientos()
    if move.__eq__("inicio"):
        r1.inicio()
