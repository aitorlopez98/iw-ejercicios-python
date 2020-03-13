import random

intento = -1

def comprobar(intento, num):
    if intento < num:
        print("El numero es mayor")
    elif intento > num:
        print("El numero es menor")
    elif intento == num:
        print(f"Has acertado, el numero era {num}")

num = random.randrange(10)

while intento != num:
    intento = int(input("Escribe el numero: "))
    comprobar(intento, num)
