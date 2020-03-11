i = 0
j = 0
lista = []
lista2 = []

while i < 5:
    num = int(input("escribe un nuemro"))
    lista.append(num)
    i += 1
print(lista)

while j < 5:
    num = int(input("escribe un nuemro"))
    lista2.append(num)
    j += 1
print(lista2)

for n in lista:
    for k in lista2:
        
