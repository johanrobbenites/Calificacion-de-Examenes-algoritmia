# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P0E1jKVKLPJKVw7-TVBfxTBXT86jpfai
"""

f=open("ventasv.txt","w")
rpta="si"
while(rpta=="si"):
  venta=float(input("INGRESE VENTA: "))
  nombre=input("INGRESE NOMBRE DEL VENDEDOR: ")
  linea=str(venta)+" "+nombre+"\n"
  f.write(linea)
  rpta=input("DESEA INGRESAR MAS VENDEDORES? (si/no): ")
f.close()

k=open("ventasv.txt","r")
lista=k.readlines()
datos=[]
for linea in lista:
  k=linea.split(" ")
  datos.append(k)
for i in range(1,len(datos)):
  for j in range(len(datos)-i):
    if(float(datos[j][0])<float(datos[j+1][0])):
      inv=datos[j][0]
      datos[j][0]=datos[j+1][0]
      datos[j+1][0]=inv
for i in range(len(datos)):
  print(datos[i][0]," ",datos[i][1],datos[i][2],"  ",i+1)