a=int(input("Inserte el numero: "))
while(a<0):
    a=int(input("Inserte el numero: "))
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
        print("Base ",i, "donde el numero es: ",f)
    p=a
    num=0
    f=0