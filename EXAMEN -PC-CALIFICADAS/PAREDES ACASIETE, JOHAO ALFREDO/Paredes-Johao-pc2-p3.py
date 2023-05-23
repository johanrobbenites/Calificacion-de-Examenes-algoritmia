b = int(input("Base del sistema de  numeración: "))
n1 = input("Los dígitos del primer número en base 6: ").split()
n2 = input("Los dígitos dele segundo número en base 6: ").split()

n1 = [int(i) for i in n1]
n2 = [int(i) for i in n2]

productosmedios = []

for j in n2:
    productomedio = []
    lleva = 0
    for i in reversed(n1):
        productomedio.append((i*j+lleva)%b)
        lleva = (i*j+lleva)//b
    if lleva != 0:
        productomedio.append(lleva)
    productosmedios.append(productomedio[::-1])

print(productosmedios)

for i in range(len(n2)):
    zeros_a_agregar = len(n2)-i-1
    for j in range(zeros_a_agregar):
        productosmedios[i].append(0)
print(productosmedios)

# De acá solo faltaría sumar los productos medios en base b

