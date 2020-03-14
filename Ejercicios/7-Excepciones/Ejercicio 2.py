people = {
    "nombre": "Aitor",
    "apellido": "Lopez",
    "edad": 21
}

try:
    key = input("Que dato quieres ver: ")
    print(people[key])

except:
    print("Clave inexistente")
