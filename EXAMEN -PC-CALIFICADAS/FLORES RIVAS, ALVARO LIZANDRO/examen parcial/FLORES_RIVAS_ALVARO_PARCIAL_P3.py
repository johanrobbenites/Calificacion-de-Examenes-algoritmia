m=int(input("digite cantidad de filas"))
n=int(input("digite cantidad de columnas "))
x=[]
a=[]
for i in range(m):
    y=[]
    for j in range(n):
        s=int(input("digite los elemnetos de la matriz"))
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

m1=[]
for i in range(n):
    m1.append([0]*m)
l=0
for i in range(n):
    k=m-1
    for j in range(m):
        m1[i][j]=x[k][l]
        k-=1
    l+=1
print()
for i in range(n):
    for j in range(m):
        print(m1[i][j],end=" ")
    print()

m2=[]
for i in range(m):
    m2.append([0]*n)
l=0
for i in range(m):
    k=n-1
    for j in range(n):
        m2[i][j]=m1[k][l] 
        k-=1
    l+=1 
print()
for i in range(m):
    for j in range(n):
        print(m2[i][j],end=" ")
    print()

m3=[]
for i in range(n):
    m3.append([0]*m)
l=0
for i in range(n):
    k=m-1
    for j in range(m):
        m3[i][j]=m2[k][l]
        k-=1
    l+=1
print()
for i in range(n):
    for j in range(m):
        print(m3[i][j],end=" ")
    print()


m4=[]
for i in range(m):
    m4.append([0]*n)
l=0
for i in range(m):
    k=n-1
    for j in range(n):
        m4[i][j]=m3[k][l] 
        k-=1
    l+=1
print()
for i in range(m):
    for j in range(n):
        print(m4[i][j],end=" ")
    print()
    