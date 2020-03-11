num = int(input("elige un numero del 1 al 10"))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

for n in numeros:
    total = num*n
    print(f"{num} x {n} = {total}")
    n += 1
    if n > 10:
        break
