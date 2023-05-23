n=int(input("INGRESE EL NUMERO DE FILAS : "))
m=int(input("INGRESE EL NUMERO DE COLUMNAS : "))
a=([[0]*m])*n
b=([[0]*n])*m
for i in range(0,n):
    for j in range(0,m):
        a[i][j]= int(input(f"INGRESE EL VALOR DE DE LA MATRIZ [{i}][{j}] : "))
        print(a)
print(a)
print(b)
for i in range(0,m):
    for j in range(0,n):
        b[(n-1)-i][j]=a[j][i]
print(a)
print(b)
for i in range(0,n):
    for j in range(0,m):
        a[(n-1)-i][j]= b[i][j]
print(a)
print(b)
for i in range(0,m):
    for j in range(0,n):
        b[(m-1)-i][j]= a[i][j]
print(a)
print(b)
for i in range(0,n):
    for j in range(0,m):
        a[(n-1)-i][j]= b[i][j]
print(a)
print(b)
end=input("")