lista = [12, 23, 5, 29, 92, 64]
nueva = []
total = 0
mayor = 0

#Elimina el último número y añádelo al principio.
ultimo = lista[-1]
lista.pop()
lista.insert(0, ultimo)
print(lista)

#Mueve el segundo elemento a la última posición.
ultimo = lista[1]
lista.append(ultimo)
lista.pop(1)
print(lista)

#Añade el número 14 al comienzo de la lista.
lista.insert(0, 14)
print(lista)

#Suma todos los números de la lista y añade el resultado al final de la lista.
for n in lista:
    total = total + n

lista.append(total)
print(lista)

#Fusiona la lista actual con la siguiente: [4, 11, 32]
otra_lista = [4, 11, 32]

lista.extend(otra_lista)
print(lista)

#Elimina todos los números impares de la lista.
for n in lista:
    total = n%2
    if total != 0:
        lista.remove(n)

print(lista)

#Ordena los números de la lista de forma ascendente.
for n in range(len(lista)-1,0,-1):
        for i in range(n):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp

print(lista)

#Vacía la lista.
lista.clear()
print(lista)
