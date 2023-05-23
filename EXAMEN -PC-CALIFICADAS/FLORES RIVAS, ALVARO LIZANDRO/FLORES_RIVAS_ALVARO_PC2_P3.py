num1=int(input("Inserte primer numero: "))
num2=int(input("Inserte segundo numero: "))
base=int(input("Ingrese la base :"))
lista1=[]
lista2=[]

if(lista2>lista1):
  var=lista2
  lista2=lista1
  lista1=var
while(num1>0):
  c=num1%10
  lista1.append(c)
  num1=num1//10
while(num2>0):
  c=num2%10
  lista2.append(c)
  num2=num2//10
vector=[]
for j in range(len(lista2)):
  auxiliar=0
  num=0
  for i in range(len(lista1)):
    c=lista2[j]*lista1[i]+auxiliar
    if(c<base):
      num=num*10+c
      auxiliar=0
    if(c>=base):
      auxiliar=c//base
      c=c-(auxiliar*base)
      num=num*10+c
    if(i==len(lista1)-1):
        if(auxiliar!=0):
          num=num*10+auxiliar
  vector.append(num)
sumas=[]
for i in range(len(vector)):
  p=vector[i]
  nump=0
  while(p>0):
    c=p%10
    nump=nump*10+c
    p=p//10
  sumas.append(nump)
resultado=sumas[0]
exp=1
nr=0
for i in range(1,len(sumas)):
  p=sumas[i]*(10**exp)
  exp+=1
  auxiliar=0
  o=True
  r=0
  nr=0
  while(p>0):
    c=p%10
    ver=1
    while(resultado>0 and o==True):
      d=resultado%10
      cif=c+d+auxiliar
      ver=0
      if(cif<base):
        r=r*10+cif
        auxiliar=0
      if(cif>=base):
        auxiliar=cif//base
        cif=cif-(auxiliar*base)
        r=r*10+cif
      o=False
      resultado=resultado//10
    if(resultado==0 and ver==1):
      if(p!=0):
        cif=c+auxiliar
        if(cif<base):
          r=r*10+cif
          auxiliar=0
        if(cif>=base):
          auxiliar=cif//base
          cif=cif-(auxiliar*base)
          r=r*10+cif
    p=p//10
    o=True
  if(p==0):
    if(auxiliar!=0):
      r=r*10+auxiliar
  t=r

  while(t>0):
    re=t%10
    nr=nr*10+re
    t=t//10
  resultado=nr
print(resultado) 
          