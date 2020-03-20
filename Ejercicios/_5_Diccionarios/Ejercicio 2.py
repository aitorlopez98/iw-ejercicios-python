dic = {'Mikel': 3,
       'Ane': 8,
       'Amaia': 12,
       'Unai': 5,
       'Jon': 8,
       'Ainhoa': 7,
        'Maite': 5}
lista = []

for n in dic:
    if dic[n] not in lista:
        lista.append(dic[n])

print(lista)
