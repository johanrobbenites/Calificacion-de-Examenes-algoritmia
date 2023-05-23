n= int(input("Ingrese el numero de alumnos : "))
while n >30 or n<0 :
  n=int(input("El numero ingresado no es valido, ingrese otro : "))
codigo=[0]*n
talla=[0]*n
peso= [0]*n
for i in range( 0, n):
    codigo[i]= int(input(f"Ingrese el codigo del alumno numero {i+1} : "))
    peso[i]= float(input(f"Ingrese el peso del alumno numero {i+1} : "))
    talla[i]= float(input(f"Ingrese la talla del alumno numero {i+1} : "))
print(codigo)
print(talla)
print(peso)
for i in range (0,n):
    for j in range(i+1,n):
        if peso[i]<peso[j]:
            t=peso[i]
            peso[i]=peso[j]
            peso[j]=t
            r=talla[i]
            talla[i]=talla[j]
            talla[j]=r
        if peso[i]==peso[j]:
            if talla[i]>talla[j]:
                y=talla[i]
                talla[i]=talla[j]
                talla[j]=y
print("---------------------")
print(peso)
print(talla)
end=input(" ")