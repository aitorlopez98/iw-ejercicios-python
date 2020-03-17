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

r1 = clsRobot(0, 0)
move = ""

while move != "fin":
    move = input("A-adelante/R-retroceder/I-izquierda/D-derecha/FIN-salir: ")
    i = 0
    if move.__eq__("fin"):
        print("Fin")


    while i < len(move) and move != "fin":
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
