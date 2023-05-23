n= int(input("INGRESE EL NUMERO DE ALUMNNOS : "))
a=[]
v=[0]*n
for i in range(n):
    a.append([0]*3)
def leerdatos(a):
    for i in range(n):
        for j in range(4):
            if j == 0:
                a[i][j]= input(f"INGRESE EL CODIGO DEL POSTULANTE {i+1} : ")
            elif j==1:
                a[i][j]= input(f"INGRESE EL NOMBRE COMPLETO DEL POSTULANTE {i+1} : ")
            elif j==2:
                a[i][j]= float(input(f"INGRESE EL PUNTAJE DEL POSTULANTE {i+1} : "))
    return a
def puesto(a,v):
    for i in range(n):
        for j in range(4):
            if j == 2:
                v[i]=a[i][j]
    return v
def ordenarpuesto(v):
    for i in range(len(v)):
        for j in range(i+1,len(v)):
            if v[i]< v[j]:
                t= v[i]
                v[i]=v[j]
                v[j]= t
    return v
z=leerdatos(a)
x=puesto(z,v)
y=ordenarpuesto(x)
print(z)
for i in range(n+1):
    for j in range(5):
        print(z[i][j])
        print("---------")
end=input("")