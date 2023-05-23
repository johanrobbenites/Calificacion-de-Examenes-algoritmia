'''
Escriba un programa C++, que lea las notas de los n alumnos que dieron un examen y 
determine el porcentaje de aprobados. Si el porcentaje es inferior a 70% debe añadir 
un punto a cada examen y recalcular el porcentaje de aprobados y así sucesivamente 
hasta igualar o superar 70%. Considere que cuando un examen llega a 20 ya no tiene que añadir puntos.
Su programa debe mostrar el porcentaje de aprobados en cada iteración. 
Ejemplo: se ingresan 7 notas
 7  9  14   8   6   5  10 28.57% de aprobados
 8 10  15   9   7   6  11 42.85% de aprobados 
 9 11  16  10   8   7  12 57.14% de aprobados 
10 12  17  11   9   8  13 71.42% de aprobados
'''


cantidad=int(input("Ingrese el numero de alumnos: "))
notas=[]
c1=0
for i in range(cantidad):
    h=i+1
    nota=int(input(f"Ingrese la nota del alumno {h}:"))
    notas.append(nota)
    if(nota>=10):
        c1+=1
q=cantidad*0.7
r=round((c1*100)/cantidad,2)
print(notas,r,"de aprobados")

if(c1<q):
    o=True
    while(o==True):
        contador=0
        for i in range(len(notas)):
            notas[i]=notas[i]+1
            if(notas[i]>=10):
                contador+=1
        print(notas,round((contador*100/cantidad),2),"porcentaje de aprobados")
        if(cantidad%2==0):
            if(contador>=cantidad*0.7):
                o=False
        if(cantidad%2!=0):
            if(contador>=cantidad*0.7):
                o=False