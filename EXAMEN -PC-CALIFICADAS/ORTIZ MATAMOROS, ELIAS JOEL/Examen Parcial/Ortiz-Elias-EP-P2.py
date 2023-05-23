v=[0]*8
n=int(input("INGRESE UN NUMERO : "))
for i in range (2,10):
    b=''
    m=n
    while m>=i:
        b= str(n%i)+b
        if round(m/i)< i:
            b= str(round((m-1)/i))+b
        m= round(m/i)
    v[i-2]= b
print(v)