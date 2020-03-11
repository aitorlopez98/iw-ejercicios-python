num = ""
mayor = 0
numeros = []

while num != "fin":
    num = input("escribe un numero o fin")
    if num != "fin":
        num = float(num)
        numeros.append(num)

for n in numeros:
    if mayor < n:
        mayor = n

print(f"El mayor es {mayor}")
