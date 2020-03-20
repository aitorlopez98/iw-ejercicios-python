n1 = float(input("escribe un numero"))
n2 = float(input("escribe un numero"))
n3 = float(input("escribe un numero"))
n4 = float(input("escribe un numero"))
n5 = float(input("escribe un numero"))

numeros = [n1, n2, n3, n4, n5]
mayor = 0

for n in numeros:
    if mayor < n:
        mayor = n

print(f"El mayor es {mayor}")
