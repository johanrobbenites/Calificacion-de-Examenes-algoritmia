n=int(input("Ingrese el numero de alumnos: "))
while(n>30):
    n=int(input("Ingrese el numero de alumnos nuevamente: "))
codigos=[]
pesos=[]
tallas=[]
for i in range(n):
    cod=int(input("Ingrese los datos del alumnos numero"+str(i+1)+" : "))
    while(cod>99):
        cod=int(input("Ingrese los datos del alumno nuevamente: "))
    codigos.append(cod)
    peso=float(input("Ingrese el peso del alumno numero"+str(i+1)+" : "))
    pesos.append(peso)
    talla=float(input("Ingrese la talla del alumno numero"+str(i+1)+" : "))
    tallas.append(talla)
x=[]
#Mostramos primero los datos por primera vez

for i in range(n):
    x.append([0]*3)
for j in range(3):
    for i in range(n):
        if(j==0):
            x[i][j]=codigos[i]
        if(j==1):
            x[i][j]=pesos[i]
        if(j==2):
            x[i][j]=tallas[i]
for i in range(n):
    for j in range(3):
        print(x[i][j],end=" ")
    print()

for i in range(1,len(pesos)):
    for j in range(len(pesos)-i):
        if(pesos[j]<pesos[j+1]):
            aux=pesos[j]
            pesos[j]=pesos[j+1]
            pesos[j+1]=aux
            aux1=codigos[j]
            codigos[j]=codigos[j+1]
            codigos[j+1]=aux1
            aux2=tallas[j]
            tallas[j]=tallas[j+1]
            tallas[j+1]=aux2


for j in range(3):
    for i in range(n):
        if(j==0):
            x[i][j]=codigos[i]
        if(j==1):
            x[i][j]=pesos[i]
        if(j==2):
            x[i][j]=tallas[i]

for i in range(n):
    for j in range(3):
        print(x[i][j],end=" ")
    print()
