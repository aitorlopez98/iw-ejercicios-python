usuarios = {
    "iperurena": {
        "nombre": "Iñaki",
            "apellido": "Perurena",
            "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
            "apellido": "Muguruza",
            "password": "654321"
    },
    "aolaizola": {
        "nombre": "Aimar",
            "apellido": "Olaizola",
            "password": "123456"
    }
}

i = 3

while i > 0:
    password = input("escribe tu contraseña: ")
    for key in usuarios:
        if usuarios[key]["password"].__eq__(password):
            if password == usuarios["iperurena"]["password"]:
                print("Nombre: " + usuarios["iperurena"]["nombre"])
                print("Apellido: " + usuarios["iperurena"]["apellido"])

            elif password == usuarios["fmuguruza"]["password"]:
                print("Nombre: " + usuarios["fmuguruza"]["nombre"])
                print("Apellido: " + usuarios["fmuguruza"]["apellido"])


            elif password == usuarios["aolaizola"]["password"]:
                print("Nombre: " + usuarios["aolaizola"]["nombre"])
                print("Apellido: " + usuarios["aolaizola"]["apellido"])

    i -= 1
    print(f"Te quedan {i} intentos")

    if i == 0:
        print("Adios")

