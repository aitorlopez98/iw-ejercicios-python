lista = [12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64,23]
com = []
i = 0
dic = {
    "12": "",
    "23": "",
    "5": "",
    "92": "",
    "29": "",
    "64": ""
}

for n in lista:
    num = lista.count(n)
    if n not in com:
        com.append(num)

dic["12"] = com[0]
dic["23"] = com[1]
dic["5"] = com[2]
dic["92"] = com[3]
dic["29"] = com[4]
dic["64"] = com[5]

print(dic)
