n=int(input("Cantidad de alumnos: "))
N=[]
#añadimos a la lista la nota de los alumnos
for i in range(n):
    nota =-1
    while(nota<0 or nota>20):
        nota=int(input(f"Nota del alumno {i+1}: "))
    N.append(nota)
#cantidad aprobada
c=0
for j in range(n):
    if(N[j] >= 10):
        c=c+1
print(*N,"\t",(c/n))
while((c/n)<0.7):
    for k in range(n):
        if(N[k]<20):
            N[k]=N[k]+1
    c=0
    for j in range(n):
        if(N[j]>=10):
            c=c+1
print(*N,"\t",(c/n))