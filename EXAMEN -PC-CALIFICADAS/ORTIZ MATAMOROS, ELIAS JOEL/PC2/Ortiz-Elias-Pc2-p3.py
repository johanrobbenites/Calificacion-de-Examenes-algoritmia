base= int(input("ingrese la base a evaluar : "))
n1=int(input("Ingrese el numero de digitos del primer numero : "))
v1= [0]*n1
for i in range(0, n1):
    v1[i]= int(input(f"ingrese el digito numero {i+1} del numero : ")) 
    if v1[i] >= base:
        print("ERROR EL NUMERO ESTA FUERA DE LA BASE")
        break
n2=int(input("Ingrese el numero de digitos del Segundo numero : "))
v2= [0]*n2 
for i in range(0, n2):
    v2[i]= int(input(f"ingrese el digito numero {i+1} del numero : ")) 
    if v2[i] >= base:
        print("ERROR EL NUMERO ESTA FUERA DE LA BASE")
        break
print(v1,v2)
end= input(" ")