'''
Una tienda tiene 4 empleados y 3 productos. Se desea conocer 
al final del día cuánto de cada producto ha vendido cada uno de los empleados, 
mostrando los resultados en forma ordenada por empleado y cantidad vendida por 
producto de menor a mayor. Los datos se ingresan por cada venta considerando 
el código del empleado (del 1 al 4), el código del producto (del 1 al 3) y 
la cantidad vendida. Una venta solo involucra un producto. Para terminar el 
ingreso de datos se digita cero como código de empleado. Ejemplo:

'''


lista=[]
for h in range(4):
    lista.append([0]*3)

op=True

while(op==True):
    cod=int(input("Codigo del empleado: "))
    if(cod==0):
        break
    producto=int(input("Codigo de producto: "))
    cantidad=int(input("Cantidad del producto: "))
    if((cod>=1 and cod<=4) and (producto>=1 and producto<=3) and cantidad>0):
        lista[cod-1][producto-1]=lista[cod-1][producto-1]+cantidad
for i in range(4):
    for j in range(1,3):
        for k in range(3-j):
            if(lista[i][k]>lista[i][k+1]):
                var=lista[i][k]
                lista[i][k]=lista[i][k+1]
                lista[i][k+1]=var

for i in range(4):
    print("El empleado: ",i+1)
    for j in range(3):
        if(lista[i][j]!=0):
            print(f"Codigo del producto {j+1} : {lista[i][j]}")
















