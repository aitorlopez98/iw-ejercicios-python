i = 0
j = 0
lista = []
lista2 = []
comparacion = []

while i < 5:
    num = int(input("escribe un numero"))
    lista.append(num)
    i += 1
print(f"Primera lista {lista}")

while j < 5:
    num = int(input("escribe un numero"))
    lista2.append(num)
    j += 1
print(f"Segunda lista {lista2}")

for n in lista:
    if n in lista2:
        comparacion.append(n)

print(comparacion)
