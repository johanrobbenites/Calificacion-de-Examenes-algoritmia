notas = []
n = int(input("Ingrese número de notas: "))
aprobados = 0
for i in range(n):
    nota = int(input("Ingrese nota " + str(i+1) +  ":"))
    notas.append(nota)
    if nota >= 10:
        aprobados += 1
    

for i in range(n):
    print(str(notas[i]), end = " ")
print(str(round(aprobados*100/n,2))+ "% de aprobados")

while round(aprobados*100/n,2) < 70:
    aprobados = 0
    for i in range(n):
        if notas[i] != 20:
            notas[i] = notas[i] + 1
        if notas[i] >= 10:
            aprobados += 1
        print(str(notas[i]), end= " ")
    print(str(round(aprobados*100/n,2))+ "% de aprobados")