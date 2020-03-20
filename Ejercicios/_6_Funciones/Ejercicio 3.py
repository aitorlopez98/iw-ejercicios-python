lista = [6,14,11,3,2,1,15,19]

def rango(num):
    if num < 21 and num > 0:
        print("Numero en rango")
        return True
    else:
        print("Numero fuera de rango")
        return False

def enlista(num):
    for n in lista:
        if n == num:
            print("Numero en lista")

num = int(input("Escribe un numero entre 1 y 20: "))

if rango(num):
    enlista(num)
