a=[0,0,0] , [0,0,0] , [0,0,0] , [0,0,0]
while True:
    empleado = int(input("Ingrese el codigo del empleado (1) , (2) , (3) , (4) o (0) si desea terminar : "))
    if empleado == 0:
        break
    producto = int(input("Ingrese el codigo del producto (1) , (2) , (3) : "))
    cantidad = int(input("Ingresa la cantidad vendida : "))
    a[empleado-1][producto-1] = a[empleado-1][producto-1] + cantidad
print("EMPLEADO 1:")
print("PRODUCTO 1 :"+ str(a[0][0]) +"  PRODUCTO 2 :"+ str(a[0][1]) + "  PRODUCTO 3 :"+ str(a[0][2]))
print("EMPLEADO 2:")
print("PRODUCTO 1 :"+ str(a[1][0]) +"  PRODUCTO 2 :"+ str(a[1][1]) + "  PRODUCTO 3 :"+ str(a[1][2]))
print("EMPLEADO 3:")
print("PRODUCTO 1 :"+ str(a[2][0]) +"  PRODUCTO 2 :"+ str(a[2][1]) + "  PRODUCTO 3 :"+ str(a[2][2]))
print("EMPLEADO 4:")
print("PRODUCTO 1 :"+ str(a[3][0]) +"  PRODUCTO 2 :"+ str(a[3][1]) + "  PRODUCTO 3 :"+ str(a[3][2]))
end= input(" ")