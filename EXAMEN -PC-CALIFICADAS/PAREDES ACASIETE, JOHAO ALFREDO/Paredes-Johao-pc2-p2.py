print("Entrada")
empleados = []
productos = []
cantidades = []
ventas = []
while True:
    empleado = int(input("Código de empleado: "))
    if empleado == 0: break
    producto = int(input("Código de producto: "))
    if producto == 0: break
    cantidad = int(input("Cantidad: "))
    if cantidad == 0: break
    empleados.append(empleado)
    productos.append(producto)
    cantidades.append(cantidad)
    ventas.append([empleado, producto, cantidad])
    print()

print("Salida")
for empleado in range(1,5):
    if empleado in empleados:
        print("Empleado: "+ str(empleado))
        for venta in ventas:
            if venta[0] == empleado:
                print("Producto "+str(venta[1]) +": "+ str(venta[2]))
        print()
                    

