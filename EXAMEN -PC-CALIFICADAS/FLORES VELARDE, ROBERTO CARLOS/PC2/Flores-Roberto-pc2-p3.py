''''Diseñe un programa que permita almacenar en dos vectores de enteros los dígitos de dos
números en el sistema de numeración de base b. Luego, sin convertir a decimal, 
realizar la multiplicación los números y almacenar en otro vector los dígitos del producto de dichos números. 
Finalmente presentar los dígitos del producto de dichos números.
Ejemplo:
Base del sistema de numeración: 6
Los dígitos del primer número en base 6:           5  3  0  4  1
Los dígitos del segundo número en base 6:            2  4  1  5
Los dígitos del producto de los números:      2 2 5 5 4 5 3 5
Nota: Validar la base b y los dígitos de los números en el sistema de numeración de base b.
'''
num1=int(input("Inserte el primer numero: "))
num2=int(input("Inserte el segundo numero: "))
base=int(input("Ingrese la base a operar:"))
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
variable=0
for i in range(1,len(sumas)):
  p=sumas[i]*(10**exp)
  exp+=1
  auxiliar=0
  o=True
  r=0
  variable=0
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
  k=r

  while(k>0):
    residuo=k%10
    variable=variable*10+residuo
    k=k//10
  resultado=variable
print(resultado)












