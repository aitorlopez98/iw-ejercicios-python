num1 = int(input("escribe un numero"))
num2 = int(input("escribe otro numero"))
par = 0
impar = 0

while num1 <= num2:
    resto = num1%2

    if resto == 0:
        par = par + num1

    elif resto != 0:
        impar = impar + num1

    num1 += 1

print(f"Los pares suman {par} y los impares suman {impar}")
