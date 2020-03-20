num1 = int(input("escribe un numero"))
num2 = int(input("escribe otro numero"))
total = 0

while num1 <= num2:
    total = total + num1
    num1 += 1

print(f"El resultado es {total}")
