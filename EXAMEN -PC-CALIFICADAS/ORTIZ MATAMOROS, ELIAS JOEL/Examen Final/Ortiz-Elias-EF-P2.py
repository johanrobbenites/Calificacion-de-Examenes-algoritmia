import io 
v=[]
m=[]
archivo = open("TEXTO.txt","r")

lineas_texto=archivo.readlines()
print(len(lineas_texto[1]))
for i in range(len(lineas_texto)):
    nombre=""
    ventas=""
    for z in range(lineas_texto[i].index("\t")):
        ventas=ventas+ (lineas_texto[i])[z]
        if z==lineas_texto[i].index("\t")-1:
            m.append(float(ventas))
    for j in range(lineas_texto[i].index("\t") , len(lineas_texto[i])):
        nombre=nombre+(lineas_texto[i])[j]
        if j== len(lineas_texto[i])-1:
            v.append(nombre)
for i in range(len(m)):
    for j in range(len(m)):
        if m[i]>m[j]:
            c=m[i]
            m[i]=m[j]
            m[j]=c
            a=v[i]
            v[i]=v[j]
            v[j]=a
print("Monto Nombre  Pto  Bono  Porc")
for i in range(len(v)):
    print(m[i],"  ",v[i],"  ",i+1,"  ",(m[i]*(11-i))/100,"  ",11-(i+1),"%")

archivo.close()


end=input("")