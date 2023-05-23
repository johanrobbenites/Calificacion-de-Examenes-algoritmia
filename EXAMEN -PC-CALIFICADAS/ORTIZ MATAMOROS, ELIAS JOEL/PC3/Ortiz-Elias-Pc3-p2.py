n= int(input("INGRESE EL NUMERO DE CADENAS A ANALIZAR : "))
a=[0]*n
m=[0]*26
v=["a","b","c","d","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(n):
    a[i]=input(f"INGRESE LA CADENA {i+1} : ")
for i in range(n):
    z=a[i]
    for j in range(len(z)):
        if z[j]>="a" and z[j]<="z" and z[j]!="ñ":
            for x in range(len(v)):
                if z[j]==v[x]:
                    m[x]= m[x]+1
for i in range(len(v)):
    if m[i]!=0:
        print(f"{v[i]}  {m[i]} ", "*"*m[i] )
end=input("")