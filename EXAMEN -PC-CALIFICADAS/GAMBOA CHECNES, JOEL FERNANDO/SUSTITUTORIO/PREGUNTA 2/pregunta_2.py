# -*- coding: utf-8 -*-
"""PREGUNTA 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nlVE582A6XE02nLmdykj8LnergBO7crM
"""

p=open("COVID.TXT","w")
n=int(input("INGRESE LA CANTIDAD DE PERSONAS: "))
for i in range(n):
  edad=int(input("INGRESE LA EDAD DE LA PERSONA: "))
  sexo=input("INGRESE EL SEXO DE LA PERSONA: ")
  estado=input("INGRESE ESTADO DE LA PERSONA: ")
  distrito=input("INGRESE EL DISTRITO: ")
  linea=str(edad)+" "+sexo+" "+estado+" "+distrito+"\n"
  p.write(linea)
p.close()