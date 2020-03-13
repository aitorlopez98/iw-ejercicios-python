estudiantes = {

}
est = 0
name = ""
nota = 0
i = 0
j = 0

if i < 10:
    while est != "fin":
        name = input("Escribe el nombre: ")
        nota = input("Escribe la nota: ")
        estudiantes[i] = dict(nombre = name, nota = nota)
        est = input("Otro estuadiante o fin para salir: ")
    i += 1

for n in estudiantes[j]:
    print(estudiantes[j][n])
    j += 1
