# -*- coding: utf-8 -*-
"""Untitled50.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UTlbiqjcadO4cUDkKwgeMEoyrw884F7A
"""

n = int(input("INGRESE EL NUMERO DE ALUMNOS: "))
contA = 0
contD = 0
listaN = []
for i in range(n):
  lista = []
  notas = int(input(f"INGRESE EL NUMERO DE NOTAS DEL LA PRACTICA NRO°{i+1} "))
  for i in range(notas):
    res = int(input("INGRESE LA NOTA: "))
    lista.append(res)
  print(f"LAS NOTAS SON: {lista}")
  for i in lista:
    if res > 10:
      contA += 1
    else: 
      contD += 1
    aprobados = (contA / len(lista)) * 100
    if aprobados < 70:
      for res in lista:
        res_nuevo = res + 1
  	  listaN.append(res_nuevo)
      print(f"LAS NUEVAS NOTA SON: {listaN}")
  suma = 0
  for valor in lista:    
      suma = suma + valor
  prom = suma / (len(lista))
  print(f"SU PROMEDIO ES: {prom}")
  for i in range():
