n= int(input("INGRESE EL NUMERO DE ENTEROS QUE INGRESARA: "))
v=[0]*n
for i in range(n):
    v[i]= int(input(f"INGRESE AL ARREGLO EL {i+1}º NUMERO : "))
print(v)
def encontrar_numero(m,n,i,p):
    if m[i]==n:
        return i
    elif i>p:
        return -1    
    i=i+1
    encontrar_numero(m,n,i,p)   
    
numero=int(input("INGRESE EL NUMERO QUE SE DESEA ENCONTRAR EN EL ARREGLO: "))
i=0
respuesta=(encontrar_numero(v,numero,i,n))
print(respuesta)
end=input("")