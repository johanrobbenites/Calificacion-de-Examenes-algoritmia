m=int(input("Ingrese el numero de filas de la matriz: "))
n=int(input("Ingrese el numero de columnas de la matriz: "))
x=[]
a=[]
for i in range(m):
    y=[]
    for j in range(n):
        s=int(input("Ingrese los valores de la matriz: "))
        y.append(s)
        a.append(s)
    x.append(y)

print("-"*50)
print("La matriz es: ")
for i in range(m):
    for j in range(n):
        print(x[i][j],end=" ")
    print()
print("-"*50)

matriz1=[]
for i in range(n):
    matriz1.append([0]*m)
l=0
for i in range(n):
    k=m-1
    for j in range(m):
        matriz1[i][j]=x[k][l]
        k-=1
    l+=1
print()
for i in range(n):
    for j in range(m):
        print(matriz1[i][j],end=" ")
    print()

matriz2=[]
for i in range(m):
    matriz2.append([0]*n)
l=0
for i in range(m):
    k=n-1
    for j in range(n):
        matriz2[i][j]=matriz1[k][l] # 20 10 00  21 11 11
        k-=1
    l+=1 
print()
for i in range(m):
    for j in range(n):
        print(matriz2[i][j],end=" ")
    print()

matriz3=[]
for i in range(n):
    matriz3.append([0]*m)
l=0
for i in range(n):
    k=m-1
    for j in range(m):
        matriz3[i][j]=matriz2[k][l]
        k-=1
    l+=1
print()
for i in range(n):
    for j in range(m):
        print(matriz3[i][j],end=" ")
    print()


matriz4=[]
for i in range(m):
    matriz4.append([0]*n)
l=0
for i in range(m):
    k=n-1
    for j in range(n):
        matriz4[i][j]=matriz3[k][l] # 20 10 00  21 11 11
        k-=1
    l+=1
print()
for i in range(m):
    for j in range(n):
        print(matriz4[i][j],end=" ")
    print()
