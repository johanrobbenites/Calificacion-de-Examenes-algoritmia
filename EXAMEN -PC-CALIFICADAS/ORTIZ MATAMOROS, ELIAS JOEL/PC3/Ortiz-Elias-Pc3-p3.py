def leerdatos(a):
    v=[]
    for i in range(len(a)):
        if a[i]>="0" and a[i]<"9":
            if a[i-1]=="-":
                x=0
                num=""
                while a[i+x] >="0" and a[i+x]<"9":
                    num= num + a[i+x]
                    x= x +1
                v.append(int(num)*(-1))
            elif a[i-1]==" " or a[i-1]=="{":
                x=0
                num=""
                while a[i+x] >="0" and a[i+x]<"9":
                    num= num + a[i+x]
                    x= x +1
                v.append(int(num))
    return v
def union(a,b):
    v=b
    if len(a)>len(b):
        for i in range(len(a)):
            cont=0
            for j in range(len(b)):
                if a[i]==b[j]:
                    cont=cont +1
            if cont==0:
                v.append(a[i])
    return v
def interseccion(a,b):
    v=[]
    if len(a)> len(b):
        for i in range(len(b)):
            for j in range(len(a)):
                if b[i]==a[j]:
                    v.append(b[i])
    else:
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i]==b[j]:
                    v.append(a[i])
    return v  
n=input("INGRESE LOS CONJUNTOS DE VALORES ENTEROS A (EN FORMATO A={a;b;...}) : ")
m=input("INGRESE LOS CONJUNTOS DE VALORES ENTEROS B (EN FORMATO B={a;b;...}) : ")
x=leerdatos(n)
y=leerdatos(m)
print(f"LA UNION DE LOS LOS CONJUNTOS ES : {union(x,y)} ")
print(f"LA INTERSECCION DE LOS DOS CONJUNTOS ES : {interseccion(x,y)} ")
end=input("")