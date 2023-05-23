a=int(input("Ingrese numero entero positivo en base 10: "))
while(a<0):
    a=int(input("Ingrese numero entero positivo en base 10: "))
p=a
num=0
f=0
for i in range(2,10):
    while(p>0):
        c=p%i
        num=num*10+c
        p=p//i
    q=num

    while(q>0):
        d=q%10
        f=f*10+d
        q=q//10

    if(f==num and f>=10):
        print("El número es capicúa en la base: ",i, "(pues el número es: ",f,")")
    p=a
    num=0
    f=0
