i = 3

while i > 0:
    user = input("introduce el ususario")
    password = input("introduce la contraseña")

    if user.__eq__("root") and password.__eq__("toor"):
        print("Bienvenido")

    else:
        print("Acceso Fallido")

    i -= 1
    print(f"Te quedan {i} intentos")

    if i == 0:
        print("Has agotado todos los intentos, FIN")
