# -*- coding: utf-8 -*-
"""herrera-jens-pc2-p3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vjZTFhcR-HPD3ANkZIZSz8v6QbFn2ljg
"""

d1=[]
d2=[]
dp=[]
b = int(input("Base de sistema de numeración: "))
while b<2:
  print("¡BASE INVÁLIDA!")
  b = int(input("Base de sistema de numeración: "))

print("DIGITOS DEL PRIMER NÚMERO")
c1=int(input("Cantidad de cifras del primer número: "))
for i in range(c1):
  digito1 = int(input("Ingrese dígitos: "))
  while digito1>=6 and digito1<0:
    print("¡DÍGITO INVÁLIDO!")
    digito1 = int(input("Ingrese dígitos: "))
  d1.append(digito1)

print("DIGITOS DEL SEGUNDO NÚMERO")
c2=int(input("Cantidad de cifras del segundo número: "))
for i in range(c2):
  digito1 = int(input("Ingrese dígitos: "))
  while digito1>=6 and digito1<0:
    print("¡DÍGITO INVÁLIDO!")
    digito1 = int(input("Ingrese dígitos: "))
  d2.append(digito1)


for j in range(c2,0,-1):
  for i in range(c1,0,-1):
    # 5 * {1,4,0,3}
    if d2[j-1]*d1[i-1]<=5:5
      dp.append((d2[j-1]*d1[i-1]))
    else:
      r=d2[j-1]*d1[i-1]%6
      l= d2[j-1]*d1[i-1]//6
      dp.append(r)
print(d1)
print(d2)
print(dp)
# 5 3 0 4 1
# 2 4 1 5