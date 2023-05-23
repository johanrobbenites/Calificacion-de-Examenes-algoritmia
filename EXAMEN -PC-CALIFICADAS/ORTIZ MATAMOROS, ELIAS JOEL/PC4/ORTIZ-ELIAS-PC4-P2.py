archivo_estudiantes = open("ALUMNOS.txt" ,"r")
n = int(input("Valor de n: "))
for i in range(n):
    cod = int(input("Código: "))
    curso = input("Curso: ")
    nota = float(input("Nota: "))
    linea = str(cod)+","+str(curso)+","+str(nota)+"\n"
    archivo_estudiantes.write(linea)


while(archivo_estudiantes):
    print(linea)

archivo_estudiantes.close()
end=input("")