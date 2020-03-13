def esPrimo(num):
    _num = num
    i = 2

    while i < _num and _num%i != 0:
        i = i + 1

    if i == _num:
        print(f"{_num} es primo")
    else:
        print(f"{_num} es compuesto")

num = int(input("Escribe un numero: "))
esPrimo(num)
